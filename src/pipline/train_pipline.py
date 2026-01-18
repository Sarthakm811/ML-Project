"""
Complete Training Pipeline
Run this script to train the model from scratch
"""

import sys
import os
from src.logger import logging
from src.exception import CustomException

def run_training_pipeline():
    """
    Execute the complete training pipeline:
    1. Data Ingestion
    2. Data Transformation
    3. Model Training
    """
    try:
        logging.info("=" * 60)
        logging.info("Starting Training Pipeline")
        logging.info("=" * 60)
        
        # Step 1: Data Ingestion
        logging.info("Step 1: Data Ingestion")
        from src.components.data_ingestion import DataIngestion
        
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        logging.info(f"Train data path: {train_data_path}")
        logging.info(f"Test data path: {test_data_path}")
        
        # Step 2: Data Transformation
        logging.info("Step 2: Data Transformation")
        from src.components.data_transformation import DataTransformation
        
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
            train_data_path, 
            test_data_path
        )
        
        logging.info(f"Training array shape: {train_arr.shape}")
        logging.info(f"Testing array shape: {test_arr.shape}")
        logging.info(f"Preprocessor saved at: {preprocessor_path}")
        
        # Step 3: Model Training
        logging.info("Step 3: Model Training")
        from src.components.model_trainer import ModelTrainer
        
        model_trainer = ModelTrainer()
        r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
        
        logging.info("=" * 60)
        logging.info(f"Training Complete! R2 Score: {r2_score:.4f}")
        logging.info("=" * 60)
        
        print("\n" + "=" * 60)
        print("✅ TRAINING PIPELINE COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print(f"📊 Model Performance (R² Score): {r2_score:.4f}")
        print(f"📁 Model saved at: artifacts/model.pkl")
        print(f"📁 Preprocessor saved at: artifacts/preprocessor.pkl")
        print("=" * 60)
        print("\n🚀 You can now run the Flask app: python app.py")
        
        return r2_score
        
    except Exception as e:
        logging.error("Training pipeline failed")
        raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        score = run_training_pipeline()
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Training failed: {str(e)}")
        sys.exit(1)
