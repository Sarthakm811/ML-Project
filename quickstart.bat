@echo off
REM Quick Start Script for Student Performance Predictor (Windows)

echo ========================================
echo Student Performance Predictor
echo Quick Start Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo [1/5] Checking Python installation...
python --version
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo [2/5] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
) else (
    echo [2/5] Virtual environment already exists
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo.

REM Install dependencies
echo [4/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Check if model exists
if not exist "artifacts\model.pkl" (
    echo [5/5] Model not found. Training model...
    echo This may take a few minutes...
    python -m src.pipline.train_pipline
    if errorlevel 1 (
        echo ERROR: Model training failed
        pause
        exit /b 1
    )
) else (
    echo [5/5] Model already exists, skipping training
)
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Starting Flask application...
echo The app will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

python app.py
