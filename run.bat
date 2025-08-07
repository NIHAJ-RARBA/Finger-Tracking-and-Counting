# Run this script to quickly set up and run the project
@echo off
echo Starting Finger Tracking and Counting...
echo.

# Check if environment exists
if not exist mp_env_310 (
    echo Environment not found. Running setup...
    call setup_windows.bat
    if %errorlevel% neq 0 (
        echo Setup failed!
        pause
        exit /b 1
    )
)

# Activate environment and run
echo.
echo Activating environment and starting application...
call mp_env_310\Scripts\activate.bat
python hand_recognition.py

echo.
echo Application closed.
pause
