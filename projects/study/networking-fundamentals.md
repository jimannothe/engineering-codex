# Networking Fundamentals Study Log

## Purpose

Build a practical networking mental model for OT communication, troubleshooting, segmentation, and interview discussion.

## Current Status

- Session: 3
- Focus: PLC-to-HMI communication on the same subnet
- Current depth: Layer 1 through Layer 4 troubleshooting
- Next action: diagnose repeated ARP requests with no reply

## Core Mental Model

```text
Device A --> Switch --> Firewall/Router --> Switch --> Device B
                |                           |
               VLAN 10                     VLAN 20
```

Example OT flow:

- an HMI requests data from a PLC
- the PLC responds on the control network
- a historian records selected process values
- a firewall restricts business-network access to approved paths

## Concepts Covered

- IP address and subnet
- switch and router
- VLAN and firewall
- DNS and DHCP
- ARP
- ports
- TCP and UDP
- NAT and VPN
- packet capture

## Best Recall Responses

- **Switch vs. router:** A switch forwards frames within a LAN using MAC addresses, while a router moves traffic between different networks using IP addresses.
- **DNS:** DNS translates names into IP addresses, which matters in OT because HMIs, historians, and engineering stations often rely on hostnames.
- **ARP:** ARP maps an IP address to a MAC address on the local network.
- **TCP vs. UDP:** TCP is reliable and connection-oriented; UDP is connectionless and lighter-weight.
- **VLAN:** A VLAN is a logical network segment on shared switching infrastructure, useful for separating OT zones or groups of devices.
- **Firewall:** A firewall enforces allowed traffic between networks or zones; it is not a replacement for segmentation.
- **Packet capture:** Packet capture records actual network traffic so troubleshooting can use evidence instead of guesses.

## Corrections From Quiz Feedback

- a switch is Layer 2, not Layer 22
- a router connects networks; it does not generally handle connection requests
- DNS maps names to IP addresses, not IP addresses to URLs
- TCP is reliable and connection-oriented, but it is not secure by default
- VLANs create logical segmentation, while firewalls enforce traffic policy
- packet capture is the debugging method; Packet Tracer is a simulation tool

## Troubleshooting Exercise

Scenario:

> A PLC and HMI are on the same subnet but cannot communicate.

Initial troubleshooting response:

1. Confirm that the PLC is powered, working, and physically connected.
2. Ping the devices and review their IP addresses and subnet masks.
3. Check the switch ports, VLAN assignments, and Ethernet cables.
4. Check firewall rules.

Assessment:

- the troubleshooting order is sound: start with physical state and configuration, then move upward through the network layers
- a link light proves an electrical link, not complete communication
- failed ping does not always prove that a device is unreachable because ICMP may be filtered or unsupported
- a same-subnet flow normally does not traverse a router or perimeter firewall
- successful ping proves limited IP reachability, not application or industrial-protocol health

## Detailed Troubleshooting Model

### 1. Device and Physical Layer

Confirm:

- PLC and HMI power and operating state
- link lights at both endpoints and the switch
- secure cable connections
- known-good Ethernet cables
- enabled switch ports
- negotiated speed and duplex
- interface error counters, especially CRC and input errors

A useful isolation test is to substitute a known-good cable or approved switch port while following site change-control procedures.

### 2. IP Addressing and Subnet

Example valid same-subnet configuration:

```text
PLC:  192.168.10.20/24
HMI:  192.168.10.30/24
Mask: 255.255.255.0
```

With this configuration, the HMI should recognize the PLC address as local, use ARP to learn its MAC address, and send an Ethernet frame through the switch without using the default gateway.

Check for:

- incorrect IP address
- incorrect or mismatched subnet mask
- duplicate IP address
- stale or incorrect ARP entry
- incorrect gateway when communication crosses subnets

Useful endpoint checks:

```bash
ping 192.168.10.20
arp -a
```

Interpretation:

- no ARP entry suggests a Layer 2, VLAN, cabling, port, or offline-device problem
- an ARP entry with no ping response may mean ICMP is filtered or unsupported
- a MAC address that changes unexpectedly may indicate a duplicate IP address

### 3. Switch Port and VLAN

Check whether each port is enabled, assigned to the expected VLAN, configured correctly as an access or trunk port, free of port-security violations, and learning the expected endpoint MAC address.

Representative managed-switch checks:

```text
show interfaces status
show interfaces counters errors
show vlan brief
show mac address-table
```

Exact commands depend on the switch vendor. If the switch learns the PLC MAC address on the expected port and VLAN, the PLC has transmitted frames into that switch.

Devices can use addresses from the same IP subnet and still fail to communicate when their ports are in different VLANs:

```text
PLC port --> VLAN 10
HMI port --> VLAN 20
```

The HMI ARP broadcast stays inside VLAN 20, so the PLC in VLAN 10 never receives it.

Interview-ready point:

> Same-subnet IP configuration does not guarantee Layer 2 connectivity. Both endpoints must also share the intended VLAN or have an intentionally routed path between their networks.

### 4. Firewall, Access Control, and Application

If the PLC and HMI are truly in the same VLAN and IP subnet, their traffic normally stays on the switch. A perimeter firewall is therefore not the first suspect.

Traffic may still be blocked by:

- an HMI host firewall
- PLC access controls
- a switch ACL
- private-VLAN or port-isolation settings
- an inline industrial firewall or transparent security appliance
- application security settings
- an incorrect protocol or port

Successful ping proves limited IP reachability, not application health. If ping succeeds but the application fails, verify that the PLC service is listening, the HMI uses the correct protocol and port, and the PLC permits that client.

From an authorized engineering workstation, a TCP service can be tested with:

```bash
nc -vz 192.168.10.20 <port>
```

In Wireshark, look for:

- ARP requests with no replies
- TCP SYN packets with no response
- TCP resets
- repeated retransmissions
- a successful TCP handshake followed by application errors

## Interview-Ready Troubleshooting Response

> First, I would verify power, physical links, IP addresses, subnet masks, and duplicate addresses. Then I would check whether ARP resolves and whether the switch learns both MAC addresses on the expected ports and VLAN. If Layer 2 and Layer 3 connectivity work, I would test the required industrial protocol and port, then examine device access controls, host firewalls, switch ACLs, and packet captures. I would avoid assuming that successful ping proves the application works.

## Open Questions

1. The HMI repeatedly sends ARP requests for the PLC but receives no ARP reply. What does that indicate, and which three things should be inspected next?
2. Why is segmentation especially important between business IT and control networks?
3. How would Wireshark help debug a communication issue without guessing?

## Answers

1. Repeated ARP requests with no reply usually mean the HMI can reach the local network but cannot discover the PLC's MAC address. The next things to inspect are the PLC power/state, the switch port and VLAN path, and the cabling or duplicate-IP situation.
2. Segmentation matters because business IT and control networks have different risk levels and uptime needs. Separating them limits blast radius, reduces accidental or malicious access, and helps keep control traffic predictable and safe.
3. Wireshark shows actual packets instead of assumptions. It can confirm whether ARP replies exist, whether TCP handshakes complete, whether retransmissions or resets occur, and whether the issue is Layer 2, Layer 3, or application-level.
