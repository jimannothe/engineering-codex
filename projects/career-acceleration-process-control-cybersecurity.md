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

### DeltaV Overview

- DeltaV is Emerson’s distributed control system for process control and plant operations.
- It is used to monitor, control, and coordinate industrial processes with a focus on reliability and operator visibility.
- The main pieces are usually controllers, engineering workstations, operator stations, historian functions, and redundancy where needed.
- Engineers configure logic, graphics, alarms, and control strategies; operators use the system to monitor the plant and respond to process conditions.
- In interview terms, the key point is that DeltaV is not just software. It is part of the live control environment, so change management, validation, and access control matter.

### DeltaV Lifecycle

- **FAT:** verify the system in a controlled environment before site delivery.
- **SAT:** verify the installed system at the customer site.
- **Commissioning:** bring the system into live operation carefully and in stages.
- **Maintenance:** preserve reliability while managing changes safely.
- **Cybersecurity fit:** protect engineering stations, restrict remote access, segment networks, and make sure security changes do not break operations.

### DeltaV Talk Track

> DeltaV is Emerson’s DCS platform for process control. At a high level it includes controllers, engineering workstations, operator stations, historian functions, and redundancy where needed. Engineers use it to configure logic, graphics, alarms, and control strategies, while operators use it to monitor and manage the plant. For cybersecurity, the important part is that DeltaV sits in a live operational environment, so access control, segmentation, validation, and careful change management matter a lot.

### Networking

- Devices talk through IP addresses, ports, DNS, DHCP, ARP, and transport protocols like TCP and UDP.
- VLANs separate broadcast domains, routing moves traffic between networks, and firewalls control allowed flows.
- Packet capture with Wireshark helps confirm what actually happened instead of guessing from symptoms.

### Industrial Protocols

- **Modbus:** simple industrial communication protocol often used for device registers and basic control data.
- **OPC / OPC UA:** common interoperability layer for exchanging industrial data between systems.
- **EtherNet/IP:** industrial protocol used in automation environments over Ethernet.
- **PROFINET:** industrial Ethernet protocol used in manufacturing and process environments.
- **DNP3:** protocol often associated with utilities and remote telemetry.
- **Interview framing:** you do not need to be a protocol expert here. You need to explain that different industrial protocols move process data between controllers, HMIs, historians, and supervisory systems, and that security controls must not break that communication path.

### Additional Interview Questions

- **Lab or generic OT matrix placeholder:** use an industrial application protocol such as Modbus TCP or OPC UA, then note that the port depends on the protocol.
- **Example ports:** Modbus TCP typically uses TCP 502; OPC UA commonly uses TCP 4840.
- **HMI to SCADA flow:** the HMI talks to SCADA using the plant's approved industrial application protocol, and the exact port depends on the vendor and system design.

### Networking Talk Track

> OT networks still rely on the same basic building blocks as IT networks: IP addresses, ports, routing, switching, DNS, DHCP, ARP, and packet flow. The difference is that the traffic often carries industrial protocol data between controllers, HMIs, historians, and supervisory systems, so segmentation and firewall rules have to be designed around reliable operation.

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

## Session 2 Log

### Industrial Control Systems Through Analogies

Session goal:

- make the ICS model easier to remember under pressure

Analogies:

- **PLC:** the reflexes of a machine, handling local control quickly and predictably
- **SCADA:** the control room dashboard that watches many assets and surfaces alarms and trends
- **DCS:** the coordinated plant-wide control system where control is distributed but still managed together
- **HMI:** the operator display that shows status and accepts commands
- **Historian:** the logbook that records important process data over time
- **Sensor:** the instrument that measures what is happening in the process
- **Actuator:** the device that changes the process, like a valve or motor

Real examples:

- a tank level sensor reports to a PLC, and the PLC opens or closes a valve
- an operator uses an HMI to acknowledge an alarm and view trends
- a historian stores temperature or pressure values for later analysis
- a SCADA system watches multiple remote sites from a supervisory layer

Session outcome:

- the ICS pieces are easier to remember when tied to roles in a plant
- the model now maps to real equipment instead of abstract acronyms
- the next step is to test where the analogies break so the explanation stays accurate

Critique:

- a PLC is not just “a brain”; it is a controller with deterministic logic and I/O
- SCADA is supervisory, not the same thing as the controlled equipment
- a historian stores data, but it does not directly control the process
- DCS and SCADA overlap in conversation, but they are not identical

Next tutor cycle:

- explain the ICS system from memory using the analogies
- identify where each analogy fails
- connect the model to cybersecurity concerns in an OT environment

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

## Session 3 Quiz Log

### Best Responses

- **Switch vs router:** a switch forwards frames within a LAN using MAC addresses, while a router moves traffic between different networks using IP addresses.
- **DNS:** DNS translates names into IP addresses, which matters in OT because HMIs, historians, and engineering stations often rely on hostnames.
- **ARP:** ARP maps an IP address to a MAC address on the local network.
- **TCP vs UDP:** TCP is reliable and connection-oriented; UDP is connectionless and lighter-weight.
- **VLAN:** a VLAN is a logical network segment on shared switching infrastructure, useful for separating OT zones or groups of devices.
- **Firewall:** a firewall enforces allowed traffic between networks or zones; it is not a replacement for segmentation.
- **Packet capture:** packet capture records actual network traffic so you can see what is happening instead of guessing from logs alone.

