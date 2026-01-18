# ML Pipeline Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     Student Performance Predictor                │
│                         ML Pipeline System                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1. Training Pipeline Flow

```
┌──────────────┐
│  Raw Data    │
│  stud.csv    │
└──────┬───────┘
       │
       ▼
┌──────────────────────────┐
│   Data Ingestion         │
│ ─────────────────────    │
│ • Load CSV data          │
│ • Train/Test split (80/20)│
│ • Save artifacts         │
└──────────┬───────────────┘
       │
       ▼
┌──────────────────────────┐
│  Data Transformation     │
│ ─────────────────────    │
│ • Handle missing values  │
│ • Numerical: StandardScaler│
│ • Categorical: OneHotEncoder│
│ • Create preprocessor    │
└──────────┬───────────────┘
       │
       ▼
┌──────────────────────────┐
│   Model Training         │
│ ─────────────────────    │
│ • Train 8 ML models      │
│ • Hyperparameter tuning  │
│ • GridSearchCV           │
│ • Select best model      │
│ • Save model             │
└──────────┬───────────────┘
       │
       ▼
┌──────────────────────────┐
│     Artifacts            │
│ ─────────────────────    │
│ • model.pkl              │
│ • preprocessor.pkl       │
│ • train.csv              │
│ • test.csv               │
└──────────────────────────┘
```

---

## 2. Prediction Pipeline Flow

```
┌─────────────────┐
│   User Input    │
│   (Web Form)    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│   Flask Application     │
│ ─────────────────────   │
│ • Receive form data     │
│ • Create CustomData obj │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Data Preparation      │
│ ─────────────────────   │
│ • Convert to DataFrame  │
│ • Handle missing values │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Load Preprocessor     │
│ ─────────────────────   │
│ • Load preprocessor.pkl │
│ • Transform features    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│     Load Model          │
│ ─────────────────────   │
│ • Load model.pkl        │
│ • Make prediction       │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Display Result        │
│ ─────────────────────   │
│ • Render template       │
│ • Show predicted score  │
└─────────────────────────┘
```

---

## 3. Component Architecture

```
┌───────────────────────────────────────────────────────┐
│                    Application Layer                   │
│  ┌──────────────────────────────────────────────┐    │
│  │              app.py (Flask)                   │    │
│  │  • Routes: /, /predictdata                    │    │
│  │  • Template rendering                         │    │
│  └──────────────────────────────────────────────┘    │
└────────────────────┬──────────────────────────────────┘
                     │
┌────────────────────┴──────────────────────────────────┐
│                   Pipeline Layer                       │
│  ┌────────────────────────┐  ┌────────────────────┐  │
│  │  predict_pipline.py    │  │  train_pipline.py  │  │
│  │  • CustomData          │  │  • Training flow   │  │
│  │  • PredictPipeline     │  │                    │  │
│  └────────────────────────┘  └────────────────────┘  │
└────────────────────┬──────────────────────────────────┘
                     │
┌────────────────────┴──────────────────────────────────┐
│                  Component Layer                       │
│  ┌────────────────┐ ┌──────────────────┐ ┌─────────┐ │
│  │ data_ingestion │ │data_transformation│ │  model  │ │
│  │     .py        │ │       .py         │ │ trainer │ │
│  │                │ │                   │ │  .py    │ │
│  └────────────────┘ └──────────────────┘ └─────────┘ │
└────────────────────┬──────────────────────────────────┘
                     │
┌────────────────────┴──────────────────────────────────┐
│                    Utility Layer                       │
│  ┌────────────┐  ┌────────────┐  ┌──────────────┐   │
│  │ exception  │  │  logger    │  │    utils     │   │
│  │    .py     │  │    .py     │  │     .py      │   │
│  └────────────┘  └────────────┘  └──────────────┘   │
└───────────────────────────────────────────────────────┘
```

---

## 4. Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        INPUT FEATURES                        │
├──────────────────┬──────────────────────────────────────────┤
│   Categorical    │           Numerical                      │
├──────────────────┼──────────────────────────────────────────┤
│ • gender         │ • reading_score                          │
│ • race_ethnicity │ • writing_score                          │
│ • parental_edu   │                                          │
│ • lunch          │                                          │
│ • test_prep      │                                          │
└──────────┬───────┴─────────┬────────────────────────────────┘
           │                 │
           ▼                 ▼
    ┌─────────────┐   ┌─────────────┐
    │ OneHotEncoder│   │StandardScaler│
    │             │   │              │
    └──────┬──────┘   └──────┬───────┘
           │                 │
           └────────┬────────┘
                    │
                    ▼
         ┌──────────────────┐
         │ ColumnTransformer│
         │   (Preprocessor) │
         └─────────┬────────┘
                   │
                   ▼
         ┌──────────────────┐
         │  Transformed     │
         │    Features      │
         └─────────┬────────┘
                   │
                   ▼
         ┌──────────────────┐
         │   ML Model       │
         │  (Best of 8)     │
         └─────────┬────────┘
                   │
                   ▼
         ┌──────────────────┐
         │   PREDICTION     │
         │  (Math Score)    │
         └──────────────────┘
