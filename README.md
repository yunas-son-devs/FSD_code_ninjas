# FSD Assignment - University Student Management App
## Project Overview
This project is an interactive university student/admin system developed for the Fundamentals of Software Development (FSD) group assignment. It provides both a command-line interface (CLI) and a graphical user interface (GUI) for students and admins.

## Features
Student Functions: Register, login, enrol/drop subjects, change passwords, and view enrolments.

Admin Functions: View and manage all student records, remove students, group students by grade, categorise them by pass or fail status, summarise academic results, and clear student data.

Data Persistence: All student and admin data is stored in students.data using CRUD operations.

## Project Structure
```
FSD_code_ninjas/
├── cli/ # Code for the Command-Line Interface (CLI)
│   ├── __init__.py
│   ├── admin_cli.py
│   ├── enrol_cli.py
│   ├── login_cli.py
│   └── main.py # CLI entry point
├── controllers/ # Application logic and system management
│   ├── admin_subsystem.py
│   ├── data_manager.py # Handles file I/O for students.data
│   └── student_subsystem.py
├── data/
│   └── students.data # The main data file for persistence
├── document/ # Project documentation files
│   └── groupCoding Ninjas-Cmp1.pdf
├── gui/ # Code for the Graphical User Interface (GUI)
│   ├── __init__.py
│   ├── admin_frame.py
│   ├── enrol_frame.py
│   ├── exception_frame.py
│   ├── gui_main.py # GUI entry point
│   ├── login_frame.py
│   └── subject_frame.py
├── models/ # Data structure classes for the application
│   ├── admin.py
│   ├── student.py
│   └── subject.py
├── utils/ # Common utility functions (validation, services, patterns)
│   ├── academic_service.py
│   ├── patterns.py
│   └── validator.py
├── .gitignore # Specifies files to be ignored by Git
├── LICENSE
├── README.md # This file
└── requirements.txt # Python dependencies
```

## Getting Started

### 1. Prerequisites
- Python 3.8 or higher must be installed.

### 2. Download the Project
1. Download the `FSD_code_ninjas.zip` file.
2. Unzip it to your preferred folder on your computer.

### 3. Install Required Packages
1. Open **Terminal** (Mac/Linux) or **Command Prompt** (Windows).
2. Navigate to the unzipped project folder:
   ```
   cd FSD_code_ninjas
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### 4. Run the Application
You can choose between two modes:

#### Command-Line Interface (CLI)
```
python -m cli.main
```

#### Graphical User Interface (GUI)
```
python -m gui.gui_main
```

### 5. How to Use

## CLI Demo
![CLI Demo](https://github.com/user-attachments/assets/49ca16c2-f2be-4dc7-b12e-022f7f2ac01b)

## GUI Demo
![GUI Demo](https://github.com/user-attachments/assets/49ca16c2-f2be-4dc7-b12e-022f7f2ac01b)

#### Student Functions
- Register and log in
- Enrol or remove subjects (up to 4)
- View grades, average mark, and pass/fail status
- Change password securely

#### Admin Functions
- View all registered students
- Group students by grade (HD/D/C/P/F)
- Categorise by Pass/Fail
- Remove a student or clear all data

### 6. Data Storage
All information is automatically stored in:
```
data/students.data
```
This ensures your student and admin data are saved persistently between sessions.