### Corrections From Quiz Feedback

- a switch is Layer 2, not Layer 22
- a router connects networks; it does not generally “handle connection requests”
- DNS maps names to IPs, not “IP to URL”
- TCP is not secure by default; it is reliable and connection-oriented
- VLANs segment networks, while firewalls enforce traffic policy
- packet capture is the debugging method, not Packet Tracer

### Harder Follow-Up Questions

- A PLC and HMI are on the same subnet but cannot talk. Name three likely causes.
- Why is segmentation especially important between business IT and control networks?
- How would Wireshark help you debug a communication issue without guessing?

### Session 3 Answers

- If a PLC and HMI are on the same subnet but cannot talk, likely causes include a bad cable or disabled switch port, a VLAN or port-isolation mismatch, a duplicate or incorrect IP setup, or an endpoint that is powered off or not responding.
- Segmentation is important because business IT and control networks have different risk and uptime requirements. Separating them limits blast radius, reduces exposure to untrusted traffic, and helps keep OT communication predictable.
- Wireshark helps by showing actual packets and timing. It can confirm whether ARP resolves, whether TCP handshakes complete, whether there are retransmissions or resets, and whether the issue sits at the network layer or in the application protocol.

## Session 3 Next Step

- answer the three follow-up questions above
- tie the answers to OT segmentation and troubleshooting
- keep the response short enough to use in an interview

## Session 4 Log

### Cybersecurity Fundamentals And Controls

Session goal:

- connect basic security language to OT and process control environments

Topics covered:

- defense in depth
- least privilege
- zones and conduits
- firewalls
- NIST Cybersecurity Framework
- IEC 62443
- availability, safety, and change control

Working model:

```text
Business Network -> DMZ -> OT Zone -> Control System
        |             |        |           |
     users/data   jump hosts  firewalls   PLC/HMI/SCADA
```

Best responses:

- **Defense in depth:** use multiple layers of protection so one failed control does not expose the whole system
- **Least privilege:** give users and systems only the access they need for the task
- **Zones and conduits:** separate systems into groups with controlled paths between them
- **NIST CSF:** identify, protect, detect, respond, recover
- **IEC 62443:** the OT security framework for zones, conduits, and layered controls
- **OT vs IT:** OT cares deeply about uptime, safety, and controlled change, not just confidentiality

Practical examples:

- a jump host in a DMZ limits direct access to control systems
- a firewall allows only approved flows between business and control networks
- read-only access is safer than broad admin access when full control is not needed
- patching in OT must be planned because untested change can interrupt operations

Critique:

- a firewall alone is not defense in depth
- segmentation is not enough if credentials are over-privileged
- availability and safety can outweigh convenience in OT
- security controls must fit the process and maintenance window, not the other way around

Next tutor cycle:

- explain OT security controls from memory
- map a simple zone-and-conduit example to Emerson
- give a one-minute answer on why OT differs from IT

### Session 4 Answers

- **Defense in depth:** use multiple layers of protection so one failed control does not expose the whole system
- **Least privilege:** give users and systems only the access they need for the task
- **Zones and conduits:** separate systems into groups with controlled paths between them
- **NIST CSF:** identify, protect, detect, respond, recover
- **IEC 62443:** the OT security framework for zones, conduits, and layered controls
- **OT vs IT:** OT cares deeply about uptime, safety, and controlled change, not just confidentiality

One-minute OT security answer:

> In OT, security has to protect the process, not just the data. I would start with defense in depth, so no single control is trusted on its own. I would segment the environment into zones with only approved conduits between them, then enforce least privilege with read-only access where possible and tightly controlled admin access where needed. IEC 62443 gives the OT language for zones, conduits, and layered controls, while NIST CSF helps organize identify, protect, detect, respond, and recover. The key difference from IT is that uptime, safety, and controlled change often matter as much as confidentiality.

Emerson zone-and-conduit example:

- business users and enterprise systems stay on the business network
- a jump host in the DMZ provides controlled access into OT
- a firewall allows only approved flows into the OT zone
- PLCs, HMIs, and SCADA assets remain inside the control system zone
- vendor or engineer access is time-bounded and logged rather than open-ended

## Session 5 Log

### Cybersecurity Specifics For OT

Session goal:

- turn the general OT security model into concrete control points an interviewer can ask about

Topics covered:

- asset inventory
- network segmentation
- jump hosts
- remote vendor access
- identity and privileges
- logging and monitoring
- patching and change windows
- backups and recovery
- removable media control
- endpoint hardening

Working model:

```text
Business IT -> DMZ -> Jump Host -> OT Zone -> Controllers / HMIs / Historians
                  |         |           |
             logging/SIEM  MFA    firewall rules
```

Best responses:

- **Asset inventory:** you cannot secure what you do not know exists, so OT needs an accurate list of controllers, HMIs, engineering stations, historians, network gear, and vendor connections
- **Segmentation:** keep business IT, DMZ, and control networks separated so the blast radius stays small and traffic stays predictable
- **Jump host:** use a controlled entry point for admin or vendor access instead of letting people connect directly into the control network
- **Identity and privileges:** use named accounts, MFA where possible, and tightly scoped access instead of shared or over-privileged credentials
- **Logging and monitoring:** collect enough logs to see who connected, what changed, and what traffic was allowed, but avoid tooling that creates instability in the control environment
- **Patching:** patch on a planned schedule with testing and maintenance windows because an untested change can interrupt operations
- **Backups and recovery:** keep recoverable configurations, images, and restore procedures so the plant can return to a known good state
- **Removable media:** treat USB and portable media as a risk and control them with scanning, approval, and process rules
- **Endpoint hardening:** disable unnecessary services, restrict software, and protect engineering workstations because they often have broad control access

Practical examples:

- a vendor connects through a jump host in the DMZ, not directly to a PLC network
- a firewall only allows approved ports and protocols between zones
- an engineering workstation uses a named account with admin rights only when needed
- backup copies of controller and workstation configs are kept so recovery is possible after a bad change
- USB media is scanned before it enters the OT environment

Critique:

- monitoring should not break a live process
- segmentation is weak if credentials are shared or unmanaged
- patching without testing can be more dangerous than delaying the patch
- recovery planning matters as much as prevention in OT

Next tutor cycle:

- explain the OT cyber controls in one minute
- give a simple example of remote access into a plant
- answer how you would handle patching without disrupting production

### Session 5 Answers

- **Asset inventory:** keep an up-to-date list of OT devices, software, versions, dependencies, and connections so security work is based on reality
- **Segmentation:** isolate business, DMZ, and OT traffic so a problem in one area does not spread into the control system
- **Jump host:** a jump host is a controlled gateway that brokers access into OT, usually with logging and tighter access rules
- **Identity and privileges:** use individual accounts, strong authentication, and only the access needed for the task
- **Logging and monitoring:** log access and security events so you can reconstruct what happened without disturbing operations
- **Patching:** plan, test, and schedule patches because OT change management has to protect uptime and safety
- **Backups and recovery:** keep known-good backups and a restore process so the environment can be recovered after a failure or bad change
- **Removable media:** scan and control USB devices because portable media is a common OT infection path
- **Endpoint hardening:** reduce exposed services and applications on engineering and operator stations to cut attack surface

One-minute OT cyber answer:

> I would secure an OT environment by treating it as a live operational system, not a standard office network. The basics are accurate asset inventory, network segmentation, controlled remote access through a jump host, named accounts with least privilege, and logging that shows who did what without destabilizing the process. Patch management has to be scheduled and tested because downtime or a bad update can affect production and safety. I would also keep backups, control removable media, and harden engineering workstations because those are high-value entry points in OT.

## Session 6 Log

### Final Recall Drill

Session goal:

- compress the core OT security and ICS answers into short interview-ready language
- identify any answers that drifted too generic or too IT-like
- prepare the final mock interview around the hardest likely questions

What was drilled:

- remote vendor access
- OT asset inventory
- defense in depth
- least privilege
- OT vs IT
- IEC 62443
- zone and conduit model
- PLC vs HMI
- SCADA vs DCS
- historian
- firewall
- jump host
- FAT vs SAT
- commissioning
- risk assessment
- NIST CSF vs IEC 62443
- VLANs
- packet capture
- segmentation plus firewalls

Best final answers captured:

- **Remote vendor access:** terminate in a controlled DMZ, preferably through a jump host, with named accounts, strong authentication, logging, and time-bounded approval
- **Asset inventory:** you cannot protect what you cannot see, so track controllers, HMIs, engineering workstations, historians, network gear, versions, dependencies, and vendor links
- **Defense in depth:** use multiple layers so one failure does not expose the process
- **Least privilege:** give only the access needed for the task
- **OT vs IT:** OT must protect uptime, safety, and controlled change, not just confidentiality
- **IEC 62443:** the OT security framework for zones, conduits, access control, and layered protections
- **VLANs:** logical segmentation, not security by itself
- **Packet capture:** evidence of what the network actually did

Critique targets:

- avoid saying firewall alone solves an OT security problem
- avoid treating a historian like a security log system
- avoid calling a DCS just a list of devices
- keep every answer focused on process, reliability, and controlled change

## Behavioral Prep

These are draft STAR stories. Keep them honest and swap in stronger real examples if a better one exists.

### Story 1: Turning Ambiguity Into A System

- **Situation:** the career search was broad and hard to manage as a one-off list of jobs.
- **Task:** turn it into a repeatable system with clear subprojects, matrices, and next actions.
- **Action:** organized Career Acceleration as the parent project, created offer-specific subprojects, and tied each one to evidence, gaps, and concrete follow-up work.
- **Result:** the search became resumable and auditable instead of scattered, and the first Emerson role now has a fit matrix and interview prep path.

