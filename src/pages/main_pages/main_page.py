import streamlit as st

from src.configs.config_text import (
    streat_text_agent,
    streat_text_people,
)

from src.css import font, bg_color

bg_color()
font()

st.set_page_config(
    page_title="Главная | AI Freelance Agent", page_icon="👋", layout="centered"
)

st.title("Главная страница")

st.markdown('<div class="custom-card">', unsafe_allow_html=True)
st.subheader("🚀 О проекте")
st.write("""
##### Твой персональный аналитик фриланс-индустрии на базе нейросетей. \n
Наш ИИ-агент автоматизирует рутинный сбор данных, превращая хаос предложений на биржах в четкую стратегию для роста.


    """)
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)

with col1:
    with st.expander("Про агента"):
        st.write_stream(streat_text_agent())

with col2:
    with st.expander("Для кого нужен"):
        st.write_stream(streat_text_people)