```

---

## 5. Model Selection Process

```
┌───────────────────────────────────────────────────────────┐
│                    Training Phase                          │
└───────────────────────────────────────────────────────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
    ┌─────────▼────────┐    ┌───────▼────────┐
    │  Model Training  │    │ Hyperparameter │
    │   with GridCV    │    │    Tuning      │
    └─────────┬────────┘    └───────┬────────┘
              │                     │
              └──────────┬──────────┘
                         │
          ┌──────────────▼──────────────┐
          │     Models Evaluated:       │
          ├─────────────────────────────┤
          │ 1. Random Forest            │
          │ 2. Decision Tree            │
          │ 3. Gradient Boosting        │
          │ 4. Linear Regression        │
          │ 5. XGBoost                  │
          │ 6. CatBoost                 │
          │ 7. AdaBoost                 │
          │ 8. KNeighbors               │
          └──────────────┬──────────────┘
                         │
              ┌──────────▼──────────┐
              │  R² Score Comparison │
              │   (Test Set)        │
              └──────────┬──────────┘
                         │
              ┌──────────▼──────────┐
              │  Select Best Model  │
              │   (Highest R²)      │
              └──────────┬──────────┘
                         │
              ┌──────────▼──────────┐
              │   Save to Disk      │
              │   (model.pkl)       │
              └─────────────────────┘
```

---

## 6. Web Application Flow

```
┌──────────┐         ┌──────────┐         ┌──────────┐
│  User    │ ──────> │  Browser │ ──────> │  Flask   │
│          │         │          │         │   App    │
└──────────┘         └──────────┘         └────┬─────┘
                                                │
     GET /                                      │
     ◄──────────────────────────────────────────┘
     index.html (Landing Page)
                                                
     GET /predictdata                           │
     ◄──────────────────────────────────────────┘
     home.html (Form)
                                                
     POST /predictdata                          │
     (Form Data) ──────────────────────────────>│
                                                 │
                                     ┌───────────▼──────────┐
                                     │ CustomData creation  │
                                     └───────────┬──────────┘
                                                 │
                                     ┌───────────▼──────────┐
                                     │ Load preprocessor    │
                                     └───────────┬──────────┘
                                                 │
                                     ┌───────────▼──────────┐
                                     │ Load model           │
                                     └───────────┬──────────┘
                                                 │
                                     ┌───────────▼──────────┐
                                     │ Make prediction      │
                                     └───────────┬──────────┘
     ◄──────────────────────────────────────────┘
     home.html (with result)
```

---

## 7. Technology Stack

```
┌────────────────────────────────────────────────────┐
│                  Frontend Layer                     │
│  • HTML5                                            │
│  • CSS3 (Embedded styling)                         │
│  • Responsive Design                               │
└────────────┬───────────────────────────────────────┘
             │
┌────────────▼───────────────────────────────────────┐
│                 Backend Layer                       │
│  • Flask 2.x (Web Framework)                       │
│  • Python 3.8+                                     │
└────────────┬───────────────────────────────────────┘
             │
┌────────────▼───────────────────────────────────────┐
│            Machine Learning Layer                   │
│  • Scikit-learn (Models & Preprocessing)           │
│  • XGBoost (Gradient Boosting)                     │
│  • CatBoost (Gradient Boosting)                    │
│  • Pandas (Data manipulation)                      │
│  • NumPy (Numerical operations)                    │
└────────────┬───────────────────────────────────────┘
             │
┌────────────▼───────────────────────────────────────┐
│              Persistence Layer                      │
│  • Dill (Model serialization)                      │
│  • CSV (Data storage)                              │
└────────────┬───────────────────────────────────────┘
             │
┌────────────▼───────────────────────────────────────┐
│             Infrastructure Layer                    │
│  • Docker (Containerization)                       │
│  • Docker Compose (Orchestration)                  │
└────────────────────────────────────────────────────┘
```

---

## 8. Deployment Architecture

```
                    ┌──────────────┐
                    │   Developer  │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   Git Repo   │
                    └──────┬───────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    ┌────▼────┐      ┌────▼────┐      ┌────▼────┐
    │  Local  │      │ Docker  │      │  Cloud  │
    │  Deploy │      │ Deploy  │      │ Deploy  │
    └─────────┘      └────┬────┘      └────┬────┘
                          │                 │
                   ┌──────▼──────┐   ┌─────▼─────┐
                   │  Container  │   │   AWS     │
                   │   Runtime   │   │  Heroku   │
                   └─────────────┘   │  Azure    │
                                     │   GCP     │
                                     └───────────┘
```

---

*This architecture provides a complete overview of the system design and data flow.*