### Story 2: Learning A New Technical Domain Quickly

- **Situation:** the networking and OT material was new enough that guessing would have been risky.
- **Task:** build a mental model that could survive interview pressure.
- **Action:** wrote a networking study log, reduced the topic to layers, ports, ARP, VLANs, and packet flow, then added corrections from quiz feedback and follow-up questions.
- **Result:** the notes now support a short, defensible explanation of same-subnet failures and segmentation without hand-waving.

### Story 3: Debugging By Reducing Scope

- **Situation:** a communication problem can look like many different failures at once.
- **Task:** find the actual fault layer before changing anything.
- **Action:** used a step-by-step troubleshooting order: physical link, IP configuration, VLAN and switch state, then firewall or application checks.
- **Result:** the troubleshooting model now makes it easier to explain how to isolate an issue instead of guessing from symptoms.

### Story 4: Explaining Technical Work Clearly

- **Situation:** technical work only helps if another person can understand and reuse it.
- **Task:** write notes that make the reasoning visible.
- **Action:** kept the Emerson role page structured with sessions, answer notes, critique, and next actions; kept the networking epic focused on practical checks and interpretations.
- **Result:** the documentation is easier to review quickly, and the prep material can be reused instead of rebuilt every time.

### Story 5: Turning A Job Search Into A System

- **Situation:** the job search needed a structure that could be resumed and audited instead of handled as scattered notes.
- **Task:** build a single project that could manage the search by role, area, and offer.
- **Action:** organized Career Acceleration as the parent project and turned the Emerson role into a tracked subproject with a fit matrix and next actions.
- **Result:** the search became easier to review, and the prep work has a clear place to live.

### Story 6: Learning Through Feedback

- **Situation:** the networking material started broad and needed to become usable under interview pressure.
- **Task:** tighten the understanding until it could be explained without hand-waving.
- **Action:** wrote the networking study log, corrected mistakes, and captured the better answers around ARP, VLANs, packet capture, and same-subnet troubleshooting.
- **Result:** the notes now support a practical explanation of communication failures and segmentation.

### Story 7: Automating Repetitive Validation Work

- **Situation:** validation results had to be rolled up manually, which was repetitive and slow.
- **Task:** reduce the manual work and make the output more consistent.
- **Action:** scripted the roll-up so the process could happen automatically instead of by hand.
- **Result:** the workflow saved time, reduced repetitive effort, and produced a more consistent result.

### Story 8: Building Reusable Engineering Notes

- **Situation:** technical notes are only useful if they can be reused later.
- **Task:** keep the engineering material durable, short, and easy to resume.
- **Action:** maintained project notes, current context, and session logs so the work is recoverable across sessions.
- **Result:** the prep system is now resumable, and the same structure can support future projects.

## Interactive Practice Round 1

Use these as the next live drill. Answer out loud, then tighten the response to the shortest version that still sounds real.

### Question 1: Tell me about yourself.

Answer shape:

- present background in engineering and systems work
- connect that background to validation, documentation, networking, and troubleshooting
- say why the Emerson role fits the next step

Draft answer:

> I work best on systems that need careful reasoning, documentation, and troubleshooting. My background includes engineering work, Linux and Windows basics, networking, validation-style thinking, and building repeatable notes and workflows. For this Emerson role, the fit is that I can bridge OT concepts, security controls, and customer-facing communication, and I’m being direct about the gap where I still need more DeltaV-specific depth.

### Question 2: Why do you want this role?

Answer shape:

- mention process control plus security
- mention customer-facing engineering work
- mention learning by doing on a real system

Draft answer:

> I want it because it sits at the intersection of process control, security, and practical engineering. It is the kind of role where technical depth matters, but so does communication, validation, and disciplined change management. I also like that it pushes me to keep closing the gap between IT-style security thinking and OT realities like uptime, safety, and controlled access.

### Question 3: What is your biggest gap for this role?

Answer shape:

- state the gap plainly
- avoid sounding defensive
- bridge to what you do have

Draft answer:

> The biggest gap is direct DeltaV execution-project experience. I’m not pretending to have that already. What I do have is the engineering habit of reducing systems to their operating pieces, checking evidence, documenting clearly, and learning quickly enough to close a new domain gap with focused work.

### Question 4: How would you explain OT security to a customer?

Answer shape:

- protect the process, not just the data
- zones and conduits
- least privilege
- uptime and safety

Draft answer:

> I would explain that OT security protects the process itself, so the controls have to be built around uptime, safety, and controlled change. The basic model is defense in depth: segment the environment into zones, control the conduits between them, and use least privilege so people and systems only get the access they need. In practice that usually means a jump host, approved firewall rules, tightly scoped admin access, and a change process that respects the plant’s operating windows.

### Critique Targets

- remove any sentence that sounds generic or rehearsed
- keep the DeltaV gap honest
- keep the answer under one minute unless the interviewer asks for detail
- replace broad claims with one concrete example whenever possible

## Interactive Practice Round 2

Use these as the next live drill for OT cybersecurity specifics. Answer out loud, then compress each answer to the shortest version that still sounds credible.

