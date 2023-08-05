# Allurion AI - Your personal Health Coach

## 👋 Introduction
The ChatGPT Recipe Bot is a conversational AI application that uses a Kaggle dataset filled with ingredients and recipes to generate wonderful recipes based on user queries. The bot utilizes various technologies, including Pinecone for vector database storage, Streamlit for the user interface, GPT-3.5 for natural language understanding and generation, and Sentence Transformers with MPNet base model for generating embeddings.

## Demo
Test Demo here - https://allurion.streamlit.app/
![image](https://github.com/devshahofficial/allurion/assets/49101333/8c394c4c-672a-40a0-8a23-d3242363975d)


## 🎯 Objectives:
The primary objectives of this project are to:
- **Develop a conversational AI application**: Create a user-friendly chatbot using GPT-3.5 to interact with users, understand their queries, and generate recipe suggestions.
- **Utilize Kaggle recipe dataset**: Process and extract relevant information from the Kaggle dataset, including ingredients and recipes, to build a comprehensive knowledge base.
- **Provide delightful recipe recommendations**: Utilize advanced language processing techniques and embeddings to offer users a wide variety of high-quality, contextually relevant, and appealing recipe options.
- **Create an intuitive user interface**: Implement a streamlined and visually appealing interface using Streamlit, allowing users to interact seamlessly with the chatbot and receive recipe suggestions with ease.

## 📝 Methodology
The following steps are followed to achieve the project objectives:
1. **Data Acquisition**: 
   - Obtain the Kaggle dataset containing ingredients and recipes for building the recipe knowledge base.
2. **Embeddings Generation**:
   - Utilize the Sentence Transformers library with the MPNet base model to generate fixed-length embeddings for recipes and ingredients.
   - Store the embeddings efficiently using Pinecone's vector database for quick retrieval and similarity search.
3. **GPT-3.5 Integration**:
   - Integrate the GPT-3.5 language model into the application to handle user queries and generate recipe suggestions.
   - Set up API communication with the GPT-3.5 model to send prompts and receive responses.
4. **User Interface Development**:
   - Build a user-friendly interface using Streamlit to interact with the ChatGPT Recipe Bot.
   - Design the interface for users to input queries and display recipe recommendations.
5. **Query Processing**:
   - Process user queries, convert them into embeddings using Sentence Transformers, and handle any pre-processing requirements.
6. **Pinecone Search**:
   - Perform a nearest neighbor search in the Pinecone vector database to retrieve the most similar recipes based on user queries' embeddings.
7. **Recipe Generation**:
   - Provide the retrieved recipe embeddings as context to the GPT-3.5 model for generating delightful recipe suggestions.
8. **Result Presentation**:
   - Display the generated recipes on the user interface, showcasing relevant details such as ingredients, instructions, and additional tips.

## Links
* Application - [Streamlit](https://allurion.streamlit.io)
* Dataset - [Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv)


##  Technical Documentation
### vectorDB
- `batch_processing_utils.py`: The file contains two functions that can be used to generate embeddings for a list of sentence chunks and upsert them to a Pinecone index.
- `csv_utils`: This file contains a function that prepares the data to be upserted to the vector database.
- `embeddings.py`: This file contains a function that generates embeddings for a list of sentence chunks using the all-mpnet-base-v2 model
- `main.py`: This file is the app file to upsert vectors to Pinecone DB.
- `pinecone_utils.py`: This file contains vectors that enable the upsertion of a list of vectors to the Pinecone index.

### chatGPT
- `allurion_api.py`: This file is similar to the main.py and is just optimized to work with the frontend.
- `embeddings.py`: This file transforms user queries into embeddings using Mpnet model.
- `main.py`: This file has the workflow that enables you to query chatGPT.
- `openAI_utils.py`: This file has all OpenAI Utils.
- `search_query_pinecone.py`: This file has functions to perform querying on Pinecone.

### Project Root
- `README.md`: The main documentation file for the project.
- `gitignore`: The file containing the list of packages to exclude on git push.
- `requirements.txt`: The file containing the list of dependencies required for the project.




## 👉 Conclusion
The ChatGPT Recipe Bot project achieved its objectives by creating a powerful AI application for providing delightful recipe recommendations leveraging the provided Kaggle dataset.
