import os
from openai import OpenAI
from IPython.display import Image
import streamlit as st
from gwasMethods import gwasMethods as gwas

client= OpenAI(
    api_key = st.secrets["OPEN_API_KEY"]
    )

def display_image(image_url):
    response = requests.get(image_url)
    img = Image.open(response.content)
    st.image(img)

def main():
    st.title("GWAS Workout and Design Assistant")

    # User input for workout suggestion
    workout_input = st.text_input("Enter your workout goal or body part focus:", "")
    if workout_input:

        workout_suggestion = gwas.gym_ai(workout_input.client)
        cover_prompt = gwas.design_ai(workout.client)
        image_url = gwas.cover_ai(design.client)

        st.write("Workout Suggestion:")
        st.write(workout_suggestion)

        st.divider()

    if st.button("Generate Cover Image"):
        st.write("Cover Image:")
        display_image(image_url)

if __name__ == "__main__":
    main()