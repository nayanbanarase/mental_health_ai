# AI-Based Mental Health Detection System using Text, Voice and Facial Emotion Recognition

## Abstract

Mental health has become a significant concern worldwide, making early emotional assessment increasingly important. This project presents an AI-Based Mental Health Detection System that analyzes a user's emotional state using three different input modalities: text, voice, and facial expressions. The system utilizes Natural Language Processing (NLP) for text emotion analysis, Speech Recognition for converting voice to text, and Computer Vision for detecting facial emotions through a webcam. The emotions detected from these three sources are combined to generate an overall assessment of the user's mental state. The project is intended for educational purposes and demonstrates the integration of Artificial Intelligence, Machine Learning, and Computer Vision into a single application.

---

# 1. Introduction

Mental health plays a crucial role in an individual's overall well-being. Due to increasing stress levels and lifestyle changes, there is a growing need for intelligent systems capable of providing preliminary emotional assessment.

This project proposes an AI-based mental health detection system capable of analyzing user emotions through multiple input sources. Unlike traditional systems that depend on questionnaires, this application combines textual analysis, speech recognition, and facial emotion recognition to provide a more comprehensive emotional evaluation.

The project demonstrates the practical implementation of Artificial Intelligence techniques using Python and open-source libraries.

---

# 2. Literature Review

Several researchers have explored emotion recognition using Artificial Intelligence.

- Natural Language Processing (NLP) techniques have been widely used for sentiment and emotion analysis from textual data.
- Speech Recognition systems convert spoken language into text, enabling further emotion analysis.
- Computer Vision techniques such as facial expression recognition allow systems to identify emotions through facial movements.
- Multi-modal emotion recognition systems combine multiple sources of information, leading to higher prediction accuracy compared to single-input systems.

This project integrates these existing approaches into a single user-friendly application.

---

# 3. Methodology

The proposed system follows a multi-modal emotion detection approach.

### Step 1: Text Analysis
The user enters textual information describing their feelings. The system uses a Hugging Face Transformer model to classify emotions.

↓

### Step 2: Voice Analysis
The user speaks through the microphone. Speech Recognition converts speech into text, which is then analyzed using the same NLP model.

↓

### Step 3: Facial Emotion Detection
The webcam captures the user's face. The FER (Facial Emotion Recognition) library detects the dominant facial emotion.

↓

### Step 4: Decision Engine
The detected emotions from text, voice, and face are combined using a rule-based decision system to generate the final mental health assessment.

---

# 4. System Architecture

```
User
 │
 ├──────────────┐
 │              │
Text        Voice        Webcam
 │              │           │
 ▼              ▼           ▼
Transformer  Speech      FER Model
 NLP Model  Recognition
 │              │           │
 └──────┬───────┴───────────┘
        ▼
 Decision Engine
        ▼
 Final Mental Health Prediction
```

---

# 5. Implementation

The application is implemented using Python 3.10.

### Development Environment

- Python 3.10
- Visual Studio Code
- Windows Operating System

### Libraries Used

- transformers
- torch
- SpeechRecognition
- OpenCV
- FER
- NumPy

### Project Modules

### 1. Text Analysis
Detects emotions from user-entered text using Hugging Face Transformers.

### 2. Voice Analysis
Captures audio through the microphone and converts speech into text using Google's Speech Recognition API.

### 3. Face Analysis
Uses OpenCV and FER to recognize facial emotions through the webcam.

### 4. Decision Module
Combines emotions from all three inputs to determine the user's overall emotional condition.

---

# 6. Results

The developed system successfully performs:

- Text Emotion Recognition
- Voice-to-Text Conversion
- Facial Emotion Detection
- Combined Emotion Analysis

Example Output:

```
Text Emotion : Sad

Voice Emotion : Neutral

Face Emotion : Happy

Final Result:
User may be stressed.
```

---

# 7. Advantages

- Multi-modal emotion recognition
- Beginner-friendly implementation
- Easy to use
- Low-cost solution
- Real-time emotion detection
- Modular architecture

---

# 8. Limitations

- Not a medical diagnosis tool.
- Voice recognition requires internet connectivity.
- Emotion prediction depends on lighting conditions and camera quality.
- Rule-based decision making can be further improved.

---

# 9. Conclusion

This project demonstrates how Artificial Intelligence techniques can be integrated to perform preliminary mental health assessment using text, voice, and facial expressions. The proposed system provides an educational implementation of multi-modal emotion recognition and highlights the practical applications of NLP, Speech Recognition, and Computer Vision. Although the system is not intended for clinical diagnosis, it provides a strong foundation for future AI-based healthcare applications.

---

# 10. Future Scope

Future enhancements include:

- Deep Learning-based decision model
- Depression severity prediction
- Anxiety detection
- Stress monitoring dashboard
- Real-time continuous monitoring
- Mobile application development
- Cloud deployment
- Database integration
- User authentication
- AI chatbot for mental health support
- Report generation in PDF
- Doctor recommendation system

---

# 11. References

1. Vaswani, A., et al. "Attention Is All You Need." NeurIPS, 2017.

2. Hugging Face Transformers Documentation.
https://huggingface.co/docs/transformers

3. OpenCV Official Documentation.
https://opencv.org/

4. FER (Facial Emotion Recognition) Documentation.
https://github.com/justinshenk/fer

5. SpeechRecognition Python Library Documentation.
https://pypi.org/project/SpeechRecognition/

6. NumPy Documentation.
https://numpy.org/doc/

7. Python Official Documentation.
https://docs.python.org/3.10/

---

# Author

**Nayan Shankar Banarase**

Master of Computer Applications (MCA)

Academic AI Project

---

# License

This project is developed for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis or treatment.
