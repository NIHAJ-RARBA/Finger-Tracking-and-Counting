"""
Setup script for Finger Tracking and Counting project
This script ensures Python 3.10 is installed and creates the exact environment
"""
import subprocess
import sys
import os
import platform

def check_python_version():
    """Check if Python 3.10 is available"""
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        version = result.stdout.strip()
        print(f"Current Python version: {version}")
        
        # Check if it's Python 3.10.x
        if "Python 3.10" in version:
            return True
        else:
            print("Python 3.10 not found as default interpreter")
            return False
    except Exception as e:
        print(f"Error checking Python version: {e}")
        return False

def find_python310():
    """Try to find Python 3.10 installation"""
    possible_commands = [
        "python3.10",
        "python310",
        "py -3.10",
        "python"
    ]
    
    for cmd in possible_commands:
        try:
            result = subprocess.run([cmd, "--version"], capture_output=True, text=True)
            if "Python 3.10" in result.stdout:
                print(f"Found Python 3.10 at: {cmd}")
                return cmd
        except:
            continue
    
    return None

def create_environment():
    """Create virtual environment with Python 3.10"""
    python_cmd = find_python310()
    
    if not python_cmd:
        print("ERROR: Python 3.10 not found!")
        print("Please install Python 3.10 from https://www.python.org/downloads/")
        return False
    
    env_name = "mp_env_310"
    
    # Remove existing environment if it exists
    if os.path.exists(env_name):
        print(f"Removing existing environment: {env_name}")
        if platform.system() == "Windows":
            subprocess.run(f"rmdir /s /q {env_name}", shell=True)
        else:
            subprocess.run(f"rm -rf {env_name}", shell=True)
    
    # Create new environment
    print(f"Creating virtual environment: {env_name}")
    result = subprocess.run([python_cmd, "-m", "venv", env_name])
    
    if result.returncode != 0:
        print("Failed to create virtual environment")
        return False
    
    return True

def install_requirements():
    """Install requirements in the virtual environment"""
    env_name = "mp_env_310"
    
    if platform.system() == "Windows":
        pip_path = os.path.join(env_name, "Scripts", "pip.exe")
        python_path = os.path.join(env_name, "Scripts", "python.exe")
    else:
        pip_path = os.path.join(env_name, "bin", "pip")
        python_path = os.path.join(env_name, "bin", "python")
    
    # Upgrade pip first
    print("Upgrading pip...")
    subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"])
    
    # Install requirements
    print("Installing requirements...")
    result = subprocess.run([pip_path, "install", "-r", "requirements.txt"])
    
    if result.returncode == 0:
        print("Requirements installed successfully!")
        return True
    else:
        print("Failed to install requirements")
        return False

def main():
    """Main setup function"""
    print("=== Finger Tracking and Counting Environment Setup ===")
    print()
    
    # Step 1: Create environment
    if not create_environment():
        sys.exit(1)
    
    # Step 2: Install requirements
    if not install_requirements():
        sys.exit(1)
    
    print()
    print("=== Setup Complete! ===")
    print()
    print("To activate the environment:")
    if platform.system() == "Windows":
        print("  .\\mp_env_310\\Scripts\\activate")
    else:
        print("  source mp_env_310/bin/activate")
    
    print()
    print("To run the hand recognition:")
    print("  python hand_recognition.py")

if __name__ == "__main__":
    main()
