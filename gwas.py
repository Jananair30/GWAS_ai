import os
from openai import OpenAI
from PIL import Image
import streamlit as st
import requests
from gwasMethods import gwasMethods as gwas

client = OpenAI(api_key=st.secrets["OPEN_API_KEY"])


if "history" not in st.session_state:
    st.session_state.history = []

def update_history(action):
    st.session_state.history.append(action)


def display_image(image_url):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        img = Image.open(response.raw)
        st.image(img, caption='Cover Image')

def create_sidebar_navigation():
    if "navigation" not in st.session_state:
        st.session_state.navigation = False  # Initialize the navigation attribute

    if st.session_state.navigation:
        st.sidebar.header("GWAS")
        st.sidebar.subheader("Gwas Sections")
        if st.sidebar.button("History"):
            st.sidebar.write("User History:")
            for item in st.session_state.history:
                st.sidebar.write(item)
        

def main():
    create_sidebar_navigation()  # Call the function to create the sidebar navigation

    st.title("Gym Workout Activity Suggestor (GWAS.ai)")

    age_range = st.slider("Select Your Age Range:", 10, 100, (20, 30))

    with st.expander("User Options", expanded=False):
        user_option = st.radio("Select User Type:", ("Students", "Athletes", "Sport Teacher", "Random User"))

    workout_input = st.text_input("Enter your workout goal or body part focus:", "")
    if workout_input:
        workout_suggestion = gwas.gym_ai(workout_input, client)
        design_prompt = gwas.design_ai(workout_input, client)
        image_url = gwas.cover_ai(design_prompt, client)

        st.write("Workout Suggestion:")
        st.write(workout_suggestion)
        st.divider()

        update_history(f"Generated workout suggestion for: {workout_input}")

    if st.button("Generate Cover Image"):
        st.write("Cover Image:")
        display_image(image_url)

        update_history("Generated cover image")

if __name__ == "__main__":
    main()