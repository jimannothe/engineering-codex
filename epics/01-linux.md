# Linux

## Purpose

Use Linux as the base operating environment for development and lab work.

## Skills

- shell usage
- file system navigation
- process inspection
- package management

## Projects

- Engineering Codex
- automation-validation

## Backlog

- [ ] document common shell workflows
- [ ] document package install flow
- [ ] document system checks

## Experiments

### ckb-next keyboard brightness control

Purpose

- Check whether Corsair K60 brightness can go below the GUI's visible 33% step on Linux.

Procedure

- Started `ckb-next` headlessly and inspected `~/.config/ckb-next/ckb-next.conf`.
- Confirmed the GUI only exposes three brightness labels: `100%`, `67%`, and `33%`.
- Forced the stored brightness values to `0` in the config.
- Restarted `ckb-next-daemon` on the host and observed the keyboard LEDs.

Result

- The GUI settings alone did not change the LEDs in this session.
- Restarting `ckb-next-daemon` made the keyboard go much dimmer.
- The effective low setting is controlled by the daemon/hardware path, not just the config file.

Conclusion

- The Linux setup can drive the keyboard below the GUI's 33% display step, but only when the daemon is running on the host and applying the device state.

Lessons learned

- Config edits are not enough if the daemon is not talking to `/dev/input/ckb*`.
- `ckb-next -b` is only for the tray/GUI; the daemon is the part that applies LED state.
- For this device, restart the daemon to make brightness changes take effect.

## Done Criteria

This epic is useful when Linux tasks can be done from memory with good habits.