### Question 1: How would you secure remote vendor access into an OT environment?

Answer shape:

- start with controlled entry, not direct access
- mention jump host and DMZ
- mention named accounts, logging, and time-bounded access

Draft answer:

> I would not allow direct vendor access into the control network. I would put a jump host in the Industrial DMZ, require named accounts and strong authentication, log the session, and limit access to the exact window and systems needed. That gives control over who connected, what they touched, and when the access ended.

### Question 2: Why is asset inventory important in OT security?

Answer shape:

- tie inventory to risk
- mention hardware, software, versions, and dependencies
- mention that you cannot protect what you cannot see

Draft answer:

> Asset inventory is the starting point because you cannot secure what you do not know exists. In OT, that means knowing the controllers, HMIs, engineering workstations, historians, network gear, software versions, dependencies, and vendor connections. Once you have that list, you can segment, patch, monitor, and recover with less guesswork.

### Question 3: How would you handle patching in a live OT environment?

Answer shape:

- emphasize testing first
- emphasize maintenance windows and change control
- mention production and safety impact

Draft answer:

> I would treat patching as a planned change, not a routine office update. First I would test the patch in a representative environment, then schedule it in a maintenance window, verify backups, and confirm rollback steps before touching production. In OT, a bad patch can affect uptime or safety, so the process matters as much as the patch itself.

### Question 4: What makes an engineering workstation a high-value target?

Answer shape:

- explain its access level
- mention broad control and config rights
- mention hardening and limited software

Draft answer:

> Engineering workstations are high-value because they often have broad access to controllers, configurations, and plant systems. If one is compromised, the attacker may be able to make changes that affect the control environment. That is why I would harden them, limit software, restrict browsing and removable media, and apply tighter account control than on a normal office PC.

### Question 5: How do logging and monitoring work in OT without breaking the process?

Answer shape:

- mention low-impact collection
- mention who did what and when
- mention stability first

Draft answer:

> The goal is to collect enough evidence to reconstruct access and changes without adding instability. I would prefer low-impact logging, network visibility where appropriate, and logs that show who connected, what changed, and when it happened. In OT, the monitoring stack has to fit the environment, not overload it.

### Critique Targets

- avoid generic IT-security language that ignores uptime
- keep the jump-host answer concrete
- treat patching and monitoring as operational changes, not just technical controls
- mention recovery and rollback when discussing any change

## Interactive Practice Round 3

Use these as the next live drill for IEC 62443 and the OT security model. Answer out loud, then compress each answer to the shortest version that still sounds credible.

### Question 1: What is IEC 62443 in plain English?

Answer shape:

- describe it as the OT security framework
- mention zones, conduits, and layered controls
- avoid certification-level detail

Draft answer:

> IEC 62443 is the OT security framework that helps organize how industrial systems are separated and protected. In plain English, it says to divide the environment into zones, control the conduits between them, and apply layered security based on risk. It is useful because it fits how plants actually operate.

### Question 2: What are zones and conduits?

Answer shape:

- zone = group of systems with similar trust and purpose
- conduit = controlled path between zones
- mention policy enforcement

Draft answer:

> A zone is a group of systems that share a similar role and trust level, like a controller zone or an engineering zone. A conduit is the controlled path between zones, usually enforced by a firewall or gateway. The point is to make access intentional instead of letting everything talk to everything.

### Question 3: Why is least privilege important in OT?

Answer shape:

- connect to safety and blast radius
- mention read-only where possible
- mention admin access only when needed

Draft answer:

> Least privilege matters because OT environments are too important to give broad access by default. If a person or system only needs read access, it should not have write access. If admin access is needed, it should be limited, logged, and temporary so the blast radius stays small.

### Question 4: What is the biggest mistake people make when they apply IT security to OT?

Answer shape:

- mention assuming IT patterns transfer directly
- mention uptime and process impact
- mention controls must be validated

Draft answer:

> The biggest mistake is assuming IT security controls can be copied into OT without adapting them. In OT, a control that is fine for office systems can break uptime, process reliability, or maintenance flow. The right approach is to validate each control against the plant's operating needs.

### Critique Targets

- keep IEC 62443 at framework level, not certification detail
- explain zones and conduits with one concrete example
- do not overstate least privilege as a cure-all
- always tie controls back to uptime, safety, and change control

## Interactive Practice Round 4

Use these as the next live drill for OT threat scenarios and incident containment. Answer out loud, then tighten each response.

### Question 1: What is your first concern if a vendor laptop connects to an OT network?

Answer shape:

- focus on trust boundary
- mention malware, unknown configuration, and containment
- mention isolation and logging

Draft answer:

> My first concern is that the vendor laptop is an untrusted endpoint crossing into a trusted environment. It could carry malware, the wrong software, or unknown credentials. I would require controlled access through a jump host, limit the scope of the connection, and log the activity.

### Question 2: How would you respond to suspected malware in an engineering workstation?

Answer shape:

- isolate first
- preserve evidence if possible
- restore from known-good state

Draft answer:

