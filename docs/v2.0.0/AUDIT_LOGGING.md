# ODIN — The Allfather v2.0.0
## Audit Logging

**Date:** 19-10-2026  
**Status:** v2 architecture specification

---

## 1. Purpose

ODIN v1 already records actions to `Logs/actions.log`. v2 evolves that concept into structured, durable, security-relevant audit records without removing human-readable operational logs.

---

## 2. Audit Principles

- Every meaningful action has an actor, target, result, and correlation ID.
- Agents cannot silently erase or rewrite their own audit trail.
- Security, authorization, integrity, recovery, and Guardian events are first-class audit events.
- Logs must avoid storing secrets or full sensitive payloads by default.
- Human-readable logs and structured audit records serve different purposes and may coexist.

---

## 3. Minimum Event Schema

```yaml
event_id: uuid
correlation_id: uuid
timestamp: RFC3339
actor_type: user|agent|guardian|system
actor_id: claude
project_id: ExampleProject
task_id: uuid
action: workspace.write
target: src/main.py
authorization: allowed
result: success
error: null
metadata: {}
```

Additional fields may include process ID, parent process ID, command fingerprint, checkpoint ID, snapshot ID, provider, model, duration, bytes changed, and policy rule ID.

---

## 4. Event Classes

ODIN should distinguish at least:

- `auth.*` — approvals, denials, privilege requests;
- `task.*` — queued, started, checkpointed, completed, failed, cancelled;
- `agent.*` — discovered, validated, registered, unhealthy, disconnected;
- `workspace.*` — create, read, write, move, delete, protect;
- `integrity.*` — hash mismatch, unexpected change, rollback;
- `guardian.*` — resource alert, containment, emergency stop;
- `config.*` — validated, changed, migrated, rejected;
- `backup.*` — snapshot, verify, restore;
- `runtime.*` — daemon start, stop, crash, recovery;
- `model.*` — provider selected, fallback, failure, rate limit.

---

## 5. Storage

Recommended authoritative store: SQLite or another transactional local store owned by ODIN.

Human-readable rolling log files may be written in parallel for diagnostics.

Audit storage should support:

- append-oriented writes;
- rotation/archival;
- retention policy;
- integrity verification;
- indexed search by task, project, actor, event class, and time;
- export without mutating source records.

---

## 6. Secret Redaction

ODIN must redact:

- API keys;
- access tokens;
- passwords;
- authorization headers;
- session cookies;
- private keys;
- configured sensitive environment values.

Commands should be represented safely when command-line arguments may contain secrets.

---

## 7. Audit Commands

Recommended CLI evolution:

```text
odin logs
odin logs --project MyProject
odin audit task <task-id>
odin audit incident <incident-id>
odin audit verify
```

Audit inspection is read-only by default.

---

## 8. Invariant

> If ODIN performed, blocked, recovered, or authorized a meaningful action, the event must be reconstructable later without relying on an agent's memory.
