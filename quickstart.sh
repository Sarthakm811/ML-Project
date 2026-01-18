#!/bin/bash
# Quick Start Script for Student Performance Predictor (Linux/Mac)

echo "========================================"
echo "Student Performance Predictor"
echo "Quick Start Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[1/5] Checking Python installation..."
python3 --version
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[2/5] Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
    echo "Virtual environment created successfully"
else
    echo "[2/5] Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "[3/5] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate virtual environment"
    exit 1
fi
echo ""

# Install dependencies
echo "[4/5] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo ""

# Check if model exists
if [ ! -f "artifacts/model.pkl" ]; then
    echo "[5/5] Model not found. Training model..."
    echo "This may take a few minutes..."
    python -m src.pipline.train_pipline
    if [ $? -ne 0 ]; then
        echo "ERROR: Model training failed"
        exit 1
    fi
else
    echo "[5/5] Model already exists, skipping training"
fi
echo ""

echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Starting Flask application..."
echo "The app will be available at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""
echo "========================================"
echo ""

python app.py
