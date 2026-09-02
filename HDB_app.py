import streamlit as st
import pandas as pd
import xgboost as xgb
import pickle

# Load cleaned data
df = pd.read_csv('hdb_clean.csv')
df['month'] = pd.to_datetime(df['month'])

st.title("HDB Resale Price Explorer")

# --- Filters ---
st.sidebar.header("Filters")
town = st.sidebar.selectbox("Town", sorted(df['town'].unique()))
flat_type = st.sidebar.selectbox("Flat Type", sorted(df['flat_type'].unique()))
storey_range = st.sidebar.selectbox("Storey Range", sorted(df['storey_range'].unique()))

filtered = df[
    (df['town'] == town) &
    (df['flat_type'] == flat_type) &
    (df['storey_range'] == storey_range)
]

st.subheader(f"Resale Transactions: {flat_type} in {town}, {storey_range}")
st.dataframe(filtered[['month', 'block', 'street_name', 'floor_area_sqm', 'resale_price']])

if len(filtered) > 0:
    st.metric("Average Resale Price", f"${filtered['resale_price'].mean():,.0f}")
    st.line_chart(filtered.groupby('month')['resale_price'].mean())
else:
    st.warning("No transactions match this combination.")


    

st.header("Price Predictor")

# Load trained model (save this from your Week 3 notebook first — see note below)
model = pickle.load(open('xgb_model.pkl', 'rb'))

pred_floor_area = st.number_input("Floor Area (sqm)", min_value=30, max_value=250, value=90)
pred_storey_median = st.number_input("Storey (median)", min_value=1, max_value=50, value=10)
pred_lease_years = st.number_input("Remaining Lease (years)", min_value=1, max_value=99, value=70)
pred_lease_commence = st.number_input("Lease Commence Year", min_value=1960, max_value=2026, value=1990)

if st.button("Predict Price"):
    # Build input row matching your training feature columns
    input_data = pd.DataFrame({
        'floor_area_sqm': [pred_floor_area],
        'storey_median': [pred_storey_median],
        'remaining_lease_years': [pred_lease_years],
        'lease_commence_date': [pred_lease_commence],
        # add one-hot columns for town/flat_type/flat_model here, matching training set
    })
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Resale Price: ${prediction:,.0f}")