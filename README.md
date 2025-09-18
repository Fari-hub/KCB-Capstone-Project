 Dropout Risk Prediction in Schools
📌 Project Overview
This project uses machine learning to predict dropout risk in public schools based on school-level indicators such as funding, test scores, and demographics. The goal is to support early intervention strategies and promote educational equity, especially in under-resourced contexts.

🧠 Problem Statement
Dropout rates remain a critical challenge in public education. Identifying at-risk students early can help direct resources and support where they’re needed most. This model aims to flag schools with elevated dropout risk using interpretable, data-driven methods.

🧪 Methodology

🔹 Data Preprocessing
- Handled missing values through imputation and deletion
- Encoded categorical variables (`grade_level`, `school_type`, `state`)
- Scaled numerical features using `StandardScaler`

🔹 Feature Engineering
- Created `funding_per_score` to measure funding efficiency
- Defined binary target `dropout_risk` based on dropout rate threshold (>10%)

🔹 Model Training
- Applied SMOTE to balance class distribution
- Trained a `RandomForestClassifier` with `class_weight='balanced'`
- Used 80/20 train-test split with fixed random seed

🔹 Model Optimization
- Performed grid search with 5-fold cross-validation
- Tuned `n_estimators`, `max_depth`, and `min_samples_split`
- Selected best model based on F1-score

📊 Evaluation Metrics

| Metric      | Class 0 (No Risk) | Class 1 (Risk) |
|-------------|-------------------|----------------|
| Precision   | 0.61              | 0.36           |
| Recall      | 0.80              | 0.18           |
| F1-Score    | 0.69              | 0.24           |
| Accuracy    | 56%               | —              |

> The model correctly predicted 112 out of 200 test samples. While performance on the majority class is strong, recall for dropout risk cases remains limited, highlighting the need for further optimization.

📈 Optimization Results

Best hyperparameter configuration:
```python
{'max_depth': 20, 'min_samples_split': 5, 'n_estimators': 100}
Mean F1 Score: 0.144
🚀 Future Work
- Deploy model as a web app using Flask or Streamlit
- Integrate SHAP for model explainability
- Collect more minority class data to improve recall
- Engage stakeholders with interactive dashboards
🤝 Author
Kendi


