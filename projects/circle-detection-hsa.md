# Circle Detection by Harmony Search Optimization

## Project

**Name:** Circle Detection by Harmony Search Optimization

**Status:**

- Idea

**Priority:** Later

**Related Epic:** `20-ai-engineering`

## Mission

Reproduce and study the circle detection method from the paper *Circle detection by Harmony Search Optimization* and turn it into a small, benchmarkable engineering project.

The goal is to understand the algorithm, compare it against a simpler baseline, and build a reproducible validation workflow around it.

## Engineering Disciplines

- computer vision
- optimization
- validation
- Python or C++
- benchmarking
- reproducible experimentation

## Learning Objectives

After completing this project I should be able to:

- explain the harmony search approach at a practical level
- build a simple circle detection baseline
- reproduce the paper’s core detection pipeline
- compare accuracy and runtime against a baseline
- design experiments for noisy and synthetic images
- document results in a way that another human can follow

## System Overview

The project should include:

- input images
- edge extraction
- candidate circle generation
- harmony search optimization
- scoring / objective function
- baseline comparison
- validation results

## Investigation

Before implementation, answer:

- What exact circle detection pipeline does the paper use?
- What are the search parameters and objective function?
- What baseline will I compare against?
- What image sets will I use for testing?
- What metrics matter most: accuracy, speed, robustness, or all three?

## Research

- [Circle detection by Harmony Search Optimization](https://arxiv.org/pdf/1405.7242)
- OpenCV documentation
- basic circle detection / edge detection references

## Backlog

- [ ] read the paper end to end
- [ ] summarize the algorithm in my own words
- [ ] build a simple baseline detector
- [ ] reproduce the paper’s candidate generation and scoring flow
- [ ] create a synthetic image test set
- [ ] measure accuracy and runtime
- [ ] write a comparison report

## Current Context

Current task:

Define the future circle detection project as a reproducible engineering exercise.

Current blocker:

The implementation language and dataset are not yet chosen.

Next action:

Read the paper carefully and decide whether to implement in Python or C++.

Estimated time:

1-2 research sessions

## Experiments

- run the baseline on synthetic circles first
- add noise and occlusion
- compare against the harmony search version

## Decisions

- Keep the first version simple and reproducible.
- Compare against a baseline before optimizing.
- Prioritize clarity over raw performance at the start.

## Risks

- The paper may be harder to reproduce exactly than it first appears.
- The implementation could become too complex without a clear baseline.
- Poor test data could make the results meaningless.

## Validation

How will I prove the project works?

- The detector finds circles on synthetic images.
- The benchmark is reproducible.
- The baseline comparison is documented.
- A human can rerun the experiment from the repo.

## Documentation

Required docs before this project is considered complete:

- algorithm summary
- baseline description
- benchmark notes
- comparison report

## Definition Of Done

The project is complete when:

- the paper is reproduced in a minimal working form
- the baseline comparison is complete
- the results are documented
- the experiment is repeatable

