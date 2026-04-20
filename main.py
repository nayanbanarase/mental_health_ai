from text_analysis import analyze_text
from voice_analysis import analyze_voice
from face_analysis import analyze_face


def final_decision(text_emotion, voice_emotion, face_emotion):

    emotions = [
        text_emotion.lower(),
        voice_emotion.lower(),
        face_emotion.lower()
    ]

    print("All Emotions:", emotions)

    # Count emotions
    positive_count = sum(e in ["positive", "happy", "joy"] for e in emotions)
    negative_count = sum(e in ["negative", "sad", "angry", "fear"] for e in emotions)
    neutral_count = sum(e in ["neutral"] for e in emotions)
    surprise_count = sum(e in ["surprise"] for e in emotions)

    # Decision logic
    if negative_count >= 2:
        return "User is highly stressed"

    elif positive_count >= 2:
        return "User is happy"

    elif surprise_count >= 1:
        return "User is surprised"

    elif neutral_count >= 2:
        return "User is neutral"

    elif negative_count == 1:
        return "Slight stress detected"

    elif positive_count == 1:
        return "Slightly positive mood"

    else:
        return "Mixed emotions"


# STEP 1: TEXT
user_text = input("Enter your feelings: ")
text_emotion = analyze_text(user_text).lower()

# STEP 2: VOICE
voice_text = analyze_voice()
voice_emotion = analyze_text(voice_text).lower()

# STEP 3: FACE
face_emotion = analyze_face().lower()

# DEBUG
print("Text Emotion:", text_emotion)
print("Voice Emotion:", voice_emotion)
print("Face Emotion:", face_emotion)

# FINAL RESULT
result = final_decision(text_emotion, voice_emotion, face_emotion)

print("\nFinal Mental Health Status:", result)

# Save report
with open("report.txt", "w") as f:
    f.write(result)
