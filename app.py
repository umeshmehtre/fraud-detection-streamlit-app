import streamlit as st
import pandas as pd
import joblib
import numpy as np  # <-- THIS IS THE FIX!

# --- Load The Saved Model ---
# The model is loaded once when the app starts and stored in memory.
@st.cache_resource
def load_model():
    model = joblib.load('saved_models/fraud_model.pkl')
    return model

model = load_model()

# --- App Title and Description ---
st.title("Credit Card Fraud Detection 💳")
st.write(
    "This interactive app demonstrates a machine learning model's ability to detect fraudulent credit card transactions. "
    "The model was trained on a highly imbalanced dataset and uses a Logistic Regression model with balanced class weights."
)
st.write(
    "**Disclaimer:** This is a demo using an anonymous public dataset. "
    "Do not enter real credit card information."
)
st.divider()

# --- Create Input Fields for User ---
# We use sliders for some key features identified as important in fraud detection.
st.header("Simulate a Transaction")
st.write("Adjust the sliders below to simulate the features of a credit card transaction. The model will predict if it's fraudulent.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Key Transaction Features")
    v14 = st.slider('Feature V14', -19.0, 11.0, -1.0, 0.1)
    v10 = st.slider('Feature V10', -25.0, 24.0, -0.5, 0.1)
    v12 = st.slider('Feature V12', -18.0, 8.0, -0.6, 0.1)

with col2:
    st.subheader("Other Influential Features")
    v17 = st.slider('Feature V17', -26.0, 10.0, -0.5, 0.1)
    v4 = st.slider('Feature V4', -6.0, 17.0, 0.4, 0.1)
    v11 = st.slider('Feature V11', -5.0, 12.0, -0.5, 0.1)

# The model was trained on 30 features. We need to create a full array for prediction.
# The features we are not using in sliders will be set to their median (or 0 for simplicity).
# The order must be exactly as it was during training:
# scaled_Amount, scaled_Time, V1, V2, ..., V28
# For this demo, we'll construct a simplified input array.
all_features = np.zeros(30)
# We map our slider values to their correct positions in the feature array.
# (Note: Feature names are V1, V2... but indices are 0, 1...)
all_features[4] = v4   # V4 is the 5th 'V' feature
all_features[10] = v10 # V10 is the 11th 'V' feature
all_features[11] = v11 # etc.
all_features[12] = v12
all_features[14] = v14
all_features[17] = v17

# Reshape the array for a single prediction
input_data = all_features.reshape(1, -1)


# --- Prediction Button and Output ---
if st.button("Predict Transaction Status"):
    # Make prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.error("🚨 HIGH RISK: This transaction is likely FRAUDULENT!", icon="🚨")
        st.write(f"Confidence Score (Fraud): **{prediction_proba[0][1]*100:.2f}%**")
        st.progress(prediction_proba[0][1])
    else:
        st.success("✅ LOW RISK: This transaction appears to be LEGITIMATE.", icon="✅")
        st.write(f"Confidence Score (Legitimate): **{prediction_proba[0][0]*100:.2f}%**")
        st.progress(prediction_proba[0][0])

st.divider()
st.write("Try setting **V14 to -8** and **V12 to -3** to see a likely fraudulent prediction.")