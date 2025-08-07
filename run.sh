#!/bin/bash
# Run this script to quickly set up and run the project

echo "Starting Finger Tracking and Counting..."
echo

# Check if environment exists
if [ ! -d "mp_env_310" ]; then
    echo "Environment not found. Running setup..."
    ./setup_unix.sh
    if [ $? -ne 0 ]; then
        echo "Setup failed!"
        exit 1
    fi
fi

# Activate environment and run
echo
echo "Activating environment and starting application..."
source mp_env_310/bin/activate
python hand_recognition.py

echo
echo "Application closed."
