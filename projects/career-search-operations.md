# Career Search Operations

## Project

**Name:** Career Search Operations

**Status:**

- Development

**Priority:** High

**Related Epic:** `00-engineering-os`

## Mission

Run the job search like an engineering system.

This project exists to actively source, rank, tailor, apply, and follow up on roles while optimizing for the user’s full set of values, not just raw application count.

The goal is to maximize:

- fit
- compensation potential
- growth
- interview probability
- learning value
- application efficiency
- long-term career leverage

## Operating Principle

Do not apply randomly.

Each role must be scored, compared, and tracked so time goes to the highest-value opportunities first.

## Search Loop

1. Source roles from target companies, recruiter messages, referrals, and search alerts.
2. Compare each role against the current CV and proof set.
3. Score each role against the value model.
4. Classify it as target, maybe, or skip.
5. Build or reuse a fit matrix.
6. Extract the gaps and convert them into an action plan.
7. Tailor resume and outreach material.
8. Apply or contact.
9. Track follow-up, interview state, and outcome.
10. Feed results back into the score model.

## Value Model

Default dimensions:

- role fit
- compensation
- growth
- location or remote fit
- evidence match
- interview probability
- prep cost
- urgency or deadline

### Suggested Ranking Logic

- High fit + high probability + high growth = highest priority
- High compensation but low fit = review carefully
- Low fit and low probability = skip unless strategic
- High effort / low probability = deprioritize

## Offer Triage

### Target

Roles that match the user’s strongest evidence and long-term direction.

### Maybe

Roles that are promising but need more prep, better tailoring, or stronger evidence.

### Skip

Roles that are too far off, too weak, or too costly relative to expected return.

## Daily Loop

- review new roles and recruiter messages
- score each candidate role
- update the active offer list
- draft or refine tailoring for top targets
- send applications or follow-ups
- log new interview questions and gaps

## Weekly Loop

- review pipeline conversion
- inspect which role types are producing responses
- update scoring weights if needed
- identify recurring interview gaps
- prune low-value targets
- plan the next week’s applications and prep

## System Inputs

- job posts
- recruiter messages
- referrals
- portfolio projects
- resume versions
- interview feedback
- current availability

## System Outputs

- ranked opportunity list
- tracked offer subprojects
- tailored applications
- follow-up schedule
- interview prep list
- learning gaps and notes

## Metrics

Track:

- number of roles sourced
- number of roles scored
- number of target roles
- number of applications sent
- number of recruiter responses
- number of interviews
- number of offers
- time spent per application
- response rate by role type

## Risks

- too many low-fit applications
- overinvesting in low-probability roles
- inconsistent follow-up
- stale resume or portfolio materials
- losing context across sessions

## Validation

The system works if:

- roles are ranked before action
- each role is validated against the CV before action
- each gap becomes a concrete next action
- effort goes to the best opportunities first
- application materials are reusable
- results are measurable
- the search can be resumed without losing state

## Links

- `projects/career-acceleration.md`
- `projects/jobs/movable_techSupport.md`
- `templates/career-offer-template.md`
- `CURRENT_CONTEXT.md`
