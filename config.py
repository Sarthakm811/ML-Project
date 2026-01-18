# Project Configuration

# Application Settings
APP_NAME = "Student Performance Predictor"
VERSION = "1.0.0"
DEBUG = False
HOST = "0.0.0.0"
PORT = 5000

# File Paths
ARTIFACTS_DIR = "artifacts"
MODEL_FILE = "model.pkl"
PREPROCESSOR_FILE = "preprocessor.pkl"
LOGS_DIR = "logs"

# Data Configuration
DATA_FILE = "notebook/data/stud.csv"
TEST_SIZE = 0.2
RANDOM_STATE = 42

# Model Configuration
TARGET_COLUMN = "math_score"
NUMERICAL_FEATURES = ["reading_score", "writing_score"]
CATEGORICAL_FEATURES = [
    "gender",
    "race_ethnicity",
    "parental_level_of_education",
    "lunch",
    "test_preparation_course"
]

# Model Performance Threshold
MIN_R2_SCORE = 0.6

# Feature Value Options
GENDER_OPTIONS = ["male", "female"]
ETHNICITY_OPTIONS = ["group A", "group B", "group C", "group D", "group E"]
EDUCATION_OPTIONS = [
    "some high school",
    "high school",
    "some college",
    "associate's degree",
    "bachelor's degree",
    "master's degree"
]
LUNCH_OPTIONS = ["standard", "free/reduced"]
TEST_PREP_OPTIONS = ["none", "completed"]

# Score Ranges
MIN_SCORE = 0
MAX_SCORE = 100
