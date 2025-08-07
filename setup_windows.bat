@echo off
echo === Finger Tracking and Counting Environment Setup (Windows) ===
echo.

REM Check if Python 3.10 is available
python --version 2>&1 | findstr "Python 3.10" >nul
if %errorlevel% == 0 (
    set PYTHON_CMD=python
    goto :create_env
)

REM Try py launcher with 3.10
py -3.10 --version 2>&1 | findstr "Python 3.10" >nul
if %errorlevel% == 0 (
    set PYTHON_CMD=py -3.10
    goto :create_env
)

REM Try python3.10
python3.10 --version 2>&1 | findstr "Python 3.10" >nul
if %errorlevel% == 0 (
    set PYTHON_CMD=python3.10
    goto :create_env
)

echo ERROR: Python 3.10 not found!
echo Please install Python 3.10 from https://www.python.org/downloads/
echo Make sure to check "Add Python to PATH" during installation
pause
exit /b 1

:create_env
echo Found Python 3.10: %PYTHON_CMD%
echo.

REM Remove existing environment if it exists
if exist mp_env_310 (
    echo Removing existing environment...
    rmdir /s /q mp_env_310
)

REM Create virtual environment
echo Creating virtual environment: mp_env_310
%PYTHON_CMD% -m venv mp_env_310
if %errorlevel% neq 0 (
    echo Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate environment and install requirements
echo.
echo Activating environment and installing requirements...
call mp_env_310\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing project requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements
    pause
    exit /b 1
)

echo.
echo === Setup Complete! ===
echo.
echo To activate the environment in the future, run:
echo   mp_env_310\Scripts\activate.bat
echo.
echo To run the hand recognition:
echo   python hand_recognition.py
echo.
echo Environment is now ready!
pause
