# Career Acceleration - Emerson Process Control Cybersecurity

## Project

**Name:** Process Control Cybersecurity

**Company:** Emerson

**Status:**

- Research

**Priority:** High

**Related Epic:** `00-engineering-os`

## Mission

Turn the supplied job description into the first concrete offer subproject under Career Acceleration.

The purpose of this subproject is to test the fit matrix against a real role in industrial control systems and cybersecurity, then decide what evidence, gaps, and actions matter most.

## Role Summary

This role blends OT, security, customer communication, and validation work.

Core signals from the posting:

- process control systems and cybersecurity tools
- integration testing in control system environments
- risk and threat analysis
- user training and customer-facing communication
- defense-in-depth, privileges, and permissions
- networking, firewalls, routing, switching, and packet analysis
- standards such as ISA99/IEC 62443, NERC, and NIST
- assessments of control systems and surrounding IT infrastructure

## Source Job Description

### Duties And Responsibilities

- implement security tools and solutions in process control systems
- configure, optimize, and test those systems correctly
- perform integration testing of cybersecurity solutions on control system environments
- review customer security procedures and concepts
- analyze risks and threats to process control systems
- train users on supported security products and procedures
- collaborate with senior engineers, consultants, and customers on best practices and security standards
- draft technical and security documentation, controls, and customer packages
- understand customer security concerns and requirements
- perform cybersecurity assessments of control systems and surrounding IT infrastructure
- validate cybersecurity solutions with internal test groups
- give technical advice, recommendations, and presentations to drive customer adoption

### Knowledge, Skills, And Abilities

- 5+ years of OT work with DeltaV execution projects, or 5+ years of IT work with cybersecurity implementation
- 3+ years in DeltaV services, support, FAT, SAT, and commissioning, or 3+ years in cybersecurity solutions and standards
- defense in depth, trust levels, privileges, and permissions
- networking, firewalls, routing, switching, and packet analysis
- SIEM, antivirus, whitelisting, and patch management basics
- ISA99/IEC 62443, NERC, NIST, and related standards
- ability to travel up to 30 percent or more

### Education And Experience

- bachelor’s degree in electrical, electronic, mechatronic, computer engineering, or related field
- experience with industrial control system challenges across multiple industries
- excellent written and verbal communication
- high motivation to work in security and interact with customers
- CCNA, CCNP, CompTIA, or related certification is a plus
- experience in design, implementation, or life cycle support of process automation and control systems

## Interview Prep Workplan

Target interview: Monday 1:00 PM.

Preparation window: Saturday through Monday morning.

Goal:

- become interview-ready by focusing on the highest-value topics instead of trying to master the whole OT field

### Priority Matrix

Priority 1:

- PLCs
- SCADA
- DCS
- DeltaV overview
- networking fundamentals
- defense in depth
- risk assessment
- IEC 62443 basics
- NIST Cybersecurity Framework
- least privilege
- network segmentation
- firewalls
- Windows and Linux basics
- FAT / SAT / commissioning
- STAR stories

Priority 2:

- SIEM
- patch management
- antivirus
- application whitelisting
- Active Directory
- VLANs
- routing
- switching
- packet capture
- VPNs
- secure remote access
- industrial protocols
- zero trust

Priority 3:

- CCNA-level networking refresh
- NERC CIP
- Purdue Model
- ISA95
- OT incident response
- secure remote vendor access
- asset inventory
- security monitoring

### Study Schedule

- Saturday morning: ICS fundamentals and architecture
- Saturday afternoon: DeltaV overview, architecture, lifecycle, and where cybersecurity fits
- Saturday late afternoon: networking fundamentals and packet flow
- Saturday evening: cybersecurity fundamentals and controls
- Sunday morning: industrial cybersecurity standards and segmentation
- Sunday afternoon: Linux, Windows, and Wireshark review
- Sunday evening: STAR stories and behavioral prep
- Monday morning: final review only, no new topics

### Deliverables

- explain ICS components from memory
- explain DeltaV at a high level
- explain packet flow and VLANs
- explain defense in depth and least privilege
- explain why OT differs from IT
- answer behavioral questions with STAR

## Fit Matrix

