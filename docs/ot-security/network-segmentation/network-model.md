# OT Network Segmentation Fundamentals for a Hydroelectric Power Plant

## Document Purpose

This chapter introduces the fundamentals of OT network segmentation using a simplified hydroelectric power plant architecture.

The objective is to build understanding from first principles:

1. What a VLAN is.
2. How VLANs relate to Ethernet switching.
3. How VLANs relate to IP subnets.
4. What access ports and trunk ports are.
5. Why devices in different VLANs require routing.
6. Why OT environments use firewalls between security zones.
7. How packet flow works between an HMI, a SCADA server, a controller, a relay, and a remote RTU.
8. Why segmentation reduces operational and cybersecurity risk.
9. How to translate a logical design into switch, firewall, and addressing configurations.
10. How to build a small lab that demonstrates these concepts.

This chapter uses a simplified architecture for learning. A real hydroelectric power plant would normally require additional redundancy, vendor-specific protocols, safety-system separation, detailed communication matrices, physical network design, failover testing, and site-specific risk analysis.

---

# 1. Reference Hydroelectric OT Architecture

We will use the following network layout throughout this chapter:

```text
10.10.0.0/24      Business IT
10.20.0.0/24      Industrial DMZ
10.30.0.0/24      Plant SCADA and HMI
10.30.10.0/24     Controller network
10.30.20.0/24     Engineering workstations
10.40.0.0/24      Substation protection and relay network
10.50.0.0/24      Remote telemetry and RTUs
```

Each subnet represents a different operational or security function.

The intended design is:

```text
Business IT
    |
    v
IT Firewall
    |
    v
Industrial DMZ
    |
    v
OT Firewall
    |
    +--------------------+
    |                    |
    v                    v
SCADA/HMI            Engineering
    |
    v
Controller Network
    |
    +--------------------+
    |                    |
    v                    v
Protection Network   Remote Telemetry
```

The most important rule is:

```text
Business IT must not communicate directly with controllers,
protection relays, or remote field devices.
```

---

# 2. Corrected Example IP Mapping

The original addressing example placed HMIs and the historian inside the engineering subnet.

A cleaner mapping is:

```text
10.30.0.10       Operator HMI
10.30.0.11       Operator HMI backup
10.30.0.20       Primary SCADA server
10.30.0.21       Backup SCADA server
10.30.0.30       Historian
10.30.0.40       Alarm and event server

10.30.10.10      Turbine controller
10.30.10.11      Turbine controller backup
10.30.10.20      Governor controller
10.30.10.21      Excitation controller
10.30.10.30      Auxiliary systems PLC

10.30.20.10      SCADA engineering workstation
10.30.20.20      PLC engineering workstation
10.30.20.30      Protection engineering workstation
10.30.20.40      Configuration backup server

10.20.0.10       Jump host in the Industrial DMZ
10.20.0.20       Patch and update staging server
10.20.0.30       Historian replica
10.20.0.40       Remote access gateway

10.40.0.10       Generator protection relay
10.40.0.11       Transformer protection relay
10.40.0.12       Busbar protection relay
10.40.0.13       Transmission line protection relay
10.40.0.20       Disturbance recorder
10.40.0.30       Substation gateway

10.50.0.10       Remote intake RTU
10.50.0.11       Reservoir level RTU
10.50.0.12       Spillway RTU
10.50.0.13       Weather station RTU
10.50.0.14       Downstream water-level RTU
```

This mapping keeps each device in the subnet that represents its actual function.

---

# 3. Why Segmentation Exists

A network can be physically connected while still being logically separated.

Without segmentation, a hydroelectric plant might have:

```text
One switch
One subnet
One broadcast domain
Many unrelated device types
```

Example flat network:

```text
10.30.0.10     Operator HMI
10.30.0.20     Historian
10.30.0.30     Engineering workstation
10.30.0.40     Turbine controller
10.30.0.50     Protection relay
10.30.0.60     Vendor laptop
```

This creates several problems:

* A compromised engineering workstation may directly reach a turbine controller.
* A vendor laptop may directly reach a relay.
* Malware can move laterally without crossing a firewall.
* Broadcast traffic reaches unrelated devices.
* The firewall cannot inspect traffic between devices in the same subnet.
* Troubleshooting becomes more difficult.
* Access policies become vague or impossible to enforce.
* High-value devices become exposed to unnecessary protocols.
* A single misconfiguration can affect the whole plant network.

Segmentation separates devices according to function and risk.

A segmented plant might use:

```text
SCADA devices       → VLAN 30
Controllers         → VLAN 31
Engineering         → VLAN 32
Protection relays   → VLAN 40
Remote RTUs         → VLAN 50
```

Traffic between these zones must cross a router or firewall.

That routing boundary becomes the point where security policy can be enforced.

---

# 4. What Is a VLAN?

VLAN stands for:

```text
Virtual Local Area Network
```

A VLAN divides a physical Ethernet switching infrastructure into multiple logical Layer-2 networks.

A managed switch can behave as though it were several independent switches.

Consider a 24-port managed switch:

```text
Ports 1–4      Business IT
Ports 5–8      Industrial DMZ
Ports 9–12     SCADA and HMI
Ports 13–16    Controllers
Ports 17–18    Engineering workstations
Ports 19–20    Protection relays
Ports 21–22    Remote telemetry
Ports 23–24    Trunk or firewall uplinks
```

Although all devices connect to the same physical switch, the VLAN configuration separates their Ethernet traffic.

Conceptually:

```text
One physical switch
|
+-- Virtual switch for VLAN 10
|
+-- Virtual switch for VLAN 20
|
+-- Virtual switch for VLAN 30
|
+-- Virtual switch for VLAN 31
|
+-- Virtual switch for VLAN 32
|
+-- Virtual switch for VLAN 40
|
+-- Virtual switch for VLAN 50
```

A device in VLAN 30 cannot communicate directly at Layer 2 with a device in VLAN 31.

A routing device is required.

---

# 5. VLANs and the OSI Model

The OSI model helps separate the responsibilities of switches, routers, protocols, and applications.

```text
Layer 7   Application      Modbus TCP, OPC UA, HTTPS, DNP3
Layer 6   Presentation     Encoding, encryption, serialization
Layer 5   Session          Session management
Layer 4   Transport        TCP and UDP
Layer 3   Network          IP addressing and routing
Layer 2   Data Link        Ethernet, MAC addresses, VLANs
Layer 1   Physical         Copper, fiber, radio, connectors
```

VLANs are primarily a Layer-2 technology.

A Layer-2 switch makes forwarding decisions using:

```text
MAC addresses
```

A router or firewall makes forwarding decisions using:

```text
IP addresses
```

Therefore:

```text
VLAN      → Layer-2 separation
Subnet    → Layer-3 separation
Firewall  → Policy enforcement between zones
```

---

# 6. VLAN Versus IP Subnet

A VLAN and an IP subnet are related, but they are not the same thing.

A VLAN defines a Layer-2 broadcast domain.

An IP subnet defines a Layer-3 addressing boundary.

In a clean design, one VLAN normally maps to one IP subnet.

Example:

| VLAN | Name           | Subnet          |
| ---: | -------------- | --------------- |
|   10 | BUSINESS-IT    | `10.10.0.0/24`  |
|   20 | OT-IDMZ        | `10.20.0.0/24`  |
|   30 | OT-SCADA       | `10.30.0.0/24`  |
|   31 | OT-CONTROL     | `10.30.10.0/24` |
|   32 | OT-ENGINEERING | `10.30.20.0/24` |
|   40 | OT-PROTECTION  | `10.40.0.0/24`  |
|   50 | OT-TELEMETRY   | `10.50.0.0/24`  |

The VLAN number does not have to match the subnet.

For example, this is valid:

```text
VLAN 731 → 10.30.10.0/24
```

However, a consistent naming and numbering scheme improves operations and troubleshooting.

---

# 7. Understanding the `/24` Prefix

Consider:

```text
10.30.10.0/24
```

The `/24` means that the first 24 bits represent the network portion.

The corresponding subnet mask is:

```text
255.255.255.0
```

For `10.30.10.0/24`:

```text
Network address:    10.30.10.0
Usable hosts:       10.30.10.1 through 10.30.10.254
Broadcast address:  10.30.10.255
```

The network address identifies the subnet.

The broadcast address represents all devices in that subnet.

Neither address should normally be assigned to a host.

Example controller subnet:

```text
10.30.10.1      Default gateway
10.30.10.10     Turbine controller
10.30.10.11     Turbine controller backup
10.30.10.20     Governor controller
10.30.10.21     Excitation controller
10.30.10.30     Auxiliary systems PLC
10.30.10.255    Broadcast address
```

---

# 8. What Is a Broadcast Domain?

A broadcast domain is the set of devices that receive a Layer-2 broadcast frame.

Examples of traffic that may be broadcast or flooded include:

* ARP requests.
* DHCP discovery.
* Unknown unicast frames.
* Some industrial discovery protocols.
* Legacy service discovery.
* Some multicast traffic, depending on switch configuration.

Suppose the HMI at `10.30.0.10` wants to communicate with the SCADA server at `10.30.0.20`.

The HMI needs the server's MAC address.

It sends an ARP request:

```text
Who has 10.30.0.20?
Tell 10.30.0.10.
```

Every device in the local VLAN receives the request.

Only `10.30.0.20` should reply.

A VLAN limits the broadcast domain.

An ARP request generated in the SCADA VLAN should not reach:

```text
10.30.10.10     Turbine controller
10.40.0.10      Protection relay
10.50.0.10      Remote intake RTU
10.10.0.10      Business workstation
```

This is one reason VLANs improve predictability and reduce unnecessary traffic.

---

# 9. Access Ports

An access port carries traffic for one VLAN.

Example:

```text
Switch port:       Ethernet1/5
Connected device:  Operator HMI
Port mode:         Access
Assigned VLAN:     VLAN 30
```

The HMI normally sends and receives ordinary untagged Ethernet frames.

The HMI does not need to understand VLAN tagging.

The switch associates all untagged traffic arriving on that port with VLAN 30.

Conceptual switch configuration:

```text
interface Ethernet1/5
 description Operator-HMI-01
 switchport mode access
 switchport access vlan 30
```

Typical access-port devices include:

* Operator HMIs.
* PLCs.
* Protection relays.
* Engineering workstations.
* Servers.
* RTUs.
* Network printers.
* Industrial gateways.
* Time servers.
* Local maintenance laptops.

---

# 10. Trunk Ports

A trunk port carries traffic for multiple VLANs over one physical connection.

Typical trunk links include:

```text
Switch to switch
Switch to firewall
Switch to router
Switch to virtualization host
Switch to another building
```

Example:

```text
Core switch
    |
    | Trunk carrying VLANs 20, 30, 31, 32, 40, and 50
    |
Industrial firewall
```

A trunk uses IEEE 802.1Q tagging to identify the VLAN associated with each Ethernet frame.

Conceptually:

```text
Ethernet frame
|
+-- Destination MAC
+-- Source MAC
+-- 802.1Q VLAN tag
+-- EtherType
+-- Payload
+-- Frame check sequence
```

The VLAN tag includes the VLAN identifier.

Example:

```text
VLAN 30 → Plant SCADA
VLAN 31 → Controllers
VLAN 32 → Engineering
VLAN 40 → Protection relays
```

---

# 11. Tagged and Untagged Traffic

Access ports normally carry untagged frames between the endpoint and the switch.

```text
HMI
  |
  | Untagged Ethernet frame
  v
Access port in VLAN 30
```

Trunk ports normally carry tagged frames.

```text
Switch A
  |
  | 802.1Q-tagged frame
  v
Switch B
```

Summary:

| Port type   |   VLANs carried | Frame behavior          |
| ----------- | --------------: | ----------------------- |
| Access      |             One | Usually untagged        |
| Trunk       |        Multiple | Usually tagged          |
| Routed port | None at Layer 2 | Uses Layer-3 addressing |

---

# 12. VLANs Do Not Route Traffic

A VLAN separates Layer-2 traffic.

It does not automatically enable communication between VLANs.

Consider:

```text
Operator HMI:       10.30.0.10/24
Turbine controller: 10.30.10.10/24
```

These devices are in different IP subnets.

The HMI cannot communicate directly with the controller using Layer-2 switching alone.

It must send the packet to a default gateway.

```text
Operator HMI
10.30.0.10
    |
    v
SCADA gateway
10.30.0.1
    |
    v
Firewall or router
    |
    v
Controller gateway
10.30.10.1
    |
    v
Turbine controller
10.30.10.10
```

This process is called:

```text
Inter-VLAN routing
```

---

# 13. The Default Gateway

A host uses its subnet mask to determine whether a destination is local or remote.

Example HMI configuration:

```text
IP address:       10.30.0.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.0.1
```

Destination:

```text
10.30.0.20
```

The destination is inside `10.30.0.0/24`.

The HMI communicates directly using ARP and Ethernet switching.

Destination:

```text
10.30.10.10
```

The destination is outside `10.30.0.0/24`.

The HMI sends the packet to its default gateway.

The gateway then decides:

1. Whether a route exists.
2. Whether the source is allowed.
3. Whether the destination is allowed.
4. Whether the protocol and port are allowed.
5. Whether the packet should be logged.
6. Which outgoing interface should be used.

---

# 14. Why OT Networks Use Firewalls Between VLANs

A Layer-3 switch can route traffic between VLANs.

However, unrestricted routing is often inappropriate in OT.

A better design is:

```text
SCADA VLAN
    |
    v
Industrial firewall
    |
    v
Controller VLAN
```

The firewall evaluates traffic against policy.

Example rule:

```text
Source:       Primary SCADA server
Source IP:    10.30.0.20
Destination:  Turbine controller
Destination IP:
              10.30.10.10
Protocol:     Modbus TCP
Port:         TCP 502
Action:       Allow
Logging:      Enabled
```

