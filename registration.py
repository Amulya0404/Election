import streamlit as st

def run():
    st.title("Voter Registration Guide")
    st.markdown("### Make sure you're ready for Election Day!")

    st.write("""
    Registering to vote is the first step to making your voice heard. Follow this interactive guide to ensure you meet all requirements.
    """)

    st.markdown("---")
    
    st.subheader("📋 Registration Checklist")
    
    # Interactive checklist
    req1 = st.checkbox("Are you a citizen of the country where you are registering?")
    req2 = st.checkbox("Will you be of legal voting age by the next election?")
    req3 = st.checkbox("Do you have a valid form of identification (if required by your state/region)?")
    req4 = st.checkbox("Are you a resident of the district you wish to vote in?")

    if req1 and req2 and req3 and req4:
        st.success("Great! You meet the basic requirements to register to vote.")
    else:
        st.warning("Please ensure you meet all the requirements above before registering.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("How to Register")
        st.markdown("""
        * **Online:** Many regions offer online voter registration through official government portals.
        * **By Mail:** You can often download a form, fill it out, and mail it to your local election office.
        * **In-Person:** Register at local election offices, DMV branches, or sometimes public libraries and post offices.
        """)

    with col2:
        st.subheader("Key Deadlines")
        st.error("""
        * **Registration Deadline:** Varies by state (usually 15-30 days before an election).
        * **Mail-in Ballot Request:** Check your local requirements well in advance.
        """)
        st.button("Find My Local Election Office") # Dummy button for UX

    st.info("Tip: Always verify your voter registration status a few months before a major election to ensure you haven't been unexpectedly removed from the voter rolls.")