> I would isolate the workstation first so the issue cannot spread. Then I would preserve logs and any evidence that matters, check what it was connected to, and move toward a known-good rebuild or restore if needed. In OT, containment comes before cleanup.

### Question 3: How would you contain a bad configuration change?

Answer shape:

- stop the blast radius
- rollback if possible
- verify the process state

Draft answer:

> I would contain the change by limiting where it can propagate, then roll back to the last known good configuration if that is safe. After that I would verify the process state and confirm the controllers, HMI, and network behavior are stable again. The key is to recover without making a second problem.

### Question 4: What would you do if a remote access rule was too permissive?

Answer shape:

- tighten the rule
- limit destination, source, time, and protocol
- validate with operations

Draft answer:

> I would narrow the rule immediately to the smallest workable scope. That means limiting the source, destination, protocol, and time window, then validating it with the operations team so the plant still functions. In OT, a permissive rule is a standing risk until it is corrected.

### Critique Targets

- always separate containment from eradication
- mention process impact before talking about tools
- do not assume a laptop or workstation is clean just because it is trusted by policy
- be specific about rollback and verification

## Interactive Practice Round 5

Use these as the next live drill for OT firewall policy and communication matrices. Answer out loud, then shorten the response.

### Question 1: What is an OT communication matrix?

Answer shape:

- describe it as a policy table
- mention source, destination, protocol, port, and reason
- mention that it drives firewall rules

Draft answer:

> An OT communication matrix is a table that defines who is allowed to talk to whom, using which protocol and port, and for what reason. It usually includes the source zone, destination zone, service, and justification. It is the bridge between the architecture and the firewall rules.

### Question 2: Why should OT firewalls default to deny?

Answer shape:

- explain least trust
- mention only approved flows
- mention predictable behavior

Draft answer:

> OT firewalls should default to deny because the safe assumption is that no traffic is allowed unless it is explicitly required. That keeps the environment predictable and prevents accidental trust between zones. Only approved flows should be opened.

### Question 3: How do you decide what to allow in the firewall?

Answer shape:

- start from process need
- validate protocol, source, destination, and direction
- keep rule scope narrow

Draft answer:

> I would start from the process requirement, not from convenience. Then I would identify the exact source, destination, protocol, direction, and port needed for that function, and keep the rule as narrow as possible. If the business need is unclear, the rule should stay closed until it is justified.

### Question 4: Why is a communication matrix useful for troubleshooting?

Answer shape:

- gives expected behavior
- helps find missing or extra flows
- ties to logs and packet captures

Draft answer:

> It tells you what should be happening, so you can compare that to what the firewall logs or packet captures show. If traffic appears that should not exist, or expected traffic is missing, the matrix helps narrow the fault quickly. It turns troubleshooting into comparison instead of guesswork.

### Critique Targets

- keep the matrix explanation practical
- avoid saying “open everything and test later”
- mention logs and packet captures as validation tools
- keep the firewall answer aligned with default-deny and least privilege

## Mock Interview Script

Use the recommended answer first. If time is tight, use the short response.

### Tell me about yourself

Recommended:

> I’m an electrical engineer with automation and validation experience, and I’ve built automation systems to save time and remove repetitive work. I’ve also developed practical knowledge of networking protocols, switching, routing, segmentation, and cybersecurity fundamentals. That combination fits this Emerson role because it needs engineering discipline, troubleshooting, and security thinking in operational environments.

Short:

> I’m an electrical engineer with automation and validation experience. I’ve built systems to reduce repetitive work and save time, and I’ve also built a working foundation in networking, segmentation, and cybersecurity fundamentals.

### Why do you want this role?

Recommended:

> I want this role because it aligns with my career path and gives me a chance to grow deeper in networking and cybersecurity, which are strong and in-demand areas. It also fits the kind of engineering work I enjoy: systems, troubleshooting, and learning by doing in a real operational environment.

Short:

> I want this role because it fits my career path and lets me grow into networking and cybersecurity, which are highly in-demand skills.

### What is your biggest gap for this role?

Recommended:

> My control systems experience is still limited and mostly academic, and I’m being direct about that. What I do have is a strong engineering base in automation, validation, networking, and cybersecurity fundamentals, and I’m confident I can close that gap quickly.

Short:

> My control systems experience is still limited and mostly academic, but I have a strong engineering base in automation, validation, networking, and cybersecurity fundamentals.

### How would you explain OT security?

Recommended:

> OT security protects the operating environment so the process stays safe, reliable, and controlled. That usually means segmenting networks, limiting privileges, and making sure security changes do not disrupt operations.

Short:

> OT security protects the operating environment so the process stays safe, reliable, and controlled.

### Why is OT security different from IT security?

Recommended:

> OT requires much more care with downtime because it must continuously support the process. Changes have to be planned carefully, because safety, uptime, and production can be directly affected. That means security practices need to be stricter and more deliberate than in many IT environments.

Short:

> OT is different because downtime and bad changes can affect the live process, so safety, uptime, and controlled change matter more.

### Why is security so important in OT?

Recommended:

