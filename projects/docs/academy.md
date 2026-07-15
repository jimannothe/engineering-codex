# Engineering Academy

## Purpose

Treat the Codex as a self-designed engineering curriculum.

The Academy exists to turn learning into durable capability, not passive consumption.

## Academy Model

The curriculum is organized along two dimensions:

- Vertical Engineering Disciplines
- Horizontal Engineering Sciences

Every project should combine multiple vertical disciplines and apply one or more horizontal sciences.

## Learning Progression

Learning should progress through increasing depth:

Idea -> Research -> Notes -> Lab -> Prototype -> Project -> Repository -> Portfolio -> Career value

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

## Vertical Engineering Disciplines

These represent technologies and domains.

- Foundations: Linux, Git, Bash, debugging, algorithms, data structures, mathematics
- Software Engineering: Python, modern C++, SQL, APIs, testing
- Infrastructure: Docker, CI/CD, monitoring, cloud, home lab
- Networking: TCP/IP, DNS, HTTP, VPN, reverse proxies, network debugging
- Validation Engineering: automation, performance, reliability, logging, metrics, benchmarking
- Digital Systems: digital logic, Verilog, SystemVerilog, computer architecture, RISC-V, FPGA
- Embedded Systems: STM32, ESP32, sensors, electronics, PCB design
- Robotics: mechanical design, CAD, motion control, 3D printer, quadcopter, autonomous robotics
- Artificial Intelligence: machine learning, deep learning, LLM applications, AI agents, RAG
- Quantitative Engineering: statistics, probability, time series, financial engineering, research automation

## Horizontal Engineering Sciences

These apply across every discipline.

### Systems Thinking

- Topics: decomposition, abstraction, interfaces, modularity, system boundaries, trade-offs
- Deliverable: complete systems instead of isolated programs

### Software Architecture

- Topics: SOLID, design patterns, dependency injection, factories, adapters, repositories, layered architecture, hexagonal architecture, event-driven design
- Deliverable: every project has an Architecture document

### Optimization Engineering

- Topics: objective functions, constraints, search spaces, convergence, benchmarking
- Algorithms: Hill Climbing, Gradient Descent, Simulated Annealing, Genetic Algorithms, Harmony Search, Particle Swarm Optimization, Differential Evolution, Bayesian Optimization, Multi-objective Optimization
- Applications: computer vision, validation, scheduling, robotics, control systems, embedded systems, AI hyperparameter optimization, resource allocation
- Capstone: a modular Optimization Framework with interchangeable algorithms
- Thesis: an Autonomous Engineering Optimization Platform for solving constrained engineering problems

### Performance Engineering

- Topics: profiling, benchmarking, latency, throughput, memory, cache, concurrency

### Reliability Engineering

- Topics: fault tolerance, resilience, monitoring, observability, recovery, validation, verification

### Testing Science

- Topics: unit testing, integration testing, system testing, property testing, regression testing, fuzzing, TDD
- Rule: each project chooses the right testing strategy instead of applying one blindly

### Debugging Science

- Topics: root cause analysis, binary search debugging, instrumentation, tracing, logging, reproducibility
- Deliverable: every project has a debugging guide

### Engineering Research

- Topics: reading papers, reproducing papers, experimental design, hypothesis testing, statistics, scientific writing
- Rule: every paper or paper-driven spike uses a standard review template

### Engineering Methodology

- Topics: Git workflow, project planning, architecture decision records, documentation, AI workflow, versioning, code reviews, release management
- Rule: Engineering Codex itself follows this methodology

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

## Project Matrix

Every project should declare:

- vertical disciplines involved
- horizontal sciences applied
- target deliverable
- validation strategy

Example:

- Project: Reliability Lab
- Vertical: Python, Linux, SQL, Networking
- Horizontal: Software Architecture, Optimization Engineering, Testing Science, Reliability Engineering, Debugging Science, Performance Engineering

This keeps the Academy interconnected instead of a collection of isolated courses.

## References

### Internal

- `projects/docs/engineering-os.md`
- `projects/docs/architecture.md`
- `projects/docs/foundation.md`
- `templates/project-template.md`
- `templates/project-template-lite.md`
- `CURRENT_CONTEXT.md`

### External

- *A Philosophy of Software Design* by John Ousterhout
- *Refactoring* by Martin Fowler
- *The Pragmatic Programmer* by Andrew Hunt and David Thomas
- *Working Effectively with Legacy Code* by Michael Feathers
- *Clean Architecture* by Robert C. Martin
- official language documentation for the stack used in a project

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
