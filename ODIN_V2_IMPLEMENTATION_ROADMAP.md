# ODIN V2 — Implementation Roadmap

**Project:** ODIN — The Allfather  
**Target:** Version 2.0  
**Development Branch:** `odin-v2`  
**Date:** 19-10-2026  
**Strategy:** Evolution of ODIN V1, not a redesign  
**Weaver Engine:** Not part of ODIN-Allfather V2

---

## 1. Mission

ODIN V2 evolves the existing V1 multi-agent orchestration and system-monitoring foundation into a production-grade macOS AI/Agent Guardian and development control plane.

V2 preserves V1's identity and working foundations while adding the safety, recovery, persistence, intelligence, and native interaction layers required for reliable day-to-day operation with autonomous coding agents.

### Non-negotiable principles

1. Preserve V1 history and backward compatibility wherever practical.
2. Do not replace proven V1 components merely to rename or redesign them.
3. Keep ODIN-Allfather independent from the Weaver Engine.
4. Agents operate through explicit capabilities and permissions.
5. Potentially destructive operations require policy evaluation and appropriate authorization.
6. Protect project integrity before maximizing autonomy.
7. Persist sufficient state for recovery after terminal, agent, app, or machine interruption.
8. Prefer deterministic system operations; use AI for intent interpretation, reasoning, recommendations, and assistance.
9. English and Bangla remain first-class interaction languages.
10. Every phase must be testable and independently resumable.

---

## 2. V1 Baseline — KEEP

These existing ODIN concepts form the V2 foundation:

- ODIN daemon architecture
- Unix-socket IPC foundation
- Workspace-based project management
- `.odin-meta.yaml` project metadata
- Automatic agent discovery
- Claude adapter
- Gemini adapter
- Template agent system
- English + Bangla command foundation
- CPU, memory, and disk monitoring foundation
- Action logging
- Configuration architecture
- Local/cloud model configuration concept
- Portable installation concept
- Existing documentation and version history

V2 must extend these systems rather than silently discarding them.

---

## 3. Classification of Existing Roadmap

### KEEP

- Multi-agent orchestration
- Project workspaces
- Agent templates
- English/Bangla support
- System monitoring
- Model configuration
- Portable installation

### UPGRADE

- `/models` → Model Router and interactive model management
- Simple Mode/Wizard → Conversational Intent + Guided Workflow Engine
- Voice → unified English/Bangla text/voice intent pipeline
- Project templates → governed project creation profiles
- Smart suggestions → contextual recommendations with explicit approval
- Analytics → system/project/agent observability
- GUI dashboard → native ODIN control application
- Plugin system → capability-declared extension system
- Permissions → project + agent + action capability policy
- History/Undo → transaction history + reversible operations
- Backup/Rollback → checkpoint and recovery subsystem
- Monitoring → historical anomaly/runaway-process detection

### BUILD FOR V2

- Guardian Layer
- Policy Engine
- Risk Classifier
- Safe Executor
- File Integrity Engine
- Project checkpoints and snapshots
- Crash/session recovery
- Persistent task/project state
- Dependency Manager
- macOS command intelligence
- controlled macOS settings navigation
- Agent Control Plane
- structured audit ledger
- multimodal asset ingestion
- real native ODIN application
- native alerts/notifications
- approval workflows
- protected/quarantine deletion flow

### DEFER

Unless required by V2 architecture, defer these until the V2 core is stable:

- iOS/Android full clients
- team collaboration
- public/community marketplace
- Kubernetes
- large-scale enterprise deployment
- certification/education marketplace
- gamification/achievements
- broad social integrations
- unrelated experimental productivity features

---

## 4. Target V2 Architecture

