#!/usr/bin/env python3
"""Ingest a saved job HTML page and emit a structured markdown summary.

This is intentionally offline and rule-based:
- no browser automation
- no LinkedIn login automation
- no AI dependency for the first pass

Input:
  - --html path to a saved HTML file
  - --url optional job URL for reference
  - --resume optional path to the master resume text file

Output:
  - structured markdown summary printed to stdout
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup


SKILL_BUCKETS = {
    "Python": ["python"],
    "Bash": ["bash", "shell", "zsh"],
    "JavaScript": ["javascript", "js"],
    "Java": ["java"],
    "C": [" c ", " c,", " c.", " c/"],
    "C++": ["c++"],
    "SQL": ["sql", "postgres", "mysql", "relational database"],
    "CI/CD": ["ci/cd", "cicd", "build pipeline", "pipeline"],
    "APIs": ["api", "rest", "webhook", "integration"],
    "SaaS": ["saas", "cloud-based"],
    "Networking": ["dns", "dhcp", "tcp/ip", "vlan", "vpn", "ssh"],
    "Troubleshooting": ["troubleshoot", "debug", "root cause", "failure analysis", "incident"],
    "Documentation": ["document", "documentation", "technical report", "design document", "knowledge base"],
    "Manual testing": ["manual test", "exploratory test", "test case", "test plan", "bug report", "regression"],
    "Automation": ["automation", "automated", "automation test"],
    "Agile": ["agile", "scrum", "sprint"],
    "CSV": ["csv"],
    "Validation": ["gxp", "gamp", "iq", "oq", "pq", "rtm", "validation"],
    "Docker / Kubernetes": ["docker", "kubernetes", "container"],
    "Windows Server": ["windows server", "active directory", "group policy"],
    "Linux": ["linux", "ubuntu", "rhel", "suse", "rocky"],
    "Project management": ["project management", "prioritize", "multitask", "schedule"],
    "JIRA": ["jira", "confluence"],
    "Security / auth": ["oauth", "saml", "scim", "auth", "ssO".lower()],
    "Cybersecurity": ["cyber security", "network security", "application security", "cyber exposure"],
    "ServiceNow": ["servicenow"],
    "Dell Boomi": ["dell boomi", "boomi"],
    "NetSuite": ["netsuite"],
    "Salesforce": ["salesforce"],
    "ADP": ["adp"],
    "ChatGPT Enterprise": ["chatgpt enterprise"],
    "Claude": ["claude"],
}

NOISE_LINE_PATTERNS = [
    r"linkedin",
    r"notificaciones",
    r"guardar",
    r"solicitar",
    r"reactivar premium",
    r"mira una comparación",
    r"accede a información exclusiva",
    r"personas han hecho clic",
    r"conoce al equipo de contratación",
    r"mostrar más",
    r"mostrar todo",
    r"acerca del empleo",
    r"compartido hace",
    r"promocionado por técnico de selección",
    r"respuestas gestionadas fuera de linkedin",
    r"/voyager/api/",
    r"\bbpr-guid\b",
    r"\brequest\b",
    r"\bstatus\b",
    r"\bheaders\b",
    r"\bbody\b",
    r"\burn:li:",
]


EXPERIENCE_BUCKETS = [
    (
        "UST - Validation Engineer II",
        ["validation", "automation", "logs", "telemetry", "regression", "cross-functional", "troubleshooting"],
    ),
    (
        "Pertec - Service Desk Agent",
        ["support", "windows", "active directory", "incident", "service request", "network"],
    ),
    (
        "Intel - Xeon Product Validation Intern",
        ["platform", "validation", "automation", "ci/cd", "logs", "telemetry", "defect"],
    ),
    (
        "Foundever - Applications Design Engineer",
        ["schematics", "pcb", "bios", "firmware", "bring-up", "integration", "debug"],
    ),
]

EXPERIENCE_DETAILS = {
    "UST - Validation Engineer II": {
        "skills": ["validation", "automation", "logs", "telemetry", "regression", "troubleshooting", "cross-functional"],
        "bullets": [
            "Performed end-to-end system validation across hardware, firmware, operating systems, networking, and I/O interfaces.",
            "Developed Python automation tools to streamline test execution, data collection, and engineering workflows.",
            "Investigated platform failures using logs, telemetry, and platform diagnostics to identify root causes.",
            "Collaborated with cross-functional teams to validate fixes and improve platform reliability.",
            "Executed regression testing to verify system stability, functionality, and performance.",
        ],
        "story": "Describe a validation issue you isolated with logs or telemetry, how you automated part of the workflow, and how you helped validate the fix.",
    },
    "Pertec - Service Desk Agent": {
        "skills": ["support", "windows", "active directory", "incident", "service request", "network", "customer communication", "documentation"],
        "bullets": [
            "Provided technical support for enterprise Windows environments.",
            "Diagnosed and resolved operating system, Active Directory, hardware, software, and network connectivity issues.",
            "Managed incidents and service requests while meeting service-level objectives.",
            "Documented resolutions and collaborated with internal teams to restore user productivity.",
        ],
        "story": "Describe a customer incident you took ownership of, the diagnostic steps you followed, and how you restored service quickly.",
    },
    "Intel - Xeon Product Validation Intern": {
        "skills": ["platform", "validation", "automation", "ci/cd", "logs", "telemetry", "defect", "code reviews"],
        "bullets": [
            "Performed platform validation and system-level troubleshooting for Intel Xeon server technologies.",
            "Developed Python automation tools to improve test execution, log analysis, and engineering productivity.",
            "Applied software engineering best practices, including version control, unit testing, code reviews, modular design, and reusable design patterns.",
            "Integrated automated validation into CI/CD workflows to improve test reliability and maintainability.",
            "Performed failure analysis using platform logs, telemetry, and hardware diagnostics to isolate complex system issues.",
            "Collaborated with engineering teams to reproduce, document, and resolve platform defects.",
        ],
        "story": "Describe a validation workflow you improved with automation or CI/CD and how that reduced time to reproduce or diagnose failures.",
    },
    "Foundever - Applications Design Engineer": {
        "skills": ["schematics", "pcb", "bios", "firmware", "bring-up", "integration", "debug"],
        "bullets": [
            "Provided engineering support to OEM and ODM partners developing Intel-based PC and server platforms.",
            "Reviewed hardware schematics and PCB layouts using OrCAD to identify design issues before manufacturing.",
            "Debugged hardware, BIOS/firmware, and software issues during platform integration and customer bring-up.",
        ],
        "story": "Describe a bring-up or integration issue where you had to trace the problem across hardware and firmware boundaries.",
    },
}

RESUME_SKILL_TAGS = {
    "Python",
    "Bash",
    "Git",
    "CI/CD",
    "Unit testing",
    "Integration testing",
    "Code reviews",
    "Design patterns",
    "Root Cause Analysis",
    "Failure Analysis",
    "Log Analysis",
    "Platform Validation",
    "Automation Development",
    "Telemetry Analysis",
    "Performance and Power Validation",
    "Networking Protocols",
    "Remote Diagnostics",
    "Client-Server Troubleshooting",
    "Windows",
    "Active Directory",
    "Incident Handling",
    "Service Requests",
    "Customer Communication",
    "Hardware",
    "Software",
    "Firmware",
    "BIOS",
    "Schematics",
    "PCB Layouts",
    "Bring-up",
    "Integration",
    "Debugging",
    "Documentation",
    "Testing",
    "Support",
}

SPECIFIC_TOOL_KEYWORDS = {
    "Dell Boomi": ["dell boomi", "boomi"],
    "NetSuite": ["netsuite"],
    "Salesforce": ["salesforce"],
    "ADP": ["adp"],
    "ChatGPT Enterprise": ["chatgpt enterprise"],
    "Claude": ["claude"],
    "ServiceNow": ["servicenow"],
    "Docker / Kubernetes": ["docker", "kubernetes"],
    "Boomi / iPaaS": ["ipaas", "integration platform"],
    "Selenium": ["selenium"],
    "Cypress": ["cypress"],
    "Jira": ["jira"],
    "Confluence": ["confluence"],
}

COMMON_GENERIC_TERMS = {
    "job summary",
    "key responsibilities",
    "responsibilities",
    "requirements",
    "qualifications",
    "preferred",
    "preferred qualifications",
    "about the job",
    "acerca del empleo",
    "summary",
    "company",
    "location",
    "remote",
    "hybrid",
    "onsite",
    "on site",
    "costa rica",
    "san jose",
    "san josé",
    "support",
    "validation",
    "automation",
    "integration",
    "testing",
    "documentation",
    "troubleshooting",
}

COMMON_GENERIC_WORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "have",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "our",
    "the",
    "this",
    "to",
    "with",
    "you",
    "your",
    "we",
    "will",
    "work",
    "support",
    "design",
    "experience",
    "responsibilities",
    "requirements",
    "preferred",
    "required",
    "summary",
    "integration",
    "engineer",
    "qualification",
    "qualifications",
    "platform",
    "platforms",
    "system",
    "systems",
    "solution",
    "solutions",
    "technical",
    "job",
    "role",
    "core",
    "key",
    "information",
    "management",
    "what",
    "gain",
    "hands-on",
    "opportunity",
    "document",
    "monitor",
    "related",
    "this",
    "experience",
    "design",
    "support",
    "implementation",
    "implement",
    "maintain",
    "building",
    "build",
    "existing",
    "current",
    "solution",
    "solutions",
    "team",
    "teams",
}

BAD_TAIL_WORDS = {
    "this",
    "experience",
    "support",
    "design",
    "related",
    "role",
    "roles",
    "summary",
    "opportunity",
    "responsibilities",
    "requirements",
}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs):
        if tag in {"script", "style", "noscript"}:
            self._skip_depth += 1
        elif tag in {"p", "div", "br", "li", "section", "article", "h1", "h2", "h3", "h4"}:
            self._chunks.append("\n")

    def handle_endtag(self, tag: str):
        if tag in {"script", "style", "noscript"} and self._skip_depth > 0:
            self._skip_depth -= 1
        elif tag in {"p", "div", "li", "section", "article", "h1", "h2", "h3", "h4"}:
            self._chunks.append("\n")

    def handle_data(self, data: str):
        if self._skip_depth == 0:
            self._chunks.append(data)

    def text(self) -> str:
        raw = "".join(self._chunks)
        raw = raw.replace("\xa0", " ")
        raw = re.sub(r"\r", "\n", raw)
        raw = re.sub(r"\n[ \t]+\n", "\n\n", raw)
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip()


def extract_html_title(html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    title = re.sub(r"\s+", " ", match.group(1))
    return title.strip()


@dataclass
class JobSummary:
    title: str
    company: str
    location: str
    compensation: str
    employment_type: str
    fit_score: int
    missing_skills: list[str]
    relevant_bullets: list[tuple[str, str]]
    star_prompts: list[str]
    candidate_terms: list[str]
    extracted_skills: list[str]
    matched_experience: list[str]
    source_url: str | None


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text


def meaningful_lines(text: str) -> list[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    filtered: list[str] = []
    for line in lines:
        lower = line.lower()
        if any(re.search(pattern, lower) for pattern in NOISE_LINE_PATTERNS):
            continue
        if len(line) < 3:
            continue
        filtered.append(line)
    return filtered


def extract_text(html: str) -> str:
    parser = TextExtractor()
    parser.feed(html)
    return parser.text()


def first_nonempty(lines: Iterable[str]) -> str:
    for line in lines:
        if line.strip():
            return line.strip()
    return ""


def collapse_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def is_location_line(line: str) -> bool:
    low = line.lower().strip()
    if not low:
        return False
    if any(token in low for token in ["costa rica", "remote", "hybrid", "onsite", "on-site"]):
        return True
    if re.search(r"\b[A-ZÁÉÍÓÚÑ][^,]+,\s*[A-ZÁÉÍÓÚÑ]", line):
        return True
    return False


def extract_description_block(soup: BeautifulSoup) -> str:
    node = soup.find(attrs={"data-testid": "expandable-text-box"})
    if not node:
        return ""
    return collapse_spaces(node.get_text(" ", strip=True))


def extract_requirement_bullets(soup: BeautifulSoup) -> list[str]:
    heading = soup.find(
        lambda tag: getattr(tag, "name", None) in {"h2", "h3", "strong"}
        and normalize(tag.get_text(" ", strip=True)) in {"about the job", "acerca del empleo"}
    )
    if not heading:
        return []

    container = heading.parent
    for _ in range(5):
        if not container:
            break
        bullets = [collapse_spaces(li.get_text(" ", strip=True)) for li in container.find_all("li")]
        bullets = [item for item in bullets if item]
        if bullets:
            return bullets
        container = container.parent
    return []


def is_candidate_term(term: str, known_terms: set[str]) -> bool:
    normalized = normalize(term)
    if not normalized:
        return False
    if normalized in known_terms:
        return False
    if normalized in COMMON_GENERIC_TERMS:
        return False
    if len(normalized) < 3:
        return False
    if normalized.isdigit():
        return False
    return True


def extract_candidate_terms(job_text: str) -> list[str]:
    text = collapse_spaces(job_text)
    known_terms = {normalize(skill) for skill in SKILL_BUCKETS}
    known_terms.update(normalize(skill) for skill in RESUME_SKILL_TAGS)
    known_terms.update(normalize(label) for label in EXPERIENCE_DETAILS)
    known_terms.update(normalize(label) for label in SPECIFIC_TOOL_KEYWORDS)

    candidates: list[str] = []
    patterns = [
        r"\b(?:[A-Z]{2,}(?:[./-][A-Z0-9]+)?(?:\s+[A-Z0-9][A-Za-z0-9+./-]*){0,3})\b",
        r"\b(?:[A-Z][A-Za-z0-9+./-]*(?:\s+[A-Z][A-Za-z0-9+./-]*){1,3})\b",
        r"\b(?:[A-Za-z]+[A-Z][A-Za-z0-9+./-]*(?:\s+[A-Z][A-Za-z0-9+./-]*){0,3})\b",
        r"\b[A-Z]{2,6}\b",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            term = collapse_spaces(match.group(0))
            words = [w.strip(".,:;()[]{}") for w in term.split() if w.strip(".,:;()[]{}")]
            if not words:
                continue
            if len(words) > 1:
                generic_word_count = sum(1 for word in words if word.lower() in COMMON_GENERIC_WORDS)
                has_tech_signal = bool(
                    re.search(r"[+/.-]", term)
                    or re.search(r"\b[A-Z]{2,6}\b", term)
                    or re.search(r"[a-z][A-Z]", term)
                    or re.search(r"\d", term)
                )
                tail = words[-1].lower()
                if not has_tech_signal or generic_word_count >= len(words):
                    continue
                if tail in BAD_TAIL_WORDS:
                    continue
                if len(words) == 2 and tail in COMMON_GENERIC_WORDS and not (
                    words[0].isupper() or re.search(r"[a-z][A-Z]", words[0]) or re.search(r"[+/.-]", words[0])
                ):
                    continue
            elif not (
                term.isupper()
                or re.search(r"[+/.-]", term)
                or re.search(r"[a-z][A-Z]", term)
                or re.search(r"\d", term)
            ):
                continue
            if is_candidate_term(term, known_terms) and term not in candidates:
                candidates.append(term)

    return candidates


def write_terms_sidecar(html_path: Path, candidate_terms: list[str], source_url: str | None = None) -> Path:
    out_path = html_path.with_suffix(".terms.json")
    payload = {
        "html_file": str(html_path),
        "source_url": source_url,
        "candidate_terms": candidate_terms,
    }
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    return out_path


def judge_terms(term_path: Path) -> list[str]:
    data = json.loads(term_path.read_text(encoding="utf-8"))
    terms = data.get("candidate_terms", [])
    if not terms:
        print("No candidate terms found.")
        return []

    print(f"Reviewing candidate terms from {term_path}")
    for idx, term in enumerate(terms, start=1):
        print(f"{idx}. {term}")
    raw = input("Select terms to approve (comma-separated numbers, 'all', or 'none'): ").strip().lower()
    if raw in {"", "none", "n"}:
        selected: list[str] = []
    elif raw == "all":
        selected = list(terms)
    else:
        selected = []
        indexes = set()
        for part in raw.split(","):
            part = part.strip()
            if not part:
                continue
            if part.isdigit():
                indexes.add(int(part))
        for idx, term in enumerate(terms, start=1):
            if idx in indexes:
                selected.append(term)

    approved_path = term_path.with_suffix(".approved.json")
    approved_path.write_text(
        json.dumps(
            {
                "html_file": data.get("html_file"),
                "source_url": data.get("source_url"),
                "approved_terms": selected,
            },
            indent=2,
            ensure_ascii=True,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {approved_path}")
    return selected


def experience_score(job_text: str, experience: str) -> int:
    details = EXPERIENCE_DETAILS[experience]
    norm = normalize(job_text)
    keyword_hits = sum(1 for needle in EXPERIENCE_BUCKETS[[label for label, _ in EXPERIENCE_BUCKETS].index(experience)][1] if needle in norm)
    skill_hits = sum(1 for skill in details["skills"] if skill.lower() in norm)
    return 40 + (keyword_hits * 10) + (skill_hits * 3)


def select_relevant_experience(job_text: str, limit: int = 2) -> list[str]:
    scored = sorted(
        ((experience_score(job_text, label), label) for label, _ in EXPERIENCE_BUCKETS),
        reverse=True,
    )
    return [label for score, label in scored[:limit] if score > 0]


def select_resume_bullets(job_text: str, experiences: list[str]) -> list[tuple[str, str]]:
    selected: list[tuple[str, str]] = []
    for experience in experiences:
        details = EXPERIENCE_DETAILS[experience]
        for bullet in details["bullets"][:2]:
            selected.append((experience, bullet))
    return selected[:6]


def derive_missing_skills(job_skills: list[str], experiences: list[str]) -> list[str]:
    covered = {skill.lower() for skill in RESUME_SKILL_TAGS}
    for experience in experiences:
        covered.update(skill.lower() for skill in EXPERIENCE_DETAILS[experience]["skills"])
    missing = [skill for skill in job_skills if skill.lower() not in covered]
    return missing


def extract_specific_tools(job_text: str) -> list[str]:
    norm = normalize(job_text)
    found: list[str] = []
    for label, needles in SPECIFIC_TOOL_KEYWORDS.items():
        if any(needle in norm for needle in needles):
            found.append(label)
    return found


def score_specific_tool_coverage(job_text: str, resume_skills: set[str]) -> tuple[int, list[str]]:
    norm = normalize(job_text)
    found_tools: list[str] = []
    penalty = 0
    for label, needles in SPECIFIC_TOOL_KEYWORDS.items():
        if any(needle in norm for needle in needles):
            found_tools.append(label)
            if label.lower() not in resume_skills:
                penalty += 4
    return penalty, found_tools


def build_star_prompts(experiences: list[str]) -> list[str]:
    prompts: list[str] = []
    for experience in experiences:
        prompts.append(EXPERIENCE_DETAILS[experience]["story"])
    return prompts[:4]


def infer_title_company_location(html_title: str, lines: list[str]) -> tuple[str, str, str, str, str]:
    title = ""
    company = ""
    location = ""
    compensation = ""
    employment_type = ""
    location_hint = ""

    if html_title:
        parts = [part.strip() for part in html_title.split("|") if part.strip()]
        if parts and parts[-1].lower() == "linkedin":
            parts = parts[:-1]
        if len(parts) >= 2:
            title = parts[0]
            company = parts[1]
        elif len(parts) == 1:
            title = parts[0]

    title_match = re.match(r"^(?P<title>.+?)\s*\((?P<extra>[^)]+)\)$", title)
    if title_match:
        title = title_match.group("title").strip()
        extra = title_match.group("extra").strip()
        for piece in [p.strip() for p in extra.split(",") if p.strip()]:
            if piece.lower() in {"remote", "hybrid", "onsite", "on-site"}:
                employment_type = piece.title()
            else:
                location_hint = piece

    company_idx = None
    for idx, line in enumerate(lines):
        if normalize(line) == normalize(company):
            company_idx = idx
            break

    if company_idx is not None:
        for line in lines[company_idx + 1 : company_idx + 8]:
            line_norm = normalize(line)
            if line_norm in {normalize(company), normalize(title), "·"}:
                continue
            if title and line_norm.startswith(normalize(title)):
                continue
            if is_location_line(line):
                location = line
                break

    if not location and location_hint:
        location = location_hint

    if not employment_type:
        for line in lines[:20]:
            if any(token in line.lower() for token in ["remote", "remoto", "híbrido", "hybrid", "onsite", "on-site"]):
                if "hybrid" in line.lower() or "híbrido" in line.lower():
                    employment_type = "Hybrid"
                elif "remote" in line.lower() or "remoto" in line.lower():
                    employment_type = "Remote"
                else:
                    employment_type = "Onsite"
                break

    comp_match = re.search(
        r"(?:USD\s*)?\$?\d[\d,]*(?:\.\d+)?\s*(?:-\s*(?:USD\s*)?\$?\d[\d,]*(?:\.\d+)?)?\s*(?:/hr|per hour|hour|hr)",
        " ".join(lines),
        re.IGNORECASE,
    )
    if comp_match:
        compensation = comp_match.group(0).strip()

    location = re.sub(r"^(?:hybrid|remote|onsite|on-site)\s*,\s*", "", location, flags=re.IGNORECASE)
    location = re.sub(r"\s*,\s*(?:hybrid|remote|onsite|on-site)$", "", location, flags=re.IGNORECASE)

    return title, company, location, compensation, employment_type


def extract_skills(text: str) -> list[str]:
    found: list[str] = []
    norm = normalize(text)
    for skill, needles in SKILL_BUCKETS.items():
        if any(needle in norm for needle in needles):
            found.append(skill)
    return found


def match_experience(text: str) -> list[str]:
    norm = normalize(text)
    matches: list[str] = []
    for label, needles in EXPERIENCE_BUCKETS:
        score = sum(1 for needle in needles if needle in norm)
        if score >= 2:
            matches.append(label)
    return matches


def load_html(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def build_summary(html_path: Path, source_url: str | None = None) -> JobSummary:
    html = load_html(html_path)
    soup = BeautifulSoup(html, "html.parser")
    text = extract_text(html)
    html_title = extract_html_title(html)
    visible_lines = meaningful_lines(soup.get_text("\n"))
    title, company, location, compensation, employment_type = infer_title_company_location(html_title, visible_lines)

    description = extract_description_block(soup)
    requirements = extract_requirement_bullets(soup)
    match_text = " ".join(part for part in [html_title, description, " ".join(requirements)] if part)

    skills = extract_skills(match_text)
    candidate_source = " ".join(part for part in [description, " ".join(requirements)] if part)
    candidate_terms = extract_candidate_terms(candidate_source)
    experience = match_experience(match_text)
    relevant_experiences = select_relevant_experience(match_text)
    fit_score = 0
    for label in relevant_experiences or experience:
        fit_score = max(fit_score, min(95, experience_score(match_text, label)))
    if not fit_score:
        fit_score = 45 if skills else 25

    resume_skill_norm = {skill.lower() for skill in RESUME_SKILL_TAGS}
    specific_penalty, specific_tools = score_specific_tool_coverage(match_text, resume_skill_norm)
    fit_score -= specific_penalty

    if specific_tools and specific_penalty:
        fit_score -= 4

    if specific_tools and any(tool in {"Dell Boomi", "NetSuite", "Salesforce", "ADP", "ChatGPT Enterprise", "Claude"} for tool in specific_tools):
        fit_score = min(fit_score, 85)

    if "integration engineer" in normalize(match_text) and any(tool in {"Dell Boomi", "NetSuite", "Salesforce", "ADP"} for tool in specific_tools):
        fit_score = min(fit_score, 84)

    fit_score = max(0, min(95, fit_score))

    if not relevant_experiences:
        relevant_experiences = experience

    missing_skills = derive_missing_skills(skills, relevant_experiences)
    relevant_bullets = select_resume_bullets(match_text, relevant_experiences)
    star_prompts = build_star_prompts(relevant_experiences)

    if not employment_type:
        lower_match = match_text.lower()
        if "remote" in lower_match:
            employment_type = "Remote"
        elif "hybrid" in lower_match:
            employment_type = "Hybrid"
        elif "onsite" in lower_match or "on-site" in lower_match:
            employment_type = "Onsite"

    return JobSummary(
        title=title or "Unknown",
        company=company or "Unknown",
        location=location or "Unknown",
        compensation=compensation or "Unknown",
        employment_type=employment_type or "Unknown",
        fit_score=fit_score,
        missing_skills=missing_skills,
        relevant_bullets=relevant_bullets,
        star_prompts=star_prompts,
        candidate_terms=candidate_terms,
        extracted_skills=skills,
        matched_experience=experience,
        source_url=source_url,
    )


def render_markdown(summary: JobSummary, html_path: Path) -> str:
    skills_block = "\n".join(f"- {skill}" for skill in summary.extracted_skills) or "- None found"
    exp_block = "\n".join(f"- {item}" for item in summary.matched_experience) or "- None matched"
    missing_block = "\n".join(f"- {skill}" for skill in summary.missing_skills) or "- None identified"
    bullets_block = "\n".join(f"- [{label}] {bullet}" for label, bullet in summary.relevant_bullets) or "- None identified"
    star_block = "\n".join(f"- {item}" for item in summary.star_prompts) or "- None identified"
    candidate_block = "\n".join(f"- {item}" for item in summary.candidate_terms) or "- None found"
    source = summary.source_url or "Not provided"
    return f"""# Job Ingest Summary

