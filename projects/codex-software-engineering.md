# Codex Software Engineering

## Project

**Name:** Codex Software Engineering

**Status:**

- Idea

**Priority:** High

**Related Epic:** `00-engineering-os`

## Mission

Define the software engineering standard for Engineering Codex itself.

The goal is to make the repo modular, testable, understandable, and easy to resume after interruption.

This project turns Engineering Codex into a repeatable engineering system instead of a loose collection of notes.

## Engineering Disciplines

- software design
- testing
- Git workflows
- documentation
- logging and observability
- dependency management
- prompt design
- command-line tooling

## Learning Objectives

After completing this project I should be able to:

- define a maintainable repo structure for Codex projects
- choose the right test strategy for a change
- create helper commands for repeated workflows
- explain when a factory, logger, adapter, or interface is actually useful
- keep project state resumable through `CURRENT_CONTEXT.md`
- write Git history that a human can follow

## System Overview

This project defines the operating rules and baseline structure for Codex work.

It should cover:

- project intake
- investigation before modification
- modular project layout
- testing strategy by risk
- design pattern usage
- Git discipline
- helper commands
- validation habits

## System Decomposition

Rules and workflow

↓

Repo structure and templates

↓

Project pages and current context

↓

Helper commands

↓

Testing and validation

↓

Git and release discipline

↓

Human-readable debugability

## Investigation

Before changing anything answer:

- What already exists in the repo?
- Which files are the source of truth?
- What is temporary context versus durable state?
- What should become a project page versus a backlog item?
- What should be automated with a command?
- What needs a unit test, integration test, or both?

## Knowledge Gaps

- [ ] exact helper command surface
- [ ] command implementation location
- [ ] project template defaults for new Codex work
- [ ] testing conventions for non-code notes and docs

## Research

Internal:

- `projects/docs/engineering-os.md`
- `projects/docs/architecture.md`
- `projects/docs/foundation.md`
- `projects/docs/academy.md`
- `templates/project-template.md`
- `templates/project-template-lite.md`
- `CURRENT_CONTEXT.md`

External:

- *A Philosophy of Software Design* by John Ousterhout
- *Refactoring* by Martin Fowler
- *The Pragmatic Programmer* by Andrew Hunt and David Thomas
- *Working Effectively with Legacy Code* by Michael Feathers
- *Clean Architecture* by Robert C. Martin

## Backlog

- [ ] define project skeleton for Codex work
- [ ] define helper commands for ideas, projects, and context
- [ ] define testing strategy by project type
- [ ] define Git workflow and release rules
- [ ] define factory/logger/adapter guidance
- [ ] define investigation checklist for new projects

## Current Context

Current task:

Define the baseline software engineering standard for Engineering Codex.

Current blocker:

The command surface and project template defaults are not yet finalized.

Next action:

Turn the backlog items into concrete repo files and helper commands.

Estimated time:

1-2 focused sessions

## Experiments

- Try one helper command per repeated workflow.
- Try one small project scaffold and validate it with a real project.
- Compare a factory-based design to a simpler constructor-first design before adopting it.

## Decisions

- Keep the standard small enough to follow repeatedly.
- Prefer explicit project pages over hidden process.
- Use patterns only when they reduce complexity for a human reader.

## Risks

- Overengineering the standard before using it.
- Creating too many commands too early.
- Turning documentation into ceremony.

## Validation

How will I prove the project works?

- A new project can be created from the standard without confusion.
- A human can resume work from `CURRENT_CONTEXT.md`.
- The helper command set reduces repetitive editing.
- The repo structure remains understandable after a few sessions.

## Documentation

Required docs before this project is considered complete:

- project standard
- helper command guide
- testing guide
- Git and release guide
- design pattern guidance

## Definition Of Done

The project is complete when:

- the standard exists in the repo
- project intake is repeatable
- helper commands are defined
- testing rules are documented
- Git rules are documented
- a human can understand the project structure quickly

## Future Ideas

- scaffold generator for new projects
- template for project checklists
- command for promoting ideas into projects
- command for syncing `CURRENT_CONTEXT.md`