A separate rule might deny direct HMI access:

```text
Source:       Operator HMI
Source IP:    10.30.0.10
Destination:  Controller network
Protocol:     Any
Action:       Deny
Logging:      Enabled
```

The intended communication path would then be:

```text
Operator HMI
    |
    v
SCADA server
    |
    v
Turbine controller
```

Instead of:

```text
Operator HMI
    |
    v
Turbine controller
```

---

# 15. VLAN Versus Security Zone

A VLAN is a technical Layer-2 mechanism.

A security zone is an architectural concept.

A security zone groups systems with similar:

* Operational function.
* Trust level.
* Risk.
* Criticality.
* Communication requirements.
* Administrative ownership.
* Maintenance requirements.
* Security controls.

Example:

```text
Security zone: Controller network
VLAN:         31
Subnet:       10.30.10.0/24
Devices:      Turbine, governor, excitation, and auxiliary controllers
```

A complete security zone may include:

* One or more VLANs.
* One or more IP subnets.
* Firewall rules.
* Physical access restrictions.
* User access controls.
* Logging.
* Passive monitoring.
* Patch procedures.
* Backup requirements.
* Incident-response procedures.
* Configuration-management requirements.

A VLAN alone is not a complete security control.

---

# 16. Zone 1: Business IT

```text
Subnet: 10.10.0.0/24
VLAN:  10
Name:  BUSINESS-IT
```

Example devices:

```text
10.10.0.10    Employee laptop
10.10.0.20    Office printer
10.10.0.30    File server
10.10.0.40    Enterprise application server
10.10.0.50    Domain services
```

Business IT may have access to:

* Email.
* Internet.
* Office applications.
* Collaboration platforms.
* Enterprise authentication.
* Business databases.
* Reporting systems.

Business IT should not directly access:

* PLCs.
* Turbine controllers.
* Excitation controllers.
* Protection relays.
* RTUs.
* Field devices.
* Engineering workstations.

Correct path:

```text
Business IT
    |
    v
IT firewall
    |
    v
Industrial DMZ service
```

Incorrect path:

```text
Business laptop
    |
    v
Turbine controller
```

---

# 17. Zone 2: Industrial DMZ

```text
Subnet: 10.20.0.0/24
VLAN:  20
Name:  OT-IDMZ
```

Example devices:

```text
10.20.0.10    Jump host
10.20.0.20    Patch staging server
10.20.0.30    Historian replica
10.20.0.40    Remote access gateway
10.20.0.50    File transfer server
10.20.0.60    Security monitoring collector
```

The Industrial DMZ sits between enterprise IT and OT.

```text
Business IT
    |
    v
Firewall 1
    |
    v
Industrial DMZ
    |
    v
Firewall 2
    |
    v
OT control environment
```

The IDMZ prevents direct trust between business and control networks.

Typical IDMZ functions include:

* Remote access termination.
* Jump-host access.
* Patch staging.
* Antivirus update staging.
* Historian replication.
* Controlled file transfer.
* Backup exchange.
* Authentication proxying.
* Log collection.
* Reporting.
* Security monitoring.

The IDMZ should not become a transit network where arbitrary traffic simply passes through.

Each connection should terminate at an IDMZ service.

---

# 18. Zone 3: Plant SCADA and HMI

```text
Subnet: 10.30.0.0/24
VLAN:  30
Name:  OT-SCADA
```

Example devices:

```text
10.30.0.1     Firewall or gateway
10.30.0.10    Operator HMI
10.30.0.11    Backup operator HMI
10.30.0.20    Primary SCADA server
10.30.0.21    Backup SCADA server
10.30.0.30    Historian
10.30.0.40    Alarm and event server
10.30.0.50    Application server
10.30.0.60    Read-only maintenance display
```

Typical SCADA functions include:

* Process visualization.
* Alarm display.
* Event logging.
* Trend display.
* Operator commands.
* Equipment status.
* Generator output display.
* Reservoir-level monitoring.
* Gate-position monitoring.
* Breaker-status monitoring.
* Turbine-speed monitoring.
* Bearing-temperature monitoring.
* Vibration monitoring.

The SCADA zone supervises the process.

It should not automatically be trusted to modify all controller configurations.

---

# 19. Zone 4: Controller Network

```text
Subnet: 10.30.10.0/24
VLAN:  31
Name:  OT-CONTROL
```

Example devices:

```text
10.30.10.1     Firewall or gateway
10.30.10.10    Turbine controller
10.30.10.11    Backup turbine controller
10.30.10.20    Governor controller
10.30.10.21    Excitation controller
10.30.10.30    Auxiliary systems PLC
10.30.10.40    Cooling-water PLC
10.30.10.50    Lubrication-system PLC
10.30.10.60    Local unit HMI
```

This network performs direct process control.

Examples of controlled functions:

* Turbine start and stop sequences.
* Speed control.
* Wicket-gate positioning.
* Generator excitation.
* Voltage regulation.
* Cooling systems.
* Lubrication systems.
* Drainage systems.
* Auxiliary electrical systems.
* Unit synchronization.
* Process interlocks.

This network should have:

* No direct Internet access.
* No general business access.
* Strictly controlled engineering access.
* Only required SCADA communication.
* Static addressing.
* Documented switch-port assignments.
* Passive monitoring where possible.
* Configuration backups.
* Controlled firmware management.

---

# 20. Zone 5: Engineering Workstations

```text
Subnet: 10.30.20.0/24
VLAN:  32
Name:  OT-ENGINEERING
```

Example devices:

```text
10.30.20.1     Firewall or gateway
10.30.20.10    SCADA engineering workstation
10.30.20.20    PLC engineering workstation
10.30.20.30    Protection engineering workstation
10.30.20.40    Configuration backup server
10.30.20.50    Firmware staging system
10.30.20.60    Maintenance jump workstation
```

Engineering workstations are highly privileged.

They may be able to:

* Modify PLC logic.
* Change controller parameters.
* Upload firmware.
* Download configurations.
* Change HMI screens.
* Modify SCADA databases.
* Change relay settings.
* Disable alarms.
* Change network configuration.
* Reset devices.
* Force inputs or outputs.
* Place controllers in programming mode.

These capabilities make engineering workstations more sensitive than operator HMIs.

They should not be used as ordinary office computers.

Recommended controls include:

* No general email.
* No unrestricted web browsing.
* Application allowlisting.
* Removable-media controls.
* Separate administrator accounts.
* Session logging.
* Maintenance approval.
* Configuration backups before changes.
* Defined rollback plans.
* Access only to required device groups.
* Multifactor authentication at the jump-host boundary.
* Time-limited vendor access.

---

# 21. Zone 6: Protection and Relay Network

```text
Subnet: 10.40.0.0/24
VLAN:  40
Name:  OT-PROTECTION
```

Example devices:

```text
10.40.0.1     Firewall or gateway
10.40.0.10    Generator protection relay
10.40.0.11    Transformer protection relay
10.40.0.12    Busbar protection relay
10.40.0.13    Transmission-line protection relay
10.40.0.20    Disturbance recorder
10.40.0.30    Substation gateway
10.40.0.40    Time synchronization source
10.40.0.50    Relay engineering access point
```

Protection systems may:

* Detect overcurrent.
* Detect differential faults.
* Detect ground faults.
* Detect loss of excitation.
* Detect reverse power.
* Detect overvoltage.
* Detect undervoltage.
* Detect overfrequency.
* Detect underfrequency.
* Trip generator breakers.
* Trip transformer breakers.
* Isolate damaged equipment.
* Capture disturbance records.

Protection systems have different requirements from SCADA systems.

They may require:

* Deterministic communication.
* Low latency.
* Precise time synchronization.
* High availability.
* Strict change control.
* Local operation during upstream network failure.
* Separate engineering tools.
* Dedicated multicast handling.
* Specialized redundancy protocols.

Protection traffic such as IEC 61850 GOOSE should not be routed casually through the plant core.

Critical protection traffic may require separate switching, separate VLANs, or separate physical infrastructure.

---

# 22. Zone 7: Remote Telemetry and RTUs

```text
Subnet: 10.50.0.0/24
VLAN:  50
Name:  OT-TELEMETRY
```

Example devices:

```text
10.50.0.1     Firewall or telemetry gateway
10.50.0.10    Remote intake RTU
10.50.0.11    Reservoir-level RTU
10.50.0.12    Spillway RTU
10.50.0.13    Weather-station RTU
10.50.0.14    Downstream-level RTU
10.50.0.20    Radio network gateway
10.50.0.30    Cellular telemetry gateway
```

Remote telemetry may use:

* Fiber.
* Microwave radio.
* Licensed radio.
* Cellular.
* Serial communication.
* Routed WANs.
* DNP3.
* Modbus TCP.
* Modbus RTU.
* Vendor-specific telemetry protocols.

A remote RTU may not physically connect to the main plant switch.

The telemetry subnet still represents its logical security zone.

Remote connections should be treated as lower trust because they may traverse:

* Uncontrolled geographic areas.
* Radio infrastructure.
* Cellular networks.
* Third-party carrier infrastructure.
* Remote cabinets.
* Unattended sites.

---

# 23. Full Logical Network Diagram

```text
                              INTERNET
                                  |
                                  v
                         Enterprise Firewall
                                  |
                                  v
                     BUSINESS IT — VLAN 10
                         10.10.0.0/24
                                  |
                                  v
                         IT-to-IDMZ Firewall
                                  |
                                  v
                        IDMZ — VLAN 20
                         10.20.0.0/24
                  +---------------+---------------+
                  |               |               |
                  v               v               v
             Jump Host      Patch Staging   Historian Replica
                  |
                  v
                         IDMZ-to-OT Firewall
                                  |
             +--------------------+--------------------+
             |                    |                    |
             v                    v                    v
      SCADA/HMI VLAN 30    Engineering VLAN 32   Telemetry VLAN 50
       10.30.0.0/24         10.30.20.0/24         10.50.0.0/24
             |                    |                    |
             +--------------------+                    |
                                  |                    |
                                  v                    v
                         OT Internal Firewall     Remote RTUs
                                  |
                 +----------------+----------------+
                 |                                 |
                 v                                 v
       Controller VLAN 31                 Protection VLAN 40
        10.30.10.0/24                      10.40.0.0/24
                 |                                 |
                 v                                 v
       Turbine and unit PLCs            Relays and bay devices
```

---

# 24. Packet Journey: HMI to Turbine Controller

Consider:

```text
Operator HMI:       10.30.0.10/24
SCADA gateway:      10.30.0.1
Turbine controller: 10.30.10.10/24
Controller gateway: 10.30.10.1
```

## Step 1: The HMI checks the destination

The HMI compares:

```text
Local network:       10.30.0.0/24
Destination network: 10.30.10.0/24
```

The destination is outside the local subnet.

Therefore, the HMI sends the packet to its default gateway.

## Step 2: The HMI resolves the gateway MAC address

The HMI sends:

```text
Who has 10.30.0.1?
Tell 10.30.0.10.
```

The firewall or gateway replies with its MAC address.

## Step 3: The HMI builds the Ethernet frame

Layer-2 information:

```text
Source MAC:       HMI MAC address
Destination MAC:  SCADA gateway MAC address
```

Layer-3 information:

```text
Source IP:        10.30.0.10
Destination IP:   10.30.10.10
```

The destination IP remains the controller's IP.

The Layer-2 destination is the gateway because the controller is in another subnet.

## Step 4: The firewall evaluates policy

Example policy:

```text
Source zone:       OT-SCADA
Source address:    10.30.0.10
Destination zone:  OT-CONTROL
Destination:       10.30.10.10
Protocol:          TCP
Destination port:  502
Action:            Deny
Reason:            HMIs must use the SCADA server
```

The firewall rejects the direct HMI-to-controller connection.

## Step 5: Approved communication path

The intended path is:

```text
Operator HMI
10.30.0.10
    |
    v
SCADA server
10.30.0.20
    |
    v
Industrial firewall
    |
    v
Turbine controller
10.30.10.10
```

The HMI communicates with the SCADA server.

The SCADA server communicates with the controller using an approved industrial protocol.

---

# 25. Why Application Communication Should Be Centralized

Suppose there are:

```text
10 operator HMIs
20 controllers
```

If every HMI communicates directly with every controller:

```text
10 × 20 = 200
```

potential communication relationships exist.

If two SCADA servers provide centralized communication:

```text
10 HMIs → 2 SCADA servers
2 SCADA servers → 20 controllers
```

The architecture becomes easier to:

* Document.
* Monitor.
* Troubleshoot.
* Secure.
* Test.
* Audit.
* Restrict.
* Recover.

Centralization does not eliminate all risk, but it reduces unnecessary communication paths.

---

# 26. Example Firewall Communication Matrix

A firewall policy should begin with a communication matrix.

