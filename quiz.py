import streamlit as st

def run():
    st.title("Knowledge Quiz 🧠")
    st.markdown("### Test what you've learned!")

    # Initialize session state for score
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

    questions = [
        {
            "question": "What is the primary function of the Electoral College in the US?",
            "options": ["To elect the President and Vice President", "To elect Senators", "To pass federal laws", "To count the popular vote"],
            "answer": "To elect the President and Vice President"
        },
        {
            "question": "Which voting system allows you to order candidates by preference?",
            "options": ["First-Past-The-Post", "Ranked-Choice Voting", "Proportional Representation", "Electoral College"],
            "answer": "Ranked-Choice Voting"
        },
        {
            "question": "When should you typically check your voter registration status?",
            "options": ["The day of the election", "A few months before the election", "Only when you move", "Never"],
            "answer": "A few months before the election"
        }
    ]

    with st.form("quiz_form"):
        user_answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**{i+1}. {q['question']}**")
            ans = st.radio(f"Select an answer for question {i+1}", q['options'], key=f"q{i}", label_visibility="collapsed")
            user_answers.append(ans)
            st.write("---")
        
        submitted = st.form_submit_button("Submit Answers")

        if submitted:
            st.session_state.quiz_submitted = True
            score = 0
            for i, ans in enumerate(user_answers):
                if ans == questions[i]['answer']:
                    score += 1
            st.session_state.score = score

    if st.session_state.quiz_submitted:
        st.subheader("Results")
        st.write(f"You scored **{st.session_state.score}** out of **{len(questions)}**.")
        
        if st.session_state.score == len(questions):
            st.balloons()
            st.success("Perfect score! You are ready for Election Day!")
        elif st.session_state.score > 0:
            st.info("Good job! Review the 'How the System Works' page to brush up on your knowledge.")
        else:
            st.error("Keep learning! Check out the other modules to improve your score.")
        
        if st.button("Retake Quiz"):
            st.session_state.quiz_submitted = False
            st.session_state.score = 0
            st.rerun()
