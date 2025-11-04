# FSD Assignment - University Student Management App
## Project Overview
This project is an interactive university student/admin system developed for the Fundamentals of Software Development (FSD) group assignment. It provides both a command-line interface (CLI) and a graphical user interface (GUI) for managing student data.

## Features
Student Functions: Register, login, enrol/drop subjects, change passwords, and view enrolments.

Admin Functions: Manage student data, group students by grade, partition Pass/Fail, and clear all data.

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
Follow these steps to set up and run the project.

**1. Prerequisites**
Python 3.8+ is required to run this application. You can download it from the official Python website.

**2. Clone the Repository**

```
git clone git@github.com:yunas-son-devs/FSD_code_ninjas.git
cd FSD_code_ninjas/
```

**3. Set up the Environment**
It's highly recommended to use a virtual environment to manage dependencies.

### Create a virtual environment
python -m venv venv

### Activate the virtual environment
**On Windows:**
```
venv\Scripts\activate
```

**On Mac/Linux:**
```
source venv/bin/activate
```

**4. Install Dependencies**
This command installs all necessary libraries listed in requirements.txt.
```
pip install -r requirements.txt
```

### How to Run the App
Choose between the CLI and GUI version.

**Command-Line Interface (CLI)**
```
python -m cli.main
```
**Graphical User Interface (GUI)**
```
python -m gui.gui_main
```

## Git Workflow
Use a dedicated branch for each new feature or task.
The main branch should always be stable and ready for deployment.

### Create and switch to a new feature branch
```
git checkout -b feature/<your-feature-name>
```

### Initial setup & commit
```
git init
git add .
git commit -m "feat: [Feature] Description of feature"
```

### Push your branch and create a Pull Request (PR)
```
git push origin feature/<your-feature-name>
```