| ID | Source                         | Destination                  | Protocol/Port                               | Direction                  | Purpose                        | Action             |
| -: | ------------------------------ | ---------------------------- | ------------------------------------------- | -------------------------- | ------------------------------ | ------------------ |
|  1 | Business IT                    | IDMZ jump host               | HTTPS or remote desktop                     | IT → IDMZ                  | Approved administrative access | Allow              |
|  2 | Business IT                    | OT controllers               | Any                                         | IT → OT                    | Direct access not permitted    | Deny               |
|  3 | IDMZ jump host                 | Engineering jump workstation | Approved remote access                      | IDMZ → Engineering         | Controlled OT administration   | Allow              |
|  4 | Patch staging server           | OT update relay              | Approved update protocol                    | IDMZ → OT                  | Transfer approved patches      | Allow              |
|  5 | OT historian                   | IDMZ historian replica       | Historian replication                       | OT → IDMZ                  | Business reporting             | Allow              |
|  6 | Operator HMI                   | SCADA server                 | Vendor application protocol                 | SCADA → SCADA              | Operator visualization         | Allow              |
|  7 | Operator HMI                   | Controller network           | Any                                         | SCADA → Control            | Direct access prohibited       | Deny               |
|  8 | SCADA server                   | Turbine controller           | Required industrial protocol                | SCADA → Control            | Process monitoring and command | Allow              |
|  9 | Engineering workstation        | Turbine controller           | Engineering protocol                        | Engineering → Control      | Approved configuration changes | Conditional allow  |
| 10 | Controller network             | Internet                     | Any                                         | Control → Internet         | Not required                   | Deny               |
| 11 | Protection engineering station | Protection relays            | Vendor relay protocol                       | Engineering → Protection   | Relay configuration            | Conditional allow  |
| 12 | SCADA server                   | Substation gateway           | DNP3, IEC 60870-5-104, or approved protocol | SCADA → Protection gateway | Monitoring and control         | Allow              |
| 13 | SCADA server                   | Individual protection relays | Any                                         | SCADA → Protection         | Direct access unnecessary      | Deny               |
| 14 | SCADA server                   | Telemetry gateway            | DNP3 or approved protocol                   | SCADA → Telemetry          | RTU polling                    | Allow              |
| 15 | Remote RTU                     | Engineering VLAN             | Any                                         | Telemetry → Engineering    | Not required                   | Deny               |
| 16 | OT devices                     | OT NTP server                | UDP 123                                     | OT → Infrastructure        | Time synchronization           | Allow              |
| 17 | OT devices                     | OT DNS server                | UDP/TCP 53                                  | OT → Infrastructure        | Name resolution where required | Allow              |
| 18 | OT devices                     | Log collector                | TCP/UDP 514 or approved TLS port            | OT → Monitoring            | Central logging                | Allow              |
| 19 | Passive sensor                 | OT networks                  | None initiated                              | Monitoring                 | Passive packet observation     | Allow receive-only |
| 20 | Any                            | Any                          | Any                                         | Any                        | Default policy                 | Deny and log       |

The actual ports and protocols must be verified for each vendor and system.

Never open a firewall rule based only on assumptions.

---

# 27. Default-Deny Policy

A secure OT firewall policy starts with:

```text
Deny all traffic
```

Then required traffic is added explicitly.

Conceptual policy:

```text
permit HMI_CLIENTS SCADA_SERVERS approved-scada-client-protocol
permit SCADA_SERVERS CONTROLLERS approved-control-protocol
permit SCADA_SERVERS TELEMETRY_GATEWAY approved-telemetry-protocol
permit SCADA_SERVERS SUBSTATION_GATEWAY approved-substation-protocol
permit OT_DEVICES OT_NTP udp/123
permit OT_DEVICES OT_DNS udp/53
permit OT_DEVICES SYSLOG approved-logging-port
permit HISTORIAN IDMZ_HISTORIAN approved-replication-port
permit ENGINEERING AUTHORIZED_ASSETS approved-engineering-ports
deny any any log
```

Each rule should include:

* Source zone.
* Source address.
* Destination zone.
* Destination address.
* Protocol.
* Port.
* Direction.
* Business or operational justification.
* System owner.
* Approval owner.
* Review date.
* Expiration date where applicable.
* Logging requirements.

---

# 28. Example Switch Port Plan

Consider a 24-port managed industrial switch.

| Port | Connected Device          | Mode                     |                VLAN | Description                      |
| ---: | ------------------------- | ------------------------ | ------------------: | -------------------------------- |
|    1 | Operator HMI 1            | Access                   |                  30 | Main control-room HMI            |
|    2 | Operator HMI 2            | Access                   |                  30 | Backup HMI                       |
|    3 | Primary SCADA server      | Access                   |                  30 | Main SCADA server                |
|    4 | Backup SCADA server       | Access                   |                  30 | Redundant SCADA server           |
|    5 | Historian                 | Access                   |                  30 | OT historian                     |
|    6 | Turbine controller        | Access                   |                  31 | Primary turbine controller       |
|    7 | Backup turbine controller | Access                   |                  31 | Redundant turbine controller     |
|    8 | Governor controller       | Access                   |                  31 | Turbine governor                 |
|    9 | Excitation controller     | Access                   |                  31 | AVR and excitation               |
|   10 | Auxiliary PLC             | Access                   |                  31 | Plant auxiliaries                |
|   11 | SCADA engineering station | Access                   |                  32 | SCADA configuration              |
|   12 | PLC engineering station   | Access                   |                  32 | Controller programming           |
|   13 | Generator relay           | Access                   |                  40 | Generator protection             |
|   14 | Transformer relay         | Access                   |                  40 | Transformer protection           |
|   15 | Substation gateway        | Access                   |                  40 | SCADA-to-substation gateway      |
|   16 | Telemetry gateway         | Access                   |                  50 | Remote RTU aggregation           |
|   17 | NTP server                | Access                   | Infrastructure VLAN | Time source                      |
|   18 | Log collector             | Access                   | Infrastructure VLAN | Central logging                  |
|   19 | Passive monitoring sensor | Monitor/SPAN destination |          Monitoring | Passive IDS                      |
|   20 | Spare                     | Disabled                 |                 999 | Parking VLAN                     |
|   21 | Spare                     | Disabled                 |                 999 | Parking VLAN                     |
|   22 | Spare                     | Disabled                 |                 999 | Parking VLAN                     |
|   23 | Firewall uplink           | Trunk                    |            Multiple | Allowed VLANs only               |
|   24 | Upstream switch           | Trunk                    |            Multiple | Redundant or distribution uplink |

The design should not automatically place all critical zones on the same physical switch.

This layout is intended to teach the mechanics.

---

# 29. Example Access-Port Configuration

Vendor-neutral conceptual configuration:

```text
interface Ethernet1/6
 description TURBINE-CONTROLLER-PRIMARY
 switchport mode access
 switchport access vlan 31
 spanning-tree edge
 no shutdown
```

The exact command syntax varies by switch vendor.

Important properties:

```text
Port mode:       Access
Assigned VLAN:   31
Expected device: Turbine controller
IP subnet:       10.30.10.0/24
```

The connected device should use an address consistent with the VLAN:

```text
IP address:       10.30.10.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.10.1
```

---

# 30. Example Trunk Configuration

Vendor-neutral conceptual configuration:

```text
interface Ethernet1/23
 description OT-FIREWALL-UPLINK
 switchport mode trunk
 switchport trunk allowed vlan 30,31,32,40,50
 no shutdown
```

Only required VLANs should be allowed.

Avoid:

```text
Allow all VLANs
```

Prefer:

```text
Allow VLANs 30,31,32,40,50 only
```

Unused VLANs should not be carried across the trunk.

---

# 31. Firewall Subinterfaces and Gateways

One possible design uses a trunk between the switch and firewall.

The firewall creates one logical interface per VLAN.

Example:

```text
Firewall physical interface: ethernet1
```

Subinterfaces:

```text
ethernet1.30
VLAN tag: 30
IP: 10.30.0.1/24
Zone: OT-SCADA

ethernet1.31
VLAN tag: 31
IP: 10.30.10.1/24
Zone: OT-CONTROL

ethernet1.32
VLAN tag: 32
IP: 10.30.20.1/24
Zone: OT-ENGINEERING

ethernet1.40
VLAN tag: 40
IP: 10.40.0.1/24
Zone: OT-PROTECTION

ethernet1.50
VLAN tag: 50
IP: 10.50.0.1/24
Zone: OT-TELEMETRY
```

The firewall becomes the default gateway for every OT subnet.

This ensures that traffic crossing between subnets passes through security policy.

---

# 32. Common Mistake: Incorrect VLAN and IP Combination

Suppose port 6 is assigned to VLAN 30:

```text
Port 6 → VLAN 30
```

But the connected controller is configured as:

```text
IP address:      10.30.10.10
Default gateway: 10.30.10.1
```

This is incorrect.

The device is physically connected to the Layer-2 domain for:

```text
10.30.0.0/24
```

but configured with an address from:

```text
10.30.10.0/24
```

The controller may be unable to resolve its gateway.

Correct configuration:

```text
Port 6 → VLAN 31
Controller IP → 10.30.10.10/24
Gateway → 10.30.10.1
```

The VLAN assignment and IP subnet must agree.

---

# 33. Common Mistake: Incorrect Subnet Mask

Suppose the HMI is configured as:

```text
IP address:      10.30.0.10
Subnet mask:     255.255.0.0
Default gateway: 10.30.0.1
```

This is a `/16`, not a `/24`.

The HMI may incorrectly believe that `10.30.10.10` is local.

It may send an ARP request directly for the controller instead of sending traffic to the firewall.

Correct mask:

```text
255.255.255.0
```

Correct prefix:

```text
/24
```

Now the HMI correctly recognizes that `10.30.10.10` is remote.

---

# 34. Common Mistake: Flat Layer-2 Design

If HMIs, controllers, relays, and engineering stations are all inside one VLAN, then communication stays inside the switch.

Example:

```text
Engineering workstation → Turbine controller
```

If both devices are in the same VLAN:

```text
No routing required
No firewall crossing required
No inter-zone policy applied
```

The switch forwards the frame directly.

A firewall cannot inspect traffic that never reaches it.

This is why meaningful segmentation requires:

```text
Different VLAN
+
Different subnet
+
Routed boundary
+
Firewall policy
```

---

# 35. Common Mistake: VLANs Without Firewall Rules

Creating VLANs is not sufficient if a Layer-3 switch routes freely between them.

Example:

```text
VLAN 30 → VLAN 31
VLAN 31 → VLAN 32
VLAN 32 → VLAN 40
```

If unrestricted routing exists, segmentation provides organization but little security.

A proper design requires:

```text
Default deny
Explicitly allowed traffic
Logging
Rule ownership
Periodic review
```

---

# 36. Common Mistake: Using Engineering Workstations as General PCs

An engineering workstation should not routinely be used for:

* Email.
* Web browsing.
* Social media.
* General document editing.
* Personal USB devices.
* Unapproved software.
* Remote-control tools.
* Cloud storage synchronization.

A compromised engineering workstation may provide the attacker with legitimate vendor tools capable of changing controller logic.

Engineering workstations should be treated as privileged operational assets.

---

# 37. Common Mistake: Direct Vendor Access

Unsafe path:

```text
Vendor laptop
    |
    v
Internet VPN
    |
    v
Turbine controller
```

Preferred path:

```text
Vendor
    |
    v
VPN with MFA
    |
    v
IDMZ remote-access gateway
    |
    v
Recorded jump host
    |
    v
Engineering workstation or proxy
    |
    v
Specific approved destination
```

Vendor access should be:

* Approved.
* Time limited.
* Logged.
* Monitored.
* Destination restricted.
* Protocol restricted.
* Disabled when not in use.
* Reviewed after maintenance.

---

# 38. Common Mistake: Protection Relays Treated Like Normal Servers

Protection relays are not ordinary IT systems.

They may directly affect:

* Generator breakers.
* Transformer breakers.
* Transmission lines.
* Busbars.
* Plant stability.
* Equipment safety.

Protection network design must consider:

* Latency.
* Availability.
* Determinism.
* Time synchronization.
* Local autonomy.
* Fail-safe behavior.
* Multicast behavior.
* Redundancy.
* Vendor-specific engineering tools.
* Physical access.
* Trip logic.
* Testing and commissioning.

Protection relays should not be placed into a general server VLAN.

---

# 39. Basic Switch Security Practices

Recommended managed-switch controls include:

```text
Disable unused ports
Place unused ports in a parking VLAN
Disable automatic trunk negotiation
Explicitly define trunk ports
Restrict allowed VLANs on trunks
Use SSH instead of Telnet
Use HTTPS instead of HTTP
Use SNMPv3 where supported
Use unique administrative accounts
Restrict management access
Back up switch configurations
Log administrative changes
Protect configuration files
Use secure time synchronization
Enable port descriptions
Document cable and port mappings
Protect network cabinets
```

Additional features may include:

* Port security.
* MAC-address limits.
* DHCP snooping.
* Dynamic ARP inspection.
* BPDU Guard.
* Root Guard.
* Storm control.
* Multicast filtering.
* Access-control lists.
* 802.1X where supported and operationally appropriate.

Not every enterprise feature is safe to enable blindly in an OT environment.

All changes should be tested against device compatibility and availability requirements.

---

# 40. Layer-2 Redundancy Considerations

Hydroelectric plants often require redundant paths.

Possible technologies include:

* Rapid Spanning Tree Protocol.
* Multiple Spanning Tree Protocol.
* Media Redundancy Protocol.
* Parallel Redundancy Protocol.
* High-availability Seamless Redundancy.
* Vendor-specific ring protocols.

Redundancy must be engineered carefully.

Incorrect redundancy configurations can cause:

* Layer-2 loops.
* Broadcast storms.
* Duplicate frames.
* Unexpected reconvergence.
* Multicast flooding.
* Protection-traffic disruption.
* Intermittent controller communication.

Do not enable several redundancy protocols simultaneously without a validated design.

---

# 41. Static IP Addressing

Critical OT devices should normally use static IP addressing.

Examples:

```text
10.30.0.20      Primary SCADA server
10.30.10.10     Turbine controller
10.40.0.10      Generator relay
10.50.0.10      Intake RTU
```

Static addressing provides:

* Predictability.
* Stable firewall policies.
* Easier documentation.
* Easier troubleshooting.
* Easier asset identification.
* Reduced dependence on DHCP.
* Better incident investigation.

DHCP may still be used in controlled cases, but critical devices should not depend on dynamic addressing without a clear operational reason.

---

# 42. Devices Without Default Gateways

Some devices only need to communicate inside their local subnet.

Example:

```text
Local sensor gateway
    |
    v
Unit controller
```

If the device never needs to communicate outside its VLAN, it may not require a default gateway.

Benefits:

