# ODIN — The Allfather v2.0.0
## Persistent State & Crash Recovery

**Date:** 19-10-2026

---

## 1. Objective

ODIN must survive terminal closure, daemon failure, agent crashes, machine restart, and interrupted work without forcing agents to rediscover the entire project or repeat completed work.

This evolves v1's `.odin-meta.yaml` metadata rather than discarding it.

---

## 2. State Classes

ODIN separates state into:

1. **Project metadata** — human-readable identity and configuration.
2. **Runtime state** — tasks, sessions, checkpoints, leases, recovery status.
3. **Audit state** — append-oriented historical events.
4. **Integrity state** — manifests, hashes, snapshots, protected paths.

Runtime state should use a transactional store such as SQLite. YAML remains appropriate for human-readable project configuration.

---

## 3. Durable Task State

Every task transition is persisted before ODIN reports it as accepted or complete.

```text
queued -> authorized -> running -> completed
                           |
                           +-> failed
                           +-> cancelled
                           +-> interrupted -> recovery_pending
```

ODIN records checkpoints for meaningful milestones rather than relying on conversation memory.

---

## 4. Checkpoint Contents

A checkpoint should contain or reference:

- task ID;
- agent ID/version;
- project ID;
- normalized objective;
- completed steps;
- pending steps;
- files read;
- files changed;
- relevant hashes;
- command results;
- agent-produced state required for continuation;
- timestamp;
- checkpoint schema version.

Sensitive values must not be copied into checkpoints unnecessarily.

---

## 5. Crash Recovery Sequence

```text
ODIN starts
   |
   v
validate state database
   |
   v
scan interrupted tasks
   |
   v
verify workspace integrity
   |
   v
locate latest valid checkpoint
   |
   +--> safe to resume -> recovery_pending
   |
   +--> unsafe/ambiguous -> user review required
```

ODIN must never pretend an interrupted destructive operation completed successfully.

---

## 6. Atomicity

Critical metadata and state changes must use transactional or atomic-write semantics.

For filesystem metadata:

1. write temporary file;
2. flush/sync where required;
3. validate;
4. atomically replace target.

For database state, use transactions and schema migrations.

---

## 7. Session Resume

A resumed agent should receive a compact recovery context generated from durable ODIN state rather than reanalyzing the project from zero.

The context should answer:

- What was the objective?
- What has already been completed?
- What changed?
- What remains?
- What decisions were approved?
- What checkpoint is trusted?

---

## 8. Recovery Safety

Automatic resume is allowed only when the next operation is demonstrably safe.

Require user review when:

- filesystem integrity changed unexpectedly;
- a protected file differs from the checkpoint;
- task ownership is ambiguous;
- a destructive action was interrupted;
- schema migration failed;
- required provider/tool versions changed incompatibly.

---

## 9. Backup

State backups should be created before:

- schema migration;
- ODIN upgrade;
- destructive project operation;
- major configuration migration.

Backups require retention limits so ODIN itself cannot create uncontrolled disk growth.

---

## 10. Recovery Invariant

> Restarting ODIN must restore knowledge of what happened; it must not silently reinterpret history.
