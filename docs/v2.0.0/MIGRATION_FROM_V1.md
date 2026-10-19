# ODIN — The Allfather v2.0.0
## Migration from v1

**Principle:** Upgrade ODIN; do not replace ODIN.

---

## 1. Migration Objective

ODIN v2 must allow an existing v1 installation and its projects to evolve without forcing the user to rebuild their workspaces or abandon ODIN's established CLI and agent concepts.

The migration process must be reversible until the v2 migration is explicitly accepted.

---

## 2. Preserve

The migration should preserve:

- existing `Workspaces/` projects;
- project source and asset files;
- `.odin-meta.yaml` metadata;
- existing agent folders and adapters where compatible;
- English and Bangla interaction expectations;
- local model preferences;
- user configuration that passes v2 validation;
- historical logs as legacy records.

---

## 3. Upgrade

v1 concepts should be upgraded as follows:

| v1 | v2 Evolution |
|---|---|
| Hard-coded ODIN path | Root discovery / `ODIN_HOME` |
| Plain command strings | Versioned structured IPC |
| Global in-memory agent registry | Validated agent registry + lifecycle |
| `.odin-meta.yaml` only | Metadata + durable state database |
| Basic permissions fields | Enforced capability policy |
| Text action log | Structured audit journal |
| Threshold monitor | Guardian incident system |
| Direct metadata writes | Atomic/transactional state changes |
| Conceptual workspace isolation | Enforced workspace boundary |
| Agent placeholders | Capability-declared adapters |
| Model YAML registry | Provider adapter layer |
| Manual recovery | Checkpoint/restore workflow |

---

## 4. Migration Safety Sequence

```text
Detect v1
   |
   v
Validate installation
   |
   v
Create migration backup
   |
   v
Inventory projects/config/agents
   |
   v
Validate and normalize metadata
   |
   v
Initialize v2 state store
   |
   v
Import project records
   |
   v
Build integrity manifests
   |
   v
Validate agent compatibility
   |
   v
Run health checks
   |
   +--> failure -> rollback
   |
   v
Mark migration candidate
   |
   v
User accepts migration
```

No migration step should delete the v1 backup.

---

## 5. Project Metadata

A v1 `.odin-meta.yaml` should be imported rather than discarded.

Existing fields such as project name, root, agents, dependencies, permissions, assets, created time, and last-active time should be normalized into the v2 schema.

Unknown fields should be retained when possible and reported rather than silently dropped.

---

## 6. Agent Compatibility

A v1 agent adapter may initially run through a compatibility layer.

Compatibility status should be one of:

- `native-v2`
- `compatible-v1`
- `restricted-v1`
- `incompatible`

Legacy agents must not automatically receive new v2 privileges.

---

## 7. CLI Compatibility

Existing common commands should remain familiar:

```text
odin serve
odin create
odin list
odin integrate
odin status
odin help
odin stop
```

v1 commands advertised by the shell but not implemented by the daemon must be reconciled. v2 documentation and runtime command discovery must share one authoritative command registry.

---

## 8. Logs

Existing `Logs/actions.log` should remain available as historical v1 data.

v2 should not rewrite it into fabricated structured events. Instead, mark it as a legacy log and begin structured audit events from the v2 migration point forward.

---

## 9. Configuration

Existing configuration should pass through validation and migration.

Secrets must be removed from ordinary configuration if discovered and moved to the supported secret mechanism with explicit user approval.

Model/provider names that no longer exist should be reported and require a replacement selection rather than silently switching providers.

---

## 10. Rollback

Before migration ODIN should record:

- v1 version;
- source root;
- configuration snapshot;
- project metadata snapshot;
- agent inventory;
- integrity hashes;
- migration ID.

If migration validation fails, ODIN should restore the pre-migration state and produce a migration report.

---

## 11. Migration Success Criteria

Migration is successful only when:

- all discovered projects are accounted for;
- no user project file is silently lost;
- metadata validates;
- ODIN starts successfully;
- workspace access tests pass;
- agent compatibility is known;
- Guardian health check passes;
- v2 state store passes integrity checks;
- rollback snapshot remains available;
- migration report is written.

---

## 12. Core Rule

> v2 must understand where it came from.

ODIN v1 is not disposable scaffolding. Its projects, CLI conventions, agents, multilingual behavior, monitoring concept, model configuration, and user workflow are the migration baseline for ODIN v2.
