import streamlit as st
import importlib

# App Configuration
st.set_page_config(
    page_title="Election Education Portal",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    h2, h3 {
        color: #34495e;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 24px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.sidebar.title("🗳️ Navigation")
    st.sidebar.markdown("Explore the Election Education Portal.")
    
    pages = {
        "Home": "modules.home",
        "Voter Registration": "modules.registration",
        "How the System Works": "modules.system",
        "Knowledge Quiz": "modules.quiz"
    }

    selection = st.sidebar.radio("Go to", list(pages.keys()))

    st.sidebar.markdown("---")
    st.sidebar.info("💡 Your vote is your voice!")

    # Dynamic Module Loading
    try:
        module = importlib.import_module(pages[selection])
        module.run()
    except Exception as e:
        st.error(f"Error loading module: {e}")

if __name__ == "__main__":
    main()