```text
User
 ├── Text
 ├── Voice
 ├── English
 └── Bangla
      │
      ▼
Intent Engine
      │
      ▼
ODIN Orchestrator
      │
      ├──────────── Guardian Layer ────────────┐
      │                                        │
      │   Policy Engine     Risk Classifier    │
      │        │                  │             │
      │   Permissions       Action Risk         │
      │        │                  │             │
      │   File Integrity    Process Risk        │
      │        │                  │             │
      │   Checkpoints       Resource Risk       │
      │        └──────────┬───────┘             │
      │                   ▼                     │
      │              Safe Executor              │
      └───────────────────┬─────────────────────┘
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
            macOS      Projects      Agents
                                   ├─ Claude
                                   ├─ Gemini
                                   ├─ Terminator adapter
                                   ├─ Pragga adapter
                                   ├─ Eve adapter
                                   ├─ Esha adapter
                                   └─ Future adapters
```

ODIN remains the authorization and coordination authority. Integrated agents do not automatically inherit unrestricted filesystem or shell authority.

---

# 5. Implementation Phases

## Phase 0 — Baseline Preservation & Verification

**Goal:** Establish a trustworthy V1 baseline before changing behavior.

### Work

- Inventory V1 source, configuration, scripts, documentation, and adapters.
- Record current branch/commit baseline.
- Map documented features to actual implementation.
- Identify placeholder/stub functionality.
- Establish test fixtures for current commands.
- Define compatibility expectations.
- Create V2 development branch.

### Acceptance criteria

- V1 baseline is reproducible.
- Existing functional commands have regression tests or explicit verification procedures.
- No V1 file is removed merely because V2 has a replacement concept.
- Placeholder features are clearly identified as such.

---

## Phase 1 — Guardian Foundation

**Goal:** Put safety between agents/intents and system-changing actions.

### Components

- `PolicyEngine`
- `RiskClassifier`
- `SafeExecutor`
- capability manifests
- approval workflow
- structured audit events

### Initial risk model

**Low risk:** read/list/status/inspect operations.

**Medium risk:** dependency installation, ordinary project-scoped modifications, project configuration changes.

**High risk:** recursive delete/move, privileged commands, protected-file changes, service/system configuration, large filesystem mutations, permission/ownership changes.

Risk classification must consider context, not only command names.

### Acceptance criteria

- Agent shell actions cannot bypass the Safe Executor through supported ODIN paths.
- High-risk operations require explicit authorization.
- Every governed operation receives an audit record.
- Dry-run/action-plan inspection is available for supported destructive workflows.
- Policies are testable without invoking real destructive operations.

---

## Phase 2 — Project Integrity & Recovery

**Goal:** Prevent a misplaced/deleted file from silently destroying a working project.

### Components

- project manifest
- critical-file registry
- pre-change checkpoints
- file hashing where appropriate
- structural change detection
- quarantine/trash workflow
- restore operation
- transaction journal
- crash-safe state writes

### Acceptance criteria

- ODIN can detect deletion/movement of registered critical files.
- Supported destructive project operations create a recoverable checkpoint first.
- Interrupted metadata writes do not leave project state silently corrupted.
- ODIN can explain what changed between checkpoint and current state.
- A recovery test restores a deliberately damaged test project.

---

## Phase 3 — Persistent State & Resume

**Goal:** ODIN and its managed workflows survive terminal/app/machine interruptions without starting from zero.

### Persist

- project registry
- active project
- agent assignments
- task status
- last safe checkpoint
- approvals relevant to resumable operations
- operation journal
- dependency state
- recent alerts
- recovery metadata

### Acceptance criteria

- Restarting ODIN restores registered projects and agent assignments.
- Interrupted governed tasks are marked accurately as interrupted/pending/failed rather than assumed complete.
- ODIN can show a concise resume report.
- Recovery never blindly re-executes a destructive action.

---

## Phase 4 — Intelligent System Guardian

**Goal:** Replace simple thresholds with contextual system-health detection.

### Observe

- CPU history
- memory growth
- disk utilization
- disk-write velocity
- filesystem churn
- process duration
- child-process growth
- project/process attribution when possible

### Runaway detector

Use sustained behavior and multiple signals instead of treating a momentary CPU spike as an infinite loop.

