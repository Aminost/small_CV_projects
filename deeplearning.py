import face_recognition

image = face_recognition.load_image_file("D:\\MyProject\\data_image\\will.jpg")
face_encodeing = face_recognition.face_encodings(image)[0]

image2 = face_recognition.load_image_file("D:\\MyProject\\data_image\\notwill.jpg")
face_encodeing2 = face_recognition.face_encodings(image2)[0]

unknown_image = face_recognition.load_image_file("D:\MyProject\\face_macth\\will3.jpg")
unknown_encodeing = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([face_encodeing], unknown_encodeing)

if results[0]:
    print('this is will')
else:
    print("this is not will ")
