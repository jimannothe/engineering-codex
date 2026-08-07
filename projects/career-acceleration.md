# Career Acceleration

## Project

**Name:** Career Acceleration

**Status:**

- Development

**Priority:** High

**Related Epic:** `00-engineering-os`

## Mission

Build a repeatable system for getting hired.

This project turns the job search into an engineering workflow: identify target roles, track each offer as a subproject, produce tailored application materials, and close gaps with focused preparation.

The goal is not random applying. The goal is a controlled pipeline that can be resumed, audited, and improved.

## Engineering Disciplines

- planning
- documentation
- systems thinking
- resume and portfolio design
- software engineering
- automation
- data tracking
- communication
- interview preparation

## Main System

Career Acceleration is the parent project.

It contains:

- area strategy tracks
- career search operations
- offer-specific subprojects
- a fit matrix for each role
- reusable templates for tailoring and follow-up
- career hiring skills and STAR story bank
- outcome tracking
- job ingest, role investigation, narrative building, and gap closure workflows

## Required Skills

This is the current watchlist of the most requested skills across the reviewed jobs.

Use it as a living priority list for study, resume tailoring, and portfolio work.

| Skill | Seen In |
| --- | --- |
| Python | 7 jobs |
| Bash | 4 jobs |
| Documentation | 3 jobs |
| SQL | 3 jobs |
| CI/CD | 3 jobs |
| APIs | 2 jobs |
| SaaS | 2 jobs |
| Networking | 2 jobs |
| Troubleshooting | 2 jobs |
| Manual testing | 2 jobs |
| Web testing | 2 jobs |
| API testing | 2 jobs |
| Agile | 2 jobs |
| Automation | 2 jobs |
| Project management | 2 jobs |
| CSV | 2 jobs |
| Validation | 2 jobs |
| SDLC | 2 jobs |
| Windows Server | 2 jobs |
| DNS | 2 jobs |
| Debugging | 2 jobs |

Priority interpretation:

- `Python`, `Bash`, `documentation`, `SQL`, and `CI/CD` are the broadest overlap skills
- `APIs`, `SaaS`, and `troubleshooting` are the strongest bridge skills for support and automation roles
- `manual testing`, `API testing`, and `web testing` matter mainly for the QA lane
- `CSV`, `Validation`, `SDLC`, and `project management` matter mainly for regulated validation roles

Update rule:

- add a skill when it appears in a new reviewed job
- increase its count when the skill appears again
- keep the list ordered by frequency, then by strategic value
- move skills into separate lane-specific sublists only when a lane becomes dominant

## Learning Objectives

After completing this project I should be able to:

- [ ] define target roles by area and seniority
- [ ] convert each job offer into a tracked subproject
- [ ] tailor resume, portfolio, and cover materials efficiently
- [ ] maintain a clean application pipeline with clear next actions
- [ ] measure which roles and companies produce the best response

## System Decomposition

Career strategy

↓

Target areas

↓

Target companies and offers

↓

Offer-specific subprojects

↓

Tailored materials

↓

Interviews and follow-up

↓

Result tracking and iteration

## Matrix Model

Every offer should be translated into a fit matrix before applying.

The matrix should answer:

- what the job asks for
- what proof I already have
- what is missing
- what needs to be built, learned, or rewritten

After the matrix, each offer should also be:

- scored against the current CV
- assigned a target / maybe / skip decision
- converted into a gap list
- converted into a concrete action plan

This is the standard loop for every position.

## Offer Workflow

Use this sequence for every new role.

1. Ingest the job posting into a structured note.
2. Investigate similar positions to understand the real work, common expectations, and adjacent role patterns.
3. Validate the role against the current CV and proof set.
4. Score the role and classify it as target, maybe, or skip.
5. Build a narrative from current experience that explains why the role fits.
6. Rank the most important aspects of the position for that seniority level.
7. Turn only the highest-value gaps into labs, stories, or proof artifacts.
8. Tailor the resume and interview prep from the resulting evidence.

## Default Prep Workflow

For career-helper work, especially technical interview prep for an offer subproject, use Codex as an interactive tutor instead of asking for a long standalone chapter.

Default cycle:

1. Generate a concise explanation, usually 1 to 2 pages.
2. Ask for analogies and real industrial examples.
3. Draw the architecture or system yourself.
4. Have Codex quiz you with progressively harder questions.
5. Explain the topic back in your own words.
6. Ask Codex to critique the explanation and identify gaps.

Use this cycle by default when working on this type of career-helper project.

## First Example

The first concrete offer example is the Movable Ink Technical Support Specialist role.

Working title:

- Movable Ink Technical Support Specialist

Linked subproject:

- `projects/jobs/movable_techSupport.md`

Initial matrix themes:

- technical support ownership
- troubleshooting and root cause analysis
- documentation and knowledge sharing
- web app and browser debugging
- APIs, auth, and relational data
- customer communication and escalation handling

## Offer Model

