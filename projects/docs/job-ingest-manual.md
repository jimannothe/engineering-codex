# Job Ingest Manual

## Purpose

Turn a saved job page into a structured local note without relying on manual retyping or full AI extraction.

The workflow is intentionally semi-manual:

- save the job page HTML
- run the local ingest script
- review the extracted result
- file the note in the jobs system

This keeps the process fast while avoiding browser automation or LinkedIn login automation.

## Files

- Ingest script: [`/home/jman/engineering-codex/scripts/job_ingest.py`](/home/jman/engineering-codex/scripts/job_ingest.py)
- Wrapper command: [`/home/jman/engineering-codex/scripts/job_ingest`](/home/jman/engineering-codex/scripts/job_ingest)
- New-job template: [`/home/jman/engineering-codex/jobs/new-job.md`](/home/jman/engineering-codex/jobs/new-job.md)
- Skill tracker: [`/home/jman/engineering-codex/projects/career-skill-tracker.md`](/home/jman/engineering-codex/projects/career-skill-tracker.md)
- Score comparison report: [`/home/jman/engineering-codex/projects/docs/job-score-comparison.md`](/home/jman/engineering-codex/projects/docs/job-score-comparison.md)

## Inputs

You need:

- a saved LinkedIn job HTML file
- the job URL
- optionally, a note filename for the final markdown output

## Save the Job Page

Save the job page manually from the browser as HTML.

Recommended:

- save the page after opening the full posting
- keep the filename stable and readable
- store it in `projects/jobs/` for raw captures

## Run the Ingest

Use the wrapper command:

```bash
/home/jman/engineering-codex/scripts/job_ingest \
  --html '/home/jman/engineering-codex/projects/jobs/Integration_Engineer_Access_Information_Management_LinkedIn.html' \
  --url 'https://www.linkedin.com/jobs/view/4443049539/' \
  --out '/tmp/job-summary.md'
```

If you omit `--out`, the script writes a `.md` file next to the HTML file automatically.

If you want stdout instead of a file:

```bash
/home/jman/engineering-codex/scripts/job_ingest \
  --html '/home/jman/engineering-codex/projects/jobs/Integration_Engineer_Access_Information_Management_LinkedIn.html' \
  --url 'https://www.linkedin.com/jobs/view/4443049539/'
```

If you want to review and approve candidate new terms:

```bash
printf '1,2\n' | /home/jman/engineering-codex/scripts/job_ingest \
  --html '/home/jman/engineering-codex/projects/jobs/Integration_Engineer_Access_Information_Management_LinkedIn.html' \
  --url 'https://www.linkedin.com/jobs/view/4443049539/' \
  --judge
```

That creates two sidecar files:

- `.../Integration_Engineer_Access_Information_Management_LinkedIn.terms.json`
- `.../Integration_Engineer_Access_Information_Management_LinkedIn.terms.approved.json`

## What the Script Does

- extracts a job header from the saved HTML
- pulls a rule-based skill list from the posting text
- matches the job against the current experience buckets
- writes a markdown summary if `--out` is provided
- writes candidate new terms into a separate `.terms.json` sidecar
- can prompt you to approve selected terms with `--judge`

## Scoring Methods

The ingest script has evolved through a few scoring approaches. The current model is the most reliable for ranking roles because it balances broad skill overlap with named-stack penalties.

| Method | How it scored | Strengths | Weaknesses | Better than |
| --- | --- | --- | --- | --- |
| Keyword overlap only | Counted any matching words in the job text and summed them into a score | Fast and simple | Over-scored noisy pages, rewarded generic words, and produced false positives like `validation` or `integration` | Nothing; this was the first rough draft |
| Broad bucket fit | Grouped keywords into buckets like `Python`, `SQL`, `Validation`, `Troubleshooting`, then scored by overlap with resume experience | Better recall, easier to read, and good for first-pass ranking | Still over-weighted generic words and could not distinguish stack-specific gaps | Keyword-only scoring |
| Section-aware parsing | Read the visible title, company, location, description block, and requirements list first, then scored from that structured text | Much better title and location extraction, and fewer page-chrome false positives | Still needed stronger fit penalties for missing platform-specific tools | Broad bucket fit |
| Specific-tool penalty model | Added explicit penalties for named tools and platforms like `Dell Boomi`, `NetSuite`, `Salesforce`, `ADP`, `ChatGPT Enterprise`, and `Claude` when they appear in the job but not in the resume evidence | Best precision for integration and platform-heavy roles, and scores now reflect real gap size | Slightly stricter, so a few jobs will score lower than before | Section-aware parsing alone |

