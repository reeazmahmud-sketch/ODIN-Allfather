# 🌟 ODIN - The Allfather

**Universal AI/Agent Orchestration System for the Modern Developer**

[![Version](https://img.shields.io/badge/version-1.0-blue.svg)](VERSION_HISTORY.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13+-yellow.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey.svg)](ARCHITECTURE.md)

**ODIN** (Orchestrated Distributed Intelligence Network) is a powerful, extensible system that brings together multiple AI agents, supports multilingual commands, and provides seamless integration with local and cloud AI models.

---

## ✨ Key Features

🤖 **Multi-Agent Orchestration**
- Manage multiple AI agents (Claude, Gemini, and more)
- Automatic agent discovery system
- Template system for creating custom agents

🌍 **Multilingual Support**
- English + Bangla (বাংলা) commands
- Easy to extend to other languages
- Cultural accessibility built-in

🎯 **Universal AI Model Integration**
- **Local**: Ollama, LM Studio (free, no internet)
- **Cloud Free**: Gemini 2.5 Flash (recommended)
- **Cloud Paid**: Claude Sonnet, GPT-4, Gemini Pro
- Switch models with `/models` command (coming soon)

📦 **Project Sandboxing**
- Isolated workspaces for each project
- Automatic folder structure (src/, assets/)
- Metadata tracking with YAML

📊 **System Monitoring**
- Real-time CPU, memory, and disk tracking
- Alert system for resource thresholds
- Background monitoring thread

🚀 **Easy Installation**
- One-command setup: `bash QUICK_INSTALL.sh`
- Auto-detects OS and installs dependencies
- Ready in 2 minutes

---

## 🚀 Quick Start

### Installation

```bash
# 1. Download ODIN (or clone from GitHub)
cd ~/Desktop/ODIN_Portable

# 2. Run the installer
bash QUICK_INSTALL.sh

# 3. Open a NEW terminal window and start ODIN
odin serve
```

### First Commands

```bash
# Create your first project
odin create MyFirstProject

# List all projects
odin list

# Add Claude AI assistant
odin integrate claude MyFirstProject

# Check system status
odin status

# Get help
odin help
```

### Multilingual Commands (Bangla)

```bash
# Create project (নতুন = new)
odin নতুন MyProject

# List projects (তালিকা = list)
odin তালিকা

# Integrate agent (একত্রিত = integrate)
odin একত্রিত claude MyProject
```

---

## 📚 Documentation

**Start Here:**
- 📖 [START_HERE.md](START_HERE.md) - 5-minute quick start guide
- 📘 [ODIN_README.md](ODIN_README.md) - Comprehensive beginner's guide (400+ lines)

**Architecture & Design:**
- 🏗️ [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture with visual diagrams
- 🤖 [MODELS_INTEGRATION.md](MODELS_INTEGRATION.md) - AI model setup and integration
- 🌐 [UNIVERSAL_CLI_MODEL_INTEGRATION.md](UNIVERSAL_CLI_MODEL_INTEGRATION.md) - Universal system for all CLI agents

**Future Development:**
- 🔮 [FUTURE_UPDATES.md](FUTURE_UPDATES.md) - Planned updates and improvements
- 🗺️ [FEATURES_ROADMAP.md](FEATURES_ROADMAP.md) - 20+ innovative feature ideas
- 📝 [VERSION_HISTORY.md](VERSION_HISTORY.md) - Complete version history and changelog

**Configuration:**
- ⚙️ [Config/README.md](Config/README.md) - Configuration file explanations

---

## 🎯 Use Cases

### For Developers
- **Multi-AI Code Analysis**: Use Claude for code review, Gemini for documentation
- **Project Organization**: Keep all projects in isolated sandboxes
- **Resource Monitoring**: Never run out of disk space unexpectedly

### For Students
- **Learning Assistant**: AI agents help with homework and projects
- **Multilingual Support**: Study in your native language (English/Bangla)
- **Free Tier Models**: Use Gemini Flash for zero cost

### For Researchers
- **Data Analysis**: Integrate AI agents with your research projects
- **Document Processing**: Analyze PDFs, papers, and datasets
- **Local LLM**: Keep sensitive data private with Ollama

### For Teams
- **Shared AI Resources**: Everyone uses the same model configuration
- **Project Templates**: Standardize project structure
- **Cost Tracking**: Monitor AI usage and costs (coming soon)

---

## 🤖 Supported AI Models

### Local (Free, No Internet)
- **Ollama** - Run Llama, Mistral, Phi locally
- **LM Studio** - User-friendly local LLM interface
- **Jan** - Open-source ChatGPT alternative

### Cloud Free Tier
- **Gemini 2.5 Flash** ⭐ Recommended default
  - 15 RPM, 1500 RPD
  - Multimodal support
  - Google Workspace integration

### Cloud Paid Tier
- **Claude Sonnet** - Advanced reasoning, long context
- **GPT-4** - OpenAI's most capable model
- **Gemini Pro** - Enhanced capabilities

---

## 🛠️ Available Agents

### Built-in Agents

**Template Agent** (`Agents/template_agent/`)
- Base template for creating new agents
- Standard interface implementation
- Copy and customize for your needs

**Claude Agent** (`Agents/claude/`)
- Code analysis and review
- Security vulnerability detection
- Best practices suggestions

**Gemini Agent** (`Agents/gemini/`)
- General task handling
- Google Workspace integration ready
- Multimodal capabilities

### Creating Custom Agents

```bash
# 1. Copy template
cp -r Agents/template_agent Agents/my_agent

# 2. Edit adapter.py
# Rename class: Template_agent → My_agent
# Implement custom functionality

# 3. ODIN automatically discovers it!
odin integrate my_agent MyProject
```

---

## 📊 System Requirements

**Minimum:**
- Python 3.13+
- 2GB RAM
- 500MB disk space
- macOS or Linux

**Recommended:**
- Python 3.13+
- 4GB RAM
- 1GB disk space
- Active internet connection (for cloud AI)

**Dependencies:**
- `socat` - Unix socket communication
- `PyYAML` - YAML configuration parsing
- `psutil` - System monitoring

---

## 🎨 Project Structure

```
ODIN_Portable/
├── START_HERE.md                 # Quick start guide
├── ODIN_README.md                # Comprehensive documentation
├── ARCHITECTURE.md               # System architecture
├── QUICK_INSTALL.sh              # One-command installer
├── VERSION_HISTORY.md            # Changelog
│
├── bin/
│   └── odin-cli                  # CLI interface
│
├── daemon/
│   └── odin_daemon.py            # Core orchestration engine
│
├── Agents/
│   ├── template_agent/           # Base agent template
│   ├── claude/                   # Claude AI integration
│   └── gemini/                   # Gemini AI integration
│
├── Config/
│   ├── models-config.yaml        # AI model registry
│   ├── odin-config.yaml          # System settings
│   ├── project-index.yaml        # Project database
│   └── user-preferences.yaml     # User customization
│
├── Workspaces/
│   └── ExampleProject/           # Sample project
│       ├── .odin-meta.yaml       # Project metadata
│       ├── src/                  # Source code
│       └── assets/               # Files and documents
│
├── Dashboard/                    # Web dashboard (future)
├── Voice/                        # Voice interface (future)
└── Logs/                         # System logs
```

---

## 🌟 What Makes ODIN Special?

### 1. **Truly Universal**
- Works with ANY AI model (local or cloud)
- Single configuration for all CLI agents
- Future-proof architecture

### 2. **Beginner Friendly**
- One-command installation
- Clear, simple commands
- Comprehensive documentation for non-technical users

### 3. **Multilingual**
- English + Bangla built-in
- Easy to add more languages
- Cultural accessibility priority

### 4. **Modular & Extensible**
- Add new agents without changing core code
- Plugin system planned
- Community contributions welcome

### 5. **Privacy Conscious**
- Local LLM support (Ollama)
- Project sandboxing
- No data sent to cloud unless you choose

---

## 🔮 Roadmap

### Version 1.1 (Q1 2026)
- [ ] `/models` command for easy AI model switching
- [ ] Voice interface (English + Bangla)
- [ ] Simple wizard mode for beginners
- [ ] Auto-update system

### Version 1.2 (Q2 2026)
- [ ] Project templates (web, API, data science, ML)
- [ ] Batch operations
- [ ] Smart suggestions
- [ ] Analytics dashboard

### Version 2.0 (Q3 2026)
- [ ] Web interface
- [ ] Mobile app (iOS/Android)
- [ ] Team collaboration
- [ ] Plugin system

See [FEATURES_ROADMAP.md](FEATURES_ROADMAP.md) for 20+ innovative feature ideas!

---

## 🤝 Contributing

We welcome contributions from the community!

**How to contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Areas needing help:**
- Additional language support (Hindi, Spanish, Arabic, etc.)
- New agent templates
- Documentation translations
- Bug reports and testing
- Feature suggestions

See [VERSION_HISTORY.md](VERSION_HISTORY.md) for contribution guidelines.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**MIT License Summary:**
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ℹ️ Liability and warranty limitations

---

## 🙏 Acknowledgments

**Created by:** Reeaz Mahmud
**Development Tool:** Claude Code (Claude Sonnet 4.5)
**Release Date:** January 3, 2026
**Version:** 1.0 "The Allfather Awakens"

**Special Thanks:**
- Python community for excellent libraries
- Anthropic for Claude AI
- Google for Gemini AI
- Ollama team for local LLM support
- All future contributors and users

---

## 📞 Support & Community

**Need help?**
- 📖 Read [ODIN_README.md](ODIN_README.md) for detailed instructions
- 🏗️ Check [ARCHITECTURE.md](ARCHITECTURE.md) for technical details
- 🐛 Report bugs via GitHub Issues
- 💡 Suggest features via GitHub Issues
- 📧 Contact: [Your Email/Contact]

**Join the community:**
- 🌟 Star this repository
- 🍴 Fork and contribute
- 📣 Share with others
- ⭐ Give feedback

---

## 🚀 Getting Started (TL;DR)

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ODIN-Allfather.git
cd ODIN-Allfather

# Install (one command)
bash QUICK_INSTALL.sh

# Open NEW terminal, then:
odin serve              # Start ODIN
odin create MyProject   # Create project
odin integrate claude MyProject   # Add AI
odin status             # Check system
```

**That's it! You're ready to orchestrate AI agents like the Allfather himself.**

---

**ODIN** - *Where AI agents unite under one command.*

[![GitHub Stars](https://img.shields.io/github/stars/YOUR_USERNAME/ODIN-Allfather.svg?style=social&label=Star)](https://github.com/YOUR_USERNAME/ODIN-Allfather)
[![GitHub Forks](https://img.shields.io/github/forks/YOUR_USERNAME/ODIN-Allfather.svg?style=social&label=Fork)](https://github.com/YOUR_USERNAME/ODIN-Allfather/fork)

---

**Last Updated:** January 3, 2026 | **Version:** 1.0 | [Changelog](VERSION_HISTORY.md)
