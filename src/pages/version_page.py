import streamlit as st

st.set_page_config(
    page_title="Версии | AI Freelance Agent", page_icon="🗂️", layout="centered"
)

st.title("Версии🗂️")

st.markdown(
    """
    Тут вы найдёте все версии проекта
    """
)

st.divider()

with st.expander('1.0.0'):
    st.markdown("""
    ##### Первоначальный проект
    """)


st.caption("После каждого обновление будут добавляться новые версии")
