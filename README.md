# 🎓 Student Success Prediction in Internship Programs for Micro IT

This project helps predict whether a student is likely to succeed in an internship program based on their academic and skill profile.

## 📁 Project Structure

```
student_success_prediction/
├── student_internship_data.csv      # Sample dataset
├── student_success_model.py         # Script to train and save the model
├── success_model.pkl                # Trained Random Forest model (generated after training)
├── scaler.pkl                       # Scaler object (generated after training)
└── app.py                           # Streamlit app for interactive prediction
```

---

## 🚀 How to Use

### 1. Clone or Download the Project

Download the ZIP and extract it or clone from GitHub.

### 2. Install Requirements

Make sure you have Python installed. Then install the required libraries:

```bash
pip install streamlit scikit-learn pandas numpy
```

### 3. Train the Model

Run the training script to generate the model and scaler:

```bash
python student_success_model.py
```

This will create:
- `success_model.pkl`
- `scaler.pkl`

### 4. Run the Web App

Use Streamlit to run the app:

```bash
streamlit run app.py
```

### 5. Use the App

Fill in the student's:
- CGPA
- Attendance
- Projects done
- Skill count
- Certifications

Click **Predict** to see whether the student is likely to succeed in their internship.

---

## 🧠 Model Used

- **Algorithm**: Random Forest Classifier
- **Features Used**: CGPA, Attendance, Projects Done, Skills Count, Certifications
- **Target**: Internship Success (0 = No, 1 = Yes)

---

## 📊 Example Dataset

```csv
Student_ID,CGPA,Attendance,Projects_Done,Skills_Count,Certifications,Internship_Success
S001,8.4,90,3,5,2,1
S002,7.2,75,1,3,1,0
```

---

## 🏢 Ideal for

- Micro IT Company
- Internship Program Managers
- Academic Institutions

---

## 📬 Contact

KANDUKURI OMKAR - omkark5125@gmail.com
