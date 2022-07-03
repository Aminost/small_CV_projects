import cv2
import face_recognition

# Get a reference to webcam
first_frame = None
status_list = [None, None]

video = cv2.VideoCapture(0)

# Initialize variables
face_locations = []
image_of_amin = face_recognition.load_image_file('path to the file .....')
amin_face_encoding = face_recognition.face_encodings(image_of_amin)[0]

known_face_encodings = [
    amin_face_encoding,

]

known_face_names = [
    " put here the name ",

]

while True:
    # Grab a single frame of video
    ret, frame = video.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Display the results
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Draw a box around the face

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If matchq
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]


        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,255), 2)
        cv2.rectangle(frame, (left,bottom + 25), (right, bottom),(0,255,255), cv2.FILLED)
        cv2.putText(frame, name, (left + 3, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),
                    lineType=cv2.LINE_AA)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video.release()
cv2.destroyAllWindows()
