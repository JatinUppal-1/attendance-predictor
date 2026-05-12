# 🎓 Attendance Predictor
A Python-based utility for students to track attendance and predict future status based on planned absences.

## 🚀 Features
* **Future-Proofing:** Predicts your attendance percentage after missing $n$ upcoming classes.
* **Detention Alerts:** Automatically checks against the **75% threshold**.
* **Modular Design:** Uses a clean project structure with separate logic for inputs and calculations.

---

## 🛠️ Project Structure
```text
attendance-predictor/
├── utils/
│   ├── attendance.py   # Math logic for percentages
│   └── input.py        # Input handling with integer casting
├── main.py             # Main entry point and status flags
└── .github/workflows/  # CI/CD automation blueprint
└──gui.py #GUI interface