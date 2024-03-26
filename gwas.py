import os
from openai import OpenAI
from PIL import Image
from io import BytesIO
import streamlit as st
import requests
from gwasMethods import gwasMethods as gwas

client= OpenAI(
    api_key = st.secrets["OPEN_API_KEY"]
    )

def display_image(image_url):
    response = requests.get(image_url)
    img = Image.open(response.content)
    image_stream = BytesIO(image_data)
    img = Image.open(image_stream)
    st.image(img)

def main():
    st.title("Gym Workout Activity Suggestor (GWAS.ai)")

    # User input for workout suggestion
    workout_input = st.text_input("Enter your workout goal or body part focus:", "")
    if workout_input:

        workout_suggestion = gwas.gym_ai(workout_input,client)
        design_prompt = gwas.design_ai(workout_input,client)
        image_url = gwas.cover_ai(design_prompt,client)

        st.write("Workout Suggestion:")
        st.write(workout_suggestion)

        st.divider()

    if st.button("Generate Cover Image"):
        st.write("Cover Image:")
        display_image(image_url)

if __name__ == "__main__":
    main()