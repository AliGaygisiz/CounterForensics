import streamlit as st

def make_sidebar():
    with st.sidebar:
        st.title("🕵️‍♂️ CounterForensics")
        
        st.write("")

        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link("pages/scanner.py", label="The Scanner", icon="📊")
        st.page_link("pages/humanizer.py", label="The Humanizer", icon="📷")
        st.page_link("pages/faker.py", label="The Faker", icon="🎭")

        st.divider()

        st.info("🔒 Processed in RAM only. Nothing is stored.")
