# Cancer-Risk-Prediction-Model
This project is part of a System Analysis and Design assignment where I designed, built, and deployed a cancer risk prediction API using machine learning and FastAPI and deployed it on AWS Bean Stalk

## Prediction Task: Risk Modeling
The goal is to predict cancer risk using logistic regression and random forest classifiers. Given diagnostic features from breast mass data, the API predicts the likelihood of cancer (malignant vs. benign) with a probability score from 0 to 1.

## Dataset
- **Source**: Brest Cancer Dataset from Kagel [https://www.kaggle.com/datasets/erdemtaha/cancer-data]
- **Features**: 30 numeric diagnostic attributes
- **Target**: Binary label (0 = benign, 1 = malignant)

## Target Users
- Medical professionals and health researchers
- Hospitals or clinics using risk prediction into diagnostic systems

## Expected Usage
- **Estimated Requests**: approx. 500 per day
- **Usage Pattern**: Real-time data collected single prediction requests
- **Requirements**: Fast responses, secure API, effortlessly via JSON
  
## Model Development
Two classification models were trained and evaluated:
- **Logistic Regression** (interpretable, fast)
- **Random Forest** (higher accuracy, better generalization)

### Final Averaged Model Metrics:
- **F1-Score**: `0.9703`
- **Precision**: `0.9878`
- **Recall**: `0.9535`
- **ROC-AUC**: `0.9986`
- **Log Loss**: `0.0793`
- **Brier Score**: `0.02`

## Author
**Mirza Mustafa Ali Khan**
- **Docker Hub** (mirzamustafaalikhan/cancer-risk-model) 
- **LinkedIn** (www.linkedin.com/in/mirza-mustafa-ali-khan-711043267)
- **Docker Image** [docker pull mirzamustafaalikhan/cancer-risk-model:latest]
- **AWS LINK** [https://ca-central-1.console.aws.amazon.com/elasticbeanstalk/home?region=ca-central-1#/environment/dashboard?environmentId=e-s4ujjswrp6]
