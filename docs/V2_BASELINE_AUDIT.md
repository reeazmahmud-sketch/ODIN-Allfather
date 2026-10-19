# ODIN V2 — V1 Baseline Audit

**Project:** ODIN — The Allfather
**Audit Date:** 19-10-2026
**Source Baseline:** V1 `main`
**Development Branch:** `odin-v2`
**Purpose:** Phase 0 preservation and verification before V2 runtime changes

## Executive finding

ODIN V1 is a real working foundation, not an empty prototype. Its strongest implemented pieces are the Python daemon, Unix-socket command path, workspace creation, YAML project metadata, dynamic agent discovery, Claude/Gemini adapters, multilingual keyword routing, logging, and basic resource monitoring.

However, repository documentation is ahead of implementation in several areas. V2 must preserve the working core while replacing placeholders and closing safety/recovery gaps rather than performing a rewrite.

## Baseline classification

### KEEP — implemented foundation

- Python daemon and long-running service model.
- Unix socket IPC.
- Workspace/project creation with `src/`, `assets/`, and `.odin-meta.yaml`.
- Project listing.
- Dynamic agent discovery through `Agents/<agent>/adapter.py`.
- Claude and Gemini adapter concept plus reusable template-agent contract.
- Agent integration recorded in project metadata.
- English/Bangla keyword mapping.
- CPU, memory, disk and process monitoring using `psutil`.
- Action logging.
- YAML configuration/metadata approach.
- Portable installer/configuration concepts.

### REPAIR — partial or inconsistent

- Parser recognizes delete/install intent but the daemon handler map does not provide equivalent complete implementations.
- Resource monitoring is threshold-oriented and needs sustained/anomaly-aware detection.
- Agent notification exists but lacks a formal capability and permission contract.
- Project metadata exists but is not yet a durable transactional recovery/state system.
- Sandboxing is primarily workspace organization; it must not be treated as an OS security boundary.
- Documentation and runtime behavior need a single verified command/capability matrix.
- Hard-coded ODIN base-path assumptions need configuration/migration handling.

### BUILD — missing production layers

- Guardian policy engine.
- Command/action risk classifier.
- Approval gate for risky/destructive actions.
- Safe executor with dry-run/planning support.
- Project checkpoints/snapshots and rollback.
- File integrity manifests and protected-file detection.
- Crash/session recovery and resumable task state.
- Historical resource telemetry and runaway-process scoring.
- Dependency detection/install/repair/prune workflow.
- Conversational intent engine beyond keyword matching.
- Formal agent capability manifests and scoped permissions.
- Production multimodal asset ingestion.
- Production English/Bangla voice pipeline.
- Production native macOS ODIN application/dashboard.

### PLACEHOLDER / DOCUMENTED-AHEAD-OF-CODE

- Dashboard files are currently minimal scaffolding rather than a production UI.
- Voice is roadmap-level rather than a verified production subsystem.
- Mobile, team collaboration, marketplace/plugin ecosystem, Kubernetes and enterprise distribution are future scope rather than V1 baseline requirements.

## Important implementation observations

### Daemon

The daemon is the most important V1 asset and should be evolved behind stable interfaces. It already creates required directories, discovers agent adapters, accepts socket commands, writes project metadata, reports status, and runs a monitoring thread.

### Command routing

V1's English/Bangla keyword map proves the multilingual concept, but keyword routing should become the deterministic fallback underneath the V2 intent engine. Existing command semantics should remain available for backward compatibility.

### Project isolation

`Workspaces/<project>/` gives ODIN useful organizational isolation, but a directory boundary alone is not a security sandbox. V2 documentation and implementation must use precise language and enforce permissions through Guardian + Safe Executor.

### Monitoring

V1 provides useful telemetry but threshold spikes alone cannot identify an infinite loop or runaway recursive operation. V2 should retain the measurements while adding duration, rate-of-change, filesystem churn, child-process growth, and historical context.

### Agents

The adapter architecture is worth retaining. V2 should add manifests/capabilities/policies around adapters instead of replacing them. This permits Claude, Gemini and future agents to remain modular while ODIN becomes the authorization/control layer.

### Dashboard

The current Dashboard directory should be treated as a reserved interface surface, not evidence of a completed application. Native-app work must therefore be planned as BUILD, with the existing concept preserved where useful.

## Phase 0 preservation rules

1. Do not modify V1 `main` during V2 development.
2. Do not introduce the Weaver Engine into ODIN-Allfather.
3. Preserve existing CLI command semantics unless a migration path is documented.
4. Preserve readable V1 project metadata and provide migration when the schema evolves.
5. Do not call workspace folders an OS-level sandbox without an actual enforcement boundary.
6. Add tests before replacing daemon behavior.
7. Safety-critical execution must become deterministic and policy-controlled.
8. AI interpretation must not directly bypass the Safe Executor.
9. Every destructive action must be auditable.
10. Every phase must leave a resumable checkpoint in documentation and version control.

## Phase 0 exit criteria

Phase 0 is considered complete when:

- [x] V1 roadmap and future-update documents reviewed.
- [x] V1 version history reviewed.
- [x] Core daemon behavior reviewed.
- [x] Agent directory baseline identified.
- [x] Dashboard baseline identified.
- [x] KEEP / REPAIR / BUILD / DEFER model established.
- [x] V2 development isolated on `odin-v2`.
- [x] V2 implementation roadmap committed.
- [x] Baseline audit committed.
- [ ] Automated regression tests capture critical V1 behavior.
- [ ] Configuration/path assumptions are catalogued in a machine-readable compatibility manifest.

The final two items are intentionally carried into the first engineering task before Guardian implementation. This prevents us from changing the runtime before its existing behavior is protected by tests.

## Next engineering task

Create a V1 compatibility test suite and compatibility manifest covering:

1. project creation and metadata,
2. project listing,
3. agent discovery,
4. agent integration,
5. English/Bangla command parsing,
6. status/resource reporting,
7. logging,
8. socket command/response behavior,
9. configuration and base-path resolution.

Only after that baseline is protected should V2 Guardian execution paths begin replacing direct operations.