### Acceptance criteria

- Normal short CPU bursts do not automatically trigger intervention.
- Sustained abnormal CPU/memory/disk behavior produces an explainable alert.
- ODIN identifies the responsible process where OS permissions permit.
- Pause/terminate actions remain approval-controlled according to policy.
- Disk-growth alerts report rate and likely source where determinable.

---

## Phase 5 — Intent Engine & Conversational Workflows

**Goal:** Make ODIN usable through natural English/Bangla while preserving deterministic execution.

### Pipeline

```text
User language
   ↓
Intent interpretation
   ↓
Structured ODIN action
   ↓
Validation
   ↓
Policy / Risk
   ↓
Execution
```

The LLM must not directly convert unrestricted prose into ungoverned shell execution.

### Example

`create a new project`

becomes a structured project-creation workflow that can ask for location, name, template, permissions, agents, and dependency setup.

### Acceptance criteria

- English and Bangla can trigger the same structured actions.
- Ambiguous destructive requests require clarification.
- Parsed intents can be inspected/logged.
- Deterministic handlers remain responsible for system mutation.
- A local-model path is supported for suitable intent workloads.

---

## Phase 6 — Project & Dependency Intelligence

**Goal:** Make ODIN the reliable lifecycle manager for development projects.

### Capabilities

- create
- register existing project
- list/search
- health/status
- archive
- protected delete
- combine/merge planning
- templates
- dependency detection
- dependency installation
- dependency health
- environment awareness
- project activity tracking

### Acceptance criteria

- Python and Node projects can be recognized without destructive probing.
- Environment-specific dependency actions are scoped to the project by default.
- ODIN explains planned dependency changes before high-impact installation.
- Project deletion is recoverable or explicitly irreversible with strong confirmation.

---

## Phase 7 — Agent Control Plane

**Goal:** Standardize how ODIN discovers, authorizes, invokes, monitors, and revokes agents.

### Agent manifest

Each adapter should declare identity, capabilities, executable/connection requirements, filesystem scope, shell needs, network needs, supported operations, and health-check mechanism.

### Core adapters

- Claude
- Gemini
- existing template adapter

Additional adapters are added without coupling their internals to ODIN core.

### Acceptance criteria

- Agents are dynamically discoverable.
- Missing agent executables fail gracefully.
- Permissions can differ per agent and project.
- An agent can be disabled/revoked without deleting it.
- Agent activity is attributable in the audit ledger.

---

## Phase 8 — Asset & Multimodal Pipeline

**Goal:** Safely attach development artifacts to projects and route them to appropriate capabilities.

### Candidate inputs

- Markdown/text
- source code
- JSON/YAML
- PDF
- DOCX
- spreadsheets
- presentations
- images
- audio
- archives with safe inspection rules

### Pipeline

```text
Ingest → classify → validate → register → authorize → analyze/store/route
```

### Acceptance criteria

- Assets are associated with an explicit project.
- File metadata is indexed without silently executing file content.
- Unsupported formats fail safely.
- Routing decisions are inspectable.
- Archive extraction is governed and protected against unsafe paths/resource explosions.

---

## Phase 9 — Voice Interface

**Goal:** Add voice as another input/output surface, not another execution architecture.

### Requirements

- English speech input
- Bangla speech input
- shared Intent Engine
- clear recording state
- local speech option where practical
- optional spoken responses

### Acceptance criteria

- Voice and typed equivalents resolve to the same structured ODIN actions.
- Destructive actions cannot bypass confirmation because they originated from voice.
- Failed transcription never silently becomes a destructive action.

---

## Phase 10 — Native ODIN macOS Application

**Goal:** Provide a protected visual control surface around ODIN's existing core.

### Primary surfaces

- embedded/controlled terminal
- conversation/input bar with voice control
- project navigator
- agent status/control
- Guardian status
- CPU/memory/disk/process health
- alerts
- audit/history
- checkpoint/recovery UI
- drag/drop asset ingestion
- permission/approval dialogs

