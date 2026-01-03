# ODIN Universal Configuration

This directory contains configuration files that are **shared across ALL CLI agents**.

## Files

### `models-config.yaml`
Universal AI model registry. Used by:
- ODIN
- TERMINATOR  
- Any future CLI agent

### `user-preferences.yaml`
User's personal settings for model selection and integration preferences.

### `UNIVERSAL_CLI_MODEL_INTEGRATION.md`
Complete documentation on how the universal model system works across all agents.

## Key Principle

**Configure once, use everywhere.**

When you set your preferred AI model and API keys here, ALL your CLI agents automatically use them.

## Quick Start

1. Choose your model:
   ```bash
   odin /models select
   ```

2. Settings apply to ALL agents:
   ```bash
   odin /models status        # Shows config
   terminator /models status  # Shows SAME config
   any_agent /models status   # Shows SAME config
   ```

3. Add new models here - ALL agents get them immediately!

## For Developers

When creating a new CLI agent:
1. Import `UniversalModelManager`
2. Agent automatically inherits ALL model capabilities
3. No additional configuration needed

See `UNIVERSAL_CLI_MODEL_INTEGRATION.md` for details.
