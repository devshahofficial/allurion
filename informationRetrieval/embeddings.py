from sentence_transformers import SentenceTransformer


def generate_embedding(input_string):
    """
    Generate sentence embeddings for an input string using the all-mpnet-base-v2 model.

    Parameters:
        input_string (str): The input string for which the embedding needs to be generated.

    Returns:
        list: A list containing the sentence embedding as a list of float values.
    """
    # Load all-mpnet-base-v2 model
    model = SentenceTransformer('all-mpnet-base-v2')

    # Generate the embedding for the input string
    embedding = model.encode(input_string, show_progress_bar=True)

    return embedding.tolist()
