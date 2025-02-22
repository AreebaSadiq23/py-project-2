import streamlit as st
import random

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🧠", layout="wide")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Learn", "Quiz", "Reflect"])
    
    if page == "Home":
        home_page()
    elif page == "Learn":
        learn_page()
    elif page == "Quiz":
        quiz_page()
    elif page == "Reflect":
        reflect_page()

def home_page():
    st.title("🌱 Welcome to the Growth Mindset Challenge!")
    st.write("""
    Unlock your potential by developing a growth mindset. 
    Explore the sections to learn, test your knowledge, and reflect on your progress.
    """)
    if st.button("Start Learning →"):
        st.session_state.page = "Learn"
        st.rerun()

def learn_page():
    st.title("📖 Understanding Growth Mindset")
    st.write("A growth mindset is the belief that abilities can be developed through effort and learning.")
    
    principles = {
        "💪 Embrace Challenges": "View obstacles as opportunities to grow.",
        "💡 Learn from Criticism": "Feedback helps you improve.",
        "🚀 Persist in Setbacks": "Effort leads to mastery.",
        "👀 Find Lessons in Others' Success": "Be inspired by others' achievements."
    }
    
    for title, desc in principles.items():
        st.subheader(title)
        st.write(desc)
    
    st.success("Keep pushing forward! Growth is a journey, not a destination.")

def quiz_page():
    st.title("🧠 Test Your Growth Mindset Knowledge")
    
    questions = [
        {"question": "Which statement aligns with a growth mindset?", 
         "options": ["I'm either good at something or not.", "I can learn to do anything.", "There's no point in trying if I fail.", "Some people are just naturally talented."], 
         "correct": 1},
        {"question": "How should you view challenges?", 
         "options": ["Avoid them", "A sign of limits", "An opportunity to grow", "Unfair obstacles"], 
         "correct": 2}
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        answer = st.radio(q["question"], q["options"], key=f"q{i}")
        
        if st.button(f"Submit {i}"):
            if q["options"].index(answer) == q["correct"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Incorrect. The right answer was: {q['options'][q['correct']]}")
    
    if st.button("See Results"):
        st.write(f"**Your score: {score}/{len(questions)}**")
        if score == len(questions):
            st.balloons()
            st.success("Amazing! You truly understand a growth mindset!")
        else:
            st.info("Review the 'Learn' section and try again!")

def reflect_page():
    st.title("📝 Reflect on Your Growth")
    
    goal = st.text_input("Set a learning goal:")
    if goal:
        st.write(f"Great goal! Keep working towards learning **{goal}**.")
    
    st.subheader("Daily Reflection")
    st.date_input("Date")
    st.text_area("What challenge did you face today?")
    st.text_area("What did you learn from this challenge?")
    st.text_area("What will you do differently next time?")
    
    if st.button("Save Reflection"):
        st.success("Reflection saved! Keep growing!")

if __name__ == "__main__":
    main()