* Prevents off-subnet communication.
* Limits accidental access.
* Reduces attack paths.
* Enforces local-only operation.

However, this decision must account for:

* Remote maintenance.
* Time synchronization.
* Central logging.
* Backup requirements.
* Monitoring.
* Firmware updates.

---

# 43. Example Device Naming Convention

A consistent naming convention improves operations.

Example:

```text
HYD-SCADA-SRV01
HYD-SCADA-SRV02
HYD-HMI-CR01
HYD-HMI-CR02
HYD-PLC-TURB01
HYD-PLC-TURB02
HYD-PLC-GOV01
HYD-PLC-EXC01
HYD-EWS-PLC01
HYD-EWS-REL01
HYD-REL-GEN01
HYD-REL-TRF01
HYD-RTU-INTAKE01
HYD-RTU-SPILL01
```

Possible naming fields:

```text
Site
Device class
System
Unit number
Redundancy identifier
```

Example:

```text
HYD-U1-PLC-TURB-A
HYD-U1-PLC-TURB-B
```

---

# 44. Example Addressing Standard

A plant may reserve address ranges by device type.

Example SCADA subnet:

```text
10.30.0.1–9       Gateways and infrastructure
10.30.0.10–19     HMIs
10.30.0.20–29     SCADA servers
10.30.0.30–39     Historians and alarm servers
10.30.0.40–49     Application servers
10.30.0.50–99     Reserved
10.30.0.100–199   Future systems
10.30.0.200–254   Temporary or reserved
```

Example controller subnet:

```text
10.30.10.1–9      Gateways and infrastructure
10.30.10.10–19    Turbine controllers
10.30.10.20–29    Governor and excitation systems
10.30.10.30–39    Auxiliary PLCs
10.30.10.40–49    Cooling and lubrication PLCs
10.30.10.50–99    Local HMIs and gateways
10.30.10.100–254  Reserved
```

Consistency makes the IP address itself informative.

---

# 45. Central Mental Model

When analyzing an OT connection, think in this order:

```text
Application
    |
    v
Device
    |
    v
Network interface
    |
    v
Switch access port
    |
    v
VLAN
    |
    v
IP subnet
    |
    v
Default gateway
    |
    v
Firewall policy
    |
    v
Destination zone
    |
    v
Destination subnet
    |
    v
Destination device
    |
    v
Destination application
```

Example:

```text
SCADA polling application
    |
    v
Primary SCADA server
10.30.0.20
    |
    v
Switch port 3
    |
    v
VLAN 30
    |
    v
10.30.0.0/24
    |
    v
Gateway 10.30.0.1
    |
    v
Industrial firewall
    |
    v
Allow TCP 502 to 10.30.10.10
    |
    v
VLAN 31
    |
    v
10.30.10.0/24
    |
    v
Turbine controller
10.30.10.10
```

---

# 46. Practical Lab Objective

Build a small virtual lab that demonstrates:

1. VLAN creation.
2. Access-port assignment.
3. Trunk configuration.
4. Separate IP subnets.
5. Default gateways.
6. Inter-VLAN routing.
7. Firewall policy.
8. Allowed traffic.
9. Denied traffic.
10. Packet capture.
11. ARP behavior.
12. Basic logging.

Possible lab platforms:

* GNS3.
* EVE-NG.
* Cisco Packet Tracer for basic VLAN concepts.
* Linux network namespaces.
* VirtualBox or VMware.
* pfSense.
* OPNsense.
* FortiGate VM.
* VyOS.
* Open vSwitch.
* Managed physical switch.

---

# 47. Minimal Lab Topology

```text
                 +----------------------+
                 | Firewall or Router   |
                 |                      |
                 | VLAN 30: 10.30.0.1  |
                 | VLAN 31: 10.30.10.1 |
                 | VLAN 32: 10.30.20.1 |
                 +----------+-----------+
                            |
                            | 802.1Q trunk
                            |
                 +----------+-----------+
                 | Managed Switch       |
                 +---+---------+--------+
                     |         |
          VLAN 30    |         | VLAN 31
                     |         |
                 +---v---+ +---v--------+
                 | HMI   | | Controller |
                 |.0.10  | | .10.10     |
                 +-------+ +------------+

                       VLAN 32
                          |
                    +-----v------+
                    | Engineering|
                    | .20.10     |
                    +------------+
```

---

# 48. Suggested Lab IP Addresses

## HMI

```text
IP address:       10.30.0.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.0.1
VLAN:             30
```

## Controller simulator

```text
IP address:       10.30.10.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.10.1
VLAN:             31
```

## Engineering workstation

```text
IP address:       10.30.20.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.20.1
VLAN:             32
```

## Firewall gateways

```text
VLAN 30 gateway:  10.30.0.1
VLAN 31 gateway:  10.30.10.1
VLAN 32 gateway:  10.30.20.1
```

---

# 49. Initial Lab Firewall Policy

Start with:

```text
Deny all inter-VLAN traffic
```

Then create these rules:

```text
Allow HMI → SCADA simulator
Allow SCADA simulator → Controller TCP 502
Allow Engineering workstation → Controller TCP 22
Deny HMI → Controller
Deny Controller → Engineering workstation
Deny Controller → Internet
Log all denied traffic
```

For a simplified lab without a separate SCADA server, temporarily allow:

```text
HMI → Controller TCP 502
```

Then remove that rule and introduce the SCADA server as an intermediary.

This demonstrates how architecture changes the firewall policy.

---

# 50. Lab Validation Tests

## Test 1: Same-VLAN communication

From one SCADA-zone host:

```bash
ping 10.30.0.20
```

Expected:

```text
Success
```

Reason:

```text
Both devices are in VLAN 30 and subnet 10.30.0.0/24.
```

## Test 2: Cross-VLAN routing

From the HMI:

```bash
ping 10.30.10.10
```

Expected:

```text
Denied initially
```

Reason:

```text
Default-deny firewall policy.
```

## Test 3: Allow an approved protocol

Create a firewall rule allowing:

```text
10.30.0.20 → 10.30.10.10 TCP 502
```

Test:

```bash
nc -vz 10.30.10.10 502
```

Expected:

```text
Connection succeeds from the SCADA server.
```

## Test 4: Confirm direct HMI denial

From `10.30.0.10`:

```bash
nc -vz 10.30.10.10 502
```

Expected:

```text
Denied
```

## Test 5: Verify engineering access

From `10.30.20.10`:

```bash
nc -vz 10.30.10.10 22
```

Expected:

```text
Allowed only if the maintenance rule is enabled.
```

## Test 6: Check firewall logs

Verify that denied sessions include:

* Source IP.
* Destination IP.
* Source zone.
* Destination zone.
* Protocol.
* Port.
* Action.
* Timestamp.
* Firewall rule.
* Session result.

---

# 51. Packet Capture Exercises

Use Wireshark or tcpdump to observe the traffic.

## Capture ARP

```bash
sudo tcpdump -ni eth0 arp
```

Observe:

```text
Who has 10.30.0.1?
Tell 10.30.0.10.
```

## Capture ICMP

```bash
sudo tcpdump -ni eth0 icmp
```

## Capture Modbus TCP

```bash
sudo tcpdump -ni eth0 tcp port 502
```

## Capture VLAN tags on a trunk

```bash
sudo tcpdump -eni eth0 vlan
```

A trunk capture may show:

```text
vlan 30
vlan 31
vlan 32
```

An access-port capture normally will not show VLAN tags to the endpoint.

---

# 52. Expected Learning Outcomes

After completing the chapter and lab, the learner should be able to explain:

* What a VLAN is.
* Why VLANs operate at Layer 2.
* What an IP subnet is.
* Why VLANs and subnets are normally mapped one-to-one.
* What an access port is.
* What a trunk port is.
* What an 802.1Q tag is.
* What a broadcast domain is.
* How ARP works inside a VLAN.
* Why routing is required between VLANs.
* What a default gateway does.
* Why an OT firewall should enforce inter-zone communication.
* Why a flat OT network is dangerous.
* Why engineering workstations require special protection.
* Why protection relays should be isolated.
* Why business IT should not directly access controllers.
* How an Industrial DMZ breaks direct trust.
* How to trace a packet from source application to destination application.
* How to validate an OT segmentation design in a lab.

---

# 53. Review Questions

1. What is the difference between a VLAN and an IP subnet?
2. At which OSI layer does a VLAN primarily operate?
3. At which OSI layer does routing occur?
4. Why does a device use ARP?
5. What is a broadcast domain?
6. What is the difference between an access port and a trunk port?
7. Why does a trunk use an 802.1Q tag?
8. Why should one VLAN normally map to one subnet?
9. What happens when a device has the wrong subnet mask?
10. Why does traffic between two VLANs need a gateway?
11. Why should the gateway be a firewall in an OT design?
12. Why might direct HMI-to-controller communication be denied?
13. Why are engineering workstations more sensitive than operator HMIs?
14. Why should protection relays be separated from SCADA servers?
15. What is the purpose of the Industrial DMZ?
16. Why should business IT not connect directly to controllers?
17. Why should unused switch ports be disabled?
18. Why should trunks allow only required VLANs?
19. Why is a default-deny firewall policy preferred?
20. Why may some field devices intentionally have no default gateway?

---

# 54. Practical Exercises

## Exercise 1: Create the VLAN table

Create the following VLANs:

```text
VLAN 10  BUSINESS-IT
VLAN 20  OT-IDMZ
VLAN 30  OT-SCADA
VLAN 31  OT-CONTROL
VLAN 32  OT-ENGINEERING
VLAN 40  OT-PROTECTION
VLAN 50  OT-TELEMETRY
VLAN 999 PARKING
```

## Exercise 2: Assign switch ports

Assign:

```text
Port 1  → VLAN 30
Port 2  → VLAN 31
Port 3  → VLAN 32
Port 23 → Trunk
Port 24 → Trunk
```

## Exercise 3: Configure addressing

Configure:

```text
HMI:         10.30.0.10/24
Controller:  10.30.10.10/24
Engineering: 10.30.20.10/24
```

## Exercise 4: Configure gateways

Configure:

```text
10.30.0.1
10.30.10.1
10.30.20.1
```

## Exercise 5: Test default deny

Verify that no cross-VLAN communication succeeds before rules are added.

## Exercise 6: Add a single approved rule

Allow:

```text
10.30.0.20 → 10.30.10.10 TCP 502
```

Verify that other sources remain blocked.

## Exercise 7: Capture the traffic

Capture:

* ARP.
* ICMP.
* TCP handshake.
* VLAN tags.
* Firewall deny logs.

## Exercise 8: Misconfigure the subnet mask

Set:

```text
10.30.0.10/16
```

Observe how the host treats `10.30.10.10`.

Restore:

```text
10.30.0.10/24
```

Document the difference.

## Exercise 9: Misconfigure the access VLAN

Place the controller port in VLAN 30 while leaving its IP as:

```text
10.30.10.10/24
```

Observe the failure.

Restore the port to VLAN 31.

## Exercise 10: Write a communication matrix

Document every approved flow using:

```text
Source
Destination
Protocol
Port
Direction
Purpose
Owner
Approval
Logging
Expiration
```

---

# 55. Repository Integration Proposal

Suggested repository path:

```text
docs/
└── ot-security/
    └── network-segmentation/
        ├── README.md
        ├── 01-vlan-fundamentals.md
        ├── 02-subnets-and-routing.md
        ├── 03-ot-firewall-policy.md
        ├── 04-hydroelectric-reference-architecture.md
        ├── 05-lab-guide.md
        └── assets/
            ├── diagrams/
            ├── packet-captures/
            └── configs/
```

This document can initially be stored as:

```text
docs/ot-security/network-segmentation/01-vlan-fundamentals.md
```

Future chapters should separate the material into smaller modules.

---

# 56. Suggested Future Chapters

```text
02 — IPv4 subnetting for OT engineers
03 — ARP, MAC tables, and Ethernet forwarding
04 — Access ports, trunks, and 802.1Q
05 — Inter-VLAN routing
06 — OT firewall zones and policies
07 — Industrial DMZ architecture
08 — SCADA, HMI, historian, and controller flows
09 — Engineering workstation security
10 — Substation and IEC 61850 segmentation
11 — Remote RTU and telemetry architecture
12 — Redundancy and high availability
13 — Passive OT monitoring
14 — Asset inventory and network diagrams
15 — Communication matrices
16 — OT incident-response containment
17 — GNS3 hydroelectric OT lab
18 — FortiGate or pfSense implementation
19 — Packet analysis with Wireshark
20 — Capstone hydroelectric plant architecture
```

---

# 57. Definition of Done

This chapter is complete when:

* The VLAN and subnet distinctions are clear.
* The corrected IP mapping is used consistently.
* Every security zone has a defined purpose.
* Access and trunk ports are explained.
* The default gateway is explained.
* A packet journey is documented.
* A firewall communication matrix is included.
* Common design mistakes are included.
* A lab topology is included.
* Validation tests are included.
* Review questions are included.
* Practical exercises are included.
* The document passes Markdown linting.
* Diagrams render correctly.
* Commands are placed in fenced code blocks.
* No vendor-specific command is presented as universally valid.
* Future chapters are linked from the main OT security index.

---

# 58. Key Takeaway

The central lesson is:

```text
A VLAN creates a Layer-2 boundary.
A subnet creates a Layer-3 boundary.
A gateway routes between subnets.
A firewall controls which routed communication is allowed.
A security zone combines these mechanisms with operational policy.
```

For the hydroelectric plant:

```text
Business IT
    ≠
Industrial DMZ
    ≠
SCADA and HMI
    ≠
Controllers
    ≠
Engineering workstations
    ≠
Protection relays
    ≠
Remote RTUs
```

The purpose of segmentation is not merely to organize IP addresses.

