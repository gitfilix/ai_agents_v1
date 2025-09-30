import os
import requests
from dotenv import load_dotenv
# load environment variables from .env file
load_dotenv()

OPEN_API_KEY_DEMO = os.getenv('OPEN_API_KEY_DEMO')

def generate_x_post(user_input: str) -> str:
    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that generates concise and engaging social media posts."},
            {"role": "user", "content": f"Create a concise and engaging X post about: {user_input}"}
        ],
        "max_tokens": 50,
        "temperature": 0.7
    }
    # call to AI LLM to generate X post
    response = requests.post(
        "https://api.openai.com/v1/responses", 
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPEN_API_KEY_DEMO}"
            }
    )


def main():
    # user input -> AI LLM to generate X post -> output post
    usr_input = input('what should the post be about? ')
    x_post = generate_x_post(usr_input)
    print(f"Generated X post: {x_post}")

if __name__ == "__main__":
    main()
