# Cancer-Risk-Prediction-Model
 This project is part of a System Analysis and Design assignment where I designed, built, and deployed a cancer risk prediction API using machine learning and FastAPI and deployed it on AWS Bean Stalk

## Prediction Task: Risk Modeling
The goal is to model cancer risk using logistic regression and random forest classifiers. Given diagnostic features from breast mass images, the API predicts the likelihood of cancer (malignant vs. benign) with a probability score.

## Dataset
- **Name**: Wisconsin Diagnostic Breast Cancer (WDBC)
- **Source**: UCI Machine Learning Repository
- **Samples**: 569
- **Features**: 30 numeric diagnostic attributes
- **Target**: Binary label (0 = benign, 1 = malignant)

## Target Users
- Medical professionals and health researchers
- Health-tech developers building clinical tools
- Hospitals or clinics integrating risk prediction into diagnostic systems

## Expected Usage
- **Estimated Requests**: ~500 per day
- **Usage Pattern**: Real-time single prediction requests
- **Requirements**: Fast responses, secure API, easy integration via JSON
  
## Model Development
Two classification models were trained and evaluated:
- **Logistic Regression** (interpretable, fast)
- **Random Forest** (higher accuracy, better generalization)

### Final Model Metrics:
- **F1-Score**: `0.9703`
- **Precision**: `0.9878`
- **Recall**: `0.9535`
- **ROC-AUC**: `0.9986`
- **Log Loss**: `0.0793`
- **Brier Score**: `0.02`
