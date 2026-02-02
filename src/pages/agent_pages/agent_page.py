import streamlit as st

from src.agents import run_agent_gemini
from src.files import create_docx
from src.css import font, bg_color, chat_input_text

font()
bg_color()
chat_input_text()

st.set_page_config(
    page_title="Агент | AI Freelance Agent", page_icon="🦾", layout="centered"
)

st.title("Агент🦾")

if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "models" not in st.session_state:
    st.session_state.models = "gemini-2.5-flash"

st.markdown(
    """
    На этой страничке есть агент для **аналитики** и **иследования** тем на фрилансе.
    Если нужна помощь нажмите на кнопку **Помощь**.
    """
)

st.divider()

topic = st.chat_input("Введите тему для анализа (например, Дизайн интерфейсов)")

if topic:
    try:
        if not st.session_state.api_key:
            st.error("Введите Gemini API Key в Настройках")

        else:
            with st.chat_message("user"):
                st.write(topic)

            with st.chat_message("assistant"):
                st.write("Начинаю анализ рынка по вашей теме...")

                result = run_agent_gemini(
                    api_key=st.session_state.api_key,
                    model=st.session_state.models,
                    topic=topic,
                )

                st.markdown(result)

                col1, col2 = st.columns(2)

                with col1:
                    st.download_button(
                        label="Скачать результат(Формат .txt)",
                        data=result,
                        file_name="freelance_analysis.txt",
                        mime="text/markdown",
                    )

                with col2:
                    result_docx = create_docx(result)
                    st.download_button(
                        label="Скачать результат(Формат .docx)",
                        data=result_docx,
                        file_name="freelance_analysis.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    )

    except Exception as e:
        st.error("Ошибка!")
        st.exception(e)

st.caption("Помните,ИИ может ошибаться,тож проверяйте информацию!")
