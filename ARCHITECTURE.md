# ODIN Architecture Overview

**Visual guide to understanding how ODIN works**

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                                                                 │
│  Terminal: odin create MyProject                               │
│            odin integrate claude MyProject                     │
│            odin তালিকা (Bangla support)                        │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      CLI INTERFACE (bin/odin-cli)               │
│                                                                 │
│  Commands: serve, create, list, integrate, status, help, stop  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                  UNIX SOCKET (via socat)                        │
│                                                                 │
│  Location: daemon/odin.sock                                    │
│  Protocol: Inter-process communication                         │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ODIN DAEMON (daemon/odin_daemon.py)          │
│                    The Allfather - Core Brain                  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Command Parser (Multilingual: English + Bangla)        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Agent Discovery System (Auto-detects new agents)       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Project Manager (Creates/deletes workspaces)           │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  System Monitor (CPU, Memory, Disk monitoring)          │  │
│  │  - Background thread running continuously                │  │
│  │  - Alerts agents when thresholds exceeded                │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────┬─────────────────┬─────────────────┬──────────────────────┘
      │                 │                 │
      ▼                 ▼                 ▼
┌───────────┐     ┌───────────┐     ┌───────────┐
│  CLAUDE   │     │  GEMINI   │     │ TEMPLATE  │
│   AGENT   │     │   AGENT   │     │   AGENT   │
│           │     │           │     │           │
│ adapter.py│     │ adapter.py│     │ adapter.py│
└─────┬─────┘     └─────┬─────┘     └─────┬─────┘
      │                 │                 │
      └─────────────────┴─────────────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │  AI MODEL REGISTRY    │
            │                       │
            │ Config/models-        │
            │   config.yaml         │
            │                       │
            │ - Local: Ollama       │
            │ - Free: Gemini Flash  │
            │ - Paid: Claude, GPT-4 │
            └───────────────────────┘
```

---

## 🔄 Message Flow Example

**User Command:** `odin create MyProject`

```
1. User types command
   ↓
2. CLI (bin/odin-cli) receives input
   ↓
3. Sends command via Unix socket to daemon
   ↓
4. Daemon receives: "create MyProject"
   ↓
5. Command Parser analyzes request
   - Detects: CREATE action
   - Project name: MyProject
   ↓
6. Project Manager executes:
   - Creates Workspaces/MyProject/
   - Creates src/ folder
   - Creates assets/ folder
   - Creates .odin-meta.yaml
   ↓
7. Updates Config/project-index.yaml
   ↓
8. Sends success response via socket
   ↓
9. CLI displays: "✓ Project 'MyProject' created successfully"
```

---

## 🤖 Agent Integration Flow

**User Command:** `odin integrate claude MyProject`

```
1. User requests Claude integration
   ↓
2. Daemon receives request
   ↓
3. Agent Discovery System:
   - Scans Agents/ folder
   - Finds Agents/claude/adapter.py
   - Loads Claude agent class
   ↓
4. Agent Registry updated:
   - agents_registry["claude"] = Claude
   ↓
5. Project metadata updated (.odin-meta.yaml):
   agents:
     - claude
   ↓
6. Claude agent initialized:
   - workspace_path = Workspaces/MyProject
   - Runs analyze_project()
   ↓
7. Claude ready to:
   - Analyze code files
   - Monitor system alerts
   - Process assets (PDFs, documents)
```

---

## 📊 System Monitoring Thread

**Background Process (Always Running)**

```
┌─────────────────────────────────────────┐
│  System Monitor Thread                  │
│  (Runs every 60 seconds)                │
│                                         │
│  1. Check CPU usage                     │
│     └─> If > 80%: Alert agents         │
│                                         │
│  2. Check Memory usage                  │
│     └─> If > 80%: Alert agents         │
│                                         │
│  3. Check Disk usage                    │
│     └─> If > 90%: Alert agents         │
│                                         │
│  4. Monitor top processes               │
│     └─> Log high CPU consumers         │
│                                         │
└─────────────────────────────────────────┘
           │
           ▼
    ┌─────────────┐
    │  AGENTS     │
    │  NOTIFIED   │
    │             │
    │  Each agent │
    │  receives   │
    │  alert and  │
    │  can react  │
    └─────────────┘
