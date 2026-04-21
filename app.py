import streamlit as st
# Import your custom modules (ensure they are in the same folder)
from text_analysis import analyze_text
from voice_analysis import analyze_voice
from face_analysis import analyze_face

# Final decision logic (included for completeness)
def get_final_decision(text_emotion, voice_emotion, face_emotion):
    emotions = [text_emotion.lower(), voice_emotion.lower(), face_emotion.lower()]
    pos = sum(e in ["positive", "happy", "joy"] for e in emotions)
    neg = sum(e in ["negative", "sad", "angry", "fear"] for e in emotions)
    neu = sum(e in ["neutral"] for e in emotions)
    sur = sum(e in ["surprise"] for e in emotions)

    if neg >= 2: return "User is highly stressed"
    elif pos >= 2: return "User is happy"
    elif sur >= 1: return "User is surprised"
    elif neu >= 2: return "User is neutral"
    elif neg == 1: return "Slight stress detected"
    elif pos == 1: return "Slightly positive mood"
    else: return "Mixed emotions"

# UI Setup
st.set_page_config(page_title="Mental Health AI", page_icon="🧠")
st.title("🧠 Mental Health AI Analyzer")
st.write("Please provide your input for analysis.")

# Input Field
user_text = st.text_area("How are you feeling today?")

if st.button("Analyze My State"):
    if not user_text:
        st.warning("Please enter some text first!")
    else:
        with st.spinner('Analyzing your voice and facial cues...'):
            # Run your analysis functions
            text_emo = analyze_text(user_text)
            voice_emo = analyze_voice() # Assuming voice returns text
            face_emo = analyze_face()

            # Result logic
            result = get_final_decision(text_emo, voice_emo, face_emo)
            
            # Display results
            st.success(f"### Final Status: {result}")
            
            # Save report
            with open("report.txt", "w") as f:
                f.write(result)
            st.info("Report saved to report.txt")