### macOS integration

Use supported macOS mechanisms for settings navigation, notifications, authentication, process inspection, and permissions. OS authorization boundaries must not be represented as if a project-folder permission substitutes for macOS TCC/privilege controls.

### Acceptance criteria

- App communicates with the ODIN core through a defined interface.
- Closing/reopening the UI does not destroy ODIN state.
- Critical approvals clearly show action, scope, agent, target, and consequences.
- Terminal actions remain subject to Guardian policies when executed through governed ODIN workflows.

---

## Phase 11 — Production Hardening

**Goal:** Qualify V2 for release rather than merely feature completion.

### Required verification

- unit tests
- integration tests
- permission boundary tests
- destructive-operation simulations
- recovery tests
- daemon restart tests
- app restart tests
- machine-reboot recovery tests where practical
- malformed metadata tests
- corrupted checkpoint tests
- runaway-process simulations
- disk-pressure simulations
- agent failure tests
- local-model unavailable tests
- network-unavailable tests
- English/Bangla intent tests
- dependency installation tests
- upgrade/migration tests

### Release gates

- No known path through supported ODIN interfaces bypasses high-risk authorization policy.
- Recovery tests pass for defined supported failure scenarios.
- V1 project metadata has a documented migration path.
- Logging excludes secrets by design.
- Documentation distinguishes implemented, experimental, and deferred functionality.
- Fresh-install and upgrade-install procedures both pass.

---

# 6. Deferred Ecosystem Roadmap

After V2 core stability:

## Distribution
- remote/mobile companion
- API gateway
- controlled remote administration

## Collaboration
- team workspaces
- role-based collaboration
- shared project activity

## Extensibility
- richer plugin SDK
- trusted plugin distribution
- community adapters/templates

## Enterprise
- container deployment where appropriate
- scalable services where architecture requires them
- centralized policy/audit management

These must not delay Guardian, recovery, persistence, and safe agent execution.

---

# 7. Production Definition of Done

ODIN V2 is not production-ready merely because every UI screen exists.

V2 is production-ready when:

1. V1 projects can be migrated safely.
2. ODIN survives ordinary restart/interruption scenarios with accurate state.
3. Agents cannot silently gain capabilities beyond policy through supported ODIN interfaces.
4. High-risk actions are visible and authorization-controlled.
5. Critical project damage can be detected and supported changes recovered.
6. Resource monitoring produces explainable, useful alerts rather than simple noisy thresholds.
7. English/Bangla natural-language and voice input resolve through the same governed action system.
8. The native app is a client/control surface for a durable ODIN core rather than the sole holder of state.
9. Audit records make agent/system actions attributable.
10. Tests demonstrate the above behaviors.

---

# 8. Development Order

```text
V1 Baseline
    ↓
Guardian
    ↓
Integrity + Recovery
    ↓
Persistence
    ↓
System Guardian
    ↓
Intent Engine
    ↓
Project/Dependency Intelligence
    ↓
Agent Control Plane
    ↓
Assets
    ↓
Voice
    ↓
Native App
    ↓
Production Hardening
    ↓
ODIN V2 Release Candidate
```

Safety and recoverability deliberately precede increased autonomy.

---

# 9. Resume Protocol

To make future continuation straightforward, each completed phase should record:

- phase status
- implemented components
- files changed
- tests executed and results
- unresolved issues
- migration implications
- security implications
- next dependency
- last known-good commit

A future development session should begin by reading this roadmap, the latest change/session record, and the current branch state before making changes.

---

# 10. Scope Guard

ODIN V2 is an evolution of **ODIN — The Allfather**.

It is not:

- ODIN-TERMINATOR
- RAAL Civilization
- the Weaver Engine
- a replacement architecture unrelated to V1

Cross-project integration may be designed later through explicit interfaces, but their internal architectures must not be silently merged into ODIN-Allfather.

---

**Status:** V2 roadmap established; implementation should proceed phase-by-phase with verification gates.