from fer import FER
import cv2


def analyze_face():
    detector = FER(mtcnn=True)

    cap = cv2.VideoCapture(0)

    print("Press 'q' to capture")

    while True:
        ret, frame = cap.read()

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    result = detector.detect_emotions(frame)

    if result:
        emotions = result[0]["emotions"]
        dominant_emotion = max(emotions, key=emotions.get)
        print("Face Emotion:", dominant_emotion)
        return dominant_emotion
    else:
        return "neutral"
    