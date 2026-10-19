# ODIN — The Allfather v2.0.0
## CLI, English/Bangla, Voice, and Dashboard Interfaces

**Date:** 19-10-2026  
**Status:** v2 architecture specification

---

## 1. Principle

ODIN v2 keeps the v1 CLI as the canonical control interface. Voice and dashboard interfaces are additional clients of the same command/control plane, not separate implementations of ODIN logic.

---

## 2. CLI Evolution

Existing familiar commands remain wherever safe:

```text
odin serve
odin create <project>
odin list
odin integrate <agent> <project>
odin status
odin help
odin stop
```

v2 expands the same command family:

```text
odin resume [project|task]
odin tasks
odin agents
odin models
odin guardian status
odin integrity check <project>
odin checkpoint <project>
odin recover <project>
odin permissions <project>
odin audit ...
odin doctor
```

Commands accepted by the CLI and daemon must come from one shared command specification so the v1 mismatch between exposed and implemented commands cannot recur.

---

## 3. Structured IPC

The shell command is normalized into a structured request before execution.

Conceptually:

```json
{
  "protocol": 2,
  "request_id": "uuid",
  "command": "status",
  "args": [],
  "language": "en"
}
```

Responses carry status, message, data, errors, and correlation IDs.

---

## 4. English and Bangla

English and Bangla remain first-class.

Language parsing should map different user expressions to one canonical command vocabulary.

Example:

```text
"list projects"
"প্রজেক্টের তালিকা"
       |
       v
project.list
```

Authorization must operate on the canonical action, never on translated surface text.

---

## 5. Voice

Voice evolves from the v1 scaffold into an input/output adapter.

Pipeline:

```text
Microphone
   -> speech recognition
   -> language normalization
   -> canonical ODIN command/intent
   -> authorization
   -> execution
   -> response
   -> optional speech output
```

Voice must not bypass approval requirements. Sensitive actions require the same authorization as typed commands.

The microphone must have visible active/inactive state and explicit user control.

---

## 6. Dashboard

The v1 Dashboard scaffold may evolve into a local operational view.

Default dashboard behavior should be read-only.

Useful views:

- daemon health;
- active tasks;
- agents;
- projects;
- CPU/memory/disk;
- Guardian incidents;
- model/provider health;
- integrity alerts;
- recovery points;
- audit timeline.

Mutation from the dashboard uses the same authorization service as CLI commands.

---

## 7. Locked Demo Mode

Demo mode should expose system state suitable for demonstration while disabling mutation and redacting sensitive information.

Demo mode must not merely hide buttons; the backend policy must deny mutating operations.

---

## 8. Accessibility and Failure Behavior

Interfaces should provide:

- plain-text fallback;
- clear error codes/messages;
- non-color status indicators in addition to color;
- interruption/cancellation feedback;
- confirmation of high-impact actions;
- readable Bangla Unicode rendering.

---

## 9. Invariant

> CLI, voice, and dashboard are different doors into the same ODIN authority; none receives special permission by virtue of its interface.
