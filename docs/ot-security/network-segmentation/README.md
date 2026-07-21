# OT Network Segmentation

This folder is the canonical home for the OT network segmentation series.

The goal is to move from first principles to a buildable lab without mixing unrelated material into the core path.

## Reading Order

1. [00 - Hydroelectric Lab Proposal](00-hydroelectric-lab-proposal.md)
2. [01 - VLAN Fundamentals](01-vlan-fundamentals.md)

## What This Series Covers

- VLANs and switching
- IPv4 subnets and routing
- OT firewall policy
- industrial DMZ design
- SCADA, HMI, historian, and controller flows
- engineering workstation security
- passive monitoring
- incident containment
- lab validation

## Structure

Keep the chapters small and focused.

Use one file per concept, and move implementation evidence into `assets/` instead of embedding everything in prose.

## Chapter Roadmap

### Foundations

- `00-hydroelectric-lab-proposal.md`
- `01-vlan-fundamentals.md`
- `02-subnets-and-routing.md`
- `03-arp-mac-and-ethernet-forwarding.md`
- `04-access-trunks-and-8021q.md`
- `05-inter-vlan-routing.md`

### Policy And Architecture

- `06-ot-firewall-policy.md`
- `07-industrial-dmz-architecture.md`
- `08-scada-hmi-historian-controller-flows.md`
- `09-engineering-workstation-security.md`
- `10-substation-and-iec-61850-segmentation.md`
- `11-remote-rtu-and-telemetry-architecture.md`
- `12-redundancy-and-high-availability.md`

### Operations And Validation

- `13-passive-ot-monitoring.md`
- `14-asset-inventory-and-network-diagrams.md`
- `15-communication-matrices.md`
- `16-ot-incident-response-containment.md`

### Lab And Implementation

- `17-gns3-hydroelectric-ot-lab.md`
- `18-fortigate-or-pfsense-implementation.md`
- `19-packet-analysis-with-wireshark.md`
- `20-capstone-hydroelectric-plant-architecture.md`

## Assets

- `assets/diagrams/`
- `assets/packet-captures/`
- `assets/configs/`

## Notes

- The hydroelectric example is a teaching model, not a full production design.
- If a chapter starts to get too large, split it into smaller files instead of adding more sections to the same page.
- Keep the lab artifacts aligned with the chapter numbering so the series stays easy to navigate.
