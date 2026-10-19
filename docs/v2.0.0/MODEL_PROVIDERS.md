# ODIN — The Allfather v2.0.0
## Model and Provider Architecture

**Date:** 19-10-2026  
**Status:** v2 architecture specification

---

## 1. Evolution from v1

ODIN v1 introduced `Config/models-config.yaml` with local and cloud model concepts, including Ollama, LM Studio, provider endpoints, fallback selection, and cost/performance strategies.

v2 preserves that intent but moves provider behavior behind a stable adapter interface. ODIN core must not depend on hard-coded model names or one vendor.

---

## 2. Provider Contract

Conceptual interface:

```python
class ModelProvider:
    def provider_id(self): ...
    def health_check(self): ...
    def list_models(self): ...
    def capabilities(self, model): ...
    def generate(self, request): ...
    def stream(self, request): ...
    def cancel(self, request_id): ...
```

Provider adapters normalize differences between local runtimes, cloud APIs, and CLI-backed models.

---

## 3. Provider Categories

ODIN may support:

- local runtimes such as Ollama;
- local OpenAI-compatible servers such as LM Studio;
- cloud API providers;
- installed AI CLIs;
- future custom providers.

Provider availability is discovered and verified at runtime. Documentation must not imply a provider works merely because configuration exists.

---

## 4. Model Selection

v1 strategies evolve into policy-driven routing:

```text
manual
local_first
privacy_first
cost_optimized
performance
availability
```

Selection should consider:

- task capability requirements;
- user preference;
- privacy policy;
- provider health;
- local resource pressure;
- context requirements;
- cost policy;
- network availability.

---

## 5. Local-First Behavior

ODIN should remain fully useful without cloud models where the requested capability is available locally.

Local provider health should include endpoint reachability, model availability, resource requirements, and request cancellation behavior.

---

## 6. Secrets

Provider credentials must be referenced, not stored directly in tracked configuration.

Supported secret sources may include environment variables and operating-system credential storage.

Secrets must be redacted from logs, exceptions, diagnostics, and exported support bundles.

---

## 7. Fallback

Fallback must be explicit and capability-safe.

ODIN must not silently send locally intended/private data to a cloud provider merely because a local model failed.

Cloud fallback from a local/privacy policy therefore requires policy permission or user approval.

---

## 8. Provider Status

Recommended CLI:

```text
odin models
odin models status
odin models local
odin models provider <name>
odin models select <model>
```

Status should distinguish configured, discovered, healthy, unavailable, unauthorized, rate-limited, and incompatible.

---

## 9. Invariant

> Models provide intelligence; ODIN controls routing, privacy, permissions, task state, and execution authority.
