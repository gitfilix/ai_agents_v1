import os
# run "uv sync" to install dependencies
from openai import OpenAI
from dotenv import load_dotenv
import json
# load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv('OPEN_API_KEY')
)

# Load examples from json file
with open('examples.json', 'r') as file:
    examples = json.load(file)["examples"]

def generate_x_post(topic: str) -> str:
    # Format examples into a string
    examples_text = "\n".join(
        f"<example-{i+1}>\n"
        f"    <topic>{example['topic']}</topic>\n"
        f"    <generated-post>{example['generated_post']}</generated-post>\n"
        f"</example-{i+1}>"
        for i, example in enumerate(examples)
    )
    prompt = f"""
    You are an expert social media manager. Generate a concise and engaging X (formerly Twitter) posts. 
    Your Task is to generate a post that is concise, engaging, and relevant to the topic provided by the user.
    Avoid using hashtags, mentions, or links. The post should be no longer than 280 characters.
    Use Emojis is okay to enhance engagement. Keep the post positive and professional. Keep the post short and focused. use line breaks and empty lines to make the post more readable.
    Here is the topic provided by the user to generate the post:
    <topic>
    {topic}
    </topic>
    
    Here are some examples of good X posts:
    {examples_text}

    """
    response = client.responses.create(
        model="gpt-4o",
        input=prompt
    )


    return response.output_text


def main():
    # user input -> AI LLM to generate X post text -> output post to be shared on X
    usr_input = input('what should the post be about? ')
    x_post = generate_x_post(usr_input)
    print(f"Generated X post: \n")
    print(x_post)

if __name__ == "__main__":
    main()
