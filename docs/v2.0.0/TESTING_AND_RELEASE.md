# ODIN — The Allfather v2.0.0
## Testing, Chaos Validation, and Release Gates

**Date:** 19-10-2026  
**Status:** v2 architecture specification

---

## 1. Principle

ODIN v2 is production-ready only when behavior is verified. Documentation, feature presence, or a successful happy-path demonstration is not sufficient.

---

## 2. Test Layers

### Unit

Test parsers, policies, state transitions, path resolution, manifest hashing, configuration validation, provider selection, and utility functions.

### Integration

Test CLI/IPC/daemon, state storage, agent adapters, Guardian events, authorization, integrity operations, provider adapters, and backup/restore.

### End-to-End

Test real user workflows from CLI request through task completion and audit record.

### Security

Test path traversal, permission escalation, destructive commands, secret redaction, unauthorized config changes, agent boundary violations, and demo-mode mutation attempts.

### Recovery

Test daemon kill, interrupted writes, reboot simulation, corrupted checkpoints, missing files, failed migrations, and rollback.

---

## 3. Critical Chaos Scenarios

Release candidates must survive controlled scenarios including:

1. terminate daemon during file write;
2. terminate agent during long task;
3. restart with active task;
4. fill available test disk space;
5. generate rapid disk growth;
6. create CPU-saturating child process;
7. create memory-pressure worker;
8. repeatedly crash an agent;
9. delete/move a protected project file;
10. corrupt newest checkpoint;
11. make provider unavailable mid-task;
12. deny network during cloud request;
13. provide malformed agent manifest;
14. provide invalid configuration;
15. interrupt upgrade/migration.

Tests must use safe test fixtures and isolated environments; chaos testing must not intentionally endanger unrelated user data.

---

## 4. Compatibility Tests

v2 must test migration from representative v1 structures:

- existing `Workspaces/<project>`;
- `.odin-meta.yaml`;
- v1 agent directories;
- model configuration;
- historical logs;
- existing CLI expectations.

---

## 5. Quality Gates

Before release candidate:

- tests pass;
- lint/type checks pass for supported code;
- config schemas validate;
- migration tests pass;
- no known critical security defect remains;
- secrets scan passes;
- install/uninstall test passes;
- documentation status labels match implementation.

Before production-ready:

- crash recovery verified;
- protected-file recovery verified;
- backup restore verified;
- Guardian containment verified;
- permission enforcement verified;
- audit reconstruction verified;
- upgrade and rollback verified;
- supported macOS environment verified;
- release candidate chaos suite passes.

---

## 6. Capability Status Labels

Every major feature should carry one of:

```text
PLANNED       specified but not implemented
IMPLEMENTED   code exists
VERIFIED      automated/manual acceptance evidence exists
EXPERIMENTAL  implemented but not production-supported
DEPRECATED    retained temporarily for migration
```

`IMPLEMENTED` and `VERIFIED` are deliberately different.

---

## 7. Release Sequence

```text
Design
  -> Implementation
  -> Alpha
  -> Beta
  -> Release Candidate
  -> Production Ready
```

A release candidate should be tagged only after migration, security, recovery, and operational tests pass.

---

## 8. Release Artifacts

A production release should include:

- versioned source;
- changelog;
- installation instructions;
- migration instructions;
- rollback instructions;
- supported platform/runtime matrix;
- configuration schema version;
- test/acceptance summary;
- known limitations;
- checksums/signing information where the distribution mechanism supports it.

---

## 9. v2.0.0 Exit Criteria

ODIN v2.0.0 exits development only when the core evolutionary goals are verified:

- v1 projects can migrate;
- CLI/daemon architecture remains recognizable and functional;
- agents operate under formal lifecycle and permissions;
- task state survives interruption;
- protected project files can be detected/recovered;
- Guardian safely handles defined runaway/resource scenarios;
- audit history reconstructs actions;
- local model/provider path works without mandatory cloud dependency;
- English/Bangla command normalization works;
- installation, upgrade, rollback, and recovery are documented and tested.

---

## 10. Invariant

> ODIN earns the words “Production Ready” through repeatable evidence, not through a declaration in a README.
