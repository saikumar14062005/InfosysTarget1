import os
from groq import Groq
import streamlit as st

client = Groq(
    api_key=os.environ.get("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")  # Ensure the API key is set in the environment
)

st.title("Chatbot with Streamlit")
st.write("Chat with me! Type your questions below. Type 'exit' to end the conversation.")

if "history" not in st.session_state:
    st.session_state["history"] = []  

user_input = st.text_input("You:", placeholder="Type your question here...")

if st.button("Submit") and user_input:
    if user_input.lower() == "exit":
        st.write("Chatbot: Goodbye!")
    else:
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama3-8b-8192",
            )

            bot_response = chat_completion.choices[0].message.content

            st.session_state["history"].append((user_input, bot_response))

        except Exception as e:
            bot_response = f"An error occurred: {e}"
            st.session_state["history"].append((user_input, bot_response))

if st.session_state["history"]:
    for i, (user, bot) in enumerate(st.session_state["history"]):
        st.markdown(f"**You:** {user}")
        st.markdown(f"**Chatbot:** {bot}")
