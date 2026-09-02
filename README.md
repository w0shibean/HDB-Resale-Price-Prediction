# HDB Resale Price Prediction

Predicting HDB resale flat prices in Singapore using historical transaction data pulled directly from the data.gov.sg API, covering data cleaning, exploratory analysis, an XGBoost regression model with SHAP explainability, and a deployed Streamlit app.

## Dataset

HDB resale flat transactions — January 2017 to present (data.gov.sg, pulled via REST API)

## Analysis

- Q1 — Resale price trend over time
- Q2 — Price by town
- Q3 — Price by flat type
- Q4 — Price by storey range
- Q5 — Price vs remaining lease
- Q6 — Correlation heatmap
- **Model** — XGBoost regression to predict resale price
- **Explainability** — SHAP to identify which features drive each prediction

## Tools

Python · pandas · XGBoost · SHAP · scikit-learn · Streamlit · data.gov.sg API

## Files

| File | Description |
|------|-------------|
| `hdb_analysis.ipynb` | Full analysis notebook |
| `HDB_app.py` | Streamlit web app |
| `requirements.txt` | Dependencies |
| `xgb_model.pkl` | Trained model |
| `Report.pdf` | Project report |

## Model Performance

- R²: 0.9417
- RMSE: 46,280.66

## StreamLit Live Demo

[Launch App](your-streamlit-link-here)
