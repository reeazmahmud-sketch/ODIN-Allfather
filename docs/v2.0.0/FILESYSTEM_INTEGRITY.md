# ODIN — The Allfather v2.0.0
## Filesystem Integrity & Project Protection

**Date:** 19-10-2026

---

## 1. Problem

A project can become unusable when an agent accidentally deletes, moves, renames, truncates, or overwrites a critical file.

ODIN v2 makes project integrity a core responsibility.

---

## 2. Integrity Manifest

Each managed workspace should maintain a versioned manifest of important files.

Example:

```yaml
schema: 1
project: MyProject
files:
  src/main.py:
    sha256: "..."
    class: critical
    protected: true
  README.md:
    sha256: "..."
    class: tracked
    protected: false
```

Generated caches and dependency trees should normally be excluded.

---

## 3. Protection Classes

Suggested classes:

- **critical** — project cannot safely operate without it;
- **protected** — mutation requires stronger authorization/snapshot;
- **tracked** — changes are journaled and hashed;
- **generated** — reproducible, lower protection;
- **ignored** — excluded by policy.

Protection is project-specific rather than based only on filename.

---

## 4. Safe Mutation Pipeline

For protected writes:

```text
request
  -> permission check
  -> integrity preflight
  -> snapshot/backup
  -> staged write
  -> validate result
  -> atomic replace
  -> update manifest
  -> audit event
```

For delete/move/rename operations, ODIN records source and destination and maintains a recoverable snapshot according to policy.

---

## 5. Unexpected Changes

The integrity service should detect:

- missing critical file;
- unexpected relocation;
- checksum mismatch;
- zero-byte/truncated file;
- unexpected permission change;
- path escaping the workspace;
- symlink traversal that bypasses workspace policy.

Unexpected changes should not automatically be overwritten. ODIN first determines whether the change is authorized and recoverable.

---

## 6. Known-Good Points

Projects may mark checkpoints as known-good after validation/tests.

A known-good point references:

- integrity manifest;
- project metadata version;
- relevant task/checkpoint IDs;
- optional Git commit;
- validation results.

Git is complementary but not mandatory for ODIN recovery.

---

## 7. Recovery

Recovery modes:

- restore one file;
- restore a protected set;
- restore project metadata;
- compare current vs known-good;
- roll back an interrupted ODIN task.

ODIN should show exactly what will be restored before destructive rollback.

---

## 8. Disk Safety

Snapshots themselves can consume large amounts of disk.

ODIN must enforce:

- storage quotas;
- snapshot retention;
- deduplication where practical;
- large-file policy;
- free-space preflight;
- emergency suspension before the backup system exhausts the disk.

---

## 9. Integrity Invariant

> An agent must not be able to silently destroy the only trusted copy of a critical project artifact.
