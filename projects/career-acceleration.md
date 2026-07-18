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
- offer-specific subprojects
- a fit matrix for each role
- reusable templates for tailoring and follow-up
- outcome tracking

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

## First Example

The first concrete offer example is the Emerson process control cybersecurity role the user supplied.

Working title:

- Emerson Process Control Cybersecurity / OT Security Engineer

Linked subproject:

- `projects/career-acceleration-process-control-cybersecurity.md`

Initial matrix themes:

- OT and process control experience
- cybersecurity tool integration and testing
- defense-in-depth and permissions
- networking, firewalls, and packet analysis
- standards and frameworks such as IEC 62443, NIST, and NERC
- customer communication, training, and documentation

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

## Investigation

Before changing anything answer:

- What roles am I targeting?
- What areas do I want most?
- What existing resume or portfolio material do I already have?
- Which projects are strongest proof for each area?
- What gaps are blocking interviews or offers?
- What can be automated or templatized?

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

External:

- target company job posts
- recruiter messages
- portfolio examples
- interview guides

## Backlog

- [ ] define target role categories
- [ ] list priority companies and postings
- [ ] inventory resume, LinkedIn, and portfolio assets
- [ ] create one template per offer subproject
- [ ] create one template per area strategy track
- [ ] define weekly application cadence
- [ ] define interview prep checklist
- [ ] turn the Emerson process control cybersecurity role into the first tracked offer subproject
- [ ] fill the first fit matrix with evidence, gaps, and actions

## Current Context

Current task:

Create the first tracked offer subproject and fit matrix for the Emerson process control cybersecurity role.

Current blocker:

The target role list is not finalized yet, but the first example role is defined.

Next action:

Draft the first offer matrix and connect it to the main project page.

Estimated time:

1 focused session

## Experiments

Every offer should test a hypothesis:

- Can I tailor a strong application in under one hour?
- Which project evidence gets the most traction?
- Which area produces the strongest response rate?
- Which interview gaps repeat?

## Decisions

- Use one main project to coordinate the job search.
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
- Each offer has a clear next action and status.
- Application materials are easy to tailor.
- I can see which areas are producing results.
- The process is resumable from `CURRENT_CONTEXT.md`.
- The matrix makes the fit and gaps visible before I apply.

## Definition Of Done

The project is complete when:

- target role areas are defined
- offer subprojects are tracked consistently
- materials are reusable and easy to tailor
- interview prep is organized
- results are measurable
- the workflow can be resumed without confusion
