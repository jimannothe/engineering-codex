# OT Network Segmentation Fundamentals for a Hydroelectric Power Plant

This chapter explains OT segmentation from first principles using a simplified hydroelectric plant architecture.

The goal is to understand:

1. What a VLAN is.
2. How VLANs relate to Ethernet switching.
3. How VLANs relate to IP subnets.
4. What access ports and trunk ports are.
5. Why devices in different VLANs require routing.
6. Why OT environments use firewalls between security zones.
7. How packet flow works between an HMI, SCADA server, controller, relay, and remote RTU.
8. Why segmentation reduces operational and cybersecurity risk.
9. How to translate a logical design into switch, firewall, and addressing configuration.
10. How to build a small lab that demonstrates the concepts.

This is a teaching model. A real hydroelectric facility would also need redundancy, vendor-specific protocols, protection-system separation, physical design, failover testing, and site-specific risk analysis.

## 1. Reference Architecture

Use this simplified layout throughout the chapter:

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
SCADA/HMI           Engineering
    |
    v
Controller Network
    |
    +--------------------+
    |                    |
    v                    v
Protection Network   Remote Telemetry
```

The main rule:

```text
Business IT must not communicate directly with controllers,
protection relays, or remote field devices.
```

## 2. Corrected IP Mapping

The cleaner mapping is:

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

This mapping keeps each device in the subnet that matches its actual function.

## 3. Why Segmentation Exists

A flat network creates unnecessary trust.

Without segmentation, a hydroelectric plant may have:

```text
One switch
One subnet
One broadcast domain
Many unrelated device types
```

That creates problems:

- A compromised engineering workstation can directly reach controllers.
- A vendor laptop can directly reach relays.
- Malware can move laterally without crossing a firewall.
- Broadcast traffic reaches unrelated devices.
- Security policy becomes vague or unenforceable.
- A single misconfiguration can affect the whole plant network.

Segmentation separates devices by function and risk.

## 4. What Is a VLAN?

VLAN means `Virtual Local Area Network`.

A VLAN divides one physical switching fabric into multiple logical Layer-2 networks.

Think of one managed switch as several virtual switches:

```text
VLAN 10  Business IT
VLAN 20  Industrial DMZ
VLAN 30  SCADA and HMI
VLAN 31  Controllers
VLAN 32  Engineering
VLAN 40  Protection relays
VLAN 50  Remote telemetry
```

A device in VLAN 30 does not directly share Layer-2 broadcast space with a device in VLAN 31.

## 5. VLANs and the OSI Model

VLANs are primarily a Layer-2 concept.

```text
Layer 7   Application      Modbus TCP, OPC UA, HTTPS, DNP3
Layer 6   Presentation     Encoding, encryption, serialization
Layer 5   Session          Session management
Layer 4   Transport        TCP and UDP
Layer 3   Network          IP addressing and routing
Layer 2   Data Link        Ethernet, MAC addresses, VLANs
Layer 1   Physical         Copper, fiber, radio, connectors
```

Summary:

- VLANs are Layer-2 separation.
- Subnets are Layer-3 separation.
- Firewalls enforce policy between zones.

## 6. VLAN Versus IP Subnet

A VLAN is a broadcast domain.

An IP subnet is an addressing boundary.

In a good design, one VLAN usually maps to one subnet:

| VLAN | Name           | Subnet         |
| ---: | -------------- | -------------- |
| 10   | BUSINESS-IT    | `10.10.0.0/24` |
| 20   | OT-IDMZ        | `10.20.0.0/24` |
| 30   | OT-SCADA       | `10.30.0.0/24` |
| 31   | OT-CONTROL     | `10.30.10.0/24` |
| 32   | OT-ENGINEERING | `10.30.20.0/24` |
| 40   | OT-PROTECTION  | `10.40.0.0/24` |
| 50   | OT-TELEMETRY   | `10.50.0.0/24` |

The VLAN number does not have to match the subnet, but consistency helps operations and troubleshooting.

## 7. Access Ports

An access port carries traffic for one VLAN.

Example:

```text
Switch port:       Ethernet1/5
Connected device:  Operator HMI
Port mode:         Access
Assigned VLAN:     VLAN 30
```

Conceptual configuration:

```text
interface Ethernet1/5
 description Operator-HMI-01
 switchport mode access
 switchport access vlan 30
```

The endpoint typically sends untagged frames.

## 8. Trunk Ports

A trunk port carries traffic for multiple VLANs.

Common trunk links:

- switch to switch
- switch to firewall
- switch to router
- switch to virtualization host

Example:

```text
Core switch
    |
    | Trunk carrying VLANs 20, 30, 31, 32, 40, and 50
    |
