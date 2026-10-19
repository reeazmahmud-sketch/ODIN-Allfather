# ODIN — The Allfather v2.0.0
## Security & Permissions

**Date:** 19-10-2026

---

## 1. Security Principle

ODIN agents are not inherently trusted merely because they are installed or enabled.

The user owns authority. ODIN enforces that authority. Agents operate through bounded capabilities.

---

## 2. Trust Boundaries

Primary boundaries:

1. user -> ODIN interface;
2. ODIN control plane -> agent;
3. agent -> workspace;
4. agent -> process execution;
5. agent -> network;
6. agent -> secrets;
7. ODIN -> macOS/system operations;
8. one workspace -> another workspace.

Crossing a boundary requires an explicit policy decision.

---

## 3. Permission Vocabulary

Recommended permissions:

```text
workspace.read
workspace.write
workspace.delete
workspace.move
workspace.protected.write
asset.read
asset.write
command.execute
package.install
network.request
process.inspect
process.control
system.inspect
system.modify
secrets.use
config.read
config.modify
audit.read
```

Ordinary agents must not receive `audit.modify` or equivalent permission.

---

## 4. Authorization Inputs

A decision considers:

- user policy;
- agent identity/version;
- project identity;
- requested capability;
- target path/resource;
- task context;
- prior explicit approval;
- risk class;
- demo/locked mode;
- machine policy.

The model's own statement that an action is safe is not authorization.

---

## 5. Risk Classes

### Low

Examples: read allowed project file, inspect ODIN task status.

May be pre-authorized.

### Medium

Examples: write ordinary workspace file, invoke approved local model, run known project test.

May use project-scoped approval policy.

### High

Examples: delete/move protected files, install packages, terminate processes, change system settings, access secrets.

Requires stronger policy and usually explicit approval.

### Critical

Examples: privileged system changes, broad deletion, credential changes, operations outside configured boundaries.

Requires explicit elevated authorization and must be heavily audited.

---

## 6. Approval Memory

ODIN may remember repeated approvals only as narrowly scoped policy.

A remembered approval must specify:

- exact capability;
- agent or agent class;
- project/scope;
- target constraints;
- expiration/revocation;
- maximum risk class.

Approval learning must never silently broaden privilege from a narrow action to a general one.

---

## 7. Locked / Demo Mode

Locked mode allows demonstrations and status inspection without mutation.

When enabled:

- deny workspace writes;
- deny command execution unless explicitly read-only;
- deny package installation;
- deny process control;
- deny system modification;
- deny secrets use;
- preserve status, logs, architecture views, and safe diagnostics.

The mode must be enforced by policy, not merely hidden UI controls.

---

## 8. Secrets

Secrets must not be stored in repository YAML, source code, task prompts, or ordinary logs.

ODIN should use environment variables, OS credential facilities, or pluggable secret providers.

Agents receive secret-backed capability results where possible rather than raw secret values.

Logs and checkpoints require redaction.

---

## 9. Filesystem Boundary

Path authorization must resolve real paths before checking policy to prevent `..`, symlink, and alias-based escapes.

Default agent access is its assigned workspace, not the user's entire home directory.

Access outside the workspace is a separate capability and authorization event.

---

## 10. Command Execution

Shell commands must be associated with:

- task ID;
- agent ID;
- working directory;
- timeout;
- environment allowlist;
- authorization decision;
- captured exit code;
- bounded output/logging.

Avoid implicit `shell=True` execution where structured argument invocation is possible.

---

## 11. Audit Separation

Agents may emit operational events but may not silently rewrite or delete authoritative audit history.

Audit retention and rotation are ODIN control-plane responsibilities.

---

## 12. Security Invariant

> Capability is not permission, and intelligence is not authority.

Every meaningful side effect passes through ODIN policy before execution.
