# ODIN — The Allfather v2.0.0
## Implementation Roadmap & Resume Guide

**Date:** 19-10-2026  
**Branch:** `docs/v2.0.0-production`  
**Status:** Architecture/specification complete enough to pause; implementation intentionally deferred  

---

# 1. Resume Here

When development resumes, do **not** redesign ODIN and do **not** restart discovery from scratch.

Resume from this statement:

> ODIN v2 is an evolution of ODIN v1. The v1 CLI, daemon, agent adapters, workspaces, English/Bangla interaction, system monitoring, model configuration, and logging concepts remain the foundation. The next phase is implementation of the v2 production architecture already documented under `docs/v2.0.0/`.

Before changing code, read these documents in order:

1. `PRODUCTION_READINESS_AUDIT.md`
2. `ARCHITECTURE.md`
3. `MIGRATION_FROM_V1.md`
4. `SECURITY.md`
5. `STATE_AND_RECOVERY.md`
6. `FILESYSTEM_INTEGRITY.md`
7. `AGENT_RUNTIME.md`
8. `GUARDIAN.md`
9. `AUDIT_LOGGING.md`
10. `MODEL_PROVIDERS.md`
11. `INTERFACES.md`
12. `BACKUP_AND_RECOVERY.md`
13. `OPERATIONS.md`
14. `TESTING_AND_RELEASE.md`

The current production-spec branch is:

```text
docs/v2.0.0-production
```

Do not merge into `main` merely because implementation has started.

---

# 2. Scope Guardrails

ODIN v2 must remain ODIN.

Do not fold in or depend on:

- Weaver Engine;
- TERMINATOR / ODIN-TERMINATOR;
- RAAL Civilization;
- unrelated orchestration frameworks.

These are separate projects unless a future explicit integration decision is made.

Core evolution rule:

> Preserve ODIN v1's working DNA and harden it layer-by-layer.

---

# 3. Phase 0 — Re-Baseline Before Implementation

Goal: confirm the repository still matches the architecture assumptions before editing code.

Tasks:

- inspect `main` and compare it with the latest implementation branch;
- inventory `daemon/`, `bin/`, `Agents/`, `Config/`, `Dashboard/`, `Voice/`, `Workspaces/`, tests, and install scripts;
- confirm whether any code changed since the documentation branch was created;
- map every v1 feature to one of:
  - implemented;
  - scaffolded;
  - documented only;
  - planned;
- run the existing v1 system if practical and record baseline behavior;
- capture current dependencies and Python/macOS assumptions;
- create a clean implementation branch from the agreed base.

Exit criteria:

- repository baseline documented;
- no hidden implementation drift;
- implementation branch created;
- v1 behavior remains reproducible.

---

# 4. Phase 1 — Runtime Foundation

Goal: remove fragility without changing the user-facing identity of ODIN.

Priority work:

## 4.1 Root/Path Resolution

Replace hard-coded:

```text
$HOME/Terminal-CLI/Odin/Odin
```

with one central path resolver.

Resolution order:

1. `ODIN_HOME`;
2. installed/runtime location;
3. user configuration;
4. validated fallback.

Acceptance criteria:

- CLI and daemon resolve the same root;
- moving the repository does not silently break ODIN;
- tests cover path resolution.

## 4.2 Configuration Loader

Create typed/validated configuration for:

- core ODIN settings;
- models;
- Guardian thresholds;
- permissions;
- logging;
- state storage.

Acceptance criteria:

- invalid config fails safely;
- config schema/version is explicit;
- secrets are not stored in tracked configuration.

## 4.3 Structured IPC

Evolve raw text-over-socket communication into versioned structured requests/responses while keeping CLI compatibility.

Minimum message fields:

```text
protocol_version
request_id
command
arguments
project_id
actor
```

Acceptance criteria:

- bounded payloads;
- timeouts;
- predictable errors;
- request correlation IDs;
- legacy CLI commands still work through compatibility handling.

---

# 5. Phase 2 — Durable State & Crash Recovery

Goal: solve the terminal restart / daemon crash / Mac reboot context-loss problem.

Implement:

- SQLite-backed durable task state;
- task IDs;
- task lifecycle;
- checkpoints;
- session/project resume state;
- transactional writes;
- startup recovery scan;
- interrupted-task classification;
- idempotent recovery rules.

Minimum task states:

```text
queued
 authorized
 running
 checkpointed
 completed
 failed
 cancelled
 interrupted
 recoverable
```

Critical test:

1. start a task;
2. checkpoint it;
3. terminate the daemon unexpectedly;
4. restart ODIN;
5. recover task state without full re-analysis.

Exit criteria:

- restart does not erase task context;
- recovery decisions are auditable;
- corrupted checkpoints fail safely.

---

# 6. Phase 3 — Filesystem Integrity & Project Protection

Goal: prevent agents from accidentally breaking completed projects by moving, deleting, or corrupting critical files.

Implement:

- project integrity manifests;
- content hashes;
- protected-path rules;
- known-good snapshots;
- staged/transactional writes;
- delete/move interception;
- unexpected-change detection;
- rollback/restore command;
- retention controls.

Recommended project concepts:

```text
workspace
manifest
protected_paths
snapshots
checkpoints
asset_registry
recovery_metadata
```

Critical tests:

- protected file deletion attempt;
- protected file move attempt;
- partial write/crash;
- manifest mismatch;
- restore known-good project state;
- runaway snapshot growth does not fill disk.

Exit criteria:

- destructive operations are controlled;
- finished critical artifacts can be protected;
- rollback is tested, not merely documented.

---

# 7. Phase 4 — Authorization & Capability Enforcement

Goal: make sandboxing real instead of conceptual.

Implement capability categories:

```text
workspace.read
workspace.write
workspace.delete
workspace.move
command.execute
package.install
network.request
process.inspect
process.control
secrets.read
system.read
system.modify
```

Requirements:

- least privilege by default;
- agent capability != granted permission;
- destructive actions use approval policy;
- project-scoped permissions;
- no silent privilege expansion;
- repeated approvals may be remembered only within explicit policy boundaries;
- locked/demo mode is read-only.

Exit criteria:

- unauthorized actions are actually blocked in code;
- authorization decisions appear in audit history;
- tests prove workspace boundary enforcement.

---

# 8. Phase 5 — Agent Runtime Evolution

Goal: preserve `Agents/<agent>/adapter.py` while formalizing it.

Implement:

- agent manifest validation;
- capability declarations;
- health checks;
- lifecycle management;
- timeouts;
- heartbeats;
- cancellation;
- bounded retries;
- checkpoint/recovery hooks;
- v1 compatibility wrapper.

Start with:

1. template agent;
2. Claude adapter;
3. Gemini adapter;
4. local model-backed agent/provider integration.

Exit criteria:

- every running agent action belongs to an ODIN task;
- stalled agents can be cancelled;
- agent failure cannot take down the daemon;
- v1 adapters have visible compatibility limitations instead of fake v2 compliance.

---

# 9. Phase 6 — Guardian Evolution

Goal: evolve v1's monitor into a real supervised system Guardian.

Implement detection for:

- sustained CPU saturation;
- memory pressure;
- swap pressure;
- low disk space;
- abnormal disk growth;
- runaway child processes;
- repeated crash loops;
- stuck tasks;
- runaway logs/cache;
- daemon/provider health failures.

Response ladder:

```text
Observe
  -> Warn
  -> Request Approval
  -> Contain
  -> Recover
  -> Report
```

Important rule:

> Do not kill a process merely because of a single CPU spike.

Use duration, ownership, task context, process ancestry, and policy before intervention.

Exit criteria:

- alerts are attributable to tasks/processes;
- automatic containment is bounded and reversible where possible;
- emergency stop exists;
- Guardian actions are audited.

---

# 10. Phase 7 — Model Provider Layer

Goal: turn the v1 model YAML concept into real provider adapters.

Implement a provider contract such as:

```text
health_check()
list_models()
generate()
stream()
capabilities()
```

Priority providers:

- Ollama;
- LM Studio;
- cloud-provider adapters as separate optional integrations.

Routing policies may include:

- local first;
- cloud first;
- cost optimized;
- privacy first;
- manual.

Exit criteria:

- provider failure does not crash ODIN;
- fallback is explicit and auditable;
- model names are configuration/data, not hard-coded architecture;
- secrets come from secure runtime sources.

---

# 11. Phase 8 — CLI, English/Bangla, Voice, Dashboard

Goal: extend the v1 interface instead of replacing it.

Preserve familiar commands:

```text
odin serve
odin create
odin list
odin integrate
odin status
odin stop
```

Correct v1 inconsistencies where shell commands exist without daemon handlers.