| Requirement | Evidence | Gap | Action |
| --- | --- | --- | --- |
| Implement security tools and solutions | No direct DeltaV or OT project in the repo yet; adjacent proof is validation-first system work in `projects/circle-detection-hsa.md`, `projects/reliability-lab.md`, and `projects/engineering-codex.md` | Direct DeltaV/OT implementation experience | Say this honestly and bridge from systems validation to industrial control learning |
| Integration testing and validation | Reproducible validation and baseline comparison are central in `projects/circle-detection-hsa.md`; `projects/reliability-lab.md` and `projects/engineering-codex.md` both stress checks and diagnostics | Need control-system examples | Translate validation habits into FAT, SAT, commissioning, and test discipline |
| Review customer security procedures | The repo is documentation-heavy and resumable by design; self-reported strengths include customer support, documentation, and cross-functional collaboration | Need role-specific examples | Use one story about explaining a technical issue to a non-expert |
| Risk and threat analysis | `projects/docs/engineering-os.md` and `projects/docs/architecture.md` emphasize failure modes, debugging first, and evidence over assumptions | Need OT-specific risk framing | Prepare a one-minute risk assessment of remote access into an OT zone |
| Train users and present recommendations | Documentation, planning, and support themes appear across the repo; this matches the role’s communication-heavy expectations | Need direct training or presentation proof | Use one story about teaching or persuading an audience with different technical levels |
| Draft controls and customer documentation | The repo’s core pattern is to create durable notes, project docs, and runnable helpers | Need customer-facing security package examples | Show that you can write concise technical documentation and controls clearly |
| Cybersecurity assessments | The prep plan explicitly covers defense in depth, least privilege, segmentation, and firewalls; self-reported strengths include Linux/Windows troubleshooting and networking | Need concise OT-security phrasing | Explain layered controls and limited access with a zone/conduit example |
| Defense-in-depth and permissions | The prep plan explicitly covers defense in depth, least privilege, segmentation, and firewalls; self-reported strengths include Linux/Windows troubleshooting and networking | Need concise OT-security phrasing | Explain layered controls and limited access with a zone/conduit example |
| Networking and packet analysis | `epics/06-networking.md` covers SSH, ports, HTTP, and service troubleshooting; `projects/docs/academy.md` covers TCP/IP, DNS, VPN, and network debugging | Need packet-level OT examples | Practice packet flow, VLANs, ARP, DNS, TCP handshake, and Wireshark language |
| Security tooling basics | The prep plan includes SIEM, antivirus, whitelisting, patching, and Active Directory; no direct tool-specific repo proof yet | Need practical tooling examples | Learn how to describe monitoring, endpoint protection, and patch discipline at a high level |
| Standards and frameworks | The Emerson role already names IEC 62443, ISA99, NIST CSF, NERC, Purdue, and ISA95 | Need memorized overview, not certification depth | Keep descriptions high level and map them to zones, controls, and response |
| DeltaV / FAT / SAT / commissioning | No direct DeltaV project in the repo yet; adjacent validation and lifecycle support themes exist in the broader repo structure | Need direct DeltaV examples | Be explicit that DeltaV is the learning gap and connect it to validation and lifecycle work |
| Engineering degree and experience fit | Self-reported background includes electrical engineering, Linux, Windows, automation, networking, debugging, and documentation | Need to frame the background around process automation and lifecycle support | Keep the answer honest and specific about adjacent strengths |
| Travel and customer interaction | The role expects up to 30 percent travel and customer-facing work; the repo shows planning, documentation, and support orientation | Need direct travel history / field-service examples | Be ready to say you are comfortable with customer work and field collaboration |

## First Questions

- Which parts of this posting are already credible evidence?
- Which parts are stretch but plausible?
- Which gaps need a learning plan versus a portfolio artifact?
- What single page would make this role easier to apply to?

## Priority 1 Answer Notes

### ICS Core

- OT is the part of computing that runs physical processes, so uptime and safety matter more than flexibility.
- A PLC reads sensors and drives actuators with deterministic control logic close to the machine.
- SCADA supervises, monitors, and sometimes coordinates multiple control assets from a higher level.
- DCS is a distributed control system for process plants where control is spread across controllers and operator stations.
- DeltaV is Emerson’s DCS platform for process control, operator visibility, and lifecycle support.

### DeltaV And Operations

- DeltaV architecture usually includes controllers, engineering workstations, operator stations, historian functions, and redundancy.
- FAT is factory acceptance testing, SAT is site acceptance testing, and commissioning is the transition into live operation.
- Cybersecurity fits around DeltaV by controlling access, segmenting zones, and protecting engineering and operator stations.

