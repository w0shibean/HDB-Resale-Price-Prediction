# HDB Resale Price Prediction

A Python project predicting HDB resale flat prices in Singapore, using historical transaction data from January 2017 to present.

The project covers data cleaning, exploratory analysis, an XGBoost regression model, and SHAP explainability, with a Streamlit app for making live predictions.

## Dataset

Pulled directly from the data.gov.sg REST API:

- HDB resale flat transactions
- January 2017 to present
- Town, flat type, storey range, floor area, lease info, and resale price

## Analysis

- Resale price trend over time
- Price by town, flat type, and storey range
- Price vs remaining lease
- Correlation between numeric features
- XGBoost model to predict resale price
- SHAP to identify which features drive each prediction

Full methodology and findings are in the [project report](#).

## Streamlit App

I built a Streamlit app to explore the data and get live price predictions from the model.

[Launch the app](#)

## Project Files

| File | Description |
|---|---|
| `hdb_analysis.ipynb` | Main analysis notebook |
| `HDB_app.py` | Streamlit application |
| `requirements.txt` | Python dependencies |
| `xgb_model.pkl` | Trained model |
| `Report.pdf` | Full project report |

## Technologies

Python · pandas · XGBoost · SHAP · scikit-learn · Streamlit · data.gov.sg API

## Model Performance

- R²: 0.9417
- RMSE: 46,280.66

## Running the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
