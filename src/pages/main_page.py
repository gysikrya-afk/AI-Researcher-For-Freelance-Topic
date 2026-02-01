import streamlit as st

from src.config import (
    streat_text_agent,
    streat_text_how_work,
    streat_text_technology,
    streat_text_people,
)

st.set_page_config(
    page_title="Главная | AI Freelance Agent", page_icon="👋", layout="centered"
)

st.title("Главная страница👋")

st.markdown('<div class="custom-card">', unsafe_allow_html=True)
st.subheader("🚀 О проекте")
st.write("Этот агент помогает анализировать фриланс-рынок с помощью нейросетей.")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(['🧠Про агента','🛠️Как с ним работать','👩‍💻 Технологии','👨Для кого нужен','Посмотреть текущую версию'])

with tab1:
    st.write_stream(streat_text_agent())

with tab2:
    st.write(streat_text_how_work())

with tab3:
    st.write(streat_text_technology())

with tab4:
    st.write(streat_text_people())

with tab5:
    st.write('1.0.0')

st.divider()

st.info(
    "👉 Перейдите в **Настройки**, чтобы начать"
)
st.caption("Проект ещё находиться в **разроботке**,тож могут выходить ещё обновления")
