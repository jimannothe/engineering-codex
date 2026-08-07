# Git Branch Strategy

## Purpose

This document defines the Git branching strategy for the Engineering Codex repository.

The objective is to:

- keep `main` stable
- allow multiple large projects to evolve independently
- avoid long-lived feature branches becoming alternate repositories
- maintain a clean commit history
- make collaboration predictable
- ensure every project follows the same development workflow

## Core Philosophy

The repository consists of permanent folders and temporary branches.

Folders represent knowledge and project organization.

Branches represent work in progress.

A folder may exist forever.

A branch should eventually disappear after it is merged or intentionally retired.

## Repository Hierarchy

The repository is organized by folders such as:

- `docs/`
- `notes/`
- `projects/`
- `roadmap/`
- `scripts/`
- `templates/`
- `weekly/`
- `tracks/`
- `labs/`
- `references/`

Everything eventually belongs in `main`.

## Branch Hierarchy

Use three levels of branches:

- `main`
- integration branches
- task branches

## Level 1 - Main Branch

`main` is the stable Engineering Codex.

It should contain:

- documentation
- learning tracks
- labs
- projects
- templates
- stable tooling

Nothing experimental should remain here.

Every completed project should eventually merge into `main`.

## Level 2 - Integration Branches

Each major project receives one integration branch.

Examples:

- `feat/career-helper`
- `feat/infrastructure-track`
- `feat/ot-security-track`
- `feat/engineering-os`

These branches integrate multiple related features before they are merged into `main`.

They are not permanent.

## Level 3 - Task Branches

Every feature should be developed in its own branch.

Examples:

- `feat/career-helper/job-parser`
- `feat/career-helper/cv-parser`
- `feat/career-helper/scoring-model`
- `feat/career-helper/report-generator`
- `fix/career-helper/duplicate-skills`
- `test/career-helper/scoring`
- `docs/career-helper/architecture`

Each task branch should represent one reviewable deliverable.

## Branch Philosophy

- folders are permanent knowledge and project organization
- branches are temporary work in progress
- every completed task branch should eventually disappear after merge
- everything eventually belongs in `main`

## Practical Rules

- keep `main` stable
- use one integration branch per major project or learning track
- use one short-lived task branch per deliverable
- keep unrelated work out of project branches
- name branches after the work being done, not the files being edited
- commit at logical checkpoints, not after every tiny edit
- keep each commit small enough to review and revert cleanly
- avoid giant mixed commits and ultra-tiny meaningless commits

## Mental Model

```text
working tree -> index -> commit -> branch ref -> HEAD
```

## Suggested Workflow

1. Create or switch to the right integration branch.
2. Create a task branch for one deliverable.
3. Make a clean, reviewable commit.
4. Merge back into the integration branch.
5. Merge the integration branch into `main` when the milestone is done.
6. Delete the task branch after merge.

## Commit Convention

Use Conventional Commits.

Examples:

- `feat(storage): add RAID fundamentals`
- `feat(network): add tcpdump lab`
- `docs(infrastructure): add roadmap`
- `fix(career-helper): correct scoring logic`
- `test(parser): add parser regression tests`
- `refactor(templates): standardize module layout`

## Branch Size Guidelines

A branch should represent exactly one logical deliverable.

Good:

- `feat/linux-processes`
- `feat/linux-memory`
- `feat/linux-debugging-tools`
- `feat/storage-lvm`
- `feat/storage-raid`
- `feat/storage-nfs`

Avoid:

- `feat/complete-linux-track`

Large branches are difficult to review, merge, and maintain.

## Experiment Branches

Temporary research belongs in experiment branches.

Examples:

- `experiment/ftrace-context-switches`
- `experiment/raid-failure-simulation`
- `experiment/nfs-performance`
- `experiment/linux-boot-analysis`

Possible outcomes:

- delete
- convert into documentation
- convert into a clean feature branch

Never merge messy experiments directly into `main`.

## Versioning

Do not create release branches.

Instead use Git tags.

Examples:

- `v0.1.0`
- `v0.2.0`
- `v0.3.0`
- `v0.4.0`
- `v1.0.0`

## Current Branch Cleanup

Branch names should describe work, not files.

Bad:

- `feat/academy.md`

Good:

- `docs/academy-roadmap`

## Golden Rules

1. `main` is the stable Engineering Codex.
2. One integration branch per major project or learning track.
3. One short-lived task branch per deliverable.
4. Keep unrelated work out of project branches.
5. Folders are permanent; branches are temporary.
6. Merge completed milestones into `main` rather than allowing long-lived branches to become separate repositories.
7. Prefer many small, reviewable branches over a few large, long-lived ones.
8. Use branch names to describe the work being performed, not the files being modified.
