import streamlit as st
from allurion_api import allurion


def main():
    st.title("Allurion Health Coach")

    # Get the user input
    user_input = st.text_input("Tell me something about the recipe:")

    # Create a button to submit the text
    if st.button("Submit"):
        chatGPT_response = allurion(user_input)

        # Display the recipe in markdown format
        st.markdown(f"**Our Expert Recipe:**\n\n{chatGPT_response}")


if __name__ == "__main__":
    main()