```

---

## 🧩 Agent Discovery System

**How ODIN automatically finds new agents**

```python
Agents/
├── claude/
│   └── adapter.py          # Contains: class Claude
├── gemini/
│   └── adapter.py          # Contains: class Gemini
├── template_agent/
│   └── adapter.py          # Contains: class Template_agent
└── your_new_agent/         # Add new folder
    └── adapter.py          # Define: class Your_new_agent

# ODIN automatically:
# 1. Scans all folders in Agents/
# 2. Looks for adapter.py in each folder
# 3. Loads the Python module
# 4. Finds class with matching name
# 5. Adds to agents_registry dictionary
# 6. Agent is ready to use!

# No code changes needed - just add folder + adapter.py
```

---

## 🌍 Multilingual Command System

**How English and Bangla commands work**

```python
# Language Mapping Dictionary
LANG_MAP = {
    "en": {
        "create": "create",
        "list": "list",
        "integrate": "integrate",
        "status": "status"
    },
    "bn": {
        "নতুন": "create",      # "notun" (new)
        "তালিকা": "list",      # "talika" (list)
        "একত্রিত": "integrate",  # "ekotrito" (integrate)
        "অবস্থা": "status"      # "obostha" (status)
    }
}

# User types: odin তালিকা
# ↓
# Parser checks all language mappings
# ↓
# Finds: "তালিকা" maps to "create"
# ↓
# Executes: create command
# ↓
# Returns: List of all projects (in English or Bangla)
```

**Adding new languages:**

```python
# Just add to LANG_MAP:
"es": {  # Spanish
    "crear": "create",
    "lista": "list",
    "integrar": "integrate"
}

# Now supports: odin crear MyProject
```

---

## 📦 Project Structure

**What happens when you create a project**

```
odin create MyWebsite
↓
Creates:

Workspaces/MyWebsite/
├── .odin-meta.yaml          # Project metadata
│   ├── name: MyWebsite
│   ├── created: 2026-01-03
│   ├── agents: []           # Empty initially
│   └── status: active
│
├── src/                     # Source code folder
│   └── (empty initially)
│
└── assets/                  # Files and documents
    └── (empty initially)

Also updates:
Config/project-index.yaml    # Global project registry
└── Adds MyWebsite to list
```

---

## 🔌 Universal Model Integration

**How AI model switching works**

```
Config/models-config.yaml
├── local:
│   └── ollama (free, no internet)
├── cloud_free:
│   └── gemini_flash (recommended)
└── cloud_paid:
    ├── claude_sonnet
    └── gpt4

Agent needs AI response
↓
1. Check models-config.yaml
2. Get default_model (gemini_flash)
3. Check if API key exists
   ├─> Yes: Use Gemini
   └─> No: Fall back to Ollama
4. Send request to model
5. Return response to agent

Future: /models command
↓
User runs: odin /models select
↓
Shows interactive menu:
  1. Gemini 2.5 Flash (Free) [RECOMMENDED]
  2. Claude Sonnet (Paid)
  3. Ollama (Local, No Internet)
  4. GPT-4 (Paid)
↓
User selects model
↓
Updates default_model in config
↓
All agents now use selected model
```

---

## 🎯 Data Flow: Complete Example

**User wants Claude to analyze a Python file**

```
1. USER ACTION
   odin integrate claude MyProject
   ↓

2. CLI
   Sends: "integrate claude MyProject"
   ↓

3. DAEMON
   - Parses command
   - Discovers Claude agent
   - Loads Claude class
   ↓

4. CLAUDE AGENT
   - Initialized with workspace: Workspaces/MyProject
   - Runs analyze_project()
   - Scans src/ folder
   - Finds: src/app.py
   ↓

5. ASSET ANALYSIS
   Claude receives asset:
   {
     "type": "py",
     "path": "Workspaces/MyProject/src/app.py",
     "size": 1024
   }
   ↓

6. AI MODEL REQUEST
   - Reads app.py content
   - Sends to Gemini Flash:
     "Analyze this Python code for bugs and improvements"
   ↓

