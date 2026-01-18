"""
Test script for the ML Project
Run this to verify all components are working correctly
"""

import sys
import os
import pandas as pd
import numpy as np

def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    try:
        import flask
        import sklearn
        import pandas
        import numpy
        import dill
        import catboost
        import xgboost
        print("✓ All required packages imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_project_structure():
    """Test if all required directories and files exist"""
    print("\nTesting project structure...")
    required_files = [
        'app.py',
        'requirements.txt',
        'setup.py',
        'src/__init__.py',
        'src/exception.py',
        'src/logger.py',
        'src/utils.py',
        'templates/home.html',
        'templates/index.html',
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path} exists")
        else:
            print(f"✗ {file_path} missing")
            all_exist = False
    
    return all_exist

def test_artifacts():
    """Test if model artifacts exist"""
    print("\nTesting model artifacts...")
    artifacts = [
        'artifacts/model.pkl',
        'artifacts/preprocessor.pkl',
    ]
    
    all_exist = True
    for artifact in artifacts:
        if os.path.exists(artifact):
            print(f"✓ {artifact} exists")
        else:
            print(f"✗ {artifact} missing (run training first)")
            all_exist = False
    
    return all_exist

def test_prediction_pipeline():
    """Test prediction pipeline with sample data"""
    print("\nTesting prediction pipeline...")
    try:
        from src.pipline.predict_pipline import CustomData, PredictPipeline
        
        # Create sample data
        sample_data = CustomData(
            gender='male',
            race_ethnicity='group B',
            parental_level_of_education="bachelor's degree",
            lunch='standard',
            test_preparation_course='none',
            reading_score=72,
            writing_score=74
        )
        
        # Get dataframe
        df = sample_data.get_data_as_data_frame()
        print(f"✓ Created sample dataframe: {df.shape}")
        
        # Make prediction if artifacts exist
        if os.path.exists('artifacts/model.pkl'):
            pipeline = PredictPipeline()
            prediction = pipeline.predict(df)
            print(f"✓ Prediction successful: {prediction[0]:.2f}")
            return True
        else:
            print("⚠ Skipping prediction test (model not trained)")
            return True
            
    except Exception as e:
        print(f"✗ Prediction pipeline error: {e}")
        return False

def test_flask_app():
    """Test if Flask app can be initialized"""
    print("\nTesting Flask application...")
    try:
        from app import app
        print(f"✓ Flask app initialized: {app.name}")
        
        # Test routes
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code == 200:
                print("✓ Home route working")
            else:
                print(f"✗ Home route failed: {response.status_code}")
                return False
                
            response = client.get('/predictdata')
            if response.status_code == 200:
                print("✓ Predict route working")
            else:
                print(f"✗ Predict route failed: {response.status_code}")
                return False
        
        return True
    except Exception as e:
        print(f"✗ Flask app error: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("STUDENT PERFORMANCE PREDICTOR - TEST SUITE")
    print("=" * 60)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Project Structure", test_project_structure()))
    results.append(("Artifacts", test_artifacts()))
    results.append(("Prediction Pipeline", test_prediction_pipeline()))
    results.append(("Flask Application", test_flask_app()))
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "PASSED" if result else "FAILED"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {test_name}: {status}")
    
    print("=" * 60)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