Each offer becomes its own subproject.

Suggested fields:

- company
- role title
- area
- level
- location or remote status
- application date
- status
- next action
- deadline

## Area Model

Each area gets its own strategy track.

Example areas:

- software engineering
- embedded systems
- DevOps / SRE
- validation / automation
- AI engineering
- hardware-adjacent systems

## Search Operations

Use `projects/career-search-operations.md` as the active search engine.

It handles:

- sourcing
- scoring
- ranking
- tailoring
- applying
- follow-up
- feedback loops

The search should be optimized across multiple values:

- fit
- compensation
- growth
- probability
- effort
- learning value

The search system should bias toward the highest expected return per unit time, not the largest number of applications.

For each role, the search system should run this loop:

1. Compare the role against the current CV.
2. Extract the evidence match and the missing pieces.
3. Score the role.
4. Convert the gaps into a concrete action plan.
5. Decide whether to apply, prep, or skip.

## Investigation

Before changing anything answer:

- What roles am I targeting?
- What areas do I want most?
- What existing resume or portfolio material do I already have?
- Which projects are strongest proof for each area?
- What gaps are blocking interviews or offers?
- What can be automated or templatized?

For each offer, also investigate similar positions before finalizing the action plan:

- What do comparable roles at adjacent companies actually emphasize?
- What recurring duties show up across the same job family?
- What does the real day-to-day support workflow look like?
- What investigation, documentation, or escalation behavior is expected?
- Which missing skills are truly blocking versus just nice-to-have?

Use the comparison to keep the target role grounded in market reality rather than one posting's wording.

## Knowledge Gaps

- [ ] target role list
- [ ] strongest resume version
- [ ] portfolio evidence for each area
- [ ] interview prep gaps
- [ ] application tracking structure

## Research

Internal:

- `templates/project-template.md`
- `templates/project-template-lite.md`
- `CURRENT_CONTEXT.md`
- `roadmap/backlog.md`
- `projects/docs/job-ingest-manual.md`

External:

- target company job posts
- recruiter messages
- portfolio examples
- interview guides

## Backlog

- [ ] define target role categories
- [ ] list priority companies and postings
- [ ] inventory resume, LinkedIn, and portfolio assets
- [ ] define weighted scoring for target roles
- [ ] add CV validation to every offer subproject
- [ ] add similar-role investigation to every offer subproject
- [ ] add gap-to-action planning to every offer subproject
- [ ] add narrative building to every offer subproject
- [ ] add priority analysis to every offer subproject
- [ ] create a ranked target list with target/maybe/skip labels
- [ ] connect recruiter messages to the search operations system
- [ ] create one template per offer subproject
- [ ] create one template per area strategy track
- [ ] define weekly application cadence
- [ ] define interview prep checklist
- [ ] build the career hiring skills project
- [ ] turn the Movable Ink technical support role into the first tracked offer subproject
- [ ] apply the same loop to the Cohesity support role and future offer subprojects
- [ ] fill the first fit matrix with evidence, gaps, score, and actions

## Current Context

Current task:

Build the active job-search operating system and connect it to the Movable Ink offer subproject.

Current blocker:

The target role list is not finalized yet, but the first example role and the active search system are defined.

Next action:

Use the search operations system to rank the next set of roles and then draft the next highest-value offer matrix.

Estimated time:

1 focused session

## Experiments

Every offer should test a hypothesis:

- Can I tailor a strong application in under one hour?
- Which project evidence gets the most traction?
- Which area produces the strongest response rate?
- Which interview gaps repeat?

Every search cycle should test a hypothesis:

- Does the scoring model route time toward better opportunities?
- Which job families produce the best response rate?
- Which resume angle gets the strongest replies?
- Which prep topics create the biggest interview lift?

## Decisions

- Use one main project to coordinate the job search.
- Use a separate search operations system to rank and route work.
- Treat each offer as a subproject instead of a one-off application.
- Organize strategy by area so the search stays focused.
- Prefer reusable templates over rewriting the same materials.

## Risks

- scope creep from too many target roles
- weak tailoring because of rushed applications
- poor tracking leading to repeated mistakes
- spending too much time on low-probability offers

## Validation

How will I prove this project works?

- I can create a new offer subproject from the template.
- I can rank roles before spending time on them.
- I can investigate similar roles and explain what the job actually looks like.
- Each offer has a clear next action and status.
- Each offer has a narrative and a priority analysis before I close gaps.
- Application materials are easy to tailor.
- I can see which areas are producing results.
- The process is resumable from `CURRENT_CONTEXT.md`.
- The matrix makes the fit and gaps visible before I apply.

## Definition Of Done

The project is complete when:

- target role areas are defined
- the search operations system is in use
- offer subprojects are tracked consistently
- materials are reusable and easy to tailor
- similar-role investigation is part of the flow
- narrative building and priority analysis happen for each offer
- interview prep is organized
- results are measurable
- the workflow can be resumed without confusion
