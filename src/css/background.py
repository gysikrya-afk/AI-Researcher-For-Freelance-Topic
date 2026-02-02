import streamlit as st


def bg_color():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(90deg, #054c76,#0c192a,#471c3a);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
