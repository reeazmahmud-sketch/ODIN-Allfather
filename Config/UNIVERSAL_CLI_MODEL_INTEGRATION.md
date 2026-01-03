# Universal CLI Agent Model Integration System

## Overview

This is a **universal, reusable AI model integration framework** for ALL CLI-based agents - current and future. Any agent built with a CLI interface can use this system to support multiple AI models.

## Applies To

- ✅ ODIN (The Allfather)
- ✅ TERMINATOR (Multi-agent system)
- ✅ Claude Code CLI integrations
- ✅ Gemini CLI integrations
- ✅ ANY future CLI agent you build

## Universal Architecture

```
┌─────────────────────────────────────────────────────┐
│         Universal Model Manager (Shared)            │
│  - Model Registry                                   │
│  - API Key Management                               │
│  - Selection Logic                                  │
│  - Cost Tracking                                    │
└─────────────────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
    ┌────────┐    ┌──────────┐    ┌──────────┐
    │  ODIN  │    │TERMINATOR│    │Future CLI│
    │  CLI   │    │   CLI    │    │  Agent   │
    └────────┘    └──────────┘    └──────────┘
```

## Standard Commands (All Agents)

Every CLI agent gets these commands automatically:

```bash
# Works in ANY agent CLI:
agent_name /models              # List available models
agent_name /models select       # Interactive selection
agent_name /models set <name>   # Set specific model
agent_name /models status       # Current configuration
agent_name /models test <msg>   # Test current model
```

### Examples Across Different Agents:

```bash
# ODIN
odin /models select
odin /models set gemini_flash

# TERMINATOR
terminator /models select
terminator /models set claude_sonnet

# Future Agent
my_agent /models select
my_agent /models set ollama
```

## Integration Methods

### Method 1: Import Universal Module

```python
# In any agent CLI script:
from universal_model_manager import UniversalModelManager

class MyAgentCLI:
    def __init__(self):
        self.model_manager = UniversalModelManager()

    def handle_command(self, command):
        if command.startswith('/models'):
            return self.model_manager.handle_models_command(command)
        # ... other commands
```

### Method 2: Inherit Base CLI Class

```python
from universal_cli_base import UniversalCLIBase

class MyAgentCLI(UniversalCLIBase):
    def __init__(self):
        super().__init__()
        # Automatically gets /models commands
```

### Method 3: Standalone Configuration

```yaml
# Any agent can reference universal config
include: /Terminal-CLI/Odin/Odin/Config/models-config.yaml

# Agent-specific overrides
agent_name: "MyAgent"
preferred_models:
  - gemini_flash
  - ollama
```

## Shared Model Registry

All agents share the same model registry:

**Location**: `/Terminal-CLI/Odin/Odin/Config/models-config.yaml`

**Benefits**:
- Single source of truth
- Update once, affects all agents
- Consistent pricing/limits
- Centralized API key management

## User Experience Flow

### Step 1: First-time Setup (Any Agent)

```bash
$ my_agent /models select

╔════════════════════════════════════════════════════╗
║       AI Model Selection - First Time Setup        ║
╚════════════════════════════════════════════════════╝

Choose your preferred integration method:

1. 🏠 Local LLM (Free, Private, Offline)
   - Ollama, LM Studio
   - No internet needed
   - Complete privacy

2. ☁️  Cloud Free Tier (Fast, No Cost)
   - Gemini 2.5 Flash ⭐ Recommended
   - Claude 3.5 Haiku
   - 1500 requests/day

3. 💳 Cloud Paid Tier (Premium)
   - Best performance
   - Usage costs apply

4. 🔧 Local Agents (Custom)
   - Specialized agents
   - Domain-specific

Selection [1-4]: 2

Selected: Cloud Free Tier

Available models:
1. Gemini 2.5 Flash (Google) ⭐ Recommended
   - Multimodal support
   - Google Workspace integration
   - 15 req/min, 1500 req/day

2. Claude 3.5 Haiku (Anthropic)
   - Fast responses
   - Excellent for code

Selection [1-2]: 1

✓ Model set to: Gemini 2.5 Flash

API Key Setup:
You need a Google API key (free at makersuite.google.com)

Options:
1. Enter API key now (saved securely)
2. Set environment variable: export GOOGLE_API_KEY="..."
3. Skip for now (configure later)

Selection [1-3]: 1

Enter API key: [hidden input]
✓ API key saved securely

✓ Configuration complete!
✓ All CLI agents can now use Gemini 2.5 Flash
```

### Step 2: Subsequent Use

