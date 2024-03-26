import os
from openai import OpenAI
from PIL import Image
import streamlit as st
import requests
from gwasMethods import gwasMethods as gwas

client = OpenAI(api_key=st.secrets["OPEN_API_KEY"])

def display_image(image_url):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        img = Image.open(response.raw)
        st.image(img, caption='Cover Image')

def main():
    st.title("Gym Workout Activity Suggestor (GWAS.ai)")

    # User input for workout suggestion
    workout_input = st.text_input("Enter your workout goal or body part focus:", "")
    if workout_input:
        workout_suggestion = gwas.gym_ai(workout_input, client)
        design_prompt = gwas.design_ai(workout_input, client)
        image_url = gwas.cover_ai(design_prompt, client)

        st.write("Workout Suggestion:")
        st.write(workout_suggestion)
        st.divider()

    if st.button("Generate Cover Image"):
        st.write("Cover Image:")
        display_image(image_url)

if __name__ == "__main__":
    main()