# Job Ingest Summary

## Source

- HTML file: `/home/jman/engineering-codex/projects/jobs/Senior Technical Support Engineer _ Cohesity _ LinkedIn.html`
- URL: Not provided

## Inferred Fields

- Company: Cohesity
- Role: Senior Technical Support Engineer
- Location: Technical Support Engineer (Hybrid, Costa Rica) (Empleo verificado)
- Employment: Remote
- Compensation: Unknown

## Fit Score

- Score: 69/100

## Extracted Skills

- Python
- Bash
- APIs
- Troubleshooting
- Documentation
- Linux
- Project management
- Security / auth

## Missing Skills

- APIs
- Linux
- Project management
- Security / auth

## Relevant Resume Bullets

- [Pertec - Service Desk Agent] Provided technical support for enterprise Windows environments.
- [Pertec - Service Desk Agent] Diagnosed and resolved operating system, Active Directory, hardware, software, and network connectivity issues.
- [UST - Validation Engineer II] Performed end-to-end system validation across hardware, firmware, operating systems, networking, and I/O interfaces.
- [UST - Validation Engineer II] Developed Python automation tools to streamline test execution, data collection, and engineering workflows.

## STAR Prompts

- Describe a customer incident you took ownership of, the diagnostic steps you followed, and how you restored service quickly.
- Describe a validation issue you isolated with logs or telemetry, how you automated part of the workflow, and how you helped validate the fix.

## Candidate New Terms

These are saved separately in a `.terms.json` sidecar for review.

- NVIDIA
- IBM
- HPE
- AWS
- TSE
- OR Sunday
- KVM
- LOVE TO TALK TO
- YOU IF YOU HAVE
- MANY OF THE FOLLOWING
- NFS
- SMB
- CIFS
- EMC
- EEOE
- Gen AI
- Our TSE
- Saturday OR Sunday
- Microsoft Hyper-V
- Linux KVM
- Google Cloud Platform. Write
- Cohesity Data Platform. Work
- CentOS Platform. WE
- D LOVE TO TALK
- TO YOU IF YOU
- HAVE MANY OF THE
- Powershell. Deep
- CentOS Linux Platform Architecture
- In-Office Expectations Cohesity
- CentOS Platform. Bachelor
- AI-powered
- vSphere
- CommVault
- NetApp
- LOVE
- TALK
- YOU
- HAVE
- MANY
- THE

## Relevant Experience

- Pertec - Service Desk Agent

## Notes

- This summary is rule-based and should be reviewed before filing.
- Add the job note to the appropriate `jobs/` location after confirming the extraction.

## AI Analysis Log

This section is for comparing the ingest script output with the follow-up human/AI pass.

1. Read the source HTML and the saved ingest summary side by side.
2. Identified the role as a senior support and platform-debugging position, not a general software role.
3. Pulled out the actual requirements from the HTML:
   - English and Spanish fluency
   - weekend/staggered coverage
   - Linux and CentOS debugging
   - storage, virtualization, and backup terminology
   - `bash`, `python`, `PowerShell`, and `RESTful APIs`
4. Separated signal from extraction noise in the candidate terms list.
5. Mapped the role to the strongest existing resume evidence:
   - service desk troubleshooting
   - validation and diagnostics
   - Python automation
6. Turned the role into two outputs:
   - gap-to-action checklist
   - tailored resume mapping

## Gap To Action

1. Linux and CentOS debugging
   - Action: review `strace`, `tcpdump`, `wireshark`, `gdb`, `crash`, and `systemtap` examples.
   - Outcome: be able to talk through a structured root-cause path on a Linux host.
2. Storage and backup domain vocabulary
   - Action: learn the support-level meaning of `NFS`, `SMB/CIFS`, `NetApp`, `CommVault`, `EMC`, and `Symantec`.
   - Outcome: be able to translate those terms into customer-impact language.
3. Virtualization and cluster support
   - Action: map `VMware vSphere`, `Hyper-V`, and `Linux KVM` to backup/restore and cluster failure scenarios.
   - Outcome: show you can debug across guest, hypervisor, and platform layers.
4. Scripting and APIs
   - Action: keep one or two examples ready for `bash`, `python`, `PowerShell`, and `RESTful APIs`.
   - Outcome: show automation support, not just manual troubleshooting.
5. Support cadence and communication
   - Action: prepare one STAR story for a customer incident, one for a noisy diagnosis, and one for cross-team escalation.
   - Outcome: prove you can work weekends, communicate clearly, and close the loop.

## Tailored Resume Map

Use these as the resume hooks for this posting.

- [Pertec - Service Desk Agent] Provided technical support for enterprise Windows environments.
  - Best for: customer support, troubleshooting, ticket ownership, and incident triage.
- [Pertec - Service Desk Agent] Diagnosed and resolved operating system, Active Directory, hardware, software, and network connectivity issues.
  - Best for: multi-layer debugging, systems thinking, and communication under pressure.
- [UST - Validation Engineer II] Performed end-to-end system validation across hardware, firmware, operating systems, networking, and I/O interfaces.
  - Best for: platform debugging, cross-layer analysis, and structured diagnostics.
- [UST - Validation Engineer II] Developed Python automation tools to streamline test execution, data collection, and engineering workflows.
  - Best for: `python`, automation, log handling, and repetitive-task reduction.

Virtualization-specific proof you can now use:

- Used `virt-manager` to create and manage virtual machines.
- Configured VM CPU topology and core counts for test scenarios.
- Attached or added virtual disks to guest VMs.
- Used virtualization-oriented kernel parameters, including `intel_iommu`, during validation work.
- Ran virtualized validation scenarios to study behavior under controlled platform conditions.

