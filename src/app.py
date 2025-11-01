'''
A robust chatbot application using Google Generative AI models with Streamlit.
'''

from google import genai
from google.genai.errors import APIError
import streamlit as st


class Config:
    """ Configuration settings for the chatbot application. """


    def __init__(self, _api_key: str) -> None:
        self.__api_key = _api_key
        self.__client: genai.Client | None = None

    def get_client(self) -> genai.Client:
        """ Create and return a GenAI client instance. """
        if self.__client is None:
            self.__client = genai.Client(api_key=self.__api_key)

        return self.__client


def initialize_session() -> None:
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


def generate_response(_client: genai.Client, _model_name: str, _prompt: str) -> str | None:
    """ Generate a response from the model based on the user prompt. """
    try:
        resp = _client.models.generate_content(
            model=_model_name,
            contents=_prompt
        )
        return resp.text
    except (APIError) as e:
        st.error(
            f"Failed to get a response from the model. Details: {e.message}"
        )
        return None


AVAILABLE_MODELS = [
    'gemini-2.5-pro',
    'gemini-2.5-flash',
    'gemini-2.5-flash-lite',
    'gemini-2.0-flash',
    'gemini-2.0-flash-lite',
]

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
        options=AVAILABLE_MODELS,
        index=None,
        help='Choose a Gemini model'
    )

st.set_page_config(
    page_title='Gemini Chatbot',
    page_icon=':ghost:',  # Optional: set a favicon
    layout='centered',  # Optional: set page layout
    initial_sidebar_state='auto'  # Optional: set sidebar state
)
st.title('💬 Q&A Chatbot')

initialize_session()

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

# Only enable chat input if API key and model are set
INPUT_DISABLED = not validate_inputs(api_key, model_name)
prompt = st.chat_input(disabled=INPUT_DISABLED)

GENAI_CLIENT = None

if not INPUT_DISABLED:
    GENAI_CLIENT = Config(api_key).get_client()
else:
    if GENAI_CLIENT is not None:
        GENAI_CLIENT.close()
    GENAI_CLIENT = None

if prompt and GENAI_CLIENT is not None:
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)

    response = generate_response(GENAI_CLIENT, model_name, prompt)
    if response:
        st.session_state.messages.append(
            {'role': 'assistant', 'content': response})
        st.chat_message('assistant').write(response)
    else:
        st.session_state.messages.append(
            {'role': 'assistant', 'content': "Sorry, I couldn't process your request."})
        st.chat_message('assistant').write(
            "Sorry, I couldn't process your request.")
