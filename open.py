from openai import OpenAI
from dotenv import load_dotenv
import requests
import json
# load environment variables from .env file
load_dotenv()


def get_ai_response(prompt: str, model: str = "gemma3:4b-it-qat", ctx: int = 4000) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_ctx": ctx
            }
        }
    )

    try:    
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
    
    data = response.json()

    if "response" not in data:
        print("Unexpected response format:", data)
        return ""
    
    return data["response"]



def get_website_html(url: str) -> str:
    #get HTML content of a webpage
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return "" # return empty string on error


def extract_core_webpage_content(html: str) -> str:
    # Placeholder for actual content extraction logic
    # sanitize and extract main content from HTML - remove ads, navigation, footers, etc.
    # we use gpt-4o-mini to extract and sanitize the main content from HTML
    response = get_ai_response(
        model="gemma3:4b-it-qat",
        prompt=f"""
            You are and expert in extracting and sanitize the main content from this HTML content of a webpage. remove ads, navigation and aside, footers and return only the main content in a clean text format.
            ignore all scripts, styles, and non-content elements. Especially search for content within <article> tag. Maybe include the relevant titles and headings, if they add context or meta information.
            Here is the HTML content:
            <html>
            {html}
            </html>
            Please extract and sanitize the main content and return it in a clean, plain text format.
            """,
            ctx=20000
    )
    return response.strip()


def summarize_content(content: str) -> str:
    response = get_ai_response(
        model="gemma3:4b-it-qat",
        prompt=f"""
        You are an expert content summarizer. Summarize the following content in a concise and get the relevant information. Keep the tone positive and professional.
        preferly use bullet points or numbered lists to organize the summary for better readability.
        Here is the content to summarize:
        <content>
        {content}
        </content>
        please provide a concise summary of the with all the relevant content. 
        """
    )
    return response



def main():
    # user input -> ask for a webpage url -> scrape the webpage to get the content -> AI LLM to generate a summary of the content -> output summary
    usr_input = input('What Webpage should be summarized? Webpage URL: ')
    print("Fetching webpage content...")
    try:
        html_content = get_website_html(usr_input)
        print("Webpage content fetched successfully.")
    except Exception as e:
        print(f"Error fetching webpage content: {e}")
        return
    if not html_content:
        print("No content found at the provided URL or unable to fetch content. exiting.")
        return
    
    print("---- Extracting core content from HTML")
    core_content = extract_core_webpage_content(html_content)
    print("---- Core content extracted.")
    print("---- Summarizing Core content")
    summary = summarize_content(core_content)
    print("---- Summary generated.")
    print(f"Summary of the webpage content: \n")
    print(summary)
        

if __name__ == "__main__":
    main()
