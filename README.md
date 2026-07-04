# Engineering Codex

Personal engineering roadmap and project system.

## Mission

Become an AI-amplified systems engineer who can design, build, debug, and automate systems across software, hardware, infrastructure, and AI.

## Current Focus

1. Engineering OS
2. Python + Linux automation
3. Reliability Lab
4. Home Lab with Intel NUC

## Core Rule

Every skill must produce one of:

1. A documented note
2. A GitHub project
3. A reusable tool
4. A working lab service

## WIP Limit

Maximum active work:

- 1 main project
- 1 learning track
- 1 maintenance task

## Related Existing Work

- `me-and-gpt` - interactive learning system for coding basics and workflow practice
- `automation-validation` - automation and validation work
- `pokemon-battle-sim` - terminal UI and sprite rendering lab
- `pokeshell-animation` - animation experiments for terminal output
- `cpp-performance-notebook` - C++ learning and performance notes

## How This Repo Is Used

- keep the roadmap stable
- keep backlog prioritized
- record active work in weekly notes
- keep each skill tied to a deliverable

## Memory Workflow

Use `memory-context` for session tracking and `engineering-codex` for durable roadmap state.

### What stays in memory-context

- active discussion
- decision drafts
- session summaries
- coding-session checkpoints
- temporary ideas that are not yet committed to the roadmap

### What gets promoted into engineering-codex

- confirmed mission changes
- approved roadmap updates
- backlog items that matter long term
- weekly review outcomes
- stable project notes and templates

### Rule of thumb

If it still needs debate, keep it in `memory-context`.
If it is stable enough to guide future work, write it into `engineering-codex`.

### Example flow

1. Discuss a new project idea in `memory-context`.
2. Decide whether it belongs in the roadmap.
3. If yes, add it to `roadmap/backlog.md` or a project page.
4. Record the session summary in `memory-context`.
