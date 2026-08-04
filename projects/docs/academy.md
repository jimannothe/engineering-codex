# Engineering Academy

## Purpose

Treat the Codex as a self-designed engineering curriculum.

The Academy exists to turn learning into durable capability, not passive consumption.

## Structure

The curriculum is organized into:

- foundations
- laboratories
- projects
- capstones
- research theses

## Learning Progression

Learning should progress through increasing depth:

Idea
Research
Notes
Lab
Prototype
Project
Repository
Portfolio
Career value

Nothing should skip the stages that make it durable.

## Course Design

Each course or track should define:

- learning objectives
- reading list
- labs
- mini projects
- capstone project
- thesis project
- reflection

## Resources

This section tracks the concrete things available for learning, validation, and project work.

Keep the inventory practical and easy to search. Each entry should explain what it is, where it lives, and why it matters.

### Hardware

Include physical equipment used in the repo or related labs:

- devices
- microcontrollers
- PCs
- systems
- development boards
- peripherals
- lab hardware
- current PC
- Intel NUC

For each hardware item, record:

- name
- model or identifier
- location
- purpose
- current status
- relevant notes

Current hardware inventory:

- Current PC: Lenovo `81WA` (`DevelopersDen`) - fill in details later
- Intel NUC - fill in details later

### Library

Include reference material that supports study and implementation:

- books
- manuals
- PDFs
- papers
- vendor documentation
- saved notes or reference collections
- Calibre library titles

For each library item, record:

- title
- author or source
- topic
- location
- why it is useful

Full Calibre title inventory:

- [projects/docs/calibre-library-titles.md](/home/jman/engineering-codex/projects/docs/calibre-library-titles.md)

### Software

Include software assets used for learning and building:

- local tools
- scripts
- packages
- applications
- repos
- utilities
- test harnesses

For each software item, record:

- name
- version or source
- purpose
- where it is installed or stored
- status
- dependencies or special setup notes

## Environment

This section tracks the working environment used to read, write, and operate the repo.

The goal is to keep the toolchain explicit so it can be tuned over time instead of living in memory.

### Core Tools

- `zathura`
- `tmux`
- `nvim`
- shell
- terminal emulator
- window manager or desktop environment

### Suggested Tracking Fields

For each environment tool, record:

- name
- role in the workflow
- config location
- current status
- desired changes
- notes

### Current Intent

Use this section to list the tools that form the daily work environment, then customize them from a known baseline.

Example use:

- `zathura` for reading manuals and PDFs
- `tmux` for persistent terminal sessions
- `nvim` for editing notes, scripts, and docs
- shell aliases and functions for repeated commands

## Codex Software Engineering

This is the software engineering track for the Engineering Codex itself.

The focus is not just writing code. The focus is building a maintainable system that a human can understand, extend, and debug later.

### Core Topics

- repo structure and boundaries
- project intake and promotion
- context handling and session resumption
- modular code organization
- testing strategy by risk level
- logging and observability
- dependency management
- Git history and release discipline
- command-driven workflows

### Practical Standards

- Keep the current state visible.
- Keep the next action obvious.
- Keep project files small and purpose-driven.
- Prefer explicit connections between notes, code, and decisions.
- Use helper commands when they reduce repetitive work.
- Keep behavior easy to verify with tests or checks.

### Git Notes

Use Git to save clean checkpoints, not mixed-up snapshots.

Example recovery flow for a tangled branch:

1. Park everything with `git stash push -u`.
2. Create one branch per topic.
3. Restore the stash.
4. Keep only the files for that topic with `git add -p` or `git restore --staged`.
5. Commit the clean slice.
6. Repeat for the next unrelated change.

If the history is already tangled:

- make a safety backup branch first
- use `git rebase -i` for recent commits
- use a separate worktree when the split is large
- rewrite shared history carefully before force-pushing

### References

Internal:

- `projects/docs/engineering-os.md`
- `projects/docs/architecture.md`
- `projects/docs/foundation.md`
- `templates/project-template.md`
- `templates/project-template-lite.md`
- `CURRENT_CONTEXT.md`

External:

- *A Philosophy of Software Design* by John Ousterhout
- *Refactoring* by Martin Fowler
- *The Pragmatic Programmer* by Andrew Hunt and David Thomas
- *Working Effectively with Legacy Code* by Michael Feathers
- *Clean Architecture* by Robert C. Martin
- official language documentation for the stack used in a project

## Engineering Tracks

- Foundations: Linux, Git, Bash, debugging, algorithms, data structures, mathematics
- Software Engineering: Python, modern C++, SQL, APIs, testing
- Infrastructure: Docker, CI/CD, monitoring, cloud, home lab
- Networking: TCP/IP, DNS, HTTP, VPN, reverse proxies, network debugging
- Validation: automation, logging, metrics, reporting, reliability
- Digital Design: digital logic, Verilog, SystemVerilog, computer architecture, RISC-V, FPGA
- Embedded Systems: STM32, ESP32, sensors, electronics, PCB fundamentals
- Robotics: 3D printer restoration, CAD, mechanical design, quadcopter, autonomous systems
- Artificial Intelligence: machine learning, LLM applications, agents, RAG, automation
- Quantitative Research: statistics, probability, time series, financial data, research automation

