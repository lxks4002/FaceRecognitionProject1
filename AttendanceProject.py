import cv2
import numpy as np
import face_recognition
import os
import csv
from datetime import datetime

# Define paths
image_basic_path = "ImageBasic"
attendance_file = "Attendance.csv"

# Load known images and encode them
known_face_encodings = []
known_face_names = []

print("Encoding faces...")

for filename in os.listdir(image_basic_path):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(image_basic_path, filename)
        image = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(image)

        if encoding:  # Check if encoding is successful
            known_face_encodings.append(encoding[0])
            known_face_names.append(os.path.splitext(filename)[0])  # Store name without extension

print(f"Encoded {len(known_face_encodings)} faces.")

# Function to mark attendance
def mark_attendance(name):
    try:
        with open(attendance_file, 'r+', newline='') as f:
            reader = csv.reader(f)
            existing_names = [row[0] for row in reader if row]  # Fix: Skip empty rows

            if name not in existing_names:
                now = datetime.now()
                dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
                f.write(f'{name},{dt_string}\n')
                print(f"Marked attendance for {name}")
    except FileNotFoundError:
        print("Attendance file not found, creating a new one.")
        with open(attendance_file, 'w', newline='') as f:
            f.write("Name,Time\n")
            mark_attendance(name)  # Retry marking attendance

# Open camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # Resize for faster processing
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances) if len(face_distances) > 0 else -1

        if best_match_index != -1 and matches[best_match_index]:
            name = known_face_names[best_match_index]

        top, right, bottom, left = [v * 4 for v in face_location]  # Scale back up
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        mark_attendance(name)

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
