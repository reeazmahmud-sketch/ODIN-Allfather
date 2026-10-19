# ODIN — The Allfather v2.0.0
## Backup and Disaster Recovery

**Date:** 19-10-2026  
**Status:** v2 architecture specification

---

## 1. Purpose

ODIN must be able to recover not only a task but the operational system and protected projects after corruption, failed upgrades, accidental deletion, or machine-level failure.

Task checkpoints and project backups are related but distinct.

---

## 2. Backup Domains

ODIN should separately protect:

1. configuration;
2. durable runtime state;
3. project metadata;
4. protected workspace content;
5. integrity manifests;
6. audit metadata needed for reconstruction.

Caches, downloaded models, temporary build products, and regenerable data should not automatically inflate backups.

---

## 3. Snapshot Types

```text
checkpoint     task-level resumability
restore point  project known-good state
system backup  ODIN configuration/state recovery
release backup pre-upgrade rollback point
```

Each snapshot has an ID, timestamp, source version, integrity hash, size, and retention class.

---

## 4. Backup Safety

Before high-impact operations ODIN should create or verify an appropriate restore point.

Examples:

- project-wide refactor;
- mass file move;
- dependency migration;
- ODIN upgrade;
- configuration migration;
- integrity repair.

Backups must not create uncontrolled disk growth. Retention and available-space checks are mandatory.

---

## 5. Restore

Restore is a controlled operation:

```text
Select recovery point
  -> verify integrity
  -> show affected scope
  -> authorize
  -> stage restore
  -> validate
  -> commit
  -> audit
```

A failed restore must not destroy the current state.

---

## 6. Recovery Scenarios

The release test suite must exercise at least:

- daemon killed during active task;
- machine restart with running task;
- partial state write;
- deleted protected file;
- moved protected file;
- corrupted metadata;
- invalid configuration;
- failed ODIN upgrade;
- failed project migration;
- disk-full condition during write;
- damaged latest checkpoint with older valid checkpoint available.

---

## 7. Disaster Recovery

A documented disaster recovery procedure must explain how to rebuild ODIN from a clean installation using available backups.

Recovery priority:

1. ODIN configuration and identity;
2. state database;
3. workspace metadata;
4. protected project content;
5. integrity validation;
6. agents/providers;
7. optional caches.

---

## 8. Verification

A backup is not considered reliable until ODIN can verify its metadata and integrity. Production release testing must include an actual restore test.

---

## 9. Invariant

> ODIN must never call data protected merely because a backup command completed; protection requires a verifiable recovery path.
