import os
from dotenv import load_dotenv
from groq import Groq

# load_dotenv()

def run_groq_api(prompt, model="openai/gpt-oss-20b"):

    client = Groq(
        api_key=os.getenv("GROQ_API"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":"You are an intelligent research paper analyzer whose task is to assist the user in understanding a given research paper with depth and clarity."
            }
            ,
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )

    response = chat_completion.choices[0].message.content
    return response