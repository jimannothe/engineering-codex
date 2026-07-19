# Networking

## Purpose

Understand how services communicate and fail.

## Skills

- SSH
- ports
- HTTP basics
- service troubleshooting

## Projects

- reliability-lab
- home-lab

## Backlog

- [x] document SSH workflow
- [x] document port checking
- [x] document network diagnostics

## Reference

### SSH Workflow

Use SSH when you need remote shell access to a trusted system.

Basic workflow:

1. Confirm the host is reachable.
2. Confirm the SSH service is running on the target.
3. Connect with the right username and host.
4. Verify keys, prompts, and permissions.
5. Exit cleanly when done.

Common command:

```bash
ssh user@host
```

Useful checks:

```bash
ping host
ssh -v user@host
```

Interpretation:

- a timeout often means the host is down, blocked, or unreachable
- connection refused usually means SSH is not listening on that port
- authentication failure usually means the username, key, or password is wrong
- host key warnings should be treated carefully and verified before proceeding

### Port Checking

Use port checking to confirm whether a service is listening and whether a network path allows the traffic.

Useful commands:

```bash
nc -vz host 22
nc -vz host 80
```

Other checks:

```bash
ss -tuln
sudo lsof -i -P -n
```

Interpretation:

- open means the service accepted the connection
- connection refused means the target host rejected the connection because nothing is listening
- timeout usually means filtering, routing, or host availability problems
- a listening socket on the host proves the service is up locally, not that remote access is allowed

### Network Diagnostics

Use diagnostics to decide where the failure lives before changing anything.

Basic order:

1. Check power, link, and interface state.
2. Check IP address, subnet mask, and gateway.
3. Check DNS resolution if names are involved.
4. Check port reachability.
5. Check packet behavior with capture or logs.

Helpful commands:

```bash
ip addr
ip route
ping host
traceroute host
arp -a
nslookup host
```

What to look for:

- link problems point to cable, port, or hardware issues
- address problems point to IP or subnet mismatch
- name problems point to DNS
- port problems point to service or firewall issues
- repeated retransmissions or missing replies point to packet loss, filtering, or a dead endpoint

Rule of thumb:

- start with the simplest layer that can explain the failure
- verify before guessing
- change one thing at a time
- record the result so the next diagnostic step is obvious

## Done Criteria

This epic is useful when I can diagnose basic network issues without guessing.
