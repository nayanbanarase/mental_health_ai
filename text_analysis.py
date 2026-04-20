from transformers import pipeline

classifier = pipeline("sentiment-analysis")


def analyze_text(text):
    if not text.strip():
        return "neutral"

    result = classifier(text)[0]
    label = result['label'].lower()

    if "pos" in label:
        return "positive"
    elif "neg" in label:
        return "negative"
    else:
        return "neutral"
    