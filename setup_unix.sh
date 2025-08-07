#!/bin/bash

echo "=== Finger Tracking and Counting Environment Setup (Linux/macOS) ==="
echo

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to find Python 3.10
find_python310() {
    local python_commands=("python3.10" "python310" "python3" "python")
    
    for cmd in "${python_commands[@]}"; do
        if command_exists "$cmd"; then
            version=$($cmd --version 2>&1)
            if [[ $version == *"Python 3.10"* ]]; then
                echo "$cmd"
                return 0
            fi
        fi
    done
    
    return 1
}

# Find Python 3.10
PYTHON_CMD=$(find_python310)

if [ $? -ne 0 ]; then
    echo "ERROR: Python 3.10 not found!"
    echo "Please install Python 3.10:"
    echo "  Ubuntu/Debian: sudo apt update && sudo apt install python3.10 python3.10-venv"
    echo "  macOS: brew install python@3.10"
    echo "  Or download from: https://www.python.org/downloads/"
    exit 1
fi

echo "Found Python 3.10: $PYTHON_CMD"
echo

# Remove existing environment if it exists
if [ -d "mp_env_310" ]; then
    echo "Removing existing environment..."
    rm -rf mp_env_310
fi

# Create virtual environment
echo "Creating virtual environment: mp_env_310"
$PYTHON_CMD -m venv mp_env_310
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment"
    exit 1
fi

# Activate environment
echo "Activating environment..."
source mp_env_310/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements
echo "Installing project requirements..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install requirements"
    exit 1
fi

echo
echo "=== Setup Complete! ==="
echo
echo "To activate the environment in the future, run:"
echo "  source mp_env_310/bin/activate"
echo
echo "To run the hand recognition:"
echo "  python hand_recognition.py"
echo
echo "Environment is now ready!"
