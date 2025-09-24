'''
A robust chatbot application using Google Generative AI models with Streamlit.
'''

import google.generativeai as genai
import google.api_core.exceptions as gexceptions
import streamlit as st


def initialize_session():
    """ Initialize session state variables. """
    if 'messages' not in st.session_state:
        st.session_state['messages'] = [{
            'role': 'assistant',
            'content': 'How can I help you?'
        }]
    if 'ready' not in st.session_state:
        st.session_state['ready'] = False


def validate_inputs(_api_key: str, _model_name: str) -> bool:
    """ Validate if API key and model name are provided. """
    if not _api_key:
        st.info('Please add your Google API Key to continue...')
        return False
    if not _model_name:
        st.info('Please select a model to continue...')
        return False
    return True


def get_model(_api_key: str, _model_name: str) -> genai.GenerativeModel | None:
    """ Initialize and return the GenerativeModel. """
    try:
        genai.configure(api_key=_api_key)
        return genai.GenerativeModel(model_name=_model_name)
    except (gexceptions.GoogleAPICallError) as e:
        st.error(
            f"Failed to initialize the model. Please check your API key and model selection. \
            Details: {e.message}"
        )
        return None


def generate_response(_model: genai.GenerativeModel, _prompt: str) -> str | None:
    """ Generate a response from the model based on the user prompt. """
    try:
        resp = _model.generate_content(contents=_prompt)
        return resp.text
    except (gexceptions.GoogleAPICallError) as e:
        st.error(
            f"Failed to get a response from the model. Details: {e.message}")
        return None


with st.sidebar:
    api_key = st.text_input(
        label='Google API Key',
        key='_api_key',
        type='password',
        help='Get your API key from https://aistudio.google.com/apikey',
        placeholder='Enter your Google API Key',
    )
    model_name = st.selectbox(
        label='Select Model',
        options=[
            'gemini-2.5-pro',
            'gemini-2.5-flash',
            'gemini-2.5-flash-lite',
            'gemini-2.0-flash',
            'gemini-2.0-flash-lite',
        ],
        index=None,
        help='Choose a Gemini model'
    )

st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon=":ghost:",  # Optional: set a favicon
    layout="centered",  # Optional: set page layout
    initial_sidebar_state="auto"  # Optional: set sidebar state
)
st.title('💬 Q&A Chatbot')

initialize_session()

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

# Only enable chat input if API key and model are set
INPUT_DISABLED = not validate_inputs(api_key, model_name)
prompt = st.chat_input(disabled=INPUT_DISABLED)

if prompt and not INPUT_DISABLED:
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)

    model = get_model(api_key, model_name)
    if model:
        response = generate_response(model, prompt)
        if response:
            st.session_state.messages.append(
                {'role': 'assistant', 'content': response})
            st.chat_message('assistant').write(response)
        else:
            st.session_state.messages.append(
                {'role': 'assistant', 'content': "Sorry, I couldn't process your request."})
            st.chat_message('assistant').write(
                "Sorry, I couldn't process your request.")
