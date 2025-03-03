#!/bin/bash

# Create and activate virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Try installing with pip directly first
echo "Attempting to install dependencies with pip..."
pip install gradio pybaseball pandas numpy matplotlib

# If that fails, try installing with setup.py
if [ $? -ne 0 ]; then
    echo "Pip installation failed, trying setup.py..."
    pip install -e .
fi

echo "Installation complete. Run the application with: python app.py" 