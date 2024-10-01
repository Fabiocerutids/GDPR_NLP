import streamlit as st 
from chat_with_assistant import GDPR_AI_Assistant
@st.cache_resource
def instantiate_assistant():
    my_assistant = GDPR_AI_Assistant()
    my_assistant.create_session()
    return my_assistant

my_assistant = instantiate_assistant()    

if "messages" not in st.session_state:
    st.session_state.messages = []
    
st.sidebar.header('Chatbot Settings')
system_prompt = st.sidebar.text_area(
    "System Prompt",
    value = """Using the information contained in the context, give a comprehensive answer to the question. 
    \nRespond only to the question asked, response should be concise and relevant to the question. 
    \nIf the answer cannot be deduced from the context, do not give an answer""",
    height=280,
    help="Set the system prompt for the chatbot"
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.1,
    max_value=1.0,
    value=0.1,
    step=0.05,
    help="Set the generation temperature"
)

max_new_tokens = st.sidebar.slider(
    "Max New Tokens",
    min_value=100,
    max_value=1000,
    value=200,
    step=50,
    help="Set the number of new tokens"
)

st.title("Your GDPR Assistant")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def reset_conversation():
    st.session_state.messages = []
    update_settings()

def update_settings():
    my_assistant.set_system_parameters(prompt=system_prompt, temperature=temperature, max_new_tokens=max_new_tokens)
 
st.sidebar.button('Submit Chatbot Settings', on_click=update_settings)    
st.sidebar.button('Reset Chat', on_click=reset_conversation)

# Get user input
user_input = st.chat_input("Type your question here")
if user_input:
    # Display user message in the chat
    st.chat_message("user").markdown(user_input)
    print(st.session_state.messages)
    if len(st.session_state.messages)==0:
        assistant_message = my_assistant.chat_with_llm('hello', True)[10:]
    else:
        assistant_message = my_assistant.chat_with_llm(user_input, False)[10:]

    # Append user message to the session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display assistant's response in the chat
    st.chat_message("assistant").markdown(assistant_message)

    # Append assistant response to the session state
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})