import cv2
import face_recognition
import pickle
import numpy as np


def face_recognition_func(img):
    known_faces = {}
    with open("known_faces.dat","rb") as f:
        known_faces = pickle.load(f)

    known_encoded_face = list(known_faces["encodings"])
    known_face_names = list(known_faces["labels"])

    #img = cv2.imread(test_image, 1)

    face_detections = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_detections)

    face_names = []
    for face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(known_encoded_face, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_encoded_face, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)

        for (top, right, bottom, left), name in zip(face_detections, face_names):
            # Rectangle
            cv2.rectangle(img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)
            # Label
            cv2.rectangle(img, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left - 20, bottom + 15), font, 1.0, (255, 255, 255), 2)

    return img
    #while True:
        #cv2.imshow('Video', img)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    return face_names

#print(face_recognition_func("test_data/test1.jpeg"))