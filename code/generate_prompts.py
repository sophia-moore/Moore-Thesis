import pandas as pd
from typing import List

def create_prompt_list(data_df: pd.DataFrame) -> List[str]:
    """
    Generates prompts for the rows in data_df.

    Generated prompts follow the base_prompt structure (refer to base_prompt.txt):
        Description: {{description}}
        Question: {{question}}
        Section:
        Answer:

    Arguments:
        data_df: a pandas DataFrame containing 'Description' and 'Question' columns.

    Returns:
        List[str]: A list of formatted prompts.
    """

    # Normalize
    data_df.columns = data_df.columns.str.lower()

    # Check for required columns in the DataFrame
    required_columns = {"description", "question"}
    missing_columns = required_columns - set(data_df.columns)
    assert not missing_columns, f"Missing required columns: {missing_columns}"

    prompts = []

    dicts = data_df.to_dict(orient="records")

    for row in dicts:
        # Check for null values
        if pd.isna(row['description']) or pd.isna(row['question']):
            continue

        prompt = (
            "Based on the description provided, specify the relevant section of the Internal Revenue Code (IRC) and answer the question.\n\n"
            f"Description: {row['description']}\n"
            f"Question: {row['question']}\n"
            f"Section:\n"
            f"Answer:"
        )
        prompts.append(prompt)

    # Check for duplicates
    unique_pairs = set()
    for row in dicts:
        pair = (row["description"], row["question"])
        if pair in unique_pairs:
            raise ValueError(f"Duplicate prompt detected: {pair}")
        unique_pairs.add(pair)

    return prompts