Add production commands gradually:

```text
odin doctor
odin task list
odin task resume
odin task cancel
odin guardian status
odin integrity verify
odin restore
odin logs
odin audit verify
```

Language layer:

- normalize English and Bangla into the same internal command objects;
- never give Bangla commands different authorization semantics;
- preserve user-facing Bangla naturally.

Voice:

- voice input becomes another interface to the same authorization/control plane;
- voice must never bypass confirmation requirements.

Dashboard:

- operationally read-only by default;
- locked/demo mode must expose no destructive controls or secrets.

---

# 12. Phase 9 — Audit, Backup & Recovery Operations

Implement structured audit events for:

- authorization;
- tasks;
- agents;
- workspace changes;
- integrity failures;
- Guardian actions;
- configuration changes;
- backup/restore;
- runtime lifecycle;
- model/provider events.

Implement:

- backup creation;
- backup verification;
- restore testing;
- state DB backup;
- config backup excluding secrets;
- project restore points;
- disaster-recovery procedure.

Exit criteria:

- a user can explain what happened after an incident;
- backup restore is exercised in tests;
- logs do not expose credentials.

---

# 13. Phase 10 — Production Test & Release Gate

Do not call ODIN v2 production-ready until it passes documented gates.

Required categories:

- unit tests;
- integration tests;
- end-to-end CLI tests;
- agent lifecycle tests;
- permission/security tests;
- recovery tests;
- filesystem integrity tests;
- provider failure tests;
- Guardian tests;
- install/upgrade/rollback/uninstall tests;
- supported macOS verification;
- chaos tests.

Critical chaos scenarios include:

1. kill daemon mid-task;
2. kill agent subprocess;
3. corrupt checkpoint;
4. attempt protected-file deletion;
5. attempt protected-file move;
6. fill disk rapidly;
7. generate runaway log/cache growth;
8. create sustained high CPU process;
9. create memory pressure;
10. provider goes offline mid-task;
11. malformed provider response;
12. invalid configuration;
13. interrupted upgrade;
14. restore corrupted project from known-good state;
15. reboot/restart and resume interrupted work.

Release labels must mean:

- **Planned** — specified only;
- **Implemented** — code exists;
- **Verified** — tests prove behavior;
- **Release Candidate** — all mandatory gates pass in candidate environment;
- **Production Ready** — release criteria, recovery, security, and operations evidence are complete.

---

# 14. Recommended Implementation Order

Use this order unless repository changes reveal a dependency that requires adjustment:

```text
1. Re-baseline repository
2. Root/path resolver
3. Typed configuration
4. Structured IPC
5. Durable state/task manager
6. Checkpoints/crash recovery
7. Filesystem integrity/protection
8. Authorization/capability enforcement
9. Structured audit logging
10. Agent runtime
11. Guardian
12. Model providers
13. CLI improvements
14. English/Bangla normalization
15. Voice/dashboard
16. Backup/disaster recovery
17. Operations tooling
18. Full tests + chaos suite
19. Migration rehearsal from v1
20. Release candidate
```

The dependency rule is deliberate: do not build autonomous Guardian remediation or powerful agents before permissions, state, audit, and integrity foundations exist.

---

# 15. First Session Back Checklist

When returning to this project, start with exactly this checklist:

```text
[ ] Checkout/inspect `docs/v2.0.0-production`
[ ] Read this IMPLEMENTATION_ROADMAP.md
[ ] Read ARCHITECTURE.md and PRODUCTION_READINESS_AUDIT.md
[ ] Compare `main` against current repository state
[ ] Confirm no Weaver/TERMINATOR/RAAL scope creep
[ ] Record current v1 baseline
[ ] Create implementation branch
[ ] Implement only Phase 1 first
[ ] Add tests with each subsystem
[ ] Update status from Planned -> Implemented -> Verified only with evidence
```

Do not jump directly to flashy features such as voice/dashboard before the reliability core is in place.

---

# 16. Pause Checkpoint — 19-10-2026

At this checkpoint:

- ODIN v1 remains the implementation baseline;
- ODIN v2 architecture/specification has been documented;
- implementation has intentionally **not** begun;
- `main` has not been replaced by the v2 design;
- production claims require future implementation and verification;
- the next work item is **Phase 0 / Phase 1 implementation preparation**, not further redesign.

This file is the canonical handoff point for resuming ODIN v2 development later.
