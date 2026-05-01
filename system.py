import streamlit as st

def run():
    st.title("Understanding the Electoral System")
    st.markdown("### How does voting actually work?")

    st.write("Electoral systems can be complex. Here is a breakdown of common concepts to help you understand how your vote translates into representation.")

    # Accordion for different topics
    with st.expander("🗳️ Popular Vote vs. Electoral College (US Context)", expanded=True):
        st.write("""
        **Popular Vote:** The total number of votes cast by eligible voters. In many elections (like local or congressional races), the candidate with the most popular votes wins.
        
        **Electoral College:** In US Presidential elections, the winner is determined by the Electoral College. Each state is assigned a number of 'electors' based on its congressional representation. A candidate needs a majority of electoral votes (270) to win the presidency.
        """)
    
    with st.expander("📜 Types of Voting Systems"):
        st.write("""
        * **First-Past-The-Post (Plurality):** The candidate who receives the most votes wins, even if they do not win an absolute majority (more than 50%).
        * **Ranked-Choice Voting:** Voters rank candidates by preference. If no candidate wins a majority of first-preference votes, the candidate with the fewest votes is eliminated, and their votes are redistributed to the voters' next choices. This continues until a candidate has a majority.
        * **Proportional Representation:** Seats in a legislature are allocated based on the percentage of votes each party receives.
        """)

    with st.expander("🗃️ How Ballots are Counted"):
        st.write("""
        Votes are typically counted using optical scanners or electronic voting machines. After polls close, the results are tallied at local election offices and reported to state agencies. Audits and recounts may occur if margins are extremely close.
        """)

    st.markdown("---")
    st.subheader("Did you know?")
    st.info("In Australia, voting is compulsory for all citizens aged 18 and over. Failing to vote can result in a fine!")
