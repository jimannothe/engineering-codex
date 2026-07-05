# AGENTS.md

Repository guidance for using `engineering-codex` efficiently.

## Session Flow

1. Read `README.md` first.
2. Check the relevant area of `roadmap/`, `projects/`, `epics/`, or `weekly/`.
3. Make the smallest change that satisfies the request.
4. Update only the durable source of truth for the change.
5. Keep the user-facing summary short and concrete.

## Efficiency Rules

- Prefer one focused edit over broad cleanup.
- Reuse existing templates before creating new structures.
- Avoid duplicating notes across files.
- Keep work within the current WIP limit:
  - 1 main project
  - 1 learning track
  - 1 maintenance task
- If the request is exploratory, record it in `notes/inbox.md` or `memory-context` first.
- If the request is stable, promote it into `roadmap/`, `projects/`, or a weekly note.

## Writing Rules

- Keep roadmap entries stable and durable.
- Use `templates/project-template.md` for larger efforts.
- Use `templates/project-template-lite.md` for smaller efforts.
- Keep weekly notes factual and brief.
- Use direct language and avoid long retrospective text unless it adds decision value.

## Update Rules

- When a change affects planning, update the relevant roadmap or project file.
- When a change is only discussion or temporary context, keep it out of durable files.
- When you touch a project note, make sure the related epic or roadmap item still matches it.
- If the right home for a change is unclear, stop and ask before writing it.

## Validation

- Prefer a lightweight check that proves the change is correct.
- If no test exists, do a manual consistency check against nearby files.
- Do not invent verification steps that are not relevant to the repository.
