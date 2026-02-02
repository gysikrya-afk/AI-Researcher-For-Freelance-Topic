import streamlit as st

from src.css import font,bg_color

font()
bg_color()

st.set_page_config(
    page_title="Контакты | AI Freelance Agent", page_icon="🔗", layout="centered"
)

st.title("Контакты🔗")

st.markdown(
    """
    Тут вы найдёте контакты для службы поддержки,исходный код и ссылки на социальные сети
    """
)
st.divider()

st.header("⚒️Служба поддержки")

st.markdown("""
    Email: feedback.ai.freelance.agent@gmail.com
    """)

st.divider()

st.header("🔗Контакты")

st.link_button(
    "GitHub", url="https://github.com/gysikrya-afk/AI-Researcher-For-Freelance-Topic"
)
