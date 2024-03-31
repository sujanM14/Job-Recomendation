import streamlit as st

def add_logo():

    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "ConnectHire";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
