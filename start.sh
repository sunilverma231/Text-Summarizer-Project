#!/bin/bash

# Text Summarizer - Quick Start Script
# This script helps you start the application easily

echo "╔════════════════════════════════════════════════════════════╗"
echo "║        TEXT SUMMARIZER - QUICK START (with LoRA)          ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check if conda environment exists
if conda info --envs | grep -q "textS"; then
    echo "✅ Conda environment 'textS' found"
else
    echo "❌ Conda environment 'textS' not found"
    echo "   Please create it first: conda create -n textS python=3.10"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ app.py not found in current directory"
    echo "   Please run this script from: /Users/sunilverma/Text-Summarizer-Project"
    exit 1
fi

echo "✅ app.py found"
echo ""

# Check if port 8000 is available
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "⚠️  Port 8000 is already in use"
    echo "   Stop it with: pkill -f 'python app.py'"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""
echo "🚀 Starting Text Summarizer FastAPI Server..."
echo "   Server will be available at: http://localhost:8000"
echo ""
echo "📚 API Documentation: http://localhost:8000/docs"
echo "📝 ReDoc Documentation: http://localhost:8000/redoc"
echo ""
echo "Press CTRL+C to stop the server"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Activate conda and run the app
conda run -n textS python app.py
