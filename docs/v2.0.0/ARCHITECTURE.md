# ODIN — The Allfather v2.0.0
## Evolution Architecture

**Date:** 19-10-2026  
**Branch:** `docs/v2.0.0-production`  
**Status:** Architecture definition in progress  

---

## 1. Evolution Principle

ODIN v2 is an evolution of ODIN v1, not a replacement product.

The v1 architecture already establishes ODIN's identity:

- shell CLI as the user entry point;
- a long-running local Python daemon;
- Unix-socket IPC;
- dynamic agent discovery through adapters;
- project workspaces;
- English and Bangla command support;
- system monitoring;
- YAML configuration;
- local/cloud model configuration;
- action logging.

v2 preserves those concepts and hardens them for reliability, safety, recoverability, and maintainability.

---

## 2. v1 Baseline

```text
User
  |
  v
bin/odin-cli
  |
  | Unix socket / socat
  v
daemon/odin_daemon.py
  |
  +-- command parser
  +-- project manager
  +-- agent discovery
  +-- system monitor
  +-- action logging
  |
  +--> Agents/
  |      +-- claude/
  |      +-- gemini/
  |      +-- template_agent/
  |
  +--> Workspaces/
  +--> Config/
  +--> Logs/
```

This remains the conceptual foundation of v2.

---

## 3. v2 Architecture

```text
User / CLI / Voice / Dashboard
            |
            v
+--------------------------------------+
|          ODIN Interface Layer        |
| command parsing | EN/BN | UX         |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
|           ODIN Control Plane         |
| router | authz | task state | policy |
+----------+---------------+-----------+
           |               |
           v               v
+------------------+   +------------------+
|   Agent Runtime  |   |     Guardian     |
| registry         |   | CPU / RAM / disk |
| adapters         |   | process monitor  |
| lifecycle        |   | safe remediation |
+---------+--------+   +---------+--------+
          |                      |
          +----------+-----------+
                     v
+--------------------------------------+
|       Capability Enforcement         |
| filesystem | process | network       |
| secrets    | system  | approvals     |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
|           Workspace Manager          |
| projects | assets | metadata         |
| manifests | protected paths          |
+------------------+-------------------+
                   |
          +--------+---------+
          |                  |
          v                  v
+------------------+   +------------------+
| Persistent State |   | Integrity/Backup |
| sessions         |   | checksums        |
| tasks            |   | snapshots        |
| checkpoints      |   | rollback         |
+---------+--------+   +---------+--------+
          |                      |
          +----------+-----------+
                     v
+--------------------------------------+
|        Audit & Observability         |
| structured logs | health | reports   |
+--------------------------------------+
```

---

## 4. Components We Preserve

### 4.1 CLI

The `odin` command remains the primary terminal interface.

v2 should preserve familiar commands wherever possible and correct inconsistent v1 commands rather than forcing unnecessary changes.

Examples:

```text
odin serve
odin create MyProject
odin list
odin integrate claude MyProject
odin status
odin stop
```

New commands should extend the same interface instead of creating a second CLI.

### 4.2 Daemon

The local daemon remains ODIN's core runtime.

v2 evolves it from a single large process module into clearly separated internal services while keeping one coherent local control plane.

Expected internal services:

- command service;
- project service;
- agent registry;
- task manager;
- authorization service;
- Guardian service;
- state service;
- integrity service;
- audit service.

### 4.3 Unix Socket IPC

Local Unix-socket communication remains appropriate for the local daemon.

v2 should improve it with:

- structured messages;
- protocol versioning;
- request IDs;
- bounded payloads;
- timeouts;
- authentication/ownership checks;
- predictable error responses.

`socat` may remain a compatibility transport for the shell CLI, but the protocol must not depend on ad-hoc text parsing internally.

### 4.4 Agents

The `Agents/<agent>/adapter.py` convention remains recognizable.

v2 formalizes the adapter contract instead of relying on naming conventions alone.

Each agent should declare:

- identity;
- version;
- supported capabilities;
- required permissions;
- supported file types;
- supported providers/tools;
- health status;
- timeout requirements.

### 4.5 Workspaces

`Workspaces/<project>` remains the unit of project isolation.

v2 adds enforcement and recovery around the existing idea.

Each workspace should include or reference:

- project metadata;
- agent assignments;
- permission policy;
- task state;
- integrity manifest;
- checkpoints;
- asset registry;
- recovery metadata.

### 4.6 English and Bangla

English and Bangla remain first-class interaction languages.

The v1 mapping concept should evolve into a normalized command layer so localization does not alter the underlying command semantics.

### 4.7 System Monitoring

