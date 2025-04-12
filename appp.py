import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('order_predictor.pkl')

st.title("📦 Ad Campaign Order Predictor")

st.markdown("Enter your campaign details below to predict the number of **product orders** expected.")

# Inputs
campaign_type = st.selectbox("Campaign Type", ['email', 'social media', 'print advertising'])
campaign_level = st.selectbox("Campaign Level", ['national', 'regional', 'local'])
product_level = st.selectbox("Product Level", ['high-end', 'mid-range', 'budget'])

resource_amount = st.number_input("Resource Amount (₹)", min_value=0.0, step=100.0)
email_rate = st.number_input("Email Open Rate", min_value=0.0, max_value=1.0, step=0.01)
price = st.number_input("Product Price (₹)", min_value=0.0, step=1.0)
discount_rate = st.number_input("Discount Rate", min_value=0.0, max_value=1.0, step=0.01)
hour_resources = st.number_input("Labor Hours", min_value=0.0, step=1.0)
campaign_fee = st.number_input("Campaign Fee (₹)", min_value=0.0, step=100.0)

if st.button("Predict Orders"):
    input_df = pd.DataFrame({
        'campaign_type': [campaign_type],
        'campaign_level': [campaign_level],
        'product_level': [product_level],
        'resource_amount': [resource_amount],
        'email_rate': [email_rate],
        'price': [price],
        'discount_rate': [discount_rate],
        'hour_resources': [hour_resources],
        'campaign_fee': [campaign_fee]
    })

    prediction = model.predict(input_df)[0]
    st.success(f"📈 Predicted Orders: {prediction:.0f}")
