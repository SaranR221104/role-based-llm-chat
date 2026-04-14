import streamlit as st
import ollama

# 1. Page Configuration
st.set_page_config(page_title="Multi-Role AI Chatbot", layout="centered")

# 2. Define the Roles
ROLES = {
    "Python Tutor": "You are a patient Python tutor. Explain concepts simply with code examples.",
    "Fitness Coach": "You are a motivating fitness coach. Give exercise and health advice.",
    "Travel Guide": "You are an expert travel guide. Suggest the best places to visit."
}

# 3. Sidebar for Navigation
st.sidebar.title("Configuration")
selected_role = st.sidebar.selectbox("Pick a Role", list(ROLES.keys()))

if st.sidebar.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# 4. Initialize Session State (Memory)
# In Streamlit, variables reset every time the page reloads. 
# We use 'st.session_state' to keep the memory alive.
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display Conversation History
for message in st.session_state.messages:
    # We don't show the 'system' prompt to the user
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 6. Chat Input
if prompt := st.chat_input("Type your message here..."):
    
    # Add User message to state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 7. Prepare full message list for Ollama (including System Prompt)
    # We prepend the system prompt so the AI knows its role
    full_chat_history = [{"role": "system", "content": ROLES[selected_role]}] + st.session_state.messages

    # 8. Call Ollama
    with st.chat_message("assistant"):
        response_placeholder = st.empty() # Create a placeholder for the "thinking" effect
        response_placeholder.markdown("🔍 *Thinking...*")
        
        try:
            response = ollama.chat(model='llama3.2:3b', messages=full_chat_history)
            bot_reply = response['message']['content']
            
            # Display final reply
            response_placeholder.markdown(bot_reply)
            
            # Add Assistant response to memory
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            st.error(f"Error: Ensure Ollama is running. {e}")