Industrial firewall
```

Trunks use IEEE 802.1Q tags to identify the VLAN associated with each frame.

## 9. Tagged and Untagged Traffic

- Access ports are normally untagged at the endpoint.
- Trunk ports normally carry tagged frames.

| Port type | VLANs carried | Frame behavior |
| --- | ---: | --- |
| Access | One | Usually untagged |
| Trunk | Multiple | Usually tagged |
| Routed port | None at Layer 2 | Uses Layer-3 addressing |

## 10. VLANs Do Not Route Traffic

VLANs separate Layer-2 traffic. They do not automatically enable communication between VLANs.

Example:

```text
Operator HMI:       10.30.0.10/24
Turbine controller: 10.30.10.10/24
```

These devices are in different subnets, so traffic must go through a default gateway and usually a firewall.

That is `inter-VLAN routing`.

## 11. The Default Gateway

A host uses its subnet mask to determine whether a destination is local or remote.

Example:

```text
IP address:       10.30.0.10
Subnet mask:      255.255.255.0
Default gateway:  10.30.0.1
```

If the destination is outside `10.30.0.0/24`, the host sends the packet to the gateway.

The gateway then checks:

1. Whether a route exists.
2. Whether the source is allowed.
3. Whether the destination is allowed.
4. Whether the protocol and port are allowed.
5. Whether the packet should be logged.

## 12. Why OT Networks Use Firewalls Between VLANs

A Layer-3 switch can route between VLANs, but unrestricted routing is usually too permissive for OT.

Example firewall rule:

```text
Source:       Primary SCADA server
Source IP:    10.30.0.20
Destination:  Turbine controller
Destination IP: 10.30.10.10
Protocol:     Modbus TCP
Port:         TCP 502
Action:       Allow
Logging:      Enabled
```

Example deny rule:

```text
Source:       Operator HMI
Source IP:    10.30.0.10
Destination:  Controller network
Protocol:     Any
Action:       Deny
Logging:      Enabled
```

The intended path is HMI to SCADA server, then SCADA server to controller.

## 13. VLAN Versus Security Zone

A VLAN is a technical Layer-2 mechanism.

A security zone is an architectural concept that groups systems by function, trust, and risk.

A zone may include:

- one or more VLANs
- one or more subnets
- firewall rules
- physical access restrictions
- user access controls
- logging
- patch procedures
- backup requirements

A VLAN alone is not a complete security control.

## 14. Hydroelectric Zones

### Business IT

```text
Subnet: 10.10.0.0/24
VLAN: 10
```

Business IT should not directly access PLCs, controllers, relays, RTUs, or engineering workstations.

### Industrial DMZ

```text
Subnet: 10.20.0.0/24
VLAN: 20
```

The Industrial DMZ hosts jump access, staging, transfer, replication, and monitoring services.

### SCADA and HMI

```text
Subnet: 10.30.0.0/24
VLAN: 30
```

This zone supervises the process and provides operator visibility.

### Controller Network

```text
Subnet: 10.30.10.0/24
VLAN: 31
```

This network performs direct process control.

### Engineering Workstations

```text
Subnet: 10.30.20.0/24
VLAN: 32
```

Engineering workstations are privileged and should be tightly controlled.

### Protection and Relay Network

```text
Subnet: 10.40.0.0/24
VLAN: 40
```

Protection relays have stricter latency, availability, and safety requirements.

### Remote Telemetry and RTUs

```text
Subnet: 10.50.0.0/24
VLAN: 50
```

Remote telemetry often traverses less trusted infrastructure and should be treated accordingly.

## 15. Packet Journey: HMI to Turbine Controller

Example:

```text
Operator HMI:       10.30.0.10/24
SCADA gateway:      10.30.0.1
Turbine controller: 10.30.10.10/24
Controller gateway: 10.30.10.1
```

Step 1:
- The HMI sees that `10.30.10.10` is outside its local subnet.
- It sends the packet to its default gateway.

Step 2:
- The HMI resolves the gateway MAC address with ARP.

Step 3:
- The HMI builds an Ethernet frame with the gateway as the Layer-2 destination and the controller as the Layer-3 destination.

Step 4:
- The firewall checks policy.
- If direct HMI-to-controller access is denied, the session is dropped and logged.

Step 5:
- The approved path is HMI to SCADA server, then SCADA server to controller.

## 16. Why Application Communication Should Be Centralized

If every HMI talks directly to every controller, the number of communication paths grows quickly.

Centralizing through SCADA reduces:

- complexity
- documentation burden
- troubleshooting scope
- firewall rule count
- accidental exposure

## 17. Example Firewall Communication Matrix

| ID | Source | Destination | Protocol/Port | Direction | Purpose | Action |
| -: | --- | --- | --- | --- | --- | --- |
| 1 | Business IT | IDMZ jump host | HTTPS or remote desktop | IT → IDMZ | Approved administrative access | Allow |
| 2 | Business IT | OT controllers | Any | IT → OT | Direct access not permitted | Deny |
| 3 | IDMZ jump host | Engineering workstation | Approved remote access | IDMZ → Engineering | Controlled OT administration | Allow |
| 4 | OT historian | IDMZ historian replica | Historian replication | OT → IDMZ | Business reporting | Allow |
| 5 | Operator HMI | SCADA server | Vendor application protocol | SCADA → SCADA | Operator visualization | Allow |
| 6 | Operator HMI | Controller network | Any | SCADA → Control | Direct access prohibited | Deny |
| 7 | SCADA server | Turbine controller | Required industrial protocol | SCADA → Control | Process monitoring and command | Allow |
| 8 | Engineering workstation | Turbine controller | Engineering protocol | Engineering → Control | Approved configuration changes | Conditional allow |
| 9 | Controller network | Internet | Any | Control → Internet | Not required | Deny |
| 10 | SCADA server | Telemetry gateway | DNP3 or approved protocol | SCADA → Telemetry | RTU polling | Allow |

The exact ports and protocols must be verified for each vendor system.

## 18. Default-Deny Policy

A secure OT firewall policy starts with:

```text
Deny all traffic
```

Then required traffic is added explicitly.

## 19. Example Switch Port Plan

| Port | Connected Device | Mode | VLAN | Description |
| ---: | --- | --- | ---: | --- |
| 1 | Operator HMI 1 | Access | 30 | Main control-room HMI |
| 2 | Operator HMI 2 | Access | 30 | Backup HMI |
| 3 | Primary SCADA server | Access | 30 | Main SCADA server |
| 6 | Turbine controller | Access | 31 | Primary turbine controller |
| 7 | Backup turbine controller | Access | 31 | Redundant turbine controller |
| 11 | SCADA engineering station | Access | 32 | SCADA configuration |
| 13 | Generator relay | Access | 40 | Generator protection |
| 16 | Telemetry gateway | Access | 50 | Remote RTU aggregation |
| 23 | Firewall uplink | Trunk | Multiple | Allowed VLANs only |
| 24 | Upstream switch | Trunk | Multiple | Redundant or distribution uplink |

## 20. Example Access-Port Configuration

```text
interface Ethernet1/6
 description TURBINE-CONTROLLER-PRIMARY
 switchport mode access
 switchport access vlan 31
 spanning-tree edge
 no shutdown