## AI Software Design Principles

This section defines how AI should be used in software design work inside the Academy.

The rule is not "use AI everywhere" and not "avoid AI completely." The rule is to use AI where it adds judgment speed, while keeping the structural work local, repeatable, and testable.

### Core Principles

- Use local scripts for parsing, extraction, scoring, tracking, and repeatable workflows.
- Use AI for ambiguity: judgment, ranking, summarization, and story generation.
- Keep the deterministic part of the system outside the model whenever possible.
- Add a human approval step before promoting new skills, new scoring rules, or new claims.
- Treat AI output as a draft unless it has been verified against source material.
- Prefer a small toolchain that can be rerun over a large prompt that must be recreated.
- Save the human-visible state in files and Git, not only in chat history.

### Practical Division of Labor

Scripts should handle:

- HTML and text extraction
- rule-based keyword detection
- candidate term collection
- baseline scoring
- folder iteration and batch processing
- report generation

AI should handle:

- whether a role is truly worth targeting
- how to interpret ambiguous terms in context
- which skills are transferable versus noise
- STAR story drafting
- resume tailoring language
- tradeoff analysis between speed, accuracy, and effort

Human review should handle:

- final skill promotion
- final fit judgment when the score is borderline
- resume claims that affect credibility
- any new scoring rule that changes the model materially

### Learning Objective

After this section, a student should be able to explain:

- why local scripts scale better than prompt-only workflows
- why AI is still useful for judgment and synthesis
- how to design a workflow with a deterministic core and an AI review layer
- when a new term should become a tracked skill and when it should stay a candidate term

### Example Application

For job analysis:

- save the HTML locally
- run the ingest script
- inspect extracted skills and candidate terms
- use AI to evaluate fit and draft stories
- approve or reject new terms manually
- commit the result as a durable checkpoint

## Career Income Optimization Track

This is the career-focused academy track for moving from the current resume into higher-paid roles with the least extra work.

Primary source of truth:

- `epics/23-career-income-optimization.md`
- `projects/study/career-path-optimization.md`
- `projects/career-search-operations.md`

### Purpose

- identify the highest-return roles first
- study only the gaps that actually block interviews
- convert skill gaps into reusable proof
- build a small number of targeted resume variants
- keep the path toward income improvement explicit and measurable

### Default Time Frame

Use a 4-week baseline plan first, then optimize later from results.

- **Week 1:** support and systems fundamentals
- **Week 2:** SaaS support and troubleshooting language
- **Week 3:** validation or QA specialization
- **Week 4:** project proof, resume tailoring, and application push

This time frame is intentionally adjustable. If a lane proves stronger, shorten or extend the plan based on conversion results.

### Study Blocks

#### Support / Systems Block

Study:

- Linux administration basics
- Windows administration basics
- DNS, DHCP, Active Directory, SSH
- PostgreSQL and MongoDB basics
- Apache and Nginx basics
- Jenkins and CI/CD vocabulary
- ticket triage, escalation, and incident handling

#### SaaS Support Block

Study:

- REST vs GraphQL
- OAuth, SAML, SCIM
- browser debugging terms
- HTTP status codes
- logs, HAR files, cookies, and sessions
- customer issue reproduction

#### Validation Block

Study:

- CSV lifecycle
- GxP
- FDA 21 CFR Part 11 and Part 820
- GAMP
- URS, FRS, DS, RTM
- IQ, OQ, PQ, UAT
- change control and risk-based validation

#### QA Block

Study:

- manual testing workflow
- exploratory testing
- test plans and test cases
- reproducible bug reports
- web and API testing basics
- SQL for validation
- CI/CD release-readiness language

### Possible Projects

- support troubleshooting story bank
- resume improvement and STAR story bank
- SaaS issue reproduction notebook
- small web/API test harness
- validation evidence matrix
- manual QA bug-report portfolio
- SQL validation notebook
- resume-tailoring variants by role family
- application tracker with scoring and follow-up

### Milestones

- **Milestone 1:** choose one primary lane
- **Milestone 2:** complete one study block and one proof artifact
- **Milestone 3:** create a tailored resume for the highest-return role family
- **Milestone 4:** apply to the top target roles with the strongest evidence

### Done Criteria

This track is useful when I can:

- explain why a role is target, maybe, or skip
- show one reusable artifact for the chosen lane
- tailor the resume without starting over
- apply to higher-value roles with lower prep cost
- update the plan based on response rate and interview feedback

## Thesis Model

Each track should eventually support a thesis-level project.

The purpose of a thesis is to demonstrate:

- deep understanding
- applied engineering judgment
- the ability to integrate multiple skills
- a result that is reusable or portfolio-worthy

## Learning Standard

Learning is not complete until it can be:

- explained
- built
- debugged
- documented
- taught
- reused

## Academy Outcome

The Academy should continuously produce:

- labs
- projects
- capstones
- research notes
- portfolio artifacts
- better engineering judgment
