import streamlit as st
import pandas as pd

# Title of the app
st.title("Baccarat Predictor")

# Input field for the user
user_sequence = st.text_input("Enter last 10 results (e.g., P,B,P,T,B,...):")

# Button to make a prediction
if st.button("Predict"):
    # Placeholder prediction logic (replace this with real logic later)
    if user_sequence:
        # Count the frequency of each outcome
        outcomes = user_sequence.split(",")
        player_count = outcomes.count("P")
        banker_count = outcomes.count("B")
        tie_count = outcomes.count("T")

        # Simple prediction: choose the most frequent outcome
        if player_count > banker_count and player_count > tie_count:
            prediction = "Player (P)"
        elif banker_count > player_count and banker_count > tie_count:
            prediction = "Banker (B)"
        elif tie_count > player_count and tie_count > banker_count:
            prediction = "Tie (T)"
        else:
            prediction = "No clear prediction"
    else:
        prediction = "Please enter a valid sequence."

    # Display the prediction
    st.write(f"Prediction: {prediction}")
