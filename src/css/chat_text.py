import streamlit as st

def chat_input_text():
    st.markdown(
        """
        <style>

        div[data-testid="stChatInput"] {
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding-bottom: 20px;
        }

        div[data-testid="stChatInput"] textarea {
            background-color: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: white !important;
        }

        footer {
            display: none !important;
        }

        .stApp {
            background-attachment: fixed;
        }

        </style>
        """,unsafe_allow_html=True
    )