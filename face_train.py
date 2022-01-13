import pickle
import face_recognition
import os


def encoding_train_images():
    encoded_images = {}
    for dirpath, dnames, fnames in os.walk("train_data"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png") or f.endswith("jpeg"):
                face = face_recognition.load_image_file("train_data/" + f)
                #print(f)
                encoding = face_recognition.face_encodings(face)[0]
                encoded_images[f.split(".")[0]] = encoding
    return encoded_images


def encoding_test_images(img):
    face = face_recognition.load_image_file("train_data/" + img)
    encoding = face_recognition.face_encodings(face)[0]
    return encoding


known_faces = encoding_train_images()
known_data = {"encodings": list(known_faces.values()),"labels":list(known_faces.keys())}

with open("known_faces.dat", "wb") as f:
    f.write(pickle.dumps(known_data))