7. AI RESPONSE
   Gemini returns:
   - Found 2 potential issues
   - Suggests 3 improvements
   - Security concern: SQL injection risk
   ↓

8. CLAUDE AGENT
   - Formats response
   - Logs analysis to Logs/
   - Updates project metadata
   ↓

9. DAEMON
   Returns analysis to user via socket
   ↓

10. CLI
    Displays formatted analysis
    ✓ Analysis complete!
```

---

## 🛡️ Security and Sandboxing

**How ODIN keeps projects isolated**

```
┌──────────────────────────────────────────┐
│         Project 1: WebsiteProject        │
│                                          │
│  Workspace: Workspaces/WebsiteProject/  │
│  Agents: [claude, gemini]               │
│  Files: src/app.js, src/styles.css      │
│                                          │
│  ⚠️ Claude can only access files in     │
│     Workspaces/WebsiteProject/          │
│  ⚠️ Cannot read other projects          │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│         Project 2: DataAnalysis          │
│                                          │
│  Workspace: Workspaces/DataAnalysis/    │
│  Agents: [gemini]                        │
│  Files: src/analysis.py, data.csv       │
│                                          │
│  ✓ Completely isolated from Project 1   │
└──────────────────────────────────────────┘

All projects share:
- Config/ (read-only for agents)
- Agents/ (agent code)

But workspace data is isolated!
```

---

## 🚀 Performance Considerations

**Threading Model**

```
Main Thread
├── CLI listener (Unix socket)
├── Command processor
└── Response sender

Background Thread
└── System Monitor (60s loop)
    ├── CPU check
    ├── Memory check
    ├── Disk check
    └── Alert agents if needed

Agent Threads (when needed)
├── Claude analysis
├── Gemini processing
└── Custom agent tasks

All threads communicate via:
- Shared agents_registry (dict)
- Socket communication
- Metadata files (YAML)
```

**Resource Management**

```
Memory Usage:
├── Daemon: ~50MB base
├── Each agent: ~20-30MB
├── System monitor: ~5MB
└── Total: ~100-150MB for 3 agents

Disk Usage:
├── ODIN base: ~5MB
├── Each project: ~1KB (metadata)
├── Agent logs: ~1MB/day
└── Scales with user files

CPU Usage:
├── Idle: <1% CPU
├── Processing: 5-15% CPU
├── System monitor: <1% CPU
```

---

## 🔮 Future Architecture (Planned Features)

**Voice Interface**

```
User speaks: "Create new project Website"
↓
Voice/odin_voice.py
├── Speech recognition (Whisper)
├── Language detection (EN/BN)
├── Text extraction
└── Send to daemon
    ↓
    Normal command flow continues
```

**Web Dashboard**

```
Browser → localhost:8080
↓
Dashboard/index.html (Electron)
├── WebSocket to daemon
├── Real-time project list
├── Drag-and-drop file upload
├── Visual agent management
└── System health graphs
```

**Plugin System**

```
Plugins/
├── github-integration/
│   └── Auto-push projects to GitHub
├── slack-notifications/
│   └── Send alerts to Slack
└── custom-agent-creator/
    └── Visual agent builder

Each plugin:
- Independent module
- Registers with daemon
- Extends functionality
- No core code changes needed
```

---

## 📚 Key Design Principles

1. **Modularity**: Each component is independent
   - Agents are self-contained
   - CLI doesn't know about agent internals
   - Daemon orchestrates but doesn't implement

2. **Extensibility**: Easy to add new features
   - New agent = new folder + adapter.py
   - New language = add to LANG_MAP
   - New model = add to models-config.yaml

3. **Isolation**: Projects can't interfere
   - Separate workspaces
   - Independent metadata
   - Agent access restricted

4. **Async-Ready**: Prepared for concurrent operations
   - Background monitoring
   - Multiple agent processing
   - Non-blocking I/O

5. **User-Friendly**: Simple for beginners
   - Clear commands
   - Helpful error messages
   - Multilingual support
   - Comprehensive documentation

---

**Last Updated:** January 3, 2026
**Version:** 1.0