The v1 monitor becomes the v2 Guardian.

The Guardian expands monitoring from threshold alerts into supervised detection, diagnosis, authorization, containment, recovery, and reporting.

---

## 5. New v2 Internal Layers

### 5.1 Task Manager

Every operation should have a durable task identity.

Minimum task record:

```yaml
task_id: uuid
project_id: project-name
actor: claude
command: analyze
state: running
created_at: timestamp
updated_at: timestamp
checkpoint: null
result: null
```

Task states should include:

```text
queued -> authorized -> running -> completed
                           |-> failed
                           |-> cancelled
                           |-> interrupted -> recoverable
```

### 5.2 Authorization Service

ODIN, not the AI model, decides whether an action is permitted.

Permission categories should include:

- filesystem read;
- filesystem write;
- filesystem delete/move;
- command execution;
- process management;
- network access;
- package installation;
- secrets access;
- system settings;
- privileged/elevated actions.

### 5.3 Persistent State

v1 metadata files are not enough for crash-safe orchestration.

v2 requires durable state for:

- active tasks;
- checkpoints;
- agent assignments;
- approvals;
- recovery status;
- Guardian incidents;
- project lifecycle state.

The initial implementation may use SQLite plus human-readable project metadata, provided writes are transactional and migrations are versioned.

### 5.4 Integrity Manager

The integrity layer protects finished and critical project files.

Responsibilities:

- baseline manifest;
- content hashes;
- protected paths;
- pre-change snapshots;
- staged writes;
- delete/move interception;
- unexpected-change detection;
- rollback.

### 5.5 Guardian

The Guardian evolves the existing `monitor_system()` capability.

It should detect:

- sustained CPU saturation;
- memory pressure;
- swap pressure;
- abnormal disk growth;
- low free disk;
- runaway child processes;
- repeated crash loops;
- stuck tasks;
- oversized logs/cache;
- daemon health failures.

Response levels:

```text
Observe -> Warn -> Request Approval -> Contain -> Recover -> Report
```

Automatic destructive remediation is not a default behavior.

---

## 6. Filesystem Root Discovery

v1 hard-codes:

```text
$HOME/Terminal-CLI/Odin/Odin
```

v2 must remove this assumption.

Recommended resolution order:

1. `ODIN_HOME` environment variable;
2. installed package/runtime location;
3. user config path;
4. validated fallback location.

All resolved paths should be represented through one configuration object rather than reconstructed independently throughout the codebase.

---

## 7. Configuration Evolution

v1 YAML remains useful for user-editable configuration.

v2 should split configuration into clear domains:

```text
Config/
├── odin.yaml
├── models.yaml
├── guardian.yaml
├── permissions.yaml
└── schemas/
```

Secrets do not belong in tracked YAML.

Configuration must support:

- schema validation;
- version fields;
- migrations;
- defaults;
- environment overrides;
- safe failure on invalid values.

---

## 8. Model Integration Evolution

The v1 model registry concept remains.

v2 should introduce provider adapters rather than hard-code behavior around specific model names.

Example conceptual interface:

```text
ModelProvider
  +-- health_check()
  +-- list_models()
  +-- generate()
  +-- stream()
  +-- capabilities()
```

Potential providers may include local runtimes such as Ollama and LM Studio plus cloud adapters, but the ODIN core must not depend on one vendor.

---

## 9. Logging Evolution

The v1 append-only text action log becomes structured audit logging.

Minimum event fields:

```text
event_id
correlation_id
timestamp
actor
project
task
action
target
authorization
result
error
```

Human-readable logs may still be produced, but structured records become the authoritative operational history.

---

## 10. Backward Compatibility

v2 should preserve, where safe:

- existing project folders;
- `.odin-meta.yaml` files;
- recognizable CLI command names;
- agent folder convention;
- local model configuration intent;
- English/Bangla command behavior.

Compatibility must not preserve unsafe behavior merely for convenience.

Migration should import and upgrade v1 metadata rather than requiring users to recreate projects.

---

## 11. Explicit Non-Goals

ODIN v2 does not become:

- Weaver Engine;
- RAAL;
- TERMINATOR;
- a cloud-first orchestration platform;
- an unrestricted autonomous administrator;
- a replacement for macOS security boundaries.

ODIN remains a local-first agent orchestrator and system Guardian with explicit authorization and recoverability.

---

## 12. Architecture Invariant

The central v2 invariant is:

> AI agents may propose and perform work, but ODIN owns the workspace, permissions, execution boundary, state, integrity, recovery, and audit trail.

That is the production evolution of the architecture already present in ODIN v1.
