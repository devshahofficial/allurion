import pinecone


def upsert_to_pinecone(vectors, api_key, index_name, environment):
    """
    Upserts a list of vectors to the Pinecone index.

    This function initializes Pinecone with the specified environment and API key,
    then upserts the provided vectors into the specified index.

    Args:
        vectors (tuple): A tuple to be upserted into the Pinecone index.
        api_key (str): The Pinecone API key for authentication.
        index_name (str): The name of the index to upsert the vectors into.
        environment (str): The Pinecone environment to be used for initialization.

    Returns:
        int: Returns 0 on successful upsert.

    Raises:
        pinecone.exceptions.PineconeException: If there is an issue with Pinecone's API.
    """
    try:
        # Initialize Pinecone with the specified environment and API key
        pinecone.init(api_key=api_key, environment=environment)

        # Upsert data into the index
        with pinecone.Index(index_name) as index:
            index.upsert([vectors])

        return 0

    except pinecone.exceptions.PineconeException as e:
        # Handle any Pinecone-related exceptions
        print(f"PineconeException: {e}")
        return -1
