import cv2
from deepface import DeepFace
import face_recognition


def image_analyze(image):
    # image = cv2.imread(img)
    analyze = DeepFace.analyze(image, actions=('age', 'gender', 'race', 'emotion'))
    analyze_result = {"age": analyze["age"], "gender": analyze["gender"], "race": analyze["dominant_race"],
                      "emotion": analyze["dominant_emotion"]}
    return analyze_result


def age_gender_race_analyze(img,analyze):
    face_detection = face_recognition.face_locations(img)
    for (top, right, bottom, left) in face_detection:
        # Rectangle
        cv2.rectangle(img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)
        # Label
        cv2.rectangle(img, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        text = "Age:" + str(analyze["age"]) + "-" + str(analyze["gender"]) + "-" + str(analyze["race"])
        cv2.putText(img, text, (left - 20, bottom + 15), font, 1.0, (255, 255, 255), 2)
    return img


def emotion_analyze(img,analyze):
    face_detection = face_recognition.face_locations(img)
    for (top, right, bottom, left) in face_detection:
        # Rectangle
        cv2.rectangle(img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)
        # Label
        cv2.rectangle(img, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        text = "Emotion:" + str(analyze["emotion"])
        cv2.putText(img, text, (left - 20, bottom + 15), font, 1.0, (255, 255, 255), 2)
    return img

