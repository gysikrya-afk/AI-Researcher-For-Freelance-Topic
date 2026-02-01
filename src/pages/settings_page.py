import streamlit as st

st.set_page_config(
    page_title="Настройки | AI Freelance Agent", page_icon="⚙️", layout="centered"
)

st.title("Настройки⚙️")

st.markdown(
    """
    На этой странице вы должны вбить Gemini API Key и выбрать модель
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
    st.success('Ключ принят!')

st.divider()

st.header("Выбор модели")

models = st.selectbox(
    "Выберите модель Gemini", options=["gemini-2.5-flash", "gemini-2.5-flash-lite"]
)

if st.button("✅Сохранить настройки"):
    if not api_key:
        st.warning("Введите ключ!")
    else:
        with st.spinner('Сохраняю...'):
            st.session_state.api_key = api_key
            st.session_state.models = models
    
            st.toast('Настройки применены!', icon='🔥')