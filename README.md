👁️‍🗨️ Face Recognition Attendance System

This is a Python-based Face Recognition Attendance System built using OpenCV and face_recognition libraries. It detects and recognizes faces from images or a webcam feed and marks attendance by logging names and timestamps to a CSV file.

📂 Project Structure

```
FaceRecognitionProject1/
│
├── ImageBasic/               # Folder with known face images for training
│   ├── cl1.jpg
│   ├── Lakshana_S.jpg
│   └── ...
│
├── ImagesAttendance/         # Folder to store images of recognized faces during attendance
│   └── img1.jpg
│
├── Attendance.csv            # Stores attendance records with name and time
├── AttendanceProject.py      # Main script for face recognition and attendance
├── basics.py                 # Additional helper code or tests
└── README.md                 # Project documentation
```

---

💡 Features

- Detects and recognizes faces using `face_recognition` library
- Records attendance with timestamp into a `.csv` file
- Supports adding new faces easily
- Lightweight and customizable

---

🛠️ Technologies Used

- Python 3
- OpenCV
- face_recognition (based on dlib)
- NumPy
- CSV module

---

🚀📝 Attendance Output

Each time a face is recognized, it is logged into `Attendance.csv` in the format:
```
Name, Time
Lakshana_S, 09:15:32
```

---

📸 Sample Output

![image](https://github.com/user-attachments/assets/f69a82b7-3c36-42df-934b-2ecc838c1b3e)

---

🙋‍♀️ Made By

Lakshana S
Aspiring Data Analyst + Product Engineer  
🔗 [LinkedIn] [https://www.linkedin.com/in/lakshana-s-213938259] | 🌐 [GitHub](https://github.com/lxks4002)

---

📜 License

This project is for educational purposes and open for customization and reuse.
