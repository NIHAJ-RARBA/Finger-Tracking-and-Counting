# Finger Tracking and Counting - Environment Setup

This project provides a computer vision-based finger tracking and counting system using MediaPipe and OpenCV.

## Prerequisites

- Python 3.10 (required for compatibility)
- Webcam/Camera access
- Windows, macOS, or Linux

## Quick Setup

### For a New Device (Complete Reproducibility):

1. **Clone/Download this repository**
2. **Run the appropriate setup script**:

#### Windows:
```bash
# Option 1: Double-click setup_windows.bat
# Option 2: Run in Command Prompt/PowerShell
setup_windows.bat

# Or for one-click setup and run:
run.bat
```

#### Linux/macOS:
```bash
# Make executable and run
chmod +x setup_unix.sh
./setup_unix.sh

# Or for one-click setup and run:
chmod +x run.sh
./run.sh
```

#### Cross-platform Python script:
```bash
python setup.py
```

### What the setup scripts do:

1. **Check for Python 3.10** - Tries multiple Python commands to find 3.10.x
2. **Remove existing environment** (if any) - Ensures clean installation
3. **Create `mp_env_310` virtual environment** - Exact same name as original
4. **Install exact package versions** - From requirements.txt with pinned versions
5. **Ready to run** - Environment is immediately usable

### One-Command Execution:

After initial setup, use these for future runs:

**Windows**: `run.bat`  
**Linux/macOS**: `./run.sh`

These scripts will:
- Check if environment exists (run setup if not)
- Activate environment
- Run the application

### Option 2: Manual Setup

1. **Install Python 3.10** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)
   - Ensure Python 3.10.x is installed

2. **Create virtual environment**:
   ```bash
   # Windows
   python -m venv mp_env_310
   mp_env_310\Scripts\activate

   # Linux/macOS
   python3.10 -m venv mp_env_310
   source mp_env_310/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Running the Application

1. **Activate the environment**:
   ```bash
   # Windows
   mp_env_310\Scripts\activate

   # Linux/macOS
   source mp_env_310/bin/activate
   ```

2. **Run the finger tracking**:
   ```bash
   python hand_recognition.py
   ```

3. **Exit**: Press 'q' to quit the application

## Environment Details

- **Environment Name**: `mp_env_310`
- **Python Version**: 3.10.x
- **Key Dependencies**:
  - opencv-contrib-python==4.11.0.86
  - mediapipe==0.10.5
  - numpy==1.26.4

## Features

- Real-time hand detection and tracking
- Finger counting (0-5 per hand)
- Support for multiple hands
- Visual feedback with hand landmarks
- Optimized finger extension detection

## Troubleshooting

### Python 3.10 Not Found
- Ensure Python 3.10 is installed and in PATH
- Try using `py -3.10` (Windows) or `python3.10` (Linux/macOS)

### Camera Access Issues
- Ensure camera permissions are granted
- Check if another application is using the camera
- Try changing camera index in `hand_recognition.py` (line 14): `cap = cv2.VideoCapture(1)`

### Package Installation Errors
- Ensure you're in the activated virtual environment
- Try upgrading pip: `python -m pip install --upgrade pip`
- For Windows, ensure Visual C++ Build Tools are installed

## Project Structure

```
Finger-Tracking-and-Counting/
├── hand_recognition.py      # Main application
├── requirements.txt         # Python dependencies
├── setup.py                # Cross-platform setup script
├── setup_windows.bat       # Windows setup script
├── setup_unix.sh          # Linux/macOS setup script
├── README.md              # This file
└── mp_env_310/            # Virtual environment (created after setup)
```

## Reproduction on New Device

1. Clone/download this repository
2. Run the appropriate setup script for your OS
3. The environment will be created with the exact same name and dependencies
4. No manual configuration required

This ensures 100% reproducibility across different devices and operating systems.
