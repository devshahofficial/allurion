import pinecone


def search_index(api_key, index_name, topkN, vector, environment, meta_filter=None):
    """
    Perform a vector similarity search in a Pinecone index.

    This function searches for the `topkN` most similar vectors to the `vector` in the specified Pinecone index.
    The search results will include metadata associated with the nearest neighbors if available.

    Parameters:
        api_key (str): The Pinecone API key for authentication.
        index_name (str): The name of the Pinecone index to perform the search in.
        topkN (int): The number of nearest neighbors to retrieve from the index. (k in k-nearest neighbors)
        vector (list): A list containing the query vector for similarity search. Should be a list of float values.
        environment (str): The Pinecone environment where the index is hosted (e.g., "production", "staging", etc.).
        meta_filter (str or None, optional): A filter to narrow down the search based on metadata.
            Default is None, which performs a standard vector similarity search without filtering by metadata.

    Returns:
        list: A list of dictionaries, where each dictionary contains information about a nearest neighbor.
            Each dictionary has the following keys:
                - 'id' (str): The identifier of the nearest neighbor in the index.
                - 'score' (float): The similarity score of the nearest neighbor to the query vector.
                - 'metadata' (dict or None): The metadata associated with the nearest neighbor if available,
                    or None if no metadata is provided.
    """
    pinecone.init(api_key=api_key, environment=environment)
    index = pinecone.Index(index_name)
    query_response = index.query(
        top_k=topkN,
        include_values=False,
        include_metadata=True,
        vector=vector,
        filter=meta_filter
    )
    return query_response