Possible virtualization phrasing for a resume or interview:

- Configured and validated virtual machines with `virt-manager`, including CPU allocation and storage attachment for test scenarios.
- Used virtualization-aware kernel parameters during system validation to study platform behavior under controlled conditions.
- Supported virtualized validation workflows by adjusting VM resources and observing performance or functional impact.

Possible Cohesity-specific resume phrasing:

- Senior support engineer with experience diagnosing complex Windows, networking, and platform issues across hardware, OS, and I/O layers.
- Validation engineer with Python automation experience for data collection, test execution, and repeatable diagnostics.
- Technical support background handling customer incidents, escalating cleanly, and documenting resolution steps.
- Comfortable working from logs, reproductions, and system behavior rather than guessing.

## Interview Story

Use `samtool` as the story when they ask about low-level debugging or kernel-adjacent experience.

- I built and debugged `samtool`, a Linux hardware-access utility that could read and write MMIO, PCI, I/O, and MSR locations.
- The work required controlled platform access, careful command parsing, and validation against real hardware behavior.
- I treated it as a debugging tool for platform investigation, which is the same mindset I would bring to storage or latency issues at Cohesity.

## Samtool Evidence

This is the low-level platform proof you can reuse for Cohesity:

- direct hardware access on Linux
- MMIO, PCI, I/O, and MSR operations
- kernel-adjacent debugging and validation mindset
- controlled platform investigation rather than guesswork

Use it to support claims about:

- Linux low-level debugging
- platform validation
- storage and latency investigation
- comfort working close to the hardware/software boundary

## Future Lab

Use `samtool` as a follow-up lab for this role.

Lab idea:

- set up a Linux test box
- simulate a firmware or BIOS change that affects latency or device behavior
- inspect PCI config space, MSRs, and MMIO/I/O state before and after the change
- compare the low-level platform state with the observed performance change

Why this matters for Cohesity:

- it practices the kind of low-level investigation used in platform and storage support
- it gives you a concrete story for diagnosing performance regressions below the driver layer
- it reinforces the same validation mindset used in Linux, storage, and virtualization troubleshooting

## CV Validation

Use this table to compare the posting directly against the current proof set.

| Requirement | Evidence | Gap | Score (0-2) | Action |
| --- | --- | --- | --- | --- |
| English and Spanish fluency | Working bilingual context and Costa Rica role alignment | Not explicitly stated in resume bullets | 1 | Add a direct bilingual statement if accurate |
| Python, Bash, or PowerShell | Python automation in validation work | Bash / PowerShell not yet clearly surfaced | 2 | Keep Python strong; add Bash or PowerShell only if defensible |
| Linux platform and kernel debugging | Linux-adjacent validation, `fio`, latency work, kernel-module experimentation | Need clearer Linux debug story | 1 | Prepare one concrete Linux storage-debug example |
| System diagnostics and clear communication | Service desk and validation background | Need customer-facing incident framing | 2 | Recast one past issue as an incident-to-resolution story |
| Linux debug utilities | `gdb` experience, low-level debugging habits | Need tool-specific breadth: `strace`, `tcpdump`, `wireshark`, `crash`, `systemtap`, `ftrace` | 1 | Build a small tool matrix and one example per tool |
| NFS / SMB / CIFS | Used in scripts for mapped directories | Need to show operational troubleshooting, not only use | 2 | Add one example of mount or access failure handling |
| Storage / virtualization concepts | `fio`, storage latency, validation work, kernel-adjacent benchmarking, `virt-manager`, VM CPU/storage configuration, `intel_iommu` | Need more direct storage vendor stack language | 2 | Tie virtualization proof to storage validation and platform behavior |
| AI tools for productivity | Current ingest and analysis workflow | None material | 2 | Mention workflow automation and AI-assisted analysis if relevant |

## Gap Closure Plan

1. Turn the kernel-adjacent work into a support story.
   - Write a short case study for `msr_latency.c` that explains the problem, the measurement method, and the result.
   - Frame it as controlled system investigation, not as abstract kernel hacking.

2. Build one Linux storage-debug lab.
   - Run `fio` against a filesystem target.
   - Capture `iostat`, `dmesg`, `strace`, and `vmstat` around the run.
   - Record the latency behavior and one conclusion in plain English.

3. Make the file-protocol experience explicit.
   - Write one example showing NFS or CIFS mount or scripted directory mapping.
   - Include the failure mode and how it was diagnosed.

4. Prepare one virtualization support story.
   - Use the `virt-manager` work, VM CPU sizing, disk attachment, and kernel-parameter validation as the proof base.
   - Connect that to a troubleshooting or validation scenario you can actually defend.
   - If you need `VMware vSphere`, `Hyper-V`, or `KVM` vocabulary, use it only where the evidence supports the claim.

5. Tighten the resume language for this role.
   - Lead with Python automation, incident troubleshooting, validation, and log analysis.
   - Add low-level Linux and storage wording only where the evidence is real.
   - Avoid overclaiming deep kernel expertise.

6. Prepare interview-ready stories.
   - customer incident ownership
   - storage latency investigation
   - Linux or kernel-adjacent debugging
   - escalation and documentation

7. Decide if this stays a target role.
   - If the Linux/storage/virtualization examples come together quickly, keep pursuing it.
   - If not, keep it as a strong maybe and prioritize adjacent support roles with less storage depth.

## Tailoring

- [ ] resume tailored
- [ ] LinkedIn updated if needed
- [ ] portfolio evidence selected
- [ ] cover note or message drafted
- [ ] referral or contact plan checked

## Interview Plan

- [ ] company research
- [ ] role research
- [ ] technical prep
- [ ] behavioral stories
- [ ] questions to ask
