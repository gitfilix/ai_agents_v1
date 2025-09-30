import os
# run "uv sync" to install dependencies
import requests
from dotenv import load_dotenv
# load environment variables from .env file
load_dotenv()

OPEN_API_KEY_DEMO = os.getenv('OPEN_API_KEY_DEMO')

def generate_x_post(topic: str) -> str:
    prompt = f"""
    You are an expert social media manager. Generate a concise and engaging X (formerly Twitter) posts. 
    Your Task is to generate a post that is concise, engaging, and relevant to the topic provided by the user.
    Avoid using hashtags, mentions, or links. The post should be no longer than 280 characters.
    Use Emojis is okay to enhance engagement. Keep the post positive and professional. Keep the post short and focused. use line breaks and empty lines to make the post more readable.
    Here is the topic provided by the user to generate the post:
    <topic>
    {topic}
    </topic>
    """
    payload = {
        "model": "gpt-4o",
        "input": prompt
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
    print(f"Response status code: {response.status_code}")
    # print(f"Response content: {response.content}")
    response_text = response.json().get('output', [{}])[0].get("content", [{}])[0].get("text", "")
    return response_text.strip()


def main():
    # user input -> AI LLM to generate X post text -> output post to be shared on X
    usr_input = input('what should the post be about? ')
    x_post = generate_x_post(usr_input)
    print(f"Generated X post: \n")
    print(x_post)

if __name__ == "__main__":
    main()