```bash
$ any_agent /models status

Current Configuration:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Model:     Gemini 2.5 Flash
Type:      Cloud Free Tier
Provider:  Google
Status:    ✓ Active
API Key:   ✓ Configured
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Usage Today:
  Requests: 45 / 1500
  Cost:     $0.00

Fallback: Ollama (llama3)
Strategy: cost_optimized
```

## Universal API Key Storage

All agents share API keys from one secure location:

```bash
~/.odin/api-keys/
  ├── google.key       # Encrypted
  ├── anthropic.key    # Encrypted
  ├── openai.key       # Encrypted
  └── config.json      # Key metadata

# Or use environment variables (all agents respect these):
export GOOGLE_API_KEY="..."
export ANTHROPIC_API_KEY="..."
export OPENAI_API_KEY="..."
```

## Model Selection Strategies (Universal)

All agents support these strategies:

1. **cost_optimized** (Default)
   - Use free tier → fallback to local
   - Best for: Most users

2. **local_first**
   - Prefer local → cloud backup
   - Best for: Privacy

3. **cloud_first**
   - Cloud free → cloud paid → local
   - Best for: Performance

4. **performance**
   - Best available (paid tier)
   - Best for: Production

5. **manual**
   - User selects per session
   - Best for: Advanced users

```bash
# Set strategy (affects all agents):
any_agent /models strategy cost_optimized

# Or per-agent override:
my_agent /models strategy local_first --agent-only
```

## Adding New Models (Universal)

To add a new AI model that ALL agents can use:

```yaml
# Edit: /Terminal-CLI/Odin/Odin/Config/models-config.yaml

models:
  cloud_free:
    new_model_name:
      name: "New AI Model"
      type: "cloud"
      provider: "provider_name"
      endpoint: "https://api.example.com/v1"
      api_key_env: "NEW_MODEL_KEY"
      cost: "free"
      features:
        - "feature1"
        - "feature2"
```

**Result**: ALL CLI agents immediately see the new model!

```bash
odin /models list              # Shows new model
terminator /models list        # Shows new model
my_agent /models list          # Shows new model
```

## Future Agent Integration Checklist

When creating a NEW CLI agent:

- [ ] Import `UniversalModelManager` OR inherit `UniversalCLIBase`
- [ ] Agent automatically gets `/models` commands
- [ ] Agent uses shared model registry
- [ ] Agent respects user's model preferences
- [ ] No additional configuration needed!

**That's it!** The agent inherits the entire model system.

## Code Template for New Agents

```python
#!/usr/bin/env python3
"""
New CLI Agent with Universal Model Integration
"""

from universal_model_manager import UniversalModelManager

class NewAgentCLI:
    def __init__(self):
        # This gives you the entire model system:
        self.model_manager = UniversalModelManager()

    def run(self):
        while True:
            user_input = input(f"{self.name}> ")

            # Handle universal /models commands
            if user_input.startswith('/models'):
                result = self.model_manager.handle_models_command(user_input)
                print(result)
                continue

            # Get AI response using current model
            response = self.model_manager.query(user_input)
            print(response)

if __name__ == "__main__":
    agent = NewAgentCLI()
    agent.run()
```

## Benefits of Universal System

### For Users:
- ✅ Consistent experience across all agents
- ✅ Configure once, use everywhere
- ✅ Single API key storage
- ✅ Unified cost tracking

### For Developers:
- ✅ No need to implement model selection per agent
- ✅ Automatic updates when new models added
- ✅ Shared testing and validation
- ✅ Less code duplication

### For Future:
- ✅ Easy to add new models
- ✅ Easy to add new agents
- ✅ Centralized maintenance
- ✅ Consistent upgrades

## Implementation Files

```
Terminal-CLI/Odin/Odin/
├── Config/
│   ├── models-config.yaml          # Universal model registry
│   ├── user-preferences.yaml       # User settings (shared)
│   └── UNIVERSAL_CLI_MODEL_INTEGRATION.md
│
├── universal_model_manager.py      # Core module (to be created)
├── universal_cli_base.py           # Base class (to be created)
│
└── Agents/
    ├── template_agent/             # Template for new agents
    └── [any agent]/                # All agents use universal system
```

## Next Steps to Implement

1. Create `universal_model_manager.py` - Core model management
2. Create `universal_cli_base.py` - Base CLI class
3. Add `/models` command handler to ODIN
4. Update TERMINATOR to use universal system
5. Create integration examples
6. Document API for future agents

## Summary

This universal system ensures that:

1. **Every CLI agent** (current and future) has the same model selection capabilities
2. **Users configure once** - settings apply to all agents
3. **Developers integrate easily** - just import the module
4. **New models benefit everyone** - add once, available everywhere
5. **Consistent experience** - same commands, same behavior

**The model integration system is now UNIVERSAL and FUTURE-PROOF!** 🚀
