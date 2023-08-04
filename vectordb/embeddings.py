from sentence_transformers import SentenceTransformer
import time


def generate_embedding(input_string):
    """
    Generates embeddings for a list of sentence chunks using the all-mpnet-base-v2 model from SentenceTransformers,
    along with metadata in Pinecone format.

    Args:
    - chunks (list): A list of sentence chunks to generate embeddings for.
    - file_name (str): The name of the file containing the input sentences.

    Returns:
    - pinecone_dict (dict): A dictionary containing the embeddings and metadata in Pinecone format.
    """

    # Load all-mpnet-base-v2 model
    model = SentenceTransformer('all-mpnet-base-v2')

    # Generate the embedding for the input string
    embedding = model.encode(input_string, show_progress_bar=True)

    # Create metadata dictionary
    metadata = {'desc': input_string}

    # Create Pinecone format dictionary with a unique vector ID
    timestamp = str(int(time.time() * 1000))  # get current timestamp and convert to string
    vector_id = 'vec_' + timestamp  # create a unique id using the timestamp
    pinecone_dict = (vector_id, embedding.tolist(), metadata)

    return pinecone_dict
