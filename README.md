# 🎓 AttendFusion AI

<div align="center">

# AI-Powered Smart Attendance System Using Face & Voice Recognition

A modern attendance management system that leverages **Artificial Intelligence**, **Face Recognition**, and **Voice Recognition** to automate attendance, eliminate proxy attendance, and simplify classroom management.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Supabase](https://img.shields.io/badge/Database-Supabase-green?logo=supabase)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

# 📖 Overview

AttendFusion AI is an intelligent attendance management system that replaces manual attendance with AI-powered face and voice authentication.

Students can securely log in using facial recognition, optionally enroll their voice for voice-based attendance, enroll in subjects, and monitor their attendance statistics. Teachers can efficiently manage students, subjects, and attendance records through an intuitive dashboard.

The project is designed to make attendance **faster, more secure, and more reliable** while minimizing proxy attendance.

---

# ✨ Features

## 👨‍🎓 Student Module

- Face Recognition Login
- AI-based Student Registration
- Optional Voice Enrollment
- Subject Enrollment
- Subject Unenrollment
- Attendance Statistics
- Secure Student Dashboard
- Real-time Attendance Updates

---

## 👨‍🏫 Teacher Module

- Teacher Dashboard
- Subject Management
- Student Management
- Attendance Monitoring
- Attendance Analytics

---

## 🤖 AI Features

- Face Recognition Authentication
- Face Embedding Generation
- Voice Embedding Generation
- AI-powered Student Identification
- Automatic Attendance Prediction
- Real-time Attendance Processing

---

# 🛠 Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## Artificial Intelligence

- face_recognition
- dlib
- scikit-learn
- Resemblyzer
- Librosa

## Data Processing

- NumPy
- Pandas
- Pillow

## Database

- Supabase

## Authentication

- bcrypt

## QR Code

- Segno

## Development Tools

- Git
- GitHub

---

# 📂 Project Structure

```text
AttendFusion-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│
├── models/
│
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   ├── ui/
│   └── utils/
│
└── venv/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/1Maazansari/attendfusion-ai.git
```

```bash
cd attendfusion-ai
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Supabase

Create a `.streamlit/secrets.toml` file and add your Supabase credentials.

```toml
SUPABASE_URL="your_supabase_url"
SUPABASE_KEY="your_supabase_key"
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

# 📸 Screenshots

> Add screenshots of your application here.

## Home Page

```
screenshots/home.png
```

---

## Student Dashboard

```
screenshots/student_dashboard.png
```

---

## Teacher Dashboard

```
screenshots/teacher_dashboard.png
```

---

## Attendance System

```
screenshots/attendance.png
```

---

# 🧠 How It Works

### Student Registration

1. Student opens the application.
2. Face is captured using the camera.
3. Facial embeddings are generated.
4. Student profile is created.
5. Voice enrollment is optional.
6. Student account is stored in the database.

---

### Student Login

1. Student opens Face Login.
2. AI detects the face.
3. Face embeddings are compared.
4. Matching profile is identified.
5. Student dashboard opens automatically.

---

### Attendance Workflow

1. Student logs in.
2. AI verifies identity.
3. Attendance is recorded.
4. Dashboard updates attendance statistics.

---

# 🚀 Future Enhancements

- Face Anti-Spoofing
- Voice Verification During Attendance
- Mobile Application
- Email Notifications
- SMS Alerts
- Attendance Reports (PDF & Excel)
- Admin Dashboard
- Analytics Dashboard
- Multi-Camera Support
- Cloud Deployment
- Attendance Insights using AI

---

# 🤝 Contributing

Contributions are welcome.

## Fork the repository

```bash
git fork
```

## Create a feature branch

```bash
git checkout -b feature-name
```

## Commit changes

```bash
git commit -m "Add new feature"
```

## Push changes

```bash
git push origin feature-name
```

Finally, open a Pull Request.

---

# 📋 Requirements

Main dependencies include:

- Streamlit
- NumPy
- Pandas
- scikit-learn
- dlib-bin
- face_recognition_models
- Supabase
- bcrypt
- Segno
- Pillow
- Librosa
- Resemblyzer

Install them using:

```bash
pip install -r requirements.txt
```

---

# 👨‍💻 Author

## Maaz Ansari

**Final Year B.Tech Student (Artificial Intelligence & Machine Learning)**

📧 Email

```
maazansari260@gmail.com
```

🔗 GitHub

https://github.com/1Maazansari

🔗 LinkedIn

https://linkedin.com/in/maazansari-ml

🌐 Portfolio

https://maazspace.vercel.app

---

# 📄 License

This project is licensed under the **MIT License**.

See the LICENSE file for more information.

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

Your support helps improve the project and encourages future development.

---

<div align="center">

### Built with ❤️ by Maaz Ansari

**AttendFusion AI — Smarter Attendance Through Artificial Intelligence**

</div>