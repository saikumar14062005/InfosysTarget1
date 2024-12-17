import os
from groq import Groq
import streamlit as st

# Initialize the Groq client with the API key
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")  # Ensure the API key is set in the environment
)

# Initialize the Streamlit app
st.title("Chatbot with Streamlit")
st.write("Chat with me! Type your questions below. Type 'exit' to end the conversation.")

# Initialize conversation history in session state
if "history" not in st.session_state:
    st.session_state["history"] = []  # List to store (user_input, bot_response) pairs

# Input box for the user to type prompts
user_input = st.text_input("You:", placeholder="Type your question here...")

# Handle user input
if st.button("Submit") and user_input:
    if user_input.lower() == "exit":
        st.write("Chatbot: Goodbye!")
    else:
        try:
            # Make the API call to get the chatbot's response
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama3-8b-8192",
            )

            # Get the chatbot's response
            bot_response = chat_completion.choices[0].message.content

            # Append to conversation history
            st.session_state["history"].append((user_input, bot_response))

        except Exception as e:
            bot_response = f"An error occurred: {e}"
            st.session_state["history"].append((user_input, bot_response))

# Display the conversation history
if st.session_state["history"]:
    for i, (user, bot) in enumerate(st.session_state["history"]):
        st.markdown(f"**You:** {user}")
        st.markdown(f"**Chatbot:** {bot}")
