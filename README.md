# FSD Assignment - University Student Management App
## Project Overview
This project is an interactive university student/admin system developed for the Fundamentals of Software Development (FSD) group assignment. It provides both a command-line interface (CLI) and a graphical user interface (GUI) for managing student data.

## Features
Student Functions: Register, login, enrol/drop subjects, change passwords, and view enrolments.

Admin Functions: Manage student data, group students by grade, partition Pass/Fail, and clear all data.

Data Persistence: All student and admin data is stored in students.data using CRUD operations.

## Project Structure
```
FSD_UniversityApp/
├── cli/ # CLI-related code
│ └── main.py # CLI entry point
├── gui/ # GUI-related code
│ └── gui_main.py # GUI entry point
├── models/ # Student, Subject, Admin classes
│ ├── student.py
│ ├── subject.py
│ └── admin.py
├── controllers/ # Subsystem logic
│ ├── student_subsystem.py
│ └── admin_subsystem.py
├── utils/ # Utilities like Validator
│ └── validator.py
├── tests/ # Test scripts
│ ├── test_admin.py
│ ├── test_student.py
│ └── test_data_manager.py
├── data/ # students.data storage
│ └── students.data
├── requirements.txt # Python dependencies
└── README.md # Project description
```

## Getting Started
Follow these steps to set up and run the project.

**1. Prerequisites**
Python 3.8+ is required to run this application. You can download it from the official Python website.

**2. Clone the Repository**

```
git clone git@github.com:yunas-son-devs/FSD_code_ninjas.git
cd FSD_UniversityApp
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
python cli/main.py
```
**Graphical User Interface (GUI)**
```
python gui/gui_main.py
```

### Testing
To run the automated tests, ensure you have pytest installed (pip install pytest) and then execute the following command:
```
pytest tests/
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