```

## 21. Example Trunk Configuration

```text
interface Ethernet1/23
 description OT-FIREWALL-UPLINK
 switchport mode trunk
 switchport trunk allowed vlan 30,31,32,40,50
 no shutdown
```

## 22. Firewall Subinterfaces and Gateways

```text
ethernet1.30  -> 10.30.0.1/24    OT-SCADA
ethernet1.31  -> 10.30.10.1/24   OT-CONTROL
ethernet1.32  -> 10.30.20.1/24   OT-ENGINEERING
ethernet1.40  -> 10.40.0.1/24    OT-PROTECTION
ethernet1.50  -> 10.50.0.1/24    OT-TELEMETRY
```

The firewall becomes the default gateway for each OT subnet.

## 23. Common Mistakes

- Wrong VLAN and subnet pairing.
- Wrong subnet mask.
- Flat Layer-2 design.
- VLANs without firewall rules.
- Using engineering workstations as general-purpose PCs.
- Direct vendor access into the control network.
- Treating relays like ordinary servers.

## 24. Lab Objective

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
12. Logging.

Possible lab platforms:

- GNS3
- EVE-NG
- Cisco Packet Tracer for basic VLAN concepts
- Linux network namespaces
- VirtualBox or VMware
- pfSense or OPNsense

## 25. Minimal Lab Topology

```text
                 +----------------------+
                 | Firewall or Router   |
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
                 +-------+ +------------+
```

## 26. Suggested Lab IPs

- HMI: `10.30.0.10/24`
- Controller: `10.30.10.10/24`
- Engineering workstation: `10.30.20.10/24`
- Gateways: `10.30.0.1`, `10.30.10.1`, `10.30.20.1`

## 27. Initial Lab Firewall Policy

Start with:

```text
Deny all inter-VLAN traffic
```

Then add only the required rules.

## 28. Packet Capture Exercises

Use Wireshark or tcpdump to observe:

- ARP
- ICMP
- TCP handshakes
- VLAN tags
- Firewall deny logs

## 29. Expected Learning Outcomes

After this chapter, the learner should be able to explain:

- what a VLAN is
- why VLANs operate at Layer 2
- what an IP subnet is
- why VLANs and subnets are usually mapped one-to-one
- what access and trunk ports are
- what an 802.1Q tag is
- what a broadcast domain is
- how ARP works inside a VLAN
- why routing is required between VLANs
- what a default gateway does
- why an OT firewall should enforce inter-zone communication
- why a flat OT network is dangerous
- why engineering workstations require special protection
- why protection relays should be isolated
- why business IT should not directly access controllers
- how to trace a packet from source application to destination application
- how to validate an OT segmentation design in a lab

## 30. Key Takeaway

The central lesson is:

```text
A VLAN creates a Layer-2 boundary.
A subnet creates a Layer-3 boundary.
A gateway routes between subnets.
A firewall controls which routed communication is allowed.
A security zone combines these mechanisms with operational policy.
```

## 31. Repository Integration

This chapter can live at:

```text
docs/ot-security/network-segmentation/01-vlan-fundamentals.md
```

Future chapters should split the material into smaller modules.

