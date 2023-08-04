import pinecone
from sentence_transformers import SentenceTransformer
import time


def generate_embedding_batch(input_strings):
    """
    Generates embeddings for a list of sentence chunks using the all-mpnet-base-v2 model from SentenceTransformers,
    along with metadata in Pinecone format.

    Args:
        input_strings (list): A list of sentence chunks to generate embeddings for.

    Returns:
        list: A list of tuples, each containing the vector ID, embeddings, and metadata in Pinecone format.

    Raises:
        ValueError: If the input_strings is not a list or if it is an empty list.
    """

    if not isinstance(input_strings, list):
        raise ValueError("input_strings must be a list.")

    if not input_strings:
        raise ValueError("input_strings cannot be an empty list.")

    # Load all-mpnet-base-v2 model
    model = SentenceTransformer('all-mpnet-base-v2')

    pinecone_list = []
    for input_string in input_strings:
        # Generate the embedding for the input string
        embedding = model.encode(input_string, show_progress_bar=True)

        # Create metadata dictionary
        metadata = {'desc': input_string}

        # Create Pinecone format dictionary with a unique vector ID
        timestamp = str(int(time.time() * 1000))  # get current timestamp and convert to string
        vector_id = 'vec_' + timestamp  # create a unique id using the timestamp
        pinecone_dict = (vector_id, embedding.tolist(), metadata)

        pinecone_list.append(pinecone_dict)

    return pinecone_list


def batch_upsert_to_pinecone(vectors, api_key, index_name, environment):
    """
    Upserts a batch of vectors to the Pinecone index.

    Parameters:
        vectors (list): A list of vectors to be upserted into the Pinecone index.
        api_key (str): The Pinecone API Key.
        index_name (str): The Pinecone cluster index name.
        environment (str): The cluster environment.

    Returns:
        int: Returns 0 on successful upsert.

    Raises:
        pinecone.exceptions.PineconeException: If there is an issue with Pinecone's API.
    """
    # Pinecone API key for authentication
    api_key = api_key

    try:
        # Initialize Pinecone with the GCP Starter environment
        pinecone.init(api_key=api_key, environment=environment)

        # Index name
        index_name = index_name

        # Upsert data into the index
        with pinecone.Index(index_name) as index:
            index.upsert(vectors)

        return 0

    except pinecone.exceptions.PineconeException as e:
        # Handle any Pinecone-related exceptions
        print(f"PineconeException: {e}")
        return -1
