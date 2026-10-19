# ODIN — The Allfather v2.0.0
## Operations

**Date:** 19-10-2026  
**Status:** v2 architecture specification

---

## 1. Operational Goal

ODIN should be understandable and recoverable without requiring the operator to reverse-engineer its Python process during an incident.

---

## 2. Installation

The v2 installer must:

- verify supported OS/runtime;
- verify Python and required system dependencies;
- resolve ODIN home without hard-coded source paths;
- create required directories safely;
- initialize configuration from validated defaults;
- initialize state storage;
- set appropriate file permissions;
- validate CLI-to-daemon communication;
- provide an installation report.

Installation must be idempotent where practical.

---

## 3. Runtime Commands

Recommended operational commands:

```text
odin serve
odin stop
odin restart
odin status
odin doctor
odin tasks
odin agents
odin models status
odin guardian status
odin integrity status
odin audit verify
```

`odin doctor` should be a non-destructive diagnostic command by default.

---

## 4. Health Model

ODIN should report health by subsystem rather than one generic green/red state.

```text
Daemon       healthy
State DB     healthy
IPC          healthy
Guardian     healthy
Integrity    healthy
Agents       degraded (1 unavailable)
Models       healthy
Disk         warning
Backups      healthy
```

---

## 5. Startup and Shutdown

Startup sequence:

```text
resolve paths
-> validate config
-> open/migrate state
-> verify recovery requirements
-> initialize audit
-> discover/validate agents
-> initialize providers
-> start Guardian
-> bind IPC
-> ready
```

Shutdown sequence should stop accepting new work, request task checkpoints/cancellation as policy dictates, flush state/audit records, stop Guardian workers, close IPC, and exit cleanly.

---

## 6. Crash Startup

If the previous shutdown was unclean, ODIN must enter recovery inspection before treating interrupted tasks as new work.

It should identify:

- interrupted tasks;
- incomplete transactions;
- stale sockets/PIDs;
- pending integrity operations;
- unfinished migrations;
- recent Guardian incidents.

---

## 7. Troubleshooting

Operational documentation must cover:

- daemon will not start;
- socket unavailable;
- stale socket;
- state database locked/corrupt;
- agent not discovered;
- provider unavailable;
- model unavailable;
- permission denied;
- integrity violation;
- low disk;
- runaway process;
- failed recovery;
- failed migration.

---

## 8. Support Bundle

ODIN may generate a redacted diagnostic bundle containing versions, configuration schema/version, health state, recent sanitized logs, Guardian summaries, and dependency status.

Secrets and private workspace content are excluded unless explicitly selected.

---

## 9. Updates

Updates require:

- preflight checks;
- backup/restore point;
- migration preview;
- version compatibility validation;
- post-update health check;
- rollback path.

---

## 10. Invariant

> A production ODIN installation must be diagnosable, stoppable, recoverable, and upgradeable without depending on an AI agent to guess what happened.