Practical rule:

- use the current specific-tool penalty model for decision-making
- use older broad scores only as a rough recall signal
- trust a high score only when the job has both broad overlap and named-stack evidence
- distrust any score that is high only because of generic words like `integration`, `validation`, `support`, or `automation`

## Score Ranges

Use the score as a ranking signal, then make the final decision by title, stack, and gap size.

- `80-95`: strong target
- `70-79`: target if the role matches the lane you want
- `60-69`: maybe, only if it is strategically useful or easy to tailor
- `0-59`: usually skip

Suggested decision rule:

- `target` = `70+`
- `maybe` = `60-69`
- `skip` = `<60`

For the Cohesity-style support lane, anything at `65+` is worth a real review, and `75+` is the sweet spot for high-confidence applications.

## Review Step

Always check the generated output before filing it.

Verify:

- company name
- role title
- location
- compensation, if present
- extracted skills
- matched experience
- fit score and why it landed there
- missing named tools or platform-specific evidence

If the header looks wrong, the HTML export is probably noisy or incomplete. Re-save the page and try again.

## Post-Ingest Action Plan

After the ingest is filed, convert the raw summary into a usable job-specific plan.

### Step 1: Build the narrative

- Turn the resume evidence into one coherent story.
- Explain how the current experience connects to the role.
- Keep the story consistent across the job note, resume map, and interview prep.

### Step 2: Rank the role priorities

- Identify what matters most for this specific seniority level.
- Separate the core signals from the nice-to-have keywords.
- Rank the skills, behaviors, and proof points by importance.

### Step 3: Close the highest-value gaps

- Choose only the gaps that materially affect the score or interview likelihood.
- Turn each high-value gap into one proof artifact, lab, or story.
- Avoid broad study that does not strengthen the specific role.

### Step 4: Check the output

- Revisit the score bands.
- Decide whether the role is a target, maybe, or skip.
- Update the resume and interview stories only where the evidence is strong enough.

Use this action plan to turn the ingest into a repeatable career workflow instead of leaving it as a list of extracted terms.

## File the Job Note

After review, create or update a job note under `jobs/`.

Suggested flow:

1. Copy [`jobs/new-job.md`](/home/jman/engineering-codex/jobs/new-job.md)
2. Fill in the job-specific fields
3. Paste the extracted skill list and experience matches
4. Add a fit score and target / maybe / skip decision

## Update the Skill Tracker

If the job adds a new repeated skill, update:

- [`/home/jman/engineering-codex/projects/career-skill-tracker.md`](/home/jman/engineering-codex/projects/career-skill-tracker.md)
- [`/home/jman/engineering-codex/projects/career-acceleration.md`](/home/jman/engineering-codex/projects/career-acceleration.md)

Only increase counts when the skill actually appears in another reviewed job.

For candidate terms, use this rule:

- inspect the `.terms.json` sidecar after ingest
- approve only terms that are clearly transferable technologies, platforms, or tools
- reject page-chrome phrases, generic job wording, and company-specific nouns
- when you approve a term, consider adding it to the skill model or the tracker only if it appears in more than one job

## Rules

- Do not automate LinkedIn login or aggressive scraping.
- Do not trust the first pass blindly.
- Keep the human review step.
- Use the script as a helper, not as the source of truth.

## Quick Checklist

- [ ] save the job HTML
- [ ] run `scripts/job_ingest`
- [ ] review the summary
- [ ] file the job note
- [ ] update the skill tracker if needed
- [ ] commit the change
