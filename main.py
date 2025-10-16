import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    print("Hello User!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose = False

    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        return
    
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        verbose = True
    
    user_prompt = sys.argv[1]

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )

    print(response.text)

    if response is None or response.usage_metadata is None:
        print("No usage metadata available.")
        return

    if verbose:
        print(f"Response: {response}")
        print(f"Response type: {type(response)}")
        print(f"Response text: {response.text}")
        print(f"Response type: {type(response.text)}")
        print(f"Response usage metadata: {response.usage_metadata}")
        print(f"Response usage metadata type: {type(response.usage_metadata)}")

        prompt_token_count = response.usage_metadata.prompt_token_count
        candidates_token_count = response.usage_metadata.candidates_token_count

        print(f"Prompt token count: {prompt_token_count}")
        print(f"Candidates token count: {candidates_token_count}")

main()