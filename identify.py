import face_recognition
from PIL import Image, ImageDraw, ImageFont

image_of_bill = face_recognition.load_image_file('path to file ...')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

image_of_steve = face_recognition.load_image_file('path to file ....')
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]


#  Create arrays of encodings and names
known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding,

]

known_face_names = [
    "put name here.....",
    "put name here...",

]

# Load test image to find faces in
test_image = face_recognition.load_image_file('D:\\MyProject\\data_image\\f.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0),width=5)

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 20), (right, bottom)), fill=(255, 255, 0), outline=(255, 255, 0))
    fnt = ImageFont.truetype("arial.ttf", 30);
    draw.text((left + 6, bottom - text_height -20 ), name,font= fnt ,fill=(0, 0, 0))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save('identify.jpg')