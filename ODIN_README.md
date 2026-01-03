# ODIN - The Allfather AI/Agent Orchestration System

**Complete Guide for Beginners**

---

## 📋 Table of Contents

1. [What is ODIN?](#what-is-odin)
2. [Quick Facts](#quick-facts)
3. [Why Use ODIN?](#why-use-odin)
4. [How ODIN Works (Simple Explanation)](#how-odin-works-simple-explanation)
5. [System Architecture](#system-architecture)
6. [Installation Guide](#installation-guide)
7. [Getting Started (Step by Step)](#getting-started-step-by-step)
8. [All Commands](#all-commands)
9. [Dependencies (What You Need)](#dependencies-what-you-need)
10. [Files and Folders](#files-and-folders)
11. [Code Snippets (Copy & Use)](#code-snippets-copy--use)
12. [AI Model Integration](#ai-model-integration)
13. [Troubleshooting](#troubleshooting)
14. [Moving ODIN to Another Computer](#moving-odin-to-another-computer)
15. [GitHub Upload Guide](#github-upload-guide)
16. [Credits](#credits)

---

## 🌟 What is ODIN?

**ODIN** (Orchestrated Distributed Intelligence Network) is a smart system that helps you manage multiple AI assistants from one place. Think of it as a "boss" that coordinates different AI workers (agents) to help you with your projects.

**In Simple Terms:**
- Like having a personal assistant manager
- Controls multiple AI helpers (Claude, Gemini, etc.)
- Works in your computer's terminal (command line)
- Can use AI on your computer (offline) or in the cloud (online)
- Supports both English and Bangla commands!

---

## 📊 Quick Facts

| Info | Details |
|------|---------|
| **Name** | ODIN (The Allfather) |
| **Created** | January 3, 2026 |
| **Built By** | Reeaz Mahmud with Claude AI assistance |
| **Version** | 1.0 |
| **Language** | Python 3.13+ |
| **Platform** | macOS (can be adapted for Linux/Windows) |
| **License** | Private/Personal Use |

---

## 🎯 Why Use ODIN?

### Problems ODIN Solves:

1. **Too Many AI Tools** - Instead of switching between ChatGPT, Claude, Gemini, you use one system
2. **Privacy Concerns** - Can run AI completely offline on your computer
3. **Cost Management** - Choose between free, local, or paid AI services
4. **Project Organization** - Keep your work in separate sandboxed projects
5. **Multilingual** - Use commands in English or Bangla (বাংলা)

### What You Can Do:

- ✅ Create projects with AI assistance
- ✅ Use multiple AI models (switch easily)
- ✅ Run AI locally (no internet needed)
- ✅ Monitor your computer's health (CPU, memory, disk)
- ✅ Integrate Google Workspace tools
- ✅ Add unlimited custom AI agents

---

## 🔧 How ODIN Works (Simple Explanation)

### The Restaurant Analogy:

Think of ODIN like a restaurant:

1. **You (Customer)** - Give orders through the command line
2. **ODIN Daemon (Manager)** - Takes your order and assigns tasks
3. **AI Agents (Chefs)** - Different specialists (Claude for code, Gemini for Google Docs, etc.)
4. **Projects (Tables)** - Each project has its own workspace
5. **Models (Recipes)** - Different AI models you can choose

### The Flow:

```
You type a command
    ↓
ODIN receives it
    ↓
ODIN asks the right AI agent
    ↓
Agent processes and responds
    ↓
You get the result
```

---

## 🏗️ System Architecture

### Visual Structure:

```
┌─────────────────────────────────────────────────┐
│              YOU (User)                         │
│           Terminal Commands                     │
└─────────────────┬───────────────────────────────┘
                  │
    ┌─────────────▼────────────────┐
    │    ODIN CLI (bin/odin-cli)   │
    │    Your entry point          │
    └─────────────┬────────────────┘
                  │
    ┌─────────────▼──────────────────────┐
    │  ODIN Daemon (daemon/odin_daemon.py)│
    │  - Command Router                   │
    │  - Project Manager                  │
    │  - System Monitor                   │
    │  - Agent Orchestrator               │
    └─────────────┬──────────────────────┘
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
  ┌────────┐  ┌────────┐  ┌────────┐
  │ Claude │  │ Gemini │  │Template│
  │ Agent  │  │ Agent  │  │ Agent  │
  └────────┘  └────────┘  └────────┘
      │           │           │
      └───────────┴───────────┘
                  │
      ┌───────────▼───────────┐
      │   Your Projects       │
      │   (Workspaces/)       │
      │   - TestProject       │
      │   - BanglaProject     │
      │   - YourProject       │
      └───────────────────────┘
```

### Components Explained:

1. **CLI (Command Line Interface)**
   - Where you type commands
   - Location: `bin/odin-cli`
   - Think of it as: The reception desk

2. **Daemon (Background Service)**
   - Runs in the background
   - Location: `daemon/odin_daemon.py`
   - Think of it as: The manager's office

3. **Agents (AI Workers)**
   - Different AI specialists
   - Location: `Agents/*/adapter.py`
   - Think of it as: The specialist team

4. **Workspaces (Projects)**
   - Your project folders
   - Location: `Workspaces/*/`
   - Think of it as: Individual desks/tables

5. **Config (Settings)**
   - System settings and preferences
   - Location: `Config/*.yaml`
   - Think of it as: The rule book

---

## 📥 Installation Guide

### Step 1: Check Requirements

Open Terminal and check:

```bash
# Check Python version (need 3.13+)
python3 --version

# Check if you have Homebrew (macOS package manager)
brew --version
```

### Step 2: Install Dependencies

```bash
# Install socat (for communication)
brew install socat

# Install Python packages
pip3 install pyyaml psutil
```

### Step 3: Make ODIN Executable

```bash
# Navigate to ODIN
cd ~/Terminal-CLI/Odin/Odin

# Make CLI executable
chmod +x bin/odin-cli
```

### Step 4: Add to Shell (Optional but Recommended)

Add this to your `~/.zshrc` file:

```bash
# ODIN - The Allfather
odin() {
    bash "$HOME/Terminal-CLI/Odin/Odin/bin/odin-cli" "$@"
}
```

Then reload:
```bash
source ~/.zshrc
```

---

## 🚀 Getting Started (Step by Step)

### Your First 5 Minutes with ODIN:

#### Step 1: Start ODIN

```bash
# Open Terminal and type:
odin serve

# You should see:
# 🚀 Starting ODIN - The Allfather...
# ✓ ODIN daemon started
```

#### Step 2: Create Your First Project

```bash
# In another Terminal window:
odin create MyFirstProject

# You should see:
# ✓ Project 'MyFirstProject' created successfully
```

#### Step 3: List Your Projects

```bash
odin list

# You should see:
# Found 1 project(s):
#   - MyFirstProject
```

#### Step 4: Add an AI Agent to Your Project

```bash
odin integrate claude MyFirstProject

# You should see:
# ✓ Agent 'claude' integrated into 'MyFirstProject'
```

#### Step 5: Check System Status

```bash
odin status

# You should see system info, agents, and resources
```

**Congratulations! You just used ODIN!** 🎉

---

## 📖 All Commands

### Basic Commands

```bash
# Start ODIN daemon (must do this first!)
odin serve

# Stop ODIN daemon
odin stop

# Create a new project
odin create <project_name>

# List all projects
odin list

# Add an AI agent to a project
odin integrate <agent_name> <project_name>

# Check system status
odin status

# Get help
odin help
```

### Multilingual Commands (English + Bangla)

| English | Bangla (বাংলা) | What it does |
|---------|----------------|--------------|
| `odin create MyProject` | `odin নতুন MyProject` | Create project |
| `odin list` | `odin তালিকা` | List projects |
| `odin status` | `odin স্থিতি` | Show status |
| `odin help` | `odin সাহায্য` | Get help |

### AI Model Commands (Future)

```bash
# These will be available soon:
odin /models              # Show available AI models
odin /models select       # Choose a model interactively
odin /models set gemini_flash  # Use Gemini 2.5 Flash
odin /models status       # Current model configuration
```

---

## 📦 Dependencies (What You Need)

### Required Software:

1. **Python 3.13 or higher**
   - What it is: Programming language ODIN is written in
   - Check: `python3 --version`
   - Install: Download from python.org

2. **socat**
   - What it is: Tool for communication between programs
   - Check: `which socat`
   - Install: `brew install socat`

### Required Python Packages:

```bash
# Install all at once:
pip3 install pyyaml psutil

# Or individually:
pip3 install pyyaml    # For reading config files
pip3 install psutil    # For system monitoring
```

### Optional (For AI Models):

1. **Ollama** (for local AI)
   - Install: `brew install ollama`
   - Setup: `ollama pull llama3`

2. **API Keys** (for cloud AI - all free tier available!)
   - Google Gemini: https://makersuite.google.com/
   - Anthropic Claude: https://console.anthropic.com/

---

## 📁 Files and Folders

### Complete File Structure:

```
Terminal-CLI/Odin/Odin/
│
├── bin/
│   └── odin-cli                    # Main command line interface
│
├── daemon/
│   └── odin_daemon.py              # Background service (the brain)
│
├── Agents/
│   ├── claude/
│   │   └── adapter.py              # Claude AI integration
│   ├── gemini/
│   │   └── adapter.py              # Gemini AI integration
│   └── template_agent/
│       └── adapter.py              # Template for new agents
│
├── Workspaces/
│   ├── ExampleProject/
│   │   ├── .odin-meta.yaml         # Project metadata
│   │   ├── src/                    # Source code folder
│   │   └── assets/                 # Files, images, etc.
│   └── [Your Projects Here]/
│
├── Config/
│   ├── models-config.yaml          # AI models configuration
│   ├── user-preferences.yaml       # Your preferences
│   ├── README.md                   # Config explanation
│   └── UNIVERSAL_CLI_MODEL_INTEGRATION.md  # Model integration guide
│
├── Logs/
│   └── actions.log                 # Activity log
│
├── Dashboard/                      # Future: Visual interface
├── Voice/                          # Future: Voice commands
│
├── ODIN_README.md                  # This file!
├── MODELS_INTEGRATION.md           # AI model integration guide
└── README.md                       # Quick start guide
```

### Key Files Explained:

| File | Purpose | Edit? |
|------|---------|-------|
| `bin/odin-cli` | Your entry point - type commands here | ❌ No |
| `daemon/odin_daemon.py` | The brain - handles everything | ❌ No |
| `Agents/*/adapter.py` | AI agent definitions | ✅ Yes (to customize) |
| `Config/*.yaml` | Settings and preferences | ✅ Yes (your settings) |
| `Workspaces/*/` | Your projects | ✅ Yes (your work) |
| `Logs/actions.log` | Activity history | 👁️ View only |

---

## 💻 Code Snippets (Copy & Use)

### 1. Start ODIN When Terminal Opens

Add to `~/.zshrc`:

```bash
# ODIN Auto-start (optional)
if ! pgrep -f "odin_daemon.py" > /dev/null; then
    echo "🚀 Starting ODIN..."
    odin serve &
fi
```

### 2. Create a Custom Agent

```bash
# Copy template
cp -r ~/Terminal-CLI/Odin/Odin/Agents/template_agent ~/Terminal-CLI/Odin/Odin/Agents/my_agent

# Edit the adapter
nano ~/Terminal-CLI/Odin/Odin/Agents/my_agent/adapter.py

# Change class name from Template_agent to My_agent
# ODIN will auto-discover it!
```

### 3. Check ODIN Status Script

Save as `check_odin.sh`:

```bash
#!/bin/bash
if pgrep -f "odin_daemon.py" > /dev/null; then
    echo "✅ ODIN is running"
    odin status
else
    echo "❌ ODIN is not running"
    echo "Start with: odin serve"
fi
```

### 4. Backup All Projects

```bash
#!/bin/bash
# Save as backup_odin.sh
BACKUP_DIR="$HOME/ODIN_Backups/$(date +%Y-%m-%d)"
mkdir -p "$BACKUP_DIR"
cp -r ~/Terminal-CLI/Odin/Odin/Workspaces/* "$BACKUP_DIR/"
echo "✅ Backed up to: $BACKUP_DIR"
```

### 5. Use ODIN in Python Script

```python
#!/usr/bin/env python3
import subprocess
import json

def odin_command(command):
    """Send command to ODIN and get response"""
    result = subprocess.run(
        ['bash', '/Users/reeazmahmud/Terminal-CLI/Odin/Odin/bin/odin-cli'] + command.split(),
        capture_output=True,
        text=True
    )
    return result.stdout

# Example: List projects
projects = odin_command('list')
print(projects)

# Example: Create project
result = odin_command('create AutomatedProject')
print(result)
```

---

## 🤖 AI Model Integration

### Available AI Models:

#### Local (Free, Private, Offline)
- **Ollama** - Run AI on your computer
  - Models: llama3, codellama, mistral
  - Setup: `brew install ollama && ollama pull llama3`

#### Cloud Free Tier (Fast, No Cost)
- **Gemini 2.5 Flash** ⭐ Recommended
  - Provider: Google
  - Get key: https://makersuite.google.com/
  - Features: Fast, multimodal, Google Workspace

- **Claude 3.5 Haiku**
  - Provider: Anthropic
  - Get key: https://console.anthropic.com/
  - Features: Excellent for code

#### Cloud Paid Tier (Premium)
- **Gemini 2.0 Pro** - Advanced reasoning
- **Claude 3.5 Sonnet** - Best code generation
- **GPT-4 Turbo** - Advanced AI

### Setting Up API Keys:

```bash
# Method 1: Environment variables (temporary)
export GOOGLE_API_KEY="your-key-here"
export ANTHROPIC_API_KEY="your-key-here"

# Method 2: Add to ~/.zshrc (permanent)
echo 'export GOOGLE_API_KEY="your-key-here"' >> ~/.zshrc
source ~/.zshrc

# Method 3: ODIN config (future feature)
odin /models setkey google
```

---

## 🔧 Troubleshooting

### Common Issues:

#### 1. "ODIN daemon not running"

**Problem**: You forgot to start the daemon
**Solution**:
```bash
odin serve
# Wait 2 seconds, then try your command again
```

#### 2. "command not found: odin"

**Problem**: Shell function not set up
**Solution**:
```bash
# Use full path instead:
bash ~/Terminal-CLI/Odin/Odin/bin/odin-cli serve

# Or add to ~/.zshrc:
odin() {
    bash "$HOME/Terminal-CLI/Odin/Odin/bin/odin-cli" "$@"
}
source ~/.zshrc
```

#### 3. "command not found: socat"

**Problem**: socat not installed
**Solution**:
```bash
brew install socat
```

#### 4. "ModuleNotFoundError: No module named 'yaml'"

**Problem**: Missing Python packages
**Solution**:
```bash
pip3 install pyyaml psutil
```

#### 5. Daemon not responding

**Problem**: Daemon crashed or stuck
**Solution**:
```bash
# Stop daemon
odin stop

# Or force kill
pkill -f odin_daemon.py

# Restart
odin serve
```

---

## 📦 Moving ODIN to Another Computer

### Method 1: Complete Copy

```bash
# On current computer - create portable package
cd ~
tar -czf ODIN_Portable.tar.gz Terminal-CLI/Odin/Odin/

# Copy ODIN_Portable.tar.gz to USB drive or cloud

# On new computer - extract
tar -xzf ODIN_Portable.tar.gz
cd Terminal-CLI/Odin/Odin
chmod +x bin/odin-cli

# Install dependencies
brew install socat
pip3 install pyyaml psutil

# Start ODIN
bash bin/odin-cli serve
```

### Method 2: Git Clone (After GitHub Upload)

```bash
# On new computer
git clone https://github.com/yourusername/ODIN.git
cd ODIN

# Install dependencies
brew install socat
pip3 install pyyaml psutil

# Run
bash bin/odin-cli serve
```

---

## 📤 GitHub Upload Guide

### Prepare for GitHub:

#### Step 1: Create .gitignore

Create file: `Terminal-CLI/Odin/Odin/.gitignore`

```
# Ignore sensitive data
Config/user-preferences.yaml
*.key
*.env

# Ignore logs
Logs/*.log

# Ignore workspaces (user projects)
Workspaces/*
!Workspaces/ExampleProject

# Ignore Python cache
__pycache__/
*.pyc
*.pyo

# Ignore daemon socket
daemon/*.sock

# Ignore macOS files
.DS_Store
```

#### Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Name: `ODIN`
3. Description: "The Allfather - AI/Agent Orchestration System"
4. Make it Public or Private
5. Don't initialize with README (we have one!)
6. Click "Create repository"

#### Step 3: Upload to GitHub

```bash
# Navigate to ODIN
cd ~/Terminal-CLI/Odin/Odin

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - ODIN v1.0

- Multi-agent orchestration system
- Claude and Gemini integration
- English + Bangla multilingual support
- System monitoring
- Project management
- Built on January 3, 2026"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ODIN.git

# Push to GitHub
git branch -M main
git push -u origin main
```

#### Step 4: Create Release

On GitHub:
1. Go to your repository
2. Click "Releases" → "Create a new release"
3. Tag: `v1.0.0`
4. Title: "ODIN v1.0 - The Allfather"
5. Description:
```markdown
## ODIN - The Allfather AI/Agent Orchestration System

First public release!

### Features:
- 🤖 Multi-agent orchestration
- 🌐 Universal AI model integration (Gemini, Claude, Ollama)
- 🗣️ Multilingual support (English + বাংলা)
- 📊 System monitoring (CPU, memory, disk)
- 🔐 Privacy-focused (local AI support)
- 🚀 Easy to use CLI
- 📦 Portable and modular

### Quick Start:
1. Download ODIN_Portable.tar.gz
2. Extract and run: `bash bin/odin-cli serve`
3. Create project: `bash bin/odin-cli create MyProject`

See ODIN_README.md for complete documentation.

Built: January 3, 2026
```

---

## 👏 Credits

### Created By:
- **Reeaz Mahmud** - System Architect & Developer
- **Claude AI (Anthropic)** - Development Assistant

### Built With:
- Python 3.13
- Love for AI and automation
- Coffee ☕ and determination

### Inspiration:
- Named after Odin (The Allfather) from Norse mythology
- Goal: Create a universal AI orchestration system
- Mission: Make AI accessible and manageable for everyone

### Special Thanks:
- Anthropic for Claude AI
- Google for Gemini AI
- Ollama team for local LLM
- Open source community

---

## 📝 Version History

- **v1.0** (January 3, 2026)
  - Initial release
  - Multi-agent orchestration
  - Claude and Gemini integration
  - English + Bangla support
  - System monitoring
  - Project management

---

## 🔮 Future Plans

- [ ] `/models` command implementation
- [ ] Visual dashboard (GUI)
- [ ] Voice command interface
- [ ] More AI agent templates
- [ ] Docker container version
- [ ] Windows and Linux support
- [ ] Mobile app integration
- [ ] VS Code extension

---

## 📞 Support

### Getting Help:

1. **Read this README** - Most answers are here!
2. **Check MODELS_INTEGRATION.md** - For AI model questions
3. **View Logs**: `cat ~/Terminal-CLI/Odin/Odin/Logs/actions.log`
4. **GitHub Issues**: (after upload) Report bugs or request features

### Quick Links:

- Documentation: See ODIN_README.md (this file)
- AI Models Guide: See MODELS_INTEGRATION.md
- Config Guide: See Config/README.md
- GitHub: (coming soon)

---

## ⚖️ License

**Private/Personal Use**

This software is created for personal use by Reeaz Mahmud. Feel free to use, modify, and distribute with attribution.

---

## 🎯 Summary

**ODIN in 30 Seconds:**

ODIN is your personal AI manager. It lets you:
- Use multiple AI models (Gemini, Claude, local AI)
- Organize projects in sandboxes
- Switch between free and paid AI services
- Run AI offline on your computer
- Use commands in English or Bangla
- Monitor your computer's health

**Start using ODIN in 3 steps:**
1. `odin serve` - Start the system
2. `odin create MyProject` - Create a project
3. `odin integrate claude MyProject` - Add AI assistant

**That's it! You're ready to orchestrate AI like a boss!** 🚀

---

**Created with ❤️ on January 3, 2026**
**May ODIN serve you well!**