> In OT, security is as important as the process itself because security failures can stop production, affect safety, or disrupt operations. That is why OT security has to be designed around uptime, controlled change, and protecting the process as a whole.

Short:

> In OT, security is as important as the process because failures can affect safety, uptime, and production.

### Tell me about a time you built something that saved time

Recommended:

> In one validation workflow, the results had to be rolled up manually, which was slow and repetitive. I scripted the process so it could be done automatically instead. That saved time, reduced manual effort, and made the output more consistent.

Short:

> I automated a manual validation results roll-up by scripting it, which saved time and reduced repetitive work.

## Final Mock Interview

Use this when you want the hardest likely questions. The goal is not perfect coverage of the field. The goal is to sound credible, concise, and honest under pressure.

### Likely Hard Questions

1. Why does Emerson need someone with both OT and cybersecurity awareness?
1. How would you secure a vendor connection into a live plant without disrupting operations?
1. What would you do first if a plant asset was communicating unexpectedly?
1. How do you decide whether to allow a firewall rule between two OT zones?
1. Explain how you would handle a patch on an engineering workstation.
1. What is the difference between a historian, SCADA, and a DCS?
1. What is the biggest risk when moving IT security controls into OT?
1. How do you balance security with uptime and safety?
1. What would you do if an operator wanted a broad exception to get work done faster?
1. Why should we believe you can close the DeltaV gap?

### Best Answer Shapes

#### Why Emerson needs both OT and cybersecurity awareness

> Emerson needs people who understand that security controls have to work inside a live control environment. In OT, a bad change can affect uptime, safety, and production, so the engineer has to understand both the process and the security implications. The value is being able to design controls that protect the plant without breaking the plant.

#### How to secure vendor access

> I would route vendor access through a controlled DMZ and jump host, use named accounts and strong authentication, log the session, and limit access to a specific time window and specific systems. Direct access into the OT network should be avoided unless there is a very narrow, justified exception.

#### What to do if an asset is communicating unexpectedly

> First I would verify the asset inventory and confirm whether the communication is expected. Then I would check source, destination, protocol, port, and direction against the approved matrix, look at firewall logs or packet capture, and isolate only if the traffic is truly out of policy or risky.

#### How to decide on a firewall rule

> Start from the process requirement, not convenience. Allow only the exact source, destination, protocol, direction, and port needed, then keep the rule narrow and time-bound if possible. If the business case is unclear, the default should be to deny until the need is justified.

#### How to handle a patch on an engineering workstation

> I would assess the dependency and the operational risk, test the patch in a controlled environment if possible, schedule it in a maintenance window, ensure backups and rollback options exist, and confirm the patch does not disrupt control functions or vendor tools the site depends on.

#### Historian vs SCADA vs DCS

> A historian stores time-based process data and events. SCADA is the supervisory layer that monitors and coordinates distributed assets. A DCS is the distributed control architecture used to run process control inside a plant. They overlap in conversation, but they are not the same thing.

#### Biggest risk when moving IT controls into OT

> The biggest risk is treating OT like IT and introducing controls that break availability, timing, or process behavior. In OT, a technically correct control can still be the wrong control if it interrupts production or creates a safety issue.

#### Why the DeltaV gap is manageable

> I do not claim direct DeltaV execution-project experience. What I do have is a strong engineering base in validation, documentation, networking, troubleshooting, and disciplined change control. That means I can learn the DeltaV-specific parts quickly while staying careful about the operational context.

### Final Pressure Questions

- Walk me through how you would secure an Emerson customer site from the business network to the controller level.
- Explain why a VLAN is not enough by itself to secure OT traffic.
- What would you say to a customer who wants speed over validation?
- How would you explain a security recommendation to an operator who is worried about downtime?
- What would you do if your security advice conflicts with an engineer's convenience?
- Which controls would you prioritize first if the site had limited time and budget?

### Final Interview Rule

- answer the question asked
- stay concrete
- use OT language, not generic IT language
- keep the DeltaV gap honest
- end with uptime, safety, and controlled change when relevant

### Final Mock Answers

- **Remote vendor access:** use a jump host in the DMZ as the controlled entry point, require named accounts and strong authentication, log the session, and allow only the specific approved path, protocol, and ports.
- **Unexpected plant communication:** verify whether the traffic is expected using the asset inventory and approved communication matrix, then check VLAN assignment, firewall policy, source, destination, protocol, port, and direction with logs and packet capture before isolating anything further.
- **Firewall rule decisions:** start from the plant-specific communication matrix and OT policy, then allow only the exact source, destination, protocol, port, and direction needed for the process; keep the rule narrow and deny by default when the need is unclear.
- **Patch handling:** patch through a planned maintenance window, back up the system, test in a lab or simulator if available, apply the patch, verify the workstation and OT tools still function, and reconnect only after validation.
- **Historian vs SCADA vs DCS:** a historian stores time-based process data and events, SCADA supervises and coordinates assets, and a DCS runs distributed process control in the plant.
- **OT vs IT tradeoffs:** OT changes require much more preparation because uptime, safety, and controlled change matter as much as security, and changes that are routine in IT can disrupt a live process in OT.
- **Closing the DeltaV gap:** I do not yet have direct DeltaV execution-project experience, but I have the engineering foundation, troubleshooting habits, networking background, and validation discipline to learn the DeltaV specifics quickly and apply them carefully.
- **VLANs:** VLANs provide logical segmentation, but they do not enforce communication policy by themselves; a router, firewall, or similar control is still needed between segments.
- **OT security recommendation to operators:** frame the recommendation around safe and reliable operation, explain the planned maintenance window, and validate the change before returning the system to service.
- **Broad exception request:** require the exception to be formally requested, reviewed, approved, scoped narrowly, time-bounded, and documented, then reversed when the work is complete.

