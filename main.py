import os
import openai
from dotenv import load_dotenv, find_dotenv

find_dotenv_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']


# Completion Request
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content":  prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


# Prints Messages sent to Open AI
print(get_completion("What is 1+1?"))
