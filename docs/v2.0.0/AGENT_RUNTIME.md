# ODIN — The Allfather v2.0.0
## Agent Runtime

**Date:** 19-10-2026  
**Status:** v2 architecture specification  

---

## 1. Purpose

ODIN v2 preserves the v1 `Agents/<name>/adapter.py` model and turns it into a formal runtime contract.

The goal is not to replace dynamic agent discovery. The goal is to make discovered agents predictable, observable, cancellable, permission-aware, and recoverable.

---

## 2. Agent Identity

Every agent must expose metadata that ODIN can validate before activation.

Recommended manifest fields:

```yaml
name: claude
version: 2.0.0
entrypoint: adapter.py
class: Claude
capabilities:
  - analyze_project
  - analyze_asset
  - generate_code
permissions_required:
  - workspace.read
  - workspace.write
providers:
  - anthropic
  - cli
supports:
  - py
  - js
  - ts
  - md
healthcheck: true
```

ODIN must reject malformed or incompatible manifests before loading the agent.

---

## 3. Runtime Lifecycle

```text
discovered
   |
   v
validated
   |
   v
registered
   |
   v
assigned
   |
   v
ready
   |
   v
running
  / | \
 v  v  v
completed failed cancelled
          |
          v
      recoverable
```

Each lifecycle transition must be recorded in durable task state and audit logs.

---

## 4. Adapter Contract

A v2 adapter should implement a stable interface such as:

```python
class OdinAgent:
    def metadata(self): ...
    def health_check(self): ...
    def analyze_project(self, context): ...
    def analyze_asset(self, asset, context): ...
    def execute_task(self, task, context): ...
    def cancel(self, task_id): ...
    def checkpoint(self, task_id): ...
    def recover(self, checkpoint): ...
```

Adapters may wrap a cloud API, local model, terminal CLI, or custom local process, but ODIN sees the same lifecycle contract.

---

## 5. Capability Model

Capabilities are declarative and permission-bound.

Examples:

```text
project.read
project.analyze
project.write
asset.read
asset.transform
command.execute
package.install
network.request
process.inspect
process.control
system.read
system.modify
```

Having a capability does not itself grant permission. ODIN policy must authorize the requested capability for the agent, project, and task.

---

## 6. Task Ownership

Each agent action runs under a durable ODIN task record.

A task contains:

- task ID;
- project ID;
- agent ID;
- requested capability;
- normalized user intent;
- authorization result;
- status;
- start/update/end timestamps;
- checkpoint reference;
- output/result reference;
- error information.

No long-running agent action should exist outside ODIN task tracking.

---

## 7. Timeouts, Cancellation, and Retry

v2 must prevent an agent from running forever.

Every task should support:

- start deadline;
- execution timeout;
- heartbeat interval;
- cancellation token;
- retry count;
- retry backoff;
- terminal failure state.

Retries must be bounded and idempotency-aware. Destructive actions must not be replayed blindly.

---

## 8. Workspace Boundary

The workspace remains the agent's default execution boundary.

The runtime should provide agents with resolved logical paths rather than encouraging arbitrary filesystem traversal.

An agent should not receive broad access simply because its underlying CLI or provider technically has it.

---

## 9. Health and Supervision

ODIN should distinguish between:

- agent unavailable;
- provider unavailable;
- provider authenticated but rate-limited;
- task stalled;
- subprocess exited;
- malformed response;
- permission denied;
- workspace integrity blocked.

Health status should be queryable via `odin status` and later dashboard views.

---

## 10. Compatibility with v1 Agents

v1 adapters may be loaded through a compatibility wrapper.

Compatibility mode can infer basic methods such as:

- `analyze_project()`;
- `analyze_asset()`;
- `monitor_system()`.

However, missing v2 metadata, cancellation, checkpoints, and permission declarations must be visible as compatibility limitations rather than silently assumed.

---

## 11. Runtime Rule

> Agents are workers. ODIN is the authority that owns task identity, permissions, lifecycle, persistence, and recovery.