## Interview Debrief

### Questions Asked

- remote vendor access
- unexpected plant communication
- firewall rule decisions
- patch handling
- historian vs SCADA vs DCS
- OT vs IT tradeoffs
- closing the DeltaV gap
- packet traces and firewall ACLs when a rule blocks required traffic
- how to explain a security recommendation to an operator worried about downtime
- how to handle a broad exception request
- why a VLAN is not enough by itself
- what criticism the interviewer would have about the OT background
- why the role should prefer this candidate over someone with deeper OT experience
- what a time source is in Linux
- what TSC is
- whether TSC is network connected
- what to do when a switch reboots and end devices stop communicating
- timeout vs unreachable ping behavior

### Self Feedback

- Answers were strongest when they started from OT process requirements, not generic IT language.
- Answers were weakest when they stayed too short and missed the control logic, especially on vendor access, firewall rules, and patching.
- VLAN answers need the firewall or router distinction stated clearly every time.
- Historian answers must stay focused on process data and events, not security logging.
- DeltaV gap answers need to be direct, honest, and specific about adjacent evidence.
- OT vs IT answers need to mention uptime, safety, and controlled change, not only security.
- STAR answers still need more concrete situation, action, and result detail from real examples.

### Follow-Up Practice

- turn the best answers into 30-second STAR-style responses
- drill networking terms until they are automatic
- rehearse the difference between VLAN, firewall, router, and ACL
- practice Linux timing concepts: kernel clock, RTC, NTP, clocksource, TSC
- keep the OT answer style: process first, evidence first, narrow scope, and controlled change

### Next Drill Queue

- STAR story about turning ambiguity into a system
- STAR story about learning a technical domain quickly
- networking troubleshooting when a switch comes up but end devices cannot talk
- firewall rule reasoning from an OT matrix
- OT communication matrix explanation
- historian vs SCADA vs DCS from memory
- Linux time source and TSC from memory

## Practice Cycle 7

### Focus

- tighten STAR answers
- sharpen networking troubleshooting
- keep OT phrasing concrete and non-generic

### Practice Plan

- start with the strongest STAR story
- then move to one networking troubleshooting scenario
- then review the answer for generic language and missing evidence

### Reminder

- keep answers short enough for live interview use
- state the situation, task, action, and result clearly
- use packet, VLAN, firewall, routing, and OT matrix language precisely

## Final Cheat Sheet

Keep this to one page when you rehearse.

### ICS

- PLC: local deterministic controller
- SCADA: supervisory monitoring layer
- DCS: distributed process control system
- HMI: operator interface
- Historian: data recording over time
- OT: uptime and safety matter more than flexibility

### DeltaV

- Emerson DCS for process control
- controllers, engineering workstations, operator stations, historian, redundancy
- engineers configure logic and graphics
- operators monitor and respond
- security fits through segmentation, access control, validation, and change management

### Networking

- switch = Layer 2 forwarding
- router = Layer 3 forwarding
- ARP = IP to MAC on local network
- VLAN = logical segmentation
- DNS = names to IPs
- DHCP = automatic addressing
- TCP = reliable connection-oriented transport
- UDP = lighter connectionless transport
- Wireshark = packet evidence

### Cybersecurity

- defense in depth
- least privilege
- zones and conduits
- firewalls
- NIST CSF: identify, protect, detect, respond, recover
- IEC 62443: OT security framework
- OT security protects the process, not just the data

### Interview Lines

- I’m an electrical engineer with automation and validation experience.
- I’ve built automation systems to save time and reduce repetitive work.
- My control systems experience is mostly academic, but I’m closing the gap quickly.
- OT security matters because bad changes can affect uptime, safety, and production.
- DeltaV is Emerson’s DCS platform for process control.

## Questions
- What is jump host access, and why is it important in OT?
- What is a managed switch, and how does it differ from an unmanaged switch?

## Next Actions

- [ ] complete the fit matrix with real evidence
- [ ] identify the strongest supporting projects
- [ ] draft a one-page application angle for this role
- [ ] decide whether this role should become a priority target
- [ ] clean up the current repo state so the Emerson career work is easier to resume
- [ ] work through the interview prep schedule from Saturday through Monday morning
- [ ] turn Priority 1 topics into flashcard-style recall prompts and practice them out loud
- [ ] practice the Session 4 OT security answers aloud and move to behavioral STAR stories
