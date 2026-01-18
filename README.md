# Student Performance Prediction - ML Project

## 📊 Project Overview
This project predicts student math scores based on various demographic and academic features using machine learning. The application uses a Flask web interface for easy interaction.

## 🎯 Features
- **Data Ingestion**: Automated data loading and train-test split
- **Data Transformation**: Preprocessing pipeline with scaling and encoding
- **Model Training**: Multiple ML algorithms with hyperparameter tuning
- **Web Interface**: User-friendly Flask application for predictions
- **Logging & Exception Handling**: Comprehensive error tracking and logging

## 🚀 Technologies Used
- **Python 3.8+**
- **Flask** - Web framework
- **Scikit-learn** - Machine learning library
- **Pandas & NumPy** - Data manipulation
- **CatBoost, XGBoost** - Gradient boosting algorithms
- **Dill** - Object serialization

## 📁 Project Structure
```
├── app.py                      # Flask application
├── requirements.txt            # Project dependencies
├── setup.py                   # Package setup
├── artifacts/                 # Trained models and data
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   └── test.csv
├── notebook/                  # Jupyter notebooks for EDA
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipline/
│   │   ├── predict_pipline.py
│   │   └── train_pipline.py
│   ├── exception.py           # Custom exception handling
│   ├── logger.py              # Logging configuration
│   └── utils.py               # Utility functions
└── templates/                 # HTML templates
    ├── home.html
    └── index.html

```

## 🔧 Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ML Project
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Training the Model
Run the training pipeline:
```bash
# Run the training pipeline
python -m src.pipline.train_pipline

# Or run data_ingestion directly (includes full pipeline)
python src/components/data_ingestion.py
```

### Running the Web Application
```bash
python app.py
```
The application will be available at `http://localhost:5000`

### Making Predictions
1. Navigate to `http://localhost:5000`
2. Click on "Predict Student Performance"
3. Fill in the student information form
4. Submit to get math score prediction

## 📊 Model Performance
The project trains and evaluates multiple models:
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor
- KNeighbors Regressor

The best performing model is automatically selected and saved.

## 📝 Input Features
- **Gender**: Male/Female
- **Race/Ethnicity**: Group A-E
- **Parental Level of Education**: Various education levels
- **Lunch Type**: Standard/Free or Reduced
- **Test Preparation Course**: None/Completed
- **Reading Score**: 0-100
- **Writing Score**: 0-100

## 🎯 Target Variable
- **Math Score**: Predicted score (0-100)

## 🐳 Docker Support
Build and run with Docker:
```bash
docker build -t student-performance-app .
docker run -p 5000:5000 student-performance-app
```

## 📜 License
This project is open source and available under the MIT License.

## 👨‍💻 Author
**Sarthak Mahajan**
- Email: sarthakm811@gmail.com

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!