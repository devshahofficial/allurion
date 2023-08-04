import os
from csv_utils import convert_csv_to_string
from embeddings import generate_embedding
from pinecone_utils import upsert_to_pinecone


def main():
    # Path to the CSV file containing recipes data
    csv_path = "../data/recipes.csv"

    # Read recipes data from the CSV file (limiting to 5 rows for demonstration purposes)
    recipes = convert_csv_to_string(csv_path, rows=5)

    # Get the Pinecone API key from the environment variable
    api_key = os.environ.get("PINECONE_API_KEY")
    if not api_key:
        raise ValueError("PINECONE_API_KEY environment variable not set.")

    # Process each recipe, generate its embedding, and upsert it to the Pinecone index
    for recipe in recipes:
        # Generate the embedding representation for the recipe
        embedding = generate_embedding(recipe)

        # Upsert the recipe embedding into the Pinecone index
        upsert_to_pinecone(
            embedding,
            api_key=api_key,
            index_name="allurion",
            environment="gcp-starter"
        )


if __name__ == "__main__":
    main()
