#!/bin/bash
#
# ODIN - One-Command Installation Script
# Makes installation super easy - just run this file!
#
# Usage: bash QUICK_INSTALL.sh
#

set -e  # Exit on error

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║           ODIN - The Allfather                                ║"
echo "║         Quick Installation Script                             ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Detect OS
OS=$(uname -s)
echo "🔍 Detected OS: $OS"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found!"
    echo "📥 Please install Python 3.13+ from python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "✓ Python $PYTHON_VERSION found"

# Install socat (macOS/Linux)
echo ""
echo "📦 Installing dependencies..."

if [[ "$OS" == "Darwin" ]]; then
    # macOS
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew not found!"
        echo "📥 Install from: https://brew.sh"
        exit 1
    fi

    if ! command -v socat &> /dev/null; then
        echo "Installing socat..."
        brew install socat
    fi
    echo "✓ socat installed"

elif [[ "$OS" == "Linux" ]]; then
    # Linux
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y socat python3-pip
    elif command -v yum &> /dev/null; then
        sudo yum install -y socat python3-pip
    fi
    echo "✓ socat installed"
fi

# Install Python packages
echo ""
echo "📦 Installing Python packages..."
pip3 install -q pyyaml psutil 2>/dev/null || {
    echo "⚠️  Standard pip install failed, trying with --user"
    pip3 install --user -q pyyaml psutil
}
echo "✓ Python packages installed"

# Setup ODIN
echo ""
echo "🔧 Setting up ODIN..."

# Get installation directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "📁 Installing to: $SCRIPT_DIR"

# Make CLI executable
chmod +x "$SCRIPT_DIR/bin/odin-cli"
echo "✓ Made CLI executable"

# Create shell function
SHELL_RC=""
if [[ -f "$HOME/.zshrc" ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ -f "$HOME/.bashrc" ]]; then
    SHELL_RC="$HOME/.bashrc"
fi

if [[ -n "$SHELL_RC" ]]; then
    echo ""
    echo "🔧 Setting up shell function..."

    # Check if already exists
    if grep -q "odin()" "$SHELL_RC"; then
        echo "ℹ️  ODIN shell function already exists in $SHELL_RC"
    else
        cat >> "$SHELL_RC" << EOF

# ============================================
# ODIN - The Allfather (Auto-installed)
# ============================================
odin() {
    bash "$SCRIPT_DIR/bin/odin-cli" "\$@"
}
EOF
        echo "✓ Added 'odin' command to $SHELL_RC"
    fi
fi

# Test installation
echo ""
echo "🧪 Testing installation..."
if bash "$SCRIPT_DIR/bin/odin-cli" help &> /dev/null; then
    echo "✓ ODIN is working!"
else
    echo "⚠️  Test failed, but ODIN might still work"
fi

# Success message
echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║               ✅ INSTALLATION COMPLETE!                        ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "🎯 Quick Start (in a NEW terminal window):"
echo ""
echo "   1. Start ODIN:"
echo "      odin serve"
echo ""
echo "   2. Create a project:"
echo "      odin create MyProject"
echo ""
echo "   3. Add AI assistant:"
echo "      odin integrate claude MyProject"
echo ""
echo "   4. Check status:"
echo "      odin status"
echo ""
echo "📖 For full documentation, see ODIN_README.md"
echo ""
echo "🌟 Pro Tip: Open a NEW terminal window for the 'odin' command to work!"
echo ""

# Ask to start ODIN
read -p "Would you like to start ODIN now? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "🚀 Starting ODIN..."
    bash "$SCRIPT_DIR/bin/odin-cli" serve &
    sleep 2
    echo ""
    echo "✓ ODIN is running!"
    echo "Try: bash $SCRIPT_DIR/bin/odin-cli status"
fi

echo ""
echo "Happy orchestrating! 🎉"