### Networking

- Devices talk through IP addresses, ports, DNS, DHCP, ARP, and transport protocols like TCP and UDP.
- VLANs separate broadcast domains, routing moves traffic between networks, and firewalls control allowed flows.
- Packet capture with Wireshark helps confirm what actually happened instead of guessing from symptoms.

### Security

- Defense in depth means no single control is trusted to solve everything.
- Least privilege means users and systems get only the access they need.
- NIST CSF gives a simple frame: identify, protect, detect, respond, recover.
- IEC 62443 is the OT security language for zones, conduits, security levels, and layered controls.
- Risk assessment means naming the asset, threat, impact, likelihood, existing controls, and residual risk.

### Windows, Linux, And STAR

- In Windows and Linux, I should be comfortable talking about users, services, logs, processes, and basic network checks.
- For behavioral answers, use STAR: situation, task, action, result.
- Keep STAR answers concrete and measurable, and end with what changed because of my work.

### Honest Positioning

- I do not yet have direct DeltaV execution-project experience.
- I do have adjacent experience with validation, debugging, documentation, automation, and networking.
- The interview answer should be: I am not claiming direct OT depth I do not have, but I have the engineering habits to close the gap quickly.

## Session 1 Log

### Industrial Control Systems

Session goal:

- understand what an industrial control system is and how the pieces fit together

Topics covered:

- OT
- ICS
- automation
- PLC
- DCS
- SCADA
- HMI
- historian
- sensor
- actuator
- control loop
- OT cybersecurity importance

Working architecture:

```text
           Business Network
                  |
            ----- DMZ -----
                  |
            Control Network
                  |
      +-----------+-----------+
      |                       |
Engineering             Operator
Workstation               HMI
      |                       |
      +-----------+-----------+
                  |
               DCS / PLC
                  |
      +-----------+-----------+
      |                       |
   Sensors               Actuators
      |                       |
      +--------- Process -----+
```

Session outcome:

- created the first ICS mental model for the Emerson interview prep plan
- kept the explanation short enough to recall under interview pressure
- prepared the next step: analogies, real examples, quizzing, and critique

Best responses from Session 1:

- **ICS:** the full hardware, software, network, and people system that monitors and controls a physical process
- **PLC:** a controller that directly runs a local machine or process function, like a valve
- **SCADA:** the supervisory layer that watches distributed control equipment, shows alarms and trends, and can coordinate many PLCs or remote stations
- **DCS:** a distributed control system built for tighter process control inside a plant
- **HMI:** the operator screen that displays plant state and allows control actions
- **Availability in OT:** downtime can affect safety, equipment, and production, not just business data

Next tutor cycle:

- ask for analogies and real industrial examples
- explain the architecture back from memory
- quiz progressively harder
- critique the explanation and identify gaps

## Session 3 Log

### Networking Fundamentals

Session goal:

- understand the networking pieces that let OT devices communicate reliably

Topics introduced:

- IP address
- subnet
- switch
- router
- VLAN
- firewall
- DNS
- DHCP
- ARP
- port
- TCP
- UDP
- NAT
- VPN
- packet capture

Working model:

```text
Device A --> Switch --> Firewall/Router --> Switch --> Device B
                |                           |
               VLAN 10                     VLAN 20
```

Example OT flow:

- HMI requests data from PLC
- PLC responds on the control network
- historian records selected process values
- firewall restricts business network access to approved paths

Session outcome:

- established a first networking mental model for OT communication
- connected networking language to the Emerson role requirements
- prepared the next step: user answers, critique, and harder quiz questions

Next tutor cycle:

- answer the networking quiz questions
- explain packet flow and subnet behavior from memory
- connect networking basics to OT segmentation and security

## Next Actions

- [ ] complete the fit matrix with real evidence
- [ ] identify the strongest supporting projects
- [ ] draft a one-page application angle for this role
- [ ] decide whether this role should become a priority target
- [ ] clean up the current repo state so the Emerson career work is easier to resume
- [ ] work through the interview prep schedule from Saturday through Monday morning
- [ ] turn Priority 1 topics into flashcard-style recall prompts and practice them out loud
- [ ] continue with Session 2 using analogies, real examples, and critique
