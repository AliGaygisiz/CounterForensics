import streamlit as st
import os

def make_sidebar():
    with st.sidebar:
        st.title("🕵️‍♂️ CounterForensics")
        
        st.write("")

        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link("pages/scanner.py", label="The Scanner", icon="📊")
        st.page_link("pages/humanizer.py", label="The Humanizer", icon="📷")
        st.page_link("pages/faker.py", label="The Faker", icon="🎭")

        st.divider()

        # [CONFIG] Show upsell only on Live/PROD env
        if os.getenv("PROD", "false").lower() == "true":
            st.markdown(
                """
                <div style="font-size: 0.8em; color: #a1a1aa; line-height: 1.4;">
                    <strong>⚠️ Live Demo Limits</strong><br>
                    This instance is restricted to 10MB & 1024px. 
                    For high-resolution analysis without limits, run locally via the 
                    <a href="https://github.com/AliGaygisiz/CounterForensics" target="_blank" style="color: #4f46e5;">source code</a>.
                </div>
                """,
                unsafe_allow_html=True
            )
            st.divider()

        st.info("🔒 Processed in RAM only. Nothing is stored.")
