# Hydroelectric OT Network Segmentation Lab Proposal

## Purpose

This proposal turns the hydroelectric segmentation chapter into a buildable lab plan.

The lab will demonstrate how VLANs, IP subnets, routing, and firewalls work together in an OT environment and why the design matters for safety, reliability, and control.

## Proposal Summary

Build a small hydroelectric OT segmentation lab that models:

- business IT
- industrial DMZ
- SCADA/HMI zone
- controller zone
- engineering zone
- protection relay zone
- remote telemetry zone

The lab should prove these ideas:

1. VLANs are Layer-2 broadcast boundaries.
2. Subnets are Layer-3 addressing boundaries.
3. Access ports carry one VLAN.
4. Trunk ports carry multiple VLANs.
5. Inter-VLAN traffic must be routed.
6. OT firewalls should enforce default-deny policy between security zones.
7. SCADA, controllers, relays, and RTUs should not all trust each other equally.
8. Security policy must be tested, not assumed.

## Reference Architecture

Use the hydroelectric network model from the chapter:

```text
10.10.0.0/24      Business IT
10.20.0.0/24      Industrial DMZ
10.30.0.0/24      Plant SCADA and HMI
10.30.10.0/24     Controller network
10.30.20.0/24     Engineering workstations
10.40.0.0/24      Substation protection and relay network
10.50.0.0/24      Remote telemetry and RTUs
```

Recommended logical zones:

- VLAN 10: BUSINESS-IT
- VLAN 20: OT-IDMZ
- VLAN 30: OT-SCADA
- VLAN 31: OT-CONTROL
- VLAN 32: OT-ENGINEERING
- VLAN 40: OT-PROTECTION
- VLAN 50: OT-TELEMETRY

## Lab Objectives

The lab should let a learner:

- assign a switch port to a VLAN
- configure a trunk between switch and firewall
- assign IP addresses that match each VLAN
- route between VLANs through a firewall
- deny direct HMI-to-controller access
- allow only approved SCADA-to-controller traffic
- observe ARP, ICMP, and TCP behavior
- capture packets on access and trunk ports
- validate firewall logs
- identify mistakes caused by bad VLAN or subnet assignments

## Proposed Lab Topology

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

                       VLAN 32
                          |
                    +-----v------+
                    | Engineering|
                    +------------+
```

## Proposed Lab Stack

Choose one of these:

- GNS3
- EVE-NG
- Cisco Packet Tracer for baseline VLAN learning
- Linux network namespaces
- VirtualBox or VMware
- pfSense or OPNsense

## Proposed Lab Deliverables

1. A VLAN table with names and purposes.
2. A switch-port plan.
3. A firewall communication matrix.
4. An IP addressing plan.
5. A packet-capture set showing expected ARP, ICMP, and TCP behavior.
6. A log set showing blocked and permitted traffic.
7. A short writeup that explains what worked, what failed, and why.

## Design Rules

- Use static addressing for all critical devices.
- Use one VLAN per security zone unless a design reason says otherwise.
- Keep the firewall as the default gateway for inter-zone traffic.
- Use default-deny policy and add only required rules.
- Do not allow direct business-to-control traffic.
- Do not let engineering workstations behave like ordinary office PCs.
- Treat protection relays as special-purpose systems, not general servers.
- Keep remote access in the Industrial DMZ and behind MFA where possible.
- Log all denied traffic.

## Suggested Device Roles

### SCADA Zone

- operator HMI
- primary SCADA server
- backup SCADA server
- historian
- alarm and event server

### Controller Zone

- turbine controller
- governor controller
- excitation controller
- auxiliary PLC

### Engineering Zone

- SCADA engineering workstation
- PLC engineering workstation
- protection engineering workstation
- configuration backup server

### Protection Zone

- generator protection relay
- transformer protection relay
- busbar protection relay
- transmission-line protection relay

### Telemetry Zone

- remote intake RTU
- reservoir-level RTU
- spillway RTU
- weather-station RTU

## Implementation Phases

### Phase 1: Foundation

- build the topology
- create the VLANs
- assign access ports
- configure the trunk
- assign static IPs

### Phase 2: Routing and Policy

- create firewall subinterfaces or routed interfaces
- set default gateways
- deny all inter-VLAN traffic
- add only approved flows

### Phase 3: Validation

- verify same-VLAN communication
- verify cross-VLAN denial
- verify approved SCADA-to-controller flow
- verify engineering access only where allowed
- verify logs and packet captures

### Phase 4: Failure Injection

- misconfigure subnet masks
- misplace a port in the wrong VLAN
- remove a firewall allow rule
- confirm the failure mode is understandable
- restore the correct configuration

## 55-Step Execution Checklist

1. Confirm the hydroelectric plant scenario.
2. Define the learning objectives.
3. Fix the subnet plan.
4. Assign zone names to each subnet.
5. Choose lab software or hardware.
6. Create the VLAN list.
7. Create the IP address plan.
8. Create the device naming convention.
9. Build the switch topology.
10. Assign access ports.
11. Assign trunk ports.
12. Configure the firewall or router.
13. Create routed interfaces for each VLAN.
14. Set the default gateway for each subnet.
15. Put the HMI in VLAN 30.
16. Put the SCADA server in VLAN 30.
17. Put the controller in VLAN 31.
18. Put the engineering workstation in VLAN 32.
19. Put the relay in VLAN 40.
20. Put the RTU in VLAN 50.
21. Verify same-VLAN host communication.
22. Verify ARP resolution inside a VLAN.
23. Verify the HMI can reach its gateway.
24. Verify the HMI cannot reach the controller directly.
25. Add an allow rule for approved SCADA traffic.
26. Verify the approved SCADA-to-controller flow.
27. Add an allow rule for engineering maintenance access.
28. Verify engineering access is limited and logged.
29. Verify business IT cannot reach OT directly.
30. Verify the Industrial DMZ acts as a boundary.
31. Capture a VLAN-tagged frame on a trunk.
32. Capture an untagged frame on an access port.
33. Capture a blocked cross-zone packet.
34. Capture an allowed packet.
35. Review firewall logs.
36. Review switch MAC-table behavior.
37. Review routing behavior.
38. Review subnet-mask behavior.
39. Misconfigure a subnet mask and observe the error.
40. Restore the correct subnet mask.
41. Misplace a device in the wrong VLAN.
42. Observe the resulting connectivity failure.
43. Restore the correct VLAN assignment.
44. Remove an allow rule and confirm the traffic is blocked.
45. Re-add the allow rule and confirm recovery.
46. Add a default-deny rule set.
47. Verify only explicit flows pass.
48. Test a remote RTU path.
49. Test a protection-relay path.
50. Test a historian or replica path.
51. Document each observed result.
52. Write the final communication matrix.
53. Write the final switch-port map.
54. Write the final firewall policy summary.
55. Publish the lab notes as a reusable deliverable.

## Success Criteria

The lab is successful when a learner can explain:

- what VLANs do
- what subnets do
- why routing is required
- why firewalls belong between OT zones
- how HMI, SCADA, controller, relay, and RTU traffic should flow
- how to recognize a bad VLAN or subnet configuration
- how to validate the design with packet captures and logs

## Relationship To The Chapter

The detailed chapter remains the teaching reference.

This proposal is the build plan that turns the chapter into a lab.

The canonical chapter remains:

- `01-vlan-fundamentals.md`

The canonical proposal is this file:

- `00-hydroelectric-lab-proposal.md`

