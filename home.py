import streamlit as st
from datetime import datetime

def run():
    st.title("Welcome to the Election Education Portal")
    st.markdown("### Empowering Voters Through Education")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.write("""
        Elections are the cornerstone of a functioning democracy. This portal is designed to provide you with the information you need to participate effectively and understand how the electoral system works.
        
        **Here you can find:**
        * 📝 Step-by-step voter registration guides
        * 🏛️ Explanations of how our electoral system operates
        * 🧠 Quizzes to test your knowledge
        """)
        
        st.info("Navigate using the sidebar to explore different modules.")

    with col2:
        st.markdown("### ⏳ Countdown to Next Election")
        # Placeholder date for the next major US election (e.g., Nov 3, 2026)
        election_date = datetime(2026, 11, 3)
        today = datetime.now()
        delta = election_date - today
        
        if delta.days > 0:
            st.metric(label="Days Remaining", value=f"{delta.days} Days")
            st.write("Mark your calendar! Every vote counts.")
        else:
            st.success("Election day has arrived or passed! Stay engaged.")

    st.image("https://images.unsplash.com/photo-1540910419892-4a36d2c3266c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", use_container_width=True, caption="Democracy in Action")
