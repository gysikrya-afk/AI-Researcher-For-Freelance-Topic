import streamlit as st

from src.css import font, bg_color, text
from src.configs.config_other import GEMINI_MODELS

font()
bg_color()
text()

st.set_page_config(
    page_title="Настройки | AI Freelance Agent", page_icon="⚙️", layout="centered"
)

st.title("Настройки⚙️")

st.markdown(
    """
    ###### Для запуска исследования, пожалуйста:
    1. Вставьте ваш **Gemini API Key**.
    2. Выберите подходящую нейросеть из списка ниже.
    """
)

if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "models" not in st.session_state:
    st.session_state.models = "gemini-2.5-flash"

st.divider()

st.header("🔑Gemini API Key")

api_key = st.text_input(
    "Введите Gemini API Key",
    type="password",
    help="Ключ можна получить на официальном сайте",
)

if api_key:
    st.success("Ключ принят!")

st.divider()

st.header("Выбор модели")

models = st.selectbox(
    "Выберите модель Gemini", options=GEMINI_MODELS
)

st.divider()

if st.button("✅Сохранить настройки"):
    if not api_key:
        st.warning("Введите ключ!")
    else:
        with st.spinner("Сохраняю..."):
            st.session_state.api_key = api_key
            st.session_state.models = models

            st.toast("Настройки применены!", icon="🔥")
