import streamlit as st


def font_style():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Mulish:ital@1&display=swap');

        html, body, [class*="st-"] .main .block-container {
            font-family: 'Mulish', italic !important;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Mulish', italic !important;
            font-weight: 700;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
