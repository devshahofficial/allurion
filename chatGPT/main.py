from decouple import config
from embeddings import generate_embedding
from search_query_pinecone import search_index
from openAI_utils import chatGPT_retriever


def main():
    # Load API keys from environment variables
    pinecone_api_key = config("PINECONE_API_KEY")
    openai_api_key = config("OPENAI_API_KEY")

    # Input query string
    string_new = "baked winter squash mexican"

    # Generate embeddings for the query
    embeddings = generate_embedding(string_new)

    # Search Pinecone index for recipe metadata
    search_index_retrieve = search_index(
        api_key=pinecone_api_key,
        index_name="allurion",
        topkN=1,
        vector=embeddings,
        environment="gcp-starter"
    )

    # Retrieve recipe metadata from search results
    pinecone_response = search_index_retrieve["matches"][0]["metadata"]["desc"]

    # Print the response from Pinecone
    print("Pinecone Response:")
    print(pinecone_response)

    # Use OpenAI ChatGPT3.5 to get a response for the recipe metadata
    chatGPT_response = chatGPT_retriever(query=pinecone_response, api_key=openai_api_key)

    # Print the response from ChatGPT3.5
    print("ChatGPT Response:")
    print(chatGPT_response)


if __name__ == "__main__":
    main()