## Source

- HTML file: `{html_path}`
- URL: {source}

## Inferred Fields

- Company: {summary.company}
- Role: {summary.title}
- Location: {summary.location}
- Employment: {summary.employment_type}
- Compensation: {summary.compensation}

## Fit Score

- Score: {summary.fit_score}/100

## Extracted Skills

{skills_block}

## Missing Skills

{missing_block}

## Relevant Resume Bullets

{bullets_block}

## STAR Prompts

{star_block}

## Candidate New Terms

These are saved separately in a `.terms.json` sidecar for review.

{candidate_block}

## Relevant Experience

{exp_block}

## Notes

- This summary is rule-based and should be reviewed before filing.
- Add the job note to the appropriate `jobs/` location after confirming the extraction.
"""


def ingest_html_file(html_path: Path, source_url: str | None = None, out_path: Path | None = None) -> Path:
    summary = build_summary(html_path, source_url)
    markdown = render_markdown(summary, html_path)
    target = out_path if out_path else html_path.with_suffix(".md")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(markdown, encoding="utf-8")
    write_terms_sidecar(html_path, summary.candidate_terms, source_url=source_url)
    return target


def iter_html_files(folder: Path) -> list[Path]:
    html_files = [
        path
        for path in folder.iterdir()
        if path.is_file() and path.suffix.lower() in {".html", ".htm"}
    ]
    return sorted(html_files)


def ingest_folder(folder: Path, source_url: str | None = None) -> list[Path]:
    written: list[Path] = []
    for html_path in iter_html_files(folder):
        written.append(ingest_html_file(html_path, source_url=source_url))
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract skills and experience matches from a saved job HTML file.")
    parser.add_argument("--html", help="Path to the saved HTML file.")
    parser.add_argument("--dir", help="Optional folder of HTML files to ingest in batch.")
    parser.add_argument("--url", help="Optional source URL for the job.")
    parser.add_argument("--resume", help="Optional path to the master resume file for future expansion.")
    parser.add_argument("--out", help="Optional output path for the generated markdown summary.")
    parser.add_argument("--judge", action="store_true", help="Review the saved candidate terms and approve selected ones.")
    args = parser.parse_args()

    if args.dir:
        folder = Path(args.dir).expanduser().resolve()
        if not folder.exists() or not folder.is_dir():
            raise SystemExit(f"HTML folder not found: {folder}")
        written = ingest_folder(folder, source_url=args.url)
        for path in written:
            print(f"Wrote {path}")
        return 0

    if not args.html:
        raise SystemExit("Either --html or --dir must be provided.")

    html_path = Path(args.html).expanduser().resolve()
    if not html_path.exists():
        raise SystemExit(f"HTML file not found: {html_path}")

    out_path = Path(args.out).expanduser().resolve() if args.out else None
    written = ingest_html_file(html_path, source_url=args.url, out_path=out_path)
    print(f"Wrote {written}")
    if args.judge:
        judge_terms(html_path.with_suffix(".terms.json"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
