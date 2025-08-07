# Finger Tracking and Counting

Advanced real-time hand detection and finger counting system using MediaPipe and OpenCV with intelligent finger extension detection.

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
- **Robust thumb detection** with anatomy-specific logic
- **Edge case handling** for partially visible hands and partially curled fingers

### Display Features
- **Non-overlapping layout**: Left/right hand info on separate lines
- **Color-coded output**: Different colors for each hand and total count
- **Debug information**: Real-time finger status (T:True I:False M:True...)
- **Total count**: Combined finger count from both hands (0-10)

## How It Works

### MediaPipe Hand Detection
The system uses Google's MediaPipe framework to detect and track hands in real-time. MediaPipe identifies 21 key landmarks on each hand, including:
- **Wrist** (landmark 0): Base reference point
- **Finger joints**: MCP (knuckles), PIP (middle joints), DIP/IP (near fingertips)
- **Fingertips**: The endpoints we analyze for extension

### Multi-Criteria Finger Extension Analysis
Unlike simple distance-based counting, our system uses a sophisticated three-step verification process for each finger:

#### 1. Distance-Based Analysis
```
tip_distance_from_wrist > pip_distance_from_wrist × 1.1
```
The fingertip must be significantly farther from the wrist than the middle joint (PIP). This catches basic finger curling.

#### 2. Straightness Verification  
```
tip_to_pip_distance > mcp_to_pip_distance × 0.8
```
Ensures the finger segments are reasonably aligned, preventing false positives from bent-but-extended fingers.

#### 3. Palm-Pull Detection
```
tip_distance_from_wrist > mcp_distance_from_wrist × 0.7
```
Detects fingers that aren't curled but are pulled sideways into the palm - a common false positive case.

### Thumb-Specific Logic
Thumbs have different anatomy and movement patterns, so they use modified criteria:
- Lower straightness threshold (0.7 vs 0.8) due to natural thumb curvature
- Relaxed palm-pull detection (0.6 vs 0.7) for anatomical differences
- Additional MCP distance check for improved accuracy

### Real-Time Processing
The system processes each frame by:
1. Converting video to RGB for MediaPipe processing
2. Detecting up to 2 hands simultaneously
3. Extracting 21 landmarks per hand with pixel coordinates
4. Running extension analysis on all 5 fingers per hand
5. Aggregating counts and displaying results with visual feedback

## Quick Setup

### Automated Setup (Recommended)

**Windows**: Double-click `setup_windows.bat` or `run.bat`  
**Linux/macOS**: Run `./setup_unix.sh` or `./run.sh`  
**Cross-platform**: `python setup.py`

### Manual Setup

1. Install Python 3.10 from [python.org](https://www.python.org/downloads/)
2. Create environment: `python -m venv mp_env_310`
3. Activate: `mp_env_310\Scripts\activate` (Windows) or `source mp_env_310/bin/activate` (Linux/macOS)
4. Install: `pip install -r requirements.txt`

## Usage

1. Activate environment (if not using run scripts)
2. Run: `python hand_recognition.py`
3. Press 'q' to quit

### Display Layout
```
Total Fingers: X          (Green - Main count 0-10)
L:X + R:X                 (White - Hand breakdown)
Left: X                   (Cyan - Left hand count)
L: T:True I:False...      (White - Left finger details)
Right: X                  (Magenta - Right hand count)  
R: T:True I:False...      (White - Right finger details)
```

**Legend**: T=Thumb, I=Index, M=Middle, R=Ring, P=Pinky

## Algorithm Details

### Finger Extension Detection
Each finger is checked using three criteria:
1. **Distance Check**: Fingertip must be farther from wrist than PIP joint
2. **Straightness Check**: Finger segments must be reasonably aligned
3. **Palm-Pull Check**: Prevents counting fingers pulled sideways into palm

### Edge Cases Handled
- **Bent but extended fingers**: Caught by straightness verification
### Edge Cases Handled
- **Bent but extended fingers**: Caught by straightness verification
- **Fingers pulled into palm**: Detected by palm-pull algorithm
- **Partially visible hands**: Graceful handling of detection boundaries
- **False positives**: Multi-criteria approach reduces counting errors

## Requirements
- Python 3.10
- Webcam access
- Dependencies: opencv-contrib-python, mediapipe, numpy

## Technical Specifications

### MediaPipe Configuration
- **Detection confidence**: 0.7
- **Tracking confidence**: 0.5  
- **Max hands**: 2 (simultaneous tracking)
- **Hand landmarks**: 21 points per hand

### Performance Optimizations
- Real-time processing with optimized algorithms
- Efficient distance calculations using Euclidean geometry
- Minimal computational overhead for smooth video streaming

## Troubleshooting

**Python 3.10 not found**: Install from python.org and ensure it's in PATH  
**Camera issues**: Check permissions or try `cv2.VideoCapture(1)` for different camera  
**Package errors**: Ensure you're in activated environment, upgrade pip if needed

## Project Structure
```
├── hand_recognition.py    # Main application with advanced detection
├── requirements.txt       # Exact dependency versions
├── setup_windows.bat     # Windows automated setup
├── setup_unix.sh        # Linux/macOS automated setup  
├── run.bat/.sh          # One-click run scripts
└── README.md            # This documentation
```
