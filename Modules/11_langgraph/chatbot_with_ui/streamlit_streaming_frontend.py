import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Display previous messages
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# User input
user_input = st.chat_input('Type here')

if user_input:
    # Save user message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # Assistant response
    with st.chat_message('assistant'):
        response_placeholder = st.empty()
        full_response = ""

        # Stream each chunk
        for message_chunk, metadata in chatbot.stream(
            {'message': [HumanMessage(content=user_input)]},
            config={'configurable': {'thread_id': 'thread-1'}},
            stream_mode='messages'
        ):
            full_response += message_chunk.content
            response_placeholder.markdown(full_response + "▌")  # Add cursor effect

        # Finalize message
        response_placeholder.markdown(full_response)

    # Save assistant response
    st.session_state['message_history'].append({'role': 'assistant', 'content': full_response})
