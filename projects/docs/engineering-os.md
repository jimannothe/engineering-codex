# Engineering OS

## Purpose

Engineering Codex is the operating system for learning, building, reviewing, and improving engineering work.

This guide is the practical standard for using the repo well.

The goal is not more process. The goal is better output with less friction.

## Operating Principles

- Keep the repo useful for a human resuming work later.
- Keep ideas, projects, and decisions in the right place.
- Prefer small, durable artifacts over large, vague notes.
- Build for debugging first, then speed, then scale.
- Let every project teach something reusable.
- Use AI as an amplifier, not as a substitute for engineering judgment.

## GPT-5.5 Usage Standard

Use prompts that are short, explicit, and outcome-first.

- Say what success looks like.
- Say what evidence matters.
- Say what format the result should have.
- Stop when the task is answered well enough.
- Use the smallest useful amount of context.
- For multi-step work, send a short visible update before tool calls.

For model work and generated text, prefer concise prompts and low verbosity when the task does not need a long response.

## Project Workflow

Every project should move through the same sequence:

Idea
Research
Investigation
Planning
Scaffold
Implementation
Testing
Documentation
Review

## Repo Shape

Every project should have a clear and predictable structure.

Recommended baseline:

- `README.md` for the front door
- `CURRENT_CONTEXT.md` for the active state
- `src/` for implementation
- `tests/` for verification
- `docs/` for design and user-facing notes
- `scripts/` for repeatable actions
- `notes/` for working notes

## Project Intake

Use the lightest stage that fits the idea.

- `notes/inbox.md` for raw ideas
- `roadmap/backlog.md` for prioritized ideas
- `projects/*.md` for committed projects
- a template file when the project is ready to be worked

## Investigation Standard

Before changing a system, understand what already exists.

Answer these questions first:

- What is already built?
- What depends on it?
- What is missing?
- What assumptions am I making?
- What can fail?
- What evidence proves the current state?

Do not skip investigation for unclear systems.

## Design Patterns

Use patterns when they reduce coupling, improve testability, or make the structure easier for a human to understand.

### Factories

Use factories when object creation needs to be centralized, parameterized, or swapped cleanly.

Good uses:

- creating different implementations from one interface
- hiding construction complexity
- keeping tests isolated from concrete setup
- selecting adapters, clients, parsers, or backends

Factory rules:

- keep the factory small
- return clear interfaces, not hidden behavior
- make dependencies explicit at the boundary
- avoid factories that only wrap a single constructor with no value

Investigation before adding a factory:

- Is object creation actually complex?
- Will multiple implementations exist?
- Does the pattern improve testability?
- Can a simple function or constructor do the same job?

If the answer to those questions is no, do not add a factory.

### Loggers

Use logging to explain state transitions, failures, decisions, and boundaries.

Logging should help a human debug the system without reading the whole codebase.

### Other Patterns

Use SOLID, dependency injection, adapters, and small interfaces when they make the project easier to understand and test.

Do not add patterns for style alone.

## Testing Standard

Choose the lightest test strategy that gives real confidence.

- unit tests for pure logic
- integration tests for boundaries
- end-to-end tests for workflow-critical paths
- TDD when the behavior is clear enough to specify first

Use tests to prove behavior, not to inflate coverage numbers.

## Git Standard

Use Git so a human can understand how the system evolved.

- keep commits small and meaningful
- use atomic commits when possible
- write commit messages that explain the change
- keep `main` releasable
- tag milestones
- do not hide structural changes inside unrelated edits
- use short-lived branches for active work

## Helper Commands

Make repeated actions command-driven when they are used often enough to matter.

Good command examples:

- add idea
- create project
- update context
- promote backlog item
- run review

Current helper:

- `scripts/cdx context show`
- `scripts/cdx context edit`
- `scripts/cdx context stamp`
- `scripts/devmux status`
- `scripts/devmux context`
- `scripts/devmux git`
- `scripts/mdcheat`
- `scripts/gitcheat`

Commands should be small, predictable, and easy to inspect.

## Validation

Every meaningful change should end with the lightest useful check.

Examples:

- run targeted tests
- run a smoke check
- verify a script output
- inspect the changed files for consistency

If validation is not possible, say why.

For `CURRENT_CONTEXT.md`, include the current date and hour in the `Updated:` line so the newest state is obvious at a glance.

## Definition Of Good Use

The repo is being used well when:

- the current state is obvious
- the next action is obvious
- project structure is consistent
- investigations are recorded
- tests match the risk level
- Git history is easy to follow
- the system is easier to resume next session
