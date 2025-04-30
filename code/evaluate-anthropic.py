import os
import pandas as pd
from typing import List
from generate_prompts import create_prompt_list
from dotenv import load_dotenv
import requests

# Requirement: configure Anthropic API key
load_dotenv("anthropic-key.env")

claude_api_key = os.getenv("CLAUDE_API_KEY")
print(f"Loaded API Key: {claude_api_key}")  # Sanity check

if not claude_api_key:
    raise ValueError("CLAUDE_API_KEY not found in environment!")

def evaluate_prompts(prompts: List[str], model="claude-3-7-sonnet-20250219") -> List[str]:
    """
    Sends each prompt to Claude and collects responses.

    Args:
        prompts (List[str]): A list of formatted prompts.
        model (str): The Claude model to use.

    Returns:
        List[str]: A list of responses from the model.
    """
    responses = []

    for i, prompt in enumerate(prompts, 1):
        print(f"Sending Prompt {i} to {model}...")

        try:
            # Request headers, body for Claude's /v1/messages endpoint
            headers = {
                "x-api-key": claude_api_key,
                "anthropic-version": "2023-06-01",
                "Content-Type": "application/json"
            }
            payload = {
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 500,
                "temperature": 0.7
            }

            response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)
            response.raise_for_status() 

            response_data = response.json()
            reply = response_data.get("content", [{"text": "No response"}])[0].get("text", "No text found")

            responses.append(reply)

        except requests.HTTPError as e:
            print(f"Claude API Error: {e}")
            print(f"Response content: {response.text}")
            responses.append("Error: API request failed")

        except Exception as e:
            print(f"Unexpected error: {e}")
            responses.append("Error: Unexpected failure")

    return responses

data_df = pd.read_csv("tests.csv")  # Load constructed tasks 
prompts = create_prompt_list(data_df)  # Generate prompts
responses = evaluate_prompts(prompts)  # Get model responses

# Save responses to a .txt file
with open("claude_responses.txt", "w") as f:
    for idx, (prompt, response) in enumerate(zip(prompts, responses), start=1):
        f.write(f"Prompt {idx}:\n{prompt}\n")
        f.write(f"Claude Response:\n{response}\n")
        f.write('-' * 40 + "\n")

print("Responses have been saved to 'claude_responses.txt'.")