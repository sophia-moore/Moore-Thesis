import openai
import os
import pandas as pd
from typing import List
from generate_prompts import create_prompt_list
from dotenv import load_dotenv  

# Requirement: configure OpenAI API key
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print(f"Loaded API Key: {api_key}") # Sanity check
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment!")

client = openai.OpenAI(api_key=api_key)

def evaluate_prompts(prompts: List[str], model="gpt-4o") -> List[str]: # Plug in corresponding model
    """
    Sends each prompt to OpenAI GPT and collects responses.

    Args:
        prompts (List[str]): A list of formatted prompts.
        model (str): The OpenAI model to use

    Returns:
        List[str]: A list of responses from the model.
    """
    responses = []

    for i, prompt in enumerate(prompts, 1): 
        print(f"Sending Prompt {i} to {model}...")

        try:
            messages = [{"role": "user", "content": prompt}]

            response = client.chat.completions.create(
                model=model, 
                messages=messages,
                max_tokens=500, 
                temperature=0.7,
                n=1
            )

            reply = response.choices[0].message.content  
            responses.append(reply)

        except openai.OpenAIError as e:
            print(f"OpenAI API Error: {e}")
            responses.append("Error: API request failed")

    return responses

data_df = pd.read_csv("tests.csv")  # Load constructed tasks 
prompts = create_prompt_list(data_df)  # Generate prompts
responses = evaluate_prompts(prompts)  # Get model responses

# Save responses to a .txt file
with open("gpt_responses.txt", "w") as f:
    for idx, (prompt, response) in enumerate(zip(prompts, responses), start=1):
        f.write(f"Prompt {idx}:\n{prompt}\n")
        f.write(f"GPT Response:\n{response}\n")
        f.write('-' * 40 + "\n")
        
print("Responses have been saved to 'gpt_responses.txt'.")