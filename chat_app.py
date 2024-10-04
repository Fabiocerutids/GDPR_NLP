import streamlit as st 
from chat_with_assistant import GDPR_AI_Assistant

initial_system_prompt = """Using the information contained in the context, give a comprehensive answer to the question.
\nRespond only to the question asked, response should be concise and relevant to the question. 
\nIf the answer cannot be deduced from the context, do not give an answer"""

initial_temperature = 0.1
initial_max_length= 500

@st.cache_resource
def instantiate_assistant():
    #Available Models: https://api-inference.huggingface.co/framework/text-generation-inference
    my_assistant = GDPR_AI_Assistant(generator_model="openai-community/gpt2") #mistralai/Mistral-7B-Instruct-v0.3 
    my_assistant.create_session()
    my_assistant.set_system_parameters(prompt=initial_system_prompt, temperature=initial_temperature, max_length=initial_max_length)
    return my_assistant

my_assistant = instantiate_assistant()    

if "messages" not in st.session_state:
    st.session_state.messages = []
    
st.sidebar.header('Chatbot Settings')
system_prompt = st.sidebar.text_area(
    "System Prompt",
    value = initial_system_prompt,
    height=280,
    help="Set the system prompt for the chatbot"
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.1,
    max_value=1.0,
    value=initial_temperature,
    step=0.05,
    help="Set the generation temperature"
)

max_length = st.sidebar.slider(
    "Max Tokens Generated",
    min_value=100,
    max_value=1000,
    value=initial_max_length,
    step=50,
    help="Set the number of Tokens Generated"
)

st.title("Your GDPR Assistant")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def reset_conversation():
    st.session_state.messages = []

def update_settings():
    my_assistant.set_system_parameters(prompt=system_prompt, temperature=temperature, max_length=max_length)
 
st.sidebar.button('Submit Chatbot Settings', on_click=update_settings)    
st.sidebar.button('Reset Chat', on_click=reset_conversation)

# Get user input
user_input = st.chat_input("Type your question here")
if user_input:
    # Display user message in the chat
    st.chat_message("user").markdown(user_input)
    flag_new_message=False
    if len(st.session_state.messages)==0:
        flag_new_message=True
    assistant_message = my_assistant.chat_with_llm(user_input, flag_new_message)
    print(assistant_message)
    # Append user message to the session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display assistant's response in the chat
    st.chat_message("assistant").markdown(assistant_message)

    # Append assistant response to the session state
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})