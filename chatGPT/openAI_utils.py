import openai


def chatGPT_retriever(query, api_key):
    """
    Retrieves an answer from OpenAI ChatGPT3.5 using the given query and API key.

    Args:
        query (str): The string query to be answered.
        api_key (str): The OpenAI API key.

    Returns:
        str: The answer from OpenAI ChatGPT3.5.
    """

    # Set the OpenAI API key for authentication
    openai.api_key = api_key

    # Prepare the prompt for the conversation with ChatGPT
    prompt_recipe = "Use the following information to write a structured recipe in markdown code format: \n"

    # Create a conversation with the user query as the message content
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt_recipe + query}
        ]
    )

    # Extract the response from the completion and return the content
    response = completion.choices[0].message
    return response["content"]
