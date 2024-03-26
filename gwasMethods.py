class gwasMethods:

    def gym_ai(msg,client):
        gym_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": """You are a brilliant gym workout activity suggestor. 
                        You'll take user's prompt and generate a workout activity for every body parts.
                        This should be helpful for students, atheletes and sport teachers"""},
        {"role": "user", 
            "content": f'{msg}'
            }
        
        ],
        max_tokens=200,
        temperature=1.3
        )

        gym = gym_response.choices[0].message.content
        #print(gym)

        return gym

    def cover_ai(msg,client):
        cover_response = client.images.generate(
        model="dall-e-3",
        prompt=f"{msg}",
        size="1024x1024",
        quality="standard",
        n=1,
        )

        image_url = cover_response.data[0].url
        #display(Image(url=image_url))

        return image_url

    def design_ai(msgclient):
        design_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Based on the workout activity given, you will design a detailed image prompt for the cover image of this activity.
                                The image prompt should include theme of the activity with relevant steps, how many sets to conduct
                                and timing for each sets. The output should be within 100 characters"""},
            {"role": "user", 
            "content": f'{msg}'
            }
    
        ],
        max_tokens=100,
        temperature=1.3
        )

        design_prompt = design_response.choices[0].message.content
        #print(design_prompt)

        return design_prompt