The purpose is to ensure that the compromise or failure of one system does not automatically provide access to every other critical system in the plant.
# OT Network Segmentation Fundamentals for a Hydroelectric Power Plant

## Document Purpose

This chapter introduces the fundamentals of OT network segmentation using a simplified hydroelectric power plant architecture.

The objective is to build understanding from first principles:

1. What a VLAN is.
2. How VLANs relate to Ethernet switching.
3. How VLANs relate to IP subnets.
4. What access ports and trunk ports are.
5. Why devices in different VLANs require routing.
6. Why OT environments use firewalls between security zones.
7. How packet flow works between an HMI, a SCADA server, a controller, a relay, and a remote RTU.
8. Why segmentation reduces operational and cybersecurity risk.
9. How to translate a logical design into switch, firewall, and addressing configurations.
10. How to build a small lab that demonstrates these concepts.

This chapter uses a simplified architecture for learning. A real hydroelectric power plant would normally require additional redundancy, vendor-specific protocols, safety-system separation, detailed communication matrices, physical network design, failover testing, and site-specific risk analysis.

---

# 1. Reference Hydroelectric OT Architecture

We will use the following network layout throughout this chapter:

```text
10.10.0.0/24      Business IT
10.20.0.0/24      Industrial DMZ
10.30.0.0/24      Plant SCADA and HMI
10.30.10.0/24     Controller network
10.30.20.0/24     Engineering workstations
10.40.0.0/24      Substation protection and relay network
10.50.0.0/24      Remote telemetry and RTUs
```

Each subnet represents a different operational or security function.

The intended design is:

```text
Business IT
    |
    v
IT Firewall
    |
    v
Industrial DMZ
    |
    v
OT Firewall
    |
    +--------------------+
    |                    |
    v                    v
SCADA/HMI            Engineering
    |
    v
Controller Network
    |
    +--------------------+
    |                    |
    v                    v
Protection Network   Remote Telemetry
```

The most important rule is:

```text
Business IT must not communicate directly with controllers,
protection relays, or remote field devices.
```

---

# 2. Corrected Example IP Mapping

The original addressing example placed HMIs and the historian inside the engineering subnet.

A cleaner mapping is:

```text
10.30.0.10       Operator HMI
10.30.0.11       Operator HMI backup
10.30.0.20       Primary SCADA server
10.30.0.21       Backup SCADA server
10.30.0.30       Historian
10.30.0.40       Alarm and event server

10.30.10.10      Turbine controller
10.30.10.11      Turbine controller backup
10.30.10.20      Governor controller
10.30.10.21      Excitation controller
10.30.10.30      Auxiliary systems PLC

10.30.20.10      SCADA engineering workstation
10.30.20.20      PLC engineering workstation
10.30.20.30      Protection engineering workstation
10.30.20.40      Configuration backup server

10.20.0.10       Jump host in the Industrial DMZ
10.20.0.20       Patch and update staging server
10.20.0.30       Historian replica
10.20.0.40       Remote access gateway

10.40.0.10       Generator protection relay
10.40.0.11       Transformer protection relay
10.40.0.12       Busbar protection relay
10.40.0.13       Transmission line protection relay
10.40.0.20       Disturbance recorder
10.40.0.30       Substation gateway

10.50.0.10       Remote intake RTU
10.50.0.11       Reservoir level RTU
10.50.0.12       Spillway RTU
10.50.0.13       Weather station RTU
10.50.0.14       Downstream water-level RTU
```

This mapping keeps each device in the subnet that represents its actual function.

---

# 3. Why Segmentation Exists

A network can be physically connected while still being logically separated.

Without segmentation, a hydroelectric plant might have:

```text
One switch
One subnet
One broadcast domain
Many unrelated device types
```

Example flat network:

```text
10.30.0.10     Operator HMI
10.30.0.20     Historian
10.30.0.30     Engineering workstation
10.30.0.40     Turbine controller
10.30.0.50     Protection relay
10.30.0.60     Vendor laptop
```

This creates several problems:

* A compromised engineering workstation may directly reach a turbine controller.
* A vendor laptop may directly reach a relay.
* Malware can move laterally without crossing a firewall.
* Broadcast traffic reaches unrelated devices.
* The firewall cannot inspect traffic between devices in the same subnet.
* Troubleshooting becomes more difficult.
* Access policies become vague or impossible to enforce.
* High-value devices become exposed to unnecessary protocols.
* A single misconfiguration can affect the whole plant network.

Segmentation separates devices according to function and risk.

A segmented plant might use:

```text
SCADA devices       → VLAN 30
Controllers         → VLAN 31
Engineering         → VLAN 32
Protection relays   → VLAN 40
Remote RTUs         → VLAN 50
```

Traffic between these zones must cross a router or firewall.

That routing boundary becomes the point where security policy can be enforced.

---

# 4. What Is a VLAN?

VLAN stands for:

```text
Virtual Local Area Network
```

A VLAN divides a physical Ethernet switching infrastructure into multiple logical Layer-2 networks.

A managed switch can behave as though it were several independent switches.

Consider a 24-port managed switch:

```text
Ports 1–4      Business IT
Ports 5–8      Industrial DMZ
Ports 9–12     SCADA and HMI
Ports 13–16    Controllers
Ports 17–18    Engineering workstations
Ports 19–20    Protection relays
Ports 21–22    Remote telemetry
Ports 23–24    Trunk or firewall uplinks
```

Although all devices connect to the same physical switch, the VLAN configuration separates their Ethernet traffic.

Conceptually:

```text
One physical switch
|
+-- Virtual switch for VLAN 10
|
+-- Virtual switch for VLAN 20
|
+-- Virtual switch for VLAN 30
|
+-- Virtual switch for VLAN 31
|
+-- Virtual switch for VLAN 32
|
+-- Virtual switch for VLAN 40
|
+-- Virtual switch for VLAN 50
```

A device in VLAN 30 cannot communicate directly at Layer 2 with a device in VLAN 31.

A routing device is required.

---

# 5. VLANs and the OSI Model

The OSI model helps separate the responsibilities of switches, routers, protocols, and applications.

```text
Layer 7   Application      Modbus TCP, OPC UA, HTTPS, DNP3
Layer 6   Presentation     Encoding, encryption, serialization
Layer 5   Session          Session management
Layer 4   Transport        TCP and UDP
Layer 3   Network          IP addressing and routing
Layer 2   Data Link        Ethernet, MAC addresses, VLANs
Layer 1   Physical         Copper, fiber, radio, connectors
```

VLANs are primarily a Layer-2 technology.

A Layer-2 switch makes forwarding decisions using:

```text
MAC addresses
```

A router or firewall makes forwarding decisions using:

```text
IP addresses
```

Therefore:

```text
VLAN      → Layer-2 separation
Subnet    → Layer-3 separation
Firewall  → Policy enforcement between zones
```

---

# 6. VLAN Versus IP Subnet

A VLAN and an IP subnet are related, but they are not the same thing.

A VLAN defines a Layer-2 broadcast domain.

An IP subnet defines a Layer-3 addressing boundary.

In a clean design, one VLAN normally maps to one IP subnet.

Example:

| VLAN | Name           | Subnet          |
| ---: | -------------- | --------------- |
|   10 | BUSINESS-IT    | `10.10.0.0/24`  |
|   20 | OT-IDMZ        | `10.20.0.0/24`  |
|   30 | OT-SCADA       | `10.30.0.0/24`  |
|   31 | OT-CONTROL     | `10.30.10.0/24` |
|   32 | OT-ENGINEERING | `10.30.20.0/24` |
|   40 | OT-PROTECTION  | `10.40.0.0/24`  |
|   50 | OT-TELEMETRY   | `10.50.0.0/24`  |

The VLAN number does not have to match the subnet.

For example, this is valid:

```text
VLAN 731 → 10.30.10.0/24
```

However, a consistent naming and numbering scheme improves operations and troubleshooting.

---

# 7. Understanding the `/24` Prefix

Consider:

```text
10.30.10.0/24
```

The `/24` means that the first 24 bits represent the network portion.

The corresponding subnet mask is:

```text
255.255.255.0
```

For `10.30.10.0/24`:

```text
Network address:    10.30.10.0
Usable hosts:       10.30.10.1 through 10.30.10.254
Broadcast address:  10.30.10.255
```

The network address identifies the subnet.

The broadcast address represents all devices in that subnet.

Neither address should normally be assigned to a host.

Example controller subnet:

```text
10.30.10.1      Default gateway
10.30.10.10     Turbine controller
10.30.10.11     Turbine controller backup
10.30.10.20     Governor controller
10.30.10.21     Excitation controller
10.30.10.30     Auxiliary systems PLC
10.30.10.255    Broadcast address
```

---

# 8. What Is a Broadcast Domain?

A broadcast domain is the set of devices that receive a Layer-2 broadcast frame.

Examples of traffic that may be broadcast or flooded include:

* ARP requests.
* DHCP discovery.
* Unknown unicast frames.
* Some industrial discovery protocols.
* Legacy service discovery.
* Some multicast traffic, depending on switch configuration.

Suppose the HMI at `10.30.0.10` wants to communicate with the SCADA server at `10.30.0.20`.

The HMI needs the server's MAC address.

It sends an ARP request:

```text
Who has 10.30.0.20?
Tell 10.30.0.10.
```

Every device in the local VLAN receives the request.

Only `10.30.0.20` should reply.

A VLAN limits the broadcast domain.

An ARP request generated in the SCADA VLAN should not reach:

```text
10.30.10.10     Turbine controller
10.40.0.10      Protection relay
10.50.0.10      Remote intake RTU
10.10.0.10      Business workstation
```

This is one reason VLANs improve predictability and reduce unnecessary traffic.

---

# 9. Access Ports

An access port carries traffic for one VLAN.

Example:

```text
Switch port:       Ethernet1/5
Connected device:  Operator HMI
Port mode:         Access
Assigned VLAN:     VLAN 30
```

The HMI normally sends and receives ordinary untagged Ethernet frames.

The HMI does not need to understand VLAN tagging.

The switch associates all untagged traffic arriving on that port with VLAN 30.

Conceptual switch configuration:

```text
interface Ethernet1/5
 description Operator-HMI-01
 switchport mode access
 switchport access vlan 30
```

Typical access-port devices include:

* Operator HMIs.
* PLCs.
* Protection relays.
* Engineering workstations.
* Servers.
* RTUs.
* Network printers.
* Industrial gateways.
* Time servers.
* Local maintenance laptops.

---

# 10. Trunk Ports

A trunk port carries traffic for multiple VLANs over one physical connection.

Typical trunk links include:

```text
Switch to switch
Switch to firewall
Switch to router
Switch to virtualization host
Switch to another building
```

Example:

```text
Core switch
    |
    | Trunk carrying VLANs 20, 30, 31, 32, 40, and 50
    |
Industrial firewall
```

A trunk uses IEEE 802.1Q tagging to identify the VLAN associated with each Ethernet frame.

Conceptually:

```text
Ethernet frame
|
+-- Destination MAC
+-- Source MAC
+-- 802.1Q VLAN tag
+-- EtherType
+-- Payload
+-- Frame check sequence
```

The VLAN tag includes the VLAN identifier.

Example:

```text
VLAN 30 → Plant SCADA
VLAN 31 → Controllers
VLAN 32 → Engineering
VLAN 40 → Protection relays
```

---

# 11. Tagged and Untagged Traffic

Access ports normally carry untagged frames between the endpoint and the switch.

```text
HMI
  |
  | Untagged Ethernet frame
  v
Access port in VLAN 30
```

Trunk ports normally carry tagged frames.

```text
Switch A
  |
  | 802.1Q-tagged frame
  v
Switch B
```

Summary:

| Port type   |   VLANs carried | Frame behavior          |
| ----------- | --------------: | ----------------------- |
| Access      |             One | Usually untagged        |
| Trunk       |        Multiple | Usually tagged          |
| Routed port | None at Layer 2 | Uses Layer-3 addressing |

---

# 12. VLANs Do Not Route Traffic

A VLAN separates Layer-2 traffic.

It does not automatically enable communication between VLANs.

Consider:

```text
Operator HMI:       10.30.0.10/24
Turbine controller: 10.30.10.10/24
```

These devices are in different IP subnets.

The HMI cannot communicate directly with the controller using Layer-2 switching alone.

It must send the packet to a default gateway.

```text
Operator HMI
10.30.0.10
    |
    v
SCADA gateway
10.30.0.1
    |
    v
Firewall or router
    |
    v
Controller gateway
10.30.10.1
    |
    v
Turbine controller
10.30.10.10
```

This process is called:

```text
Inter-VLAN routing
```

---

# 13. The Default Gateway

A host uses its subnet mask to determine whether a destination is local or remote.

Example HMI configuration:

```text
IP address:       10.30.0.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.0.1
```

Destination:

```text
10.30.0.20
```

The destination is inside `10.30.0.0/24`.

The HMI communicates directly using ARP and Ethernet switching.

Destination:

```text
10.30.10.10
```

The destination is outside `10.30.0.0/24`.

The HMI sends the packet to its default gateway.

The gateway then decides:

1. Whether a route exists.
2. Whether the source is allowed.
3. Whether the destination is allowed.
4. Whether the protocol and port are allowed.
5. Whether the packet should be logged.
6. Which outgoing interface should be used.

---

# 14. Why OT Networks Use Firewalls Between VLANs

A Layer-3 switch can route traffic between VLANs.

However, unrestricted routing is often inappropriate in OT.

A better design is:

```text
SCADA VLAN
    |
    v
Industrial firewall
    |
    v
Controller VLAN
```

The firewall evaluates traffic against policy.

Example rule:

```text
Source:       Primary SCADA server
Source IP:    10.30.0.20
Destination:  Turbine controller
Destination IP:
              10.30.10.10
Protocol:     Modbus TCP
Port:         TCP 502
Action:       Allow
Logging:      Enabled
```

A separate rule might deny direct HMI access:

```text
Source:       Operator HMI
Source IP:    10.30.0.10
Destination:  Controller network
Protocol:     Any
Action:       Deny
Logging:      Enabled
```

The intended communication path would then be:

```text
Operator HMI
    |
    v
SCADA server
    |
    v
Turbine controller
```

Instead of:

```text
Operator HMI
    |
    v
Turbine controller
```

---

# 15. VLAN Versus Security Zone

A VLAN is a technical Layer-2 mechanism.

A security zone is an architectural concept.

A security zone groups systems with similar:

* Operational function.
* Trust level.
* Risk.
* Criticality.
* Communication requirements.
* Administrative ownership.
* Maintenance requirements.
* Security controls.

Example:

```text
Security zone: Controller network
VLAN:         31
Subnet:       10.30.10.0/24
Devices:      Turbine, governor, excitation, and auxiliary controllers
```

A complete security zone may include:

* One or more VLANs.
* One or more IP subnets.
* Firewall rules.
* Physical access restrictions.
* User access controls.
* Logging.
* Passive monitoring.
* Patch procedures.
* Backup requirements.
* Incident-response procedures.
* Configuration-management requirements.

A VLAN alone is not a complete security control.

---

# 16. Zone 1: Business IT

```text
Subnet: 10.10.0.0/24
VLAN:  10
Name:  BUSINESS-IT
```

Example devices:

```text
10.10.0.10    Employee laptop
10.10.0.20    Office printer
10.10.0.30    File server
10.10.0.40    Enterprise application server
10.10.0.50    Domain services
```

Business IT may have access to:

* Email.
* Internet.
* Office applications.
* Collaboration platforms.
* Enterprise authentication.
* Business databases.
* Reporting systems.

Business IT should not directly access:

* PLCs.
* Turbine controllers.
* Excitation controllers.
* Protection relays.
* RTUs.
* Field devices.
* Engineering workstations.

Correct path:

```text
Business IT
    |
    v
IT firewall
    |
    v
Industrial DMZ service
```

Incorrect path:

```text
Business laptop
    |
    v
Turbine controller
```

---

# 17. Zone 2: Industrial DMZ

```text
Subnet: 10.20.0.0/24
VLAN:  20
Name:  OT-IDMZ
```

Example devices:

```text
10.20.0.10    Jump host
10.20.0.20    Patch staging server
10.20.0.30    Historian replica
10.20.0.40    Remote access gateway
10.20.0.50    File transfer server
10.20.0.60    Security monitoring collector
```

The Industrial DMZ sits between enterprise IT and OT.

```text
Business IT
    |
    v
Firewall 1
    |
    v
Industrial DMZ
    |
    v
Firewall 2
    |
    v
OT control environment
```

The IDMZ prevents direct trust between business and control networks.

Typical IDMZ functions include:

* Remote access termination.
* Jump-host access.
* Patch staging.
* Antivirus update staging.
* Historian replication.
* Controlled file transfer.
* Backup exchange.
* Authentication proxying.
* Log collection.
* Reporting.
* Security monitoring.

The IDMZ should not become a transit network where arbitrary traffic simply passes through.

Each connection should terminate at an IDMZ service.

---

# 18. Zone 3: Plant SCADA and HMI

```text
Subnet: 10.30.0.0/24
VLAN:  30
Name:  OT-SCADA
```

Example devices:

```text
10.30.0.1     Firewall or gateway
10.30.0.10    Operator HMI
10.30.0.11    Backup operator HMI
10.30.0.20    Primary SCADA server
10.30.0.21    Backup SCADA server
10.30.0.30    Historian
10.30.0.40    Alarm and event server
10.30.0.50    Application server
10.30.0.60    Read-only maintenance display
```

Typical SCADA functions include:

* Process visualization.
* Alarm display.
* Event logging.
* Trend display.
* Operator commands.
* Equipment status.
* Generator output display.
* Reservoir-level monitoring.
* Gate-position monitoring.
* Breaker-status monitoring.
* Turbine-speed monitoring.
* Bearing-temperature monitoring.
* Vibration monitoring.

The SCADA zone supervises the process.

It should not automatically be trusted to modify all controller configurations.

---

# 19. Zone 4: Controller Network

```text
Subnet: 10.30.10.0/24
VLAN:  31
Name:  OT-CONTROL
```

Example devices:

```text
10.30.10.1     Firewall or gateway
10.30.10.10    Turbine controller
10.30.10.11    Backup turbine controller
10.30.10.20    Governor controller
10.30.10.21    Excitation controller
10.30.10.30    Auxiliary systems PLC
10.30.10.40    Cooling-water PLC
10.30.10.50    Lubrication-system PLC
10.30.10.60    Local unit HMI
```

This network performs direct process control.

Examples of controlled functions:

* Turbine start and stop sequences.
* Speed control.
* Wicket-gate positioning.
* Generator excitation.
* Voltage regulation.
* Cooling systems.
* Lubrication systems.
* Drainage systems.
* Auxiliary electrical systems.
* Unit synchronization.
* Process interlocks.

This network should have:

* No direct Internet access.
* No general business access.
* Strictly controlled engineering access.
* Only required SCADA communication.
* Static addressing.
* Documented switch-port assignments.
* Passive monitoring where possible.
* Configuration backups.
* Controlled firmware management.

---

# 20. Zone 5: Engineering Workstations

```text
Subnet: 10.30.20.0/24
VLAN:  32
Name:  OT-ENGINEERING
```

Example devices:

```text
10.30.20.1     Firewall or gateway
10.30.20.10    SCADA engineering workstation
10.30.20.20    PLC engineering workstation
10.30.20.30    Protection engineering workstation
10.30.20.40    Configuration backup server
10.30.20.50    Firmware staging system
10.30.20.60    Maintenance jump workstation
```

Engineering workstations are highly privileged.

They may be able to:

* Modify PLC logic.
* Change controller parameters.
* Upload firmware.
* Download configurations.
* Change HMI screens.
* Modify SCADA databases.
* Change relay settings.
* Disable alarms.
* Change network configuration.
* Reset devices.
* Force inputs or outputs.
* Place controllers in programming mode.

These capabilities make engineering workstations more sensitive than operator HMIs.

They should not be used as ordinary office computers.

Recommended controls include:

* No general email.
* No unrestricted web browsing.
* Application allowlisting.
* Removable-media controls.
* Separate administrator accounts.
* Session logging.
* Maintenance approval.
* Configuration backups before changes.
* Defined rollback plans.
* Access only to required device groups.
* Multifactor authentication at the jump-host boundary.
* Time-limited vendor access.

---

# 21. Zone 6: Protection and Relay Network

```text
Subnet: 10.40.0.0/24
VLAN:  40
Name:  OT-PROTECTION
```

Example devices:

```text
10.40.0.1     Firewall or gateway
10.40.0.10    Generator protection relay
10.40.0.11    Transformer protection relay
10.40.0.12    Busbar protection relay
10.40.0.13    Transmission-line protection relay
10.40.0.20    Disturbance recorder
10.40.0.30    Substation gateway
10.40.0.40    Time synchronization source
10.40.0.50    Relay engineering access point
```

Protection systems may:

* Detect overcurrent.
* Detect differential faults.
* Detect ground faults.
* Detect loss of excitation.
* Detect reverse power.
* Detect overvoltage.
* Detect undervoltage.
* Detect overfrequency.
* Detect underfrequency.
* Trip generator breakers.
* Trip transformer breakers.
* Isolate damaged equipment.
* Capture disturbance records.

Protection systems have different requirements from SCADA systems.

They may require:

* Deterministic communication.
* Low latency.
* Precise time synchronization.
* High availability.
* Strict change control.
* Local operation during upstream network failure.
* Separate engineering tools.
* Dedicated multicast handling.
* Specialized redundancy protocols.

Protection traffic such as IEC 61850 GOOSE should not be routed casually through the plant core.

Critical protection traffic may require separate switching, separate VLANs, or separate physical infrastructure.

---

# 22. Zone 7: Remote Telemetry and RTUs

```text
Subnet: 10.50.0.0/24
VLAN:  50
Name:  OT-TELEMETRY
```

Example devices:

```text
10.50.0.1     Firewall or telemetry gateway
10.50.0.10    Remote intake RTU
10.50.0.11    Reservoir-level RTU
10.50.0.12    Spillway RTU
10.50.0.13    Weather-station RTU
10.50.0.14    Downstream-level RTU
10.50.0.20    Radio network gateway
10.50.0.30    Cellular telemetry gateway
```

Remote telemetry may use:

* Fiber.
* Microwave radio.
* Licensed radio.
* Cellular.
* Serial communication.
* Routed WANs.
* DNP3.
* Modbus TCP.
* Modbus RTU.
* Vendor-specific telemetry protocols.

A remote RTU may not physically connect to the main plant switch.

The telemetry subnet still represents its logical security zone.

Remote connections should be treated as lower trust because they may traverse:

* Uncontrolled geographic areas.
* Radio infrastructure.
* Cellular networks.
* Third-party carrier infrastructure.
* Remote cabinets.
* Unattended sites.

---

# 23. Full Logical Network Diagram

```text
                              INTERNET
                                  |
                                  v
                         Enterprise Firewall
                                  |
                                  v
                     BUSINESS IT — VLAN 10
                         10.10.0.0/24
                                  |
                                  v
                         IT-to-IDMZ Firewall
                                  |
                                  v
                        IDMZ — VLAN 20
                         10.20.0.0/24
                  +---------------+---------------+
                  |               |               |
                  v               v               v
             Jump Host      Patch Staging   Historian Replica
                  |
                  v
                         IDMZ-to-OT Firewall
                                  |
             +--------------------+--------------------+
             |                    |                    |
             v                    v                    v
      SCADA/HMI VLAN 30    Engineering VLAN 32   Telemetry VLAN 50
       10.30.0.0/24         10.30.20.0/24         10.50.0.0/24
             |                    |                    |
             +--------------------+                    |
                                  |                    |
                                  v                    v
                         OT Internal Firewall     Remote RTUs
                                  |
                 +----------------+----------------+
                 |                                 |
                 v                                 v
       Controller VLAN 31                 Protection VLAN 40
        10.30.10.0/24                      10.40.0.0/24
                 |                                 |
                 v                                 v
       Turbine and unit PLCs            Relays and bay devices
```

---

# 24. Packet Journey: HMI to Turbine Controller

Consider:

```text
Operator HMI:       10.30.0.10/24
SCADA gateway:      10.30.0.1
Turbine controller: 10.30.10.10/24
Controller gateway: 10.30.10.1
```

## Step 1: The HMI checks the destination

The HMI compares:

```text
Local network:       10.30.0.0/24
Destination network: 10.30.10.0/24
```

The destination is outside the local subnet.

Therefore, the HMI sends the packet to its default gateway.

## Step 2: The HMI resolves the gateway MAC address

The HMI sends:

```text
Who has 10.30.0.1?
Tell 10.30.0.10.
```

The firewall or gateway replies with its MAC address.

## Step 3: The HMI builds the Ethernet frame

Layer-2 information:

```text
Source MAC:       HMI MAC address
Destination MAC:  SCADA gateway MAC address
```

Layer-3 information:

```text
Source IP:        10.30.0.10
Destination IP:   10.30.10.10
```

The destination IP remains the controller's IP.

The Layer-2 destination is the gateway because the controller is in another subnet.

## Step 4: The firewall evaluates policy

Example policy:

```text
Source zone:       OT-SCADA
Source address:    10.30.0.10
Destination zone:  OT-CONTROL
Destination:       10.30.10.10
Protocol:          TCP
Destination port:  502
Action:            Deny
Reason:            HMIs must use the SCADA server
```

The firewall rejects the direct HMI-to-controller connection.

## Step 5: Approved communication path

The intended path is:

```text
Operator HMI
10.30.0.10
    |
    v
SCADA server
10.30.0.20
    |
    v
Industrial firewall
    |
    v
Turbine controller
10.30.10.10
```

The HMI communicates with the SCADA server.

The SCADA server communicates with the controller using an approved industrial protocol.

---

# 25. Why Application Communication Should Be Centralized

Suppose there are:

```text
10 operator HMIs
20 controllers
```

If every HMI communicates directly with every controller:

```text
10 × 20 = 200
```

potential communication relationships exist.

If two SCADA servers provide centralized communication:

```text
10 HMIs → 2 SCADA servers
2 SCADA servers → 20 controllers
```

The architecture becomes easier to:

* Document.
* Monitor.
* Troubleshoot.
* Secure.
* Test.
* Audit.
* Restrict.
* Recover.

Centralization does not eliminate all risk, but it reduces unnecessary communication paths.

---

# 26. Example Firewall Communication Matrix

A firewall policy should begin with a communication matrix.

| ID | Source                         | Destination                  | Protocol/Port                               | Direction                  | Purpose                        | Action             |
| -: | ------------------------------ | ---------------------------- | ------------------------------------------- | -------------------------- | ------------------------------ | ------------------ |
|  1 | Business IT                    | IDMZ jump host               | HTTPS or remote desktop                     | IT → IDMZ                  | Approved administrative access | Allow              |
|  2 | Business IT                    | OT controllers               | Any                                         | IT → OT                    | Direct access not permitted    | Deny               |
|  3 | IDMZ jump host                 | Engineering jump workstation | Approved remote access                      | IDMZ → Engineering         | Controlled OT administration   | Allow              |
|  4 | Patch staging server           | OT update relay              | Approved update protocol                    | IDMZ → OT                  | Transfer approved patches      | Allow              |
|  5 | OT historian                   | IDMZ historian replica       | Historian replication                       | OT → IDMZ                  | Business reporting             | Allow              |
|  6 | Operator HMI                   | SCADA server                 | Vendor application protocol                 | SCADA → SCADA              | Operator visualization         | Allow              |
|  7 | Operator HMI                   | Controller network           | Any                                         | SCADA → Control            | Direct access prohibited       | Deny               |
|  8 | SCADA server                   | Turbine controller           | Required industrial protocol                | SCADA → Control            | Process monitoring and command | Allow              |
|  9 | Engineering workstation        | Turbine controller           | Engineering protocol                        | Engineering → Control      | Approved configuration changes | Conditional allow  |
| 10 | Controller network             | Internet                     | Any                                         | Control → Internet         | Not required                   | Deny               |
| 11 | Protection engineering station | Protection relays            | Vendor relay protocol                       | Engineering → Protection   | Relay configuration            | Conditional allow  |
| 12 | SCADA server                   | Substation gateway           | DNP3, IEC 60870-5-104, or approved protocol | SCADA → Protection gateway | Monitoring and control         | Allow              |
| 13 | SCADA server                   | Individual protection relays | Any                                         | SCADA → Protection         | Direct access unnecessary      | Deny               |
| 14 | SCADA server                   | Telemetry gateway            | DNP3 or approved protocol                   | SCADA → Telemetry          | RTU polling                    | Allow              |
| 15 | Remote RTU                     | Engineering VLAN             | Any                                         | Telemetry → Engineering    | Not required                   | Deny               |
| 16 | OT devices                     | OT NTP server                | UDP 123                                     | OT → Infrastructure        | Time synchronization           | Allow              |
| 17 | OT devices                     | OT DNS server                | UDP/TCP 53                                  | OT → Infrastructure        | Name resolution where required | Allow              |
| 18 | OT devices                     | Log collector                | TCP/UDP 514 or approved TLS port            | OT → Monitoring            | Central logging                | Allow              |
| 19 | Passive sensor                 | OT networks                  | None initiated                              | Monitoring                 | Passive packet observation     | Allow receive-only |
| 20 | Any                            | Any                          | Any                                         | Any                        | Default policy                 | Deny and log       |

The actual ports and protocols must be verified for each vendor and system.

Never open a firewall rule based only on assumptions.

---

# 27. Default-Deny Policy

A secure OT firewall policy starts with:

```text
Deny all traffic
```

Then required traffic is added explicitly.

Conceptual policy:

```text
permit HMI_CLIENTS SCADA_SERVERS approved-scada-client-protocol
permit SCADA_SERVERS CONTROLLERS approved-control-protocol
permit SCADA_SERVERS TELEMETRY_GATEWAY approved-telemetry-protocol
permit SCADA_SERVERS SUBSTATION_GATEWAY approved-substation-protocol
permit OT_DEVICES OT_NTP udp/123
permit OT_DEVICES OT_DNS udp/53
permit OT_DEVICES SYSLOG approved-logging-port
permit HISTORIAN IDMZ_HISTORIAN approved-replication-port
permit ENGINEERING AUTHORIZED_ASSETS approved-engineering-ports
deny any any log
```

Each rule should include:

* Source zone.
* Source address.
* Destination zone.
* Destination address.
* Protocol.
* Port.
* Direction.
* Business or operational justification.
* System owner.
* Approval owner.
* Review date.
* Expiration date where applicable.
* Logging requirements.

---

# 28. Example Switch Port Plan

Consider a 24-port managed industrial switch.

| Port | Connected Device          | Mode                     |                VLAN | Description                      |
| ---: | ------------------------- | ------------------------ | ------------------: | -------------------------------- |
|    1 | Operator HMI 1            | Access                   |                  30 | Main control-room HMI            |
|    2 | Operator HMI 2            | Access                   |                  30 | Backup HMI                       |
|    3 | Primary SCADA server      | Access                   |                  30 | Main SCADA server                |
|    4 | Backup SCADA server       | Access                   |                  30 | Redundant SCADA server           |
|    5 | Historian                 | Access                   |                  30 | OT historian                     |
|    6 | Turbine controller        | Access                   |                  31 | Primary turbine controller       |
|    7 | Backup turbine controller | Access                   |                  31 | Redundant turbine controller     |
|    8 | Governor controller       | Access                   |                  31 | Turbine governor                 |
|    9 | Excitation controller     | Access                   |                  31 | AVR and excitation               |
|   10 | Auxiliary PLC             | Access                   |                  31 | Plant auxiliaries                |
|   11 | SCADA engineering station | Access                   |                  32 | SCADA configuration              |
|   12 | PLC engineering station   | Access                   |                  32 | Controller programming           |
|   13 | Generator relay           | Access                   |                  40 | Generator protection             |
|   14 | Transformer relay         | Access                   |                  40 | Transformer protection           |
|   15 | Substation gateway        | Access                   |                  40 | SCADA-to-substation gateway      |
|   16 | Telemetry gateway         | Access                   |                  50 | Remote RTU aggregation           |
|   17 | NTP server                | Access                   | Infrastructure VLAN | Time source                      |
|   18 | Log collector             | Access                   | Infrastructure VLAN | Central logging                  |
|   19 | Passive monitoring sensor | Monitor/SPAN destination |          Monitoring | Passive IDS                      |
|   20 | Spare                     | Disabled                 |                 999 | Parking VLAN                     |
|   21 | Spare                     | Disabled                 |                 999 | Parking VLAN                     |
|   22 | Spare                     | Disabled                 |                 999 | Parking VLAN                     |
|   23 | Firewall uplink           | Trunk                    |            Multiple | Allowed VLANs only               |
|   24 | Upstream switch           | Trunk                    |            Multiple | Redundant or distribution uplink |

The design should not automatically place all critical zones on the same physical switch.

This layout is intended to teach the mechanics.

---

# 29. Example Access-Port Configuration

Vendor-neutral conceptual configuration:

```text
interface Ethernet1/6
 description TURBINE-CONTROLLER-PRIMARY
 switchport mode access
 switchport access vlan 31
 spanning-tree edge
 no shutdown
```

The exact command syntax varies by switch vendor.

Important properties:

```text
Port mode:       Access
Assigned VLAN:   31
Expected device: Turbine controller
IP subnet:       10.30.10.0/24
```

The connected device should use an address consistent with the VLAN:

```text
IP address:       10.30.10.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.10.1
```

---

# 30. Example Trunk Configuration

Vendor-neutral conceptual configuration:

```text
interface Ethernet1/23
 description OT-FIREWALL-UPLINK
 switchport mode trunk
 switchport trunk allowed vlan 30,31,32,40,50
 no shutdown
```

Only required VLANs should be allowed.

Avoid:

```text
Allow all VLANs
```

Prefer:

```text
Allow VLANs 30,31,32,40,50 only
```

Unused VLANs should not be carried across the trunk.

---

# 31. Firewall Subinterfaces and Gateways

One possible design uses a trunk between the switch and firewall.

The firewall creates one logical interface per VLAN.

Example:

```text
Firewall physical interface: ethernet1
```

Subinterfaces:

```text
ethernet1.30
VLAN tag: 30
IP: 10.30.0.1/24
Zone: OT-SCADA

ethernet1.31
VLAN tag: 31
IP: 10.30.10.1/24
Zone: OT-CONTROL

ethernet1.32
VLAN tag: 32
IP: 10.30.20.1/24
Zone: OT-ENGINEERING

ethernet1.40
VLAN tag: 40
IP: 10.40.0.1/24
Zone: OT-PROTECTION

ethernet1.50
VLAN tag: 50
IP: 10.50.0.1/24
Zone: OT-TELEMETRY
```

The firewall becomes the default gateway for every OT subnet.

This ensures that traffic crossing between subnets passes through security policy.

---

# 32. Common Mistake: Incorrect VLAN and IP Combination

Suppose port 6 is assigned to VLAN 30:

```text
Port 6 → VLAN 30
```

But the connected controller is configured as:

```text
IP address:      10.30.10.10
Default gateway: 10.30.10.1
```

This is incorrect.

The device is physically connected to the Layer-2 domain for:

```text
10.30.0.0/24
```

but configured with an address from:

```text
10.30.10.0/24
```

The controller may be unable to resolve its gateway.

Correct configuration:

```text
Port 6 → VLAN 31
Controller IP → 10.30.10.10/24
Gateway → 10.30.10.1
```

The VLAN assignment and IP subnet must agree.

---

# 33. Common Mistake: Incorrect Subnet Mask

Suppose the HMI is configured as:

```text
IP address:      10.30.0.10
Subnet mask:     255.255.0.0
Default gateway: 10.30.0.1
```

This is a `/16`, not a `/24`.

The HMI may incorrectly believe that `10.30.10.10` is local.

It may send an ARP request directly for the controller instead of sending traffic to the firewall.

Correct mask:

```text
255.255.255.0
```

Correct prefix:

```text
/24
```

Now the HMI correctly recognizes that `10.30.10.10` is remote.

---

# 34. Common Mistake: Flat Layer-2 Design

If HMIs, controllers, relays, and engineering stations are all inside one VLAN, then communication stays inside the switch.

Example:

```text
Engineering workstation → Turbine controller
```

If both devices are in the same VLAN:

```text
No routing required
No firewall crossing required
No inter-zone policy applied
```

The switch forwards the frame directly.

A firewall cannot inspect traffic that never reaches it.

This is why meaningful segmentation requires:

```text
Different VLAN
+
Different subnet
+
Routed boundary
+
Firewall policy
```

---

# 35. Common Mistake: VLANs Without Firewall Rules

Creating VLANs is not sufficient if a Layer-3 switch routes freely between them.

Example:

```text
VLAN 30 → VLAN 31
VLAN 31 → VLAN 32
VLAN 32 → VLAN 40
```

If unrestricted routing exists, segmentation provides organization but little security.

A proper design requires:

```text
Default deny
Explicitly allowed traffic
Logging
Rule ownership
Periodic review
```

---

# 36. Common Mistake: Using Engineering Workstations as General PCs

An engineering workstation should not routinely be used for:

* Email.
* Web browsing.
* Social media.
* General document editing.
* Personal USB devices.
* Unapproved software.
* Remote-control tools.
* Cloud storage synchronization.

A compromised engineering workstation may provide the attacker with legitimate vendor tools capable of changing controller logic.

Engineering workstations should be treated as privileged operational assets.

---

# 37. Common Mistake: Direct Vendor Access

Unsafe path:

```text
Vendor laptop
    |
    v
Internet VPN
    |
    v
Turbine controller
```

Preferred path:

```text
Vendor
    |
    v
VPN with MFA
    |
    v
IDMZ remote-access gateway
    |
    v
Recorded jump host
    |
    v
Engineering workstation or proxy
    |
    v
Specific approved destination
```

Vendor access should be:

* Approved.
* Time limited.
* Logged.
* Monitored.
* Destination restricted.
* Protocol restricted.
* Disabled when not in use.
* Reviewed after maintenance.

---

# 38. Common Mistake: Protection Relays Treated Like Normal Servers

Protection relays are not ordinary IT systems.

They may directly affect:

* Generator breakers.
* Transformer breakers.
* Transmission lines.
* Busbars.
* Plant stability.
* Equipment safety.

Protection network design must consider:

* Latency.
* Availability.
* Determinism.
* Time synchronization.
* Local autonomy.
* Fail-safe behavior.
* Multicast behavior.
* Redundancy.
* Vendor-specific engineering tools.
* Physical access.
* Trip logic.
* Testing and commissioning.

Protection relays should not be placed into a general server VLAN.

---

# 39. Basic Switch Security Practices

Recommended managed-switch controls include:

```text
Disable unused ports
Place unused ports in a parking VLAN
Disable automatic trunk negotiation
Explicitly define trunk ports
Restrict allowed VLANs on trunks
Use SSH instead of Telnet
Use HTTPS instead of HTTP
Use SNMPv3 where supported
Use unique administrative accounts
Restrict management access
Back up switch configurations
Log administrative changes
Protect configuration files
Use secure time synchronization
Enable port descriptions
Document cable and port mappings
Protect network cabinets
```

Additional features may include:

* Port security.
* MAC-address limits.
* DHCP snooping.
* Dynamic ARP inspection.
* BPDU Guard.
* Root Guard.
* Storm control.
* Multicast filtering.
* Access-control lists.
* 802.1X where supported and operationally appropriate.

Not every enterprise feature is safe to enable blindly in an OT environment.

All changes should be tested against device compatibility and availability requirements.

---

# 40. Layer-2 Redundancy Considerations

Hydroelectric plants often require redundant paths.

Possible technologies include:

* Rapid Spanning Tree Protocol.
* Multiple Spanning Tree Protocol.
* Media Redundancy Protocol.
* Parallel Redundancy Protocol.
* High-availability Seamless Redundancy.
* Vendor-specific ring protocols.

Redundancy must be engineered carefully.

Incorrect redundancy configurations can cause:

* Layer-2 loops.
* Broadcast storms.
* Duplicate frames.
* Unexpected reconvergence.
* Multicast flooding.
* Protection-traffic disruption.
* Intermittent controller communication.

Do not enable several redundancy protocols simultaneously without a validated design.

---

# 41. Static IP Addressing

Critical OT devices should normally use static IP addressing.

Examples:

```text
10.30.0.20      Primary SCADA server
10.30.10.10     Turbine controller
10.40.0.10      Generator relay
10.50.0.10      Intake RTU
```

Static addressing provides:

* Predictability.
* Stable firewall policies.
* Easier documentation.
* Easier troubleshooting.
* Easier asset identification.
* Reduced dependence on DHCP.
* Better incident investigation.

DHCP may still be used in controlled cases, but critical devices should not depend on dynamic addressing without a clear operational reason.

---

# 42. Devices Without Default Gateways

Some devices only need to communicate inside their local subnet.

Example:

```text
Local sensor gateway
    |
    v
Unit controller
```

If the device never needs to communicate outside its VLAN, it may not require a default gateway.

Benefits:

* Prevents off-subnet communication.
* Limits accidental access.
* Reduces attack paths.
* Enforces local-only operation.

However, this decision must account for:

* Remote maintenance.
* Time synchronization.
* Central logging.
* Backup requirements.
* Monitoring.
* Firmware updates.

---

# 43. Example Device Naming Convention

A consistent naming convention improves operations.

Example:

```text
HYD-SCADA-SRV01
HYD-SCADA-SRV02
HYD-HMI-CR01
HYD-HMI-CR02
HYD-PLC-TURB01
HYD-PLC-TURB02
HYD-PLC-GOV01
HYD-PLC-EXC01
HYD-EWS-PLC01
HYD-EWS-REL01
HYD-REL-GEN01
HYD-REL-TRF01
HYD-RTU-INTAKE01
HYD-RTU-SPILL01
```

Possible naming fields:

```text
Site
Device class
System
Unit number
Redundancy identifier
```

Example:

```text
HYD-U1-PLC-TURB-A
HYD-U1-PLC-TURB-B
```

---

# 44. Example Addressing Standard

A plant may reserve address ranges by device type.

Example SCADA subnet:

```text
10.30.0.1–9       Gateways and infrastructure
10.30.0.10–19     HMIs
10.30.0.20–29     SCADA servers
10.30.0.30–39     Historians and alarm servers
10.30.0.40–49     Application servers
10.30.0.50–99     Reserved
10.30.0.100–199   Future systems
10.30.0.200–254   Temporary or reserved
```

Example controller subnet:

```text
10.30.10.1–9      Gateways and infrastructure
10.30.10.10–19    Turbine controllers
10.30.10.20–29    Governor and excitation systems
10.30.10.30–39    Auxiliary PLCs
10.30.10.40–49    Cooling and lubrication PLCs
10.30.10.50–99    Local HMIs and gateways
10.30.10.100–254  Reserved
```

Consistency makes the IP address itself informative.

---

# 45. Central Mental Model

When analyzing an OT connection, think in this order:

```text
Application
    |
    v
Device
    |
    v
Network interface
    |
    v
Switch access port
    |
    v
VLAN
    |
    v
IP subnet
    |
    v
Default gateway
    |
    v
Firewall policy
    |
    v
Destination zone
    |
    v
Destination subnet
    |
    v
Destination device
    |
    v
Destination application
```

Example:

```text
SCADA polling application
    |
    v
Primary SCADA server
10.30.0.20
    |
    v
Switch port 3
    |
    v
VLAN 30
    |
    v
10.30.0.0/24
    |
    v
Gateway 10.30.0.1
    |
    v
Industrial firewall
    |
    v
Allow TCP 502 to 10.30.10.10
    |
    v
VLAN 31
    |
    v
10.30.10.0/24
    |
    v
Turbine controller
10.30.10.10
```

---

# 46. Practical Lab Objective

Build a small virtual lab that demonstrates:

1. VLAN creation.
2. Access-port assignment.
3. Trunk configuration.
4. Separate IP subnets.
5. Default gateways.
6. Inter-VLAN routing.
7. Firewall policy.
8. Allowed traffic.
9. Denied traffic.
10. Packet capture.
11. ARP behavior.
12. Basic logging.

Possible lab platforms:

* GNS3.
* EVE-NG.
* Cisco Packet Tracer for basic VLAN concepts.
* Linux network namespaces.
* VirtualBox or VMware.
* pfSense.
* OPNsense.
* FortiGate VM.
* VyOS.
* Open vSwitch.
* Managed physical switch.

---

# 47. Minimal Lab Topology

```text
                 +----------------------+
                 | Firewall or Router   |
                 |                      |
                 | VLAN 30: 10.30.0.1  |
                 | VLAN 31: 10.30.10.1 |
                 | VLAN 32: 10.30.20.1 |
                 +----------+-----------+
                            |
                            | 802.1Q trunk
                            |
                 +----------+-----------+
                 | Managed Switch       |
                 +---+---------+--------+
                     |         |
          VLAN 30    |         | VLAN 31
                     |         |
                 +---v---+ +---v--------+
                 | HMI   | | Controller |
                 |.0.10  | | .10.10     |
                 +-------+ +------------+

                       VLAN 32
                          |
                    +-----v------+
                    | Engineering|
                    | .20.10     |
                    +------------+
```

---

# 48. Suggested Lab IP Addresses

## HMI

```text
IP address:       10.30.0.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.0.1
VLAN:             30
```

## Controller simulator

```text
IP address:       10.30.10.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.10.1
VLAN:             31
```

## Engineering workstation

```text
IP address:       10.30.20.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.20.1
VLAN:             32
```

## Firewall gateways

```text
VLAN 30 gateway:  10.30.0.1
VLAN 31 gateway:  10.30.10.1
VLAN 32 gateway:  10.30.20.1
```

---

# 49. Initial Lab Firewall Policy

Start with:

```text
Deny all inter-VLAN traffic
```

Then create these rules:

```text
Allow HMI → SCADA simulator
Allow SCADA simulator → Controller TCP 502
Allow Engineering workstation → Controller TCP 22
Deny HMI → Controller
Deny Controller → Engineering workstation
Deny Controller → Internet
Log all denied traffic
```

For a simplified lab without a separate SCADA server, temporarily allow:

```text
HMI → Controller TCP 502
```

Then remove that rule and introduce the SCADA server as an intermediary.

This demonstrates how architecture changes the firewall policy.

---

# 50. Lab Validation Tests

## Test 1: Same-VLAN communication

From one SCADA-zone host:

```bash
ping 10.30.0.20
```

Expected:

```text
Success
```

Reason:

```text
Both devices are in VLAN 30 and subnet 10.30.0.0/24.
```

## Test 2: Cross-VLAN routing

From the HMI:

```bash
ping 10.30.10.10
```

Expected:

```text
Denied initially
```

Reason:

```text
Default-deny firewall policy.
```

## Test 3: Allow an approved protocol

Create a firewall rule allowing:

```text
10.30.0.20 → 10.30.10.10 TCP 502
```

Test:

```bash
nc -vz 10.30.10.10 502
```

Expected:

```text
Connection succeeds from the SCADA server.
```

## Test 4: Confirm direct HMI denial

From `10.30.0.10`:

```bash
nc -vz 10.30.10.10 502
```

Expected:

```text
Denied
```

## Test 5: Verify engineering access

From `10.30.20.10`:

```bash
nc -vz 10.30.10.10 22
```

Expected:

```text
Allowed only if the maintenance rule is enabled.
```

## Test 6: Check firewall logs

Verify that denied sessions include:

* Source IP.
* Destination IP.
* Source zone.
* Destination zone.
* Protocol.
* Port.
* Action.
* Timestamp.
* Firewall rule.
* Session result.

---

# 51. Packet Capture Exercises

Use Wireshark or tcpdump to observe the traffic.

## Capture ARP

```bash
sudo tcpdump -ni eth0 arp
```

Observe:

```text
Who has 10.30.0.1?
Tell 10.30.0.10.
```

## Capture ICMP

```bash
sudo tcpdump -ni eth0 icmp
```

## Capture Modbus TCP

```bash
sudo tcpdump -ni eth0 tcp port 502
```

## Capture VLAN tags on a trunk

```bash
sudo tcpdump -eni eth0 vlan
```

A trunk capture may show:

```text
vlan 30
vlan 31
vlan 32
```

An access-port capture normally will not show VLAN tags to the endpoint.

---

# 52. Expected Learning Outcomes

After completing the chapter and lab, the learner should be able to explain:

* What a VLAN is.
* Why VLANs operate at Layer 2.
* What an IP subnet is.
* Why VLANs and subnets are normally mapped one-to-one.
* What an access port is.
* What a trunk port is.
* What an 802.1Q tag is.
* What a broadcast domain is.
* How ARP works inside a VLAN.
* Why routing is required between VLANs.
* What a default gateway does.
* Why an OT firewall should enforce inter-zone communication.
* Why a flat OT network is dangerous.
* Why engineering workstations require special protection.
* Why protection relays should be isolated.
* Why business IT should not directly access controllers.
* How an Industrial DMZ breaks direct trust.
* How to trace a packet from source application to destination application.
* How to validate an OT segmentation design in a lab.

---

# 53. Review Questions

1. What is the difference between a VLAN and an IP subnet?
2. At which OSI layer does a VLAN primarily operate?
3. At which OSI layer does routing occur?
4. Why does a device use ARP?
5. What is a broadcast domain?
6. What is the difference between an access port and a trunk port?
7. Why does a trunk use an 802.1Q tag?
8. Why should one VLAN normally map to one subnet?
9. What happens when a device has the wrong subnet mask?
10. Why does traffic between two VLANs need a gateway?
11. Why should the gateway be a firewall in an OT design?
12. Why might direct HMI-to-controller communication be denied?
13. Why are engineering workstations more sensitive than operator HMIs?
14. Why should protection relays be separated from SCADA servers?
15. What is the purpose of the Industrial DMZ?
16. Why should business IT not connect directly to controllers?
17. Why should unused switch ports be disabled?
18. Why should trunks allow only required VLANs?
19. Why is a default-deny firewall policy preferred?
20. Why may some field devices intentionally have no default gateway?

---

# 54. Practical Exercises

## Exercise 1: Create the VLAN table

Create the following VLANs:

```text
VLAN 10  BUSINESS-IT
VLAN 20  OT-IDMZ
VLAN 30  OT-SCADA
VLAN 31  OT-CONTROL
VLAN 32  OT-ENGINEERING
VLAN 40  OT-PROTECTION
VLAN 50  OT-TELEMETRY
VLAN 999 PARKING
```

## Exercise 2: Assign switch ports

Assign:

```text
Port 1  → VLAN 30
Port 2  → VLAN 31
Port 3  → VLAN 32
Port 23 → Trunk
Port 24 → Trunk
```

## Exercise 3: Configure addressing

Configure:

```text
HMI:         10.30.0.10/24
Controller:  10.30.10.10/24
Engineering: 10.30.20.10/24
```

## Exercise 4: Configure gateways

Configure:

```text
10.30.0.1
10.30.10.1
10.30.20.1
```

## Exercise 5: Test default deny

Verify that no cross-VLAN communication succeeds before rules are added.

## Exercise 6: Add a single approved rule

Allow:

```text
10.30.0.20 → 10.30.10.10 TCP 502
```

Verify that other sources remain blocked.

## Exercise 7: Capture the traffic

Capture:

* ARP.
* ICMP.
* TCP handshake.
* VLAN tags.
* Firewall deny logs.

## Exercise 8: Misconfigure the subnet mask

Set:

```text
10.30.0.10/16
```

Observe how the host treats `10.30.10.10`.

Restore:

```text
10.30.0.10/24
```

Document the difference.

## Exercise 9: Misconfigure the access VLAN

Place the controller port in VLAN 30 while leaving its IP as:

```text
10.30.10.10/24
```

Observe the failure.

Restore the port to VLAN 31.

## Exercise 10: Write a communication matrix

Document every approved flow using:

```text
Source
Destination
Protocol
Port
Direction
Purpose
Owner
Approval
Logging
Expiration
```

---

# 55. Repository Integration Proposal

Suggested repository path:

```text
docs/
└── ot-security/
    └── network-segmentation/
        ├── README.md
        ├── 01-vlan-fundamentals.md
        ├── 02-subnets-and-routing.md
        ├── 03-ot-firewall-policy.md
        ├── 04-hydroelectric-reference-architecture.md
        ├── 05-lab-guide.md
        └── assets/
            ├── diagrams/
            ├── packet-captures/
            └── configs/
```

This document can initially be stored as:

```text
docs/ot-security/network-segmentation/01-vlan-fundamentals.md
```

Future chapters should separate the material into smaller modules.

---

# 56. Suggested Future Chapters

```text
02 — IPv4 subnetting for OT engineers
03 — ARP, MAC tables, and Ethernet forwarding
04 — Access ports, trunks, and 802.1Q
05 — Inter-VLAN routing
06 — OT firewall zones and policies
07 — Industrial DMZ architecture
08 — SCADA, HMI, historian, and controller flows
09 — Engineering workstation security
10 — Substation and IEC 61850 segmentation
11 — Remote RTU and telemetry architecture
12 — Redundancy and high availability
13 — Passive OT monitoring
14 — Asset inventory and network diagrams
15 — Communication matrices
16 — OT incident-response containment
17 — GNS3 hydroelectric OT lab
18 — FortiGate or pfSense implementation
19 — Packet analysis with Wireshark
20 — Capstone hydroelectric plant architecture
```

---

# 57. Definition of Done

This chapter is complete when:

* The VLAN and subnet distinctions are clear.
* The corrected IP mapping is used consistently.
* Every security zone has a defined purpose.
* Access and trunk ports are explained.
* The default gateway is explained.
* A packet journey is documented.
* A firewall communication matrix is included.
* Common design mistakes are included.
* A lab topology is included.
* Validation tests are included.
* Review questions are included.
* Practical exercises are included.
* The document passes Markdown linting.
* Diagrams render correctly.
* Commands are placed in fenced code blocks.
* No vendor-specific command is presented as universally valid.
* Future chapters are linked from the main OT security index.

---

# 58. Key Takeaway

The central lesson is:

```text
A VLAN creates a Layer-2 boundary.
A subnet creates a Layer-3 boundary.
A gateway routes between subnets.
A firewall controls which routed communication is allowed.
A security zone combines these mechanisms with operational policy.
```

For the hydroelectric plant:

```text
Business IT
    ≠
Industrial DMZ
    ≠
SCADA and HMI
    ≠
Controllers
    ≠
Engineering workstations
    ≠
Protection relays
    ≠
Remote RTUs
```

The purpose of segmentation is not merely to organize IP addresses.

The purpose is to ensure that the compromise or failure of one system does not automatically provide access to every other critical system in the plant.

