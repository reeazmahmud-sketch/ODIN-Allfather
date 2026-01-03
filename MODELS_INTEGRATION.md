# ODIN AI Model Integration Guide

## Overview

ODIN supports multiple AI models across different tiers and deployment methods. Users can choose between local models, cloud-based free tier models, and premium paid models based on their needs.

## Command: `/models`

The `/models` command allows users to view, select, and switch between available AI models.

### Usage

```bash
odin /models                    # Show all available models
odin /models list               # List models with details
odin /models select             # Interactive model selection
odin /models set gemini_flash   # Set specific model
odin /models status             # Show current model and configuration
```

### Model Categories

#### 1. Local LLM Models
**Free, Private, No Internet Required**

- **Ollama** - Run models like Llama 3, Mistral, CodeLlama locally
  - Setup: `ollama pull llama3`
  - Endpoint: http://localhost:11434
  - Best for: Privacy, offline work, unlimited usage

- **LM Studio** - Desktop application for local LLM
  - Setup: Download from lmstudio.ai
  - Endpoint: http://localhost:1234
  - Best for: Easy local model management

#### 2. Cloud Free Tier Models
**Fast, No Cost (with limits)**

- **Gemini 2.5 Flash** ⭐ **Recommended Default**
  - Provider: Google
  - Features: Multimodal, fast responses, Google Workspace integration
  - Rate Limits: 15 req/min, 1500 req/day
  - Setup: Get free API key from https://makersuite.google.com/

- **Claude 3.5 Haiku**
  - Provider: Anthropic
  - Features: Fast, excellent for code
  - Setup: Get API key from https://console.anthropic.com

#### 3. Cloud Paid Tier Models
**Premium Performance**

- **Gemini 2.0 Pro**
  - Advanced reasoning, long context
  - Cost: $0.00025 per 1K input tokens

- **Claude 3.5 Sonnet**
  - Best-in-class code generation
  - Cost: $3 per 1M input tokens

- **GPT-4 Turbo**
  - Advanced reasoning, vision
  - Cost: $10 per 1M input tokens

## Integration Modes

### Mode 1: Local LLM
```bash
odin /models select
> Choose integration mode:
  1. Local LLM (Recommended for privacy)
  2. Local Agents
  3. Cloud Free Tier (Recommended for speed)
  4. Cloud Paid Tier

> Selection: 1

> Available local models:
  1. Ollama - llama3
  2. Ollama - codellama
  3. LM Studio - custom

> Selection: 1

✓ Model set to: Ollama llama3 (local)
```

### Mode 2: Cloud Free Tier (Default)
```bash
odin /models select
> Selection: 3 (Cloud Free Tier)

> Available models:
  1. Gemini 2.5 Flash (Google) ⭐ Recommended
  2. Claude 3.5 Haiku (Anthropic)

> Selection: 1

> API Key Setup:
  Enter your Google API key (or press Enter to skip):
  [Hidden input or use: export GOOGLE_API_KEY="your-key"]

✓ Model set to: Gemini 2.5 Flash (cloud free)
✓ Features: Multimodal, Google Workspace integration
✓ Rate limits: 15/min, 1500/day
```

### Mode 3: Cloud Paid Tier
```bash
odin /models select
> Selection: 4 (Cloud Paid Tier)

⚠️  Warning: This mode incurs usage costs.

> Available models:
  1. Gemini 2.0 Pro - $0.00025/1K tokens
  2. Claude 3.5 Sonnet - $3/1M tokens
  3. GPT-4 Turbo - $10/1M tokens

> Selection: 2

> Cost estimate for typical usage:
  - 100 requests/day: ~$0.50/day
  - Heavy usage: ~$2-5/day

> Confirm? (y/n): y

✓ Model set to: Claude 3.5 Sonnet (cloud paid)
```

## Configuration Strategy

### Selection Strategies

1. **cost_optimized** (Default)
   - Use: Gemini Flash (free) → Ollama (local fallback)
   - Best for: Most users, balanced cost and performance

2. **local_first**
   - Use: Ollama → Gemini Flash (cloud fallback)
   - Best for: Privacy-focused users, offline work

3. **cloud_first**
   - Use: Gemini Flash → Claude Haiku → Ollama
   - Best for: Speed and latest features

4. **performance**
   - Use: Claude Sonnet → Gemini Pro → GPT-4
   - Best for: Professional use, best results

5. **manual**
   - User explicitly selects model for each session
   - Best for: Advanced users, specific use cases

### Setting Strategy

```bash
odin /models strategy cost_optimized
odin /models strategy local_first
odin /models strategy performance
```

## API Key Management

### Setting Up API Keys

```bash
# Google (Gemini)
export GOOGLE_API_KEY="your-google-api-key"

# Anthropic (Claude)
export ANTHROPIC_API_KEY="your-anthropic-api-key"

# OpenAI (GPT-4)
export OPENAI_API_KEY="your-openai-api-key"

# Or save to ODIN config
odin /models setkey google
> Enter API key: [hidden input]
✓ API key saved securely
```

### Getting Free API Keys

1. **Google Gemini**: https://makersuite.google.com/
   - Free tier: 1500 requests/day
   - No credit card required

2. **Anthropic Claude**: https://console.anthropic.com/
   - Free tier: $5 credit
   - Credit card required for verification

3. **OpenAI**: https://platform.openai.com/
   - $5 free credit (paid tier only)

## Future Agent Integration

Any future AI model can be added to ODIN by:

1. **Adding to `models-config.yaml`**:
```yaml
models:
  cloud_free:
    new_model:
      name: "New AI Model"
      type: "cloud"
      provider: "provider_name"
      endpoint: "https://api.example.com"
      api_key_env: "NEW_MODEL_API_KEY"
      cost: "free"
```

2. **Creating Agent Adapter**:
```bash
# Copy template
cp -r Agents/template_agent Agents/new_model

# Edit Agents/new_model/adapter.py
# Update class name to match folder name
```

3. **ODIN Auto-discovers**:
```bash
odin serve  # Automatically finds new agent
odin /models list  # Shows new model
```

## Model Switching Commands

```bash
# Quick switch
odin /models use gemini_flash
odin /models use claude_sonnet
odin /models use ollama

# View current
odin /models current

# Compare models
odin /models compare gemini_flash claude_haiku

# Test model
odin /models test gemini_flash "Write hello world in Python"
```

## Best Practices

### For Development
- Use: Local Ollama or Gemini Flash (free)
- Reason: Unlimited usage, fast iteration

### For Production
- Use: Claude Sonnet or Gemini Pro (paid)
- Reason: Best quality, reliability

### For Privacy-Sensitive Work
- Use: Local Ollama only
- Reason: Complete data privacy, no cloud

### For Cost-Conscious Users
- Use: Gemini Flash → Ollama fallback
- Reason: Free tier is generous, local backup

## Implementation Status

- [x] Model configuration structure
- [x] Basic agent templates (Claude, Gemini)
- [ ] `/models` command implementation
- [ ] Interactive model selection
- [ ] API key management
- [ ] Usage tracking and cost estimation
- [ ] Automatic fallback on rate limits
- [ ] Model comparison features

## Next Steps

To implement the full `/models` system:

1. Add model manager to daemon
2. Implement `/models` command handler
3. Add API key secure storage
4. Create interactive selection UI
5. Add usage tracking
6. Implement automatic fallback logic
