import streamlit as st


def text():
    st.markdown(
        """
        <style>

        input {
            border-radius: 10px !important;
            border: 1px solid #30363d !important;
        }
        
        </style>
        """,
        unsafe_allow_html=True,
    )
