# Finger Tracking and Counting

A sophisticated real-time hand detection and finger counting system utilizing MediaPipe and OpenCV with advanced finger extension detection algorithms.

Originally built a be part of a MicroController Project to set/unset traps numbered 1-5. Excluded in revised project plans in favour of a more hardware focused approach.

## Overview

This application provides accurate finger counting capabilities through computer vision techniques, supporting simultaneous tracking of both hands with intelligent detection algorithms that handle edge cases commonly found in gesture recognition systems.

## Features

### Core Functionality
- **Real-time hand tracking** with webcam input
- **Accurate finger counting** (0-10 total, 0-5 per hand)
- **Dual hand support** with separate left/right tracking
- **Visual feedback** with hand landmark overlays

### Advanced Detection Algorithm
- **Multi-criteria finger extension detection**:
  - Distance-based analysis (tip vs knuckle distance from wrist)
  - Straightness verification (prevents counting bent fingers)
  - Palm-pull detection (catches fingers pulled sideways into palm)
- Robust thumb detection with anatomy-specific logic
- Comprehensive edge case handling for partially visible hands and partially curled fingers

### Display Interface
- Non-overlapping layout with left/right hand information on separate lines
- Color-coded output differentiating each hand and total count
- Real-time debug information displaying finger status
- Combined finger count from both hands (0-10)

## Technical Implementation

### MediaPipe Hand Detection
The system uses Google's MediaPipe framework to detect and track hands in real-time. MediaPipe identifies 21 key landmarks on each hand, including:
- **Wrist** (landmark 0): Base reference point
- **Finger joints**: MCP (knuckles), PIP (middle joints), DIP/IP (near fingertips)
- **Fingertips**: The endpoints we analyze for extension

### Multi-Criteria Finger Extension Analysis
The system implements a sophisticated three-step verification process for each finger, surpassing simple distance-based counting methods:

#### Distance-Based Analysis
```
tip_distance_from_wrist > pip_distance_from_wrist × 1.1
```
Validates that the fingertip is significantly farther from the wrist than the middle joint (PIP), effectively detecting basic finger curling.

#### Straightness Verification
```
tip_to_pip_distance > mcp_to_pip_distance × 0.8
```
Ensures finger segments maintain reasonable alignment, preventing false positives from bent-but-extended fingers.

#### Palm-Pull Detection
```
tip_distance_from_wrist > mcp_distance_from_wrist × 0.7
```
Identifies fingers that are not curled but are pulled laterally into the palm, addressing a common source of false positives.

### Thumb-Specific Algorithm
Thumb detection utilizes modified criteria accounting for anatomical differences and movement patterns:
- Reduced straightness threshold (0.7 vs 0.8) accommodating natural thumb curvature
- Relaxed palm-pull detection (0.6 vs 0.7) for anatomical variance
- Additional MCP distance verification for enhanced accuracy

### Processing Pipeline
The system processes each video frame through the following workflow:
1. Video frame conversion to RGB format for MediaPipe processing
2. Detection of up to 2 hands simultaneously
3. Extraction of 21 landmarks per hand with pixel coordinate mapping
4. Extension analysis execution on all 5 fingers per hand
5. Count aggregation and result display with visual feedback overlay

## Installation and Setup

### Automated Installation (Recommended)

**Windows**: Execute `setup_windows.bat` or `run.bat`  
**Linux/macOS**: Execute `./setup_unix.sh` or `./run.sh`  
**Cross-platform**: Execute `python setup.py`

### Manual Installation

1. Install Python 3.10 from [python.org](https://www.python.org/downloads/)
2. Create virtual environment: `python -m venv mp_env_310`
3. Activate environment: 
   - Windows: `mp_env_310\Scripts\activate`
   - Linux/macOS: `source mp_env_310/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage Instructions

1. Activate environment (if not using run scripts)
2. Run: `python hand_recognition.py`
3. Press 'q' to quit

### Display Interface Layout
```
Total Fingers: X          (Green - Primary count 0-10)
L:X + R:X                 (White - Hand breakdown)
Left: X                   (Cyan - Left hand count)
L: T:True I:False...      (White - Left finger status)
Right: X                  (Magenta - Right hand count)  
R: T:True I:False...      (White - Right finger status)
```

**Status Legend**: T=Thumb, I=Index, M=Middle, R=Ring, P=Pinky

## Algorithm Specification

### Finger Extension Detection Criteria
Each finger undergoes evaluation using three distinct criteria:
1. **Distance Verification**: Fingertip must be positioned farther from wrist than PIP joint
2. **Straightness Assessment**: Finger segments must maintain reasonable alignment
3. **Palm-Pull Prevention**: Eliminates counting of fingers pulled laterally into palm

### Edge Case Management
- **Bent extended fingers**: Detected through straightness verification algorithms
- **Palm-retracted fingers**: Identified via palm-pull detection mechanisms
- **Partially visible hands**: Handled through graceful detection boundary management
- **False positive reduction**: Achieved through multi-criteria validation approach

## System Requirements
- Python 3.10 or higher
- Webcam or camera device access
- Core dependencies: opencv-contrib-python, mediapipe, numpy

## Technical Specifications

### MediaPipe Configuration Parameters
- **Detection confidence threshold**: 0.7
- **Tracking confidence threshold**: 0.5  
- **Maximum concurrent hands**: 2
- **Hand landmark points**: 21 per hand

### Performance Characteristics
- Real-time processing with optimized computational algorithms
- Efficient Euclidean distance calculations for geometric analysis
- Minimal computational overhead maintaining smooth video stream processing

## Troubleshooting

**Python 3.10 installation issues**: Verify installation from python.org and PATH configuration  
**Camera access problems**: Verify device permissions or modify camera index using `cv2.VideoCapture(1)`  
**Package installation errors**: Ensure virtual environment activation and pip upgrade if necessary

## Project Architecture
```
├── hand_recognition.py    # Primary application with advanced detection algorithms
├── requirements.txt       # Dependency specifications with version pinning
├── setup_windows.bat     # Windows automated installation script
├── setup_unix.sh        # Linux/macOS automated installation script  
├── run.bat/.sh          # One-click execution scripts
└── README.md            # Project documentation
```
