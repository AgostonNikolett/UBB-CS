# Student & Discipline Management System

This is a Python-based application designed to manage students, disciplines, and their respective grades. The project demonstrates a solid understanding of **Layered Architecture (Separation of Concerns)** and **Object-Oriented Programming (OOP)** principles.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Persistence:** File I/O (custom `.txt` formatted storage)
* **Testing:** Unittest & Coverage.py
* **Version Control:** Git/GitHub

## 🏗 Architectural Layers
The project is structured into distinct layers to ensure maintainability and scalability:
* **Domain:** Defines the core entities (`Student`, `Disciplina`, `Nota`) and their validation logic. 
* **Repository:** Manages data storage, offering both **In-Memory** and **File-Based** persistence. 
* **Service (Controller):** Implements the business logic and coordinates data flow between the UI and Repositories.
* **UI:** A command-line interface (CLI) for user interaction. 

## 📈 Testing & Code Quality
A major focus of this project is reliability. The application achieves high code coverage through a comprehensive suite of unit tests.

* **Code Coverage:** **97%** (verified with `coverage.py`)
* **Test Suite:** Includes tests for Domain, Repository, and Service layers.
* **Error Handling:** Custom exceptions (e.g., `ValidationException`, `DuplicatedIDException`) handle edge cases gracefully.

### Running Tests
To verify the code coverage locally, follow these steps:
1. Install coverage: `pip install coverage`
2. Run tests: `coverage run -m unittest discover tests`
3. View report: `coverage report -m`

## 📖 Features
* **Student Management:** Create, update, remove, and search for students. 
* **Discipline Management:** Full CRUD (Create, Read, Update, Delete) operations for academic subjects. 
* **Grading System:** Assign grades to students for specific disciplines with built-in validation. 
* **Random Generators:** Tools to quickly populate the database with random student and discipline data. 
* **Data Persistence:** All information is saved in and loaded from text files (`.txt`). 

## 🧠 What I Learned
Through this project, I practiced:
* Implementing **Layered Architecture** to decouple business logic from the user interface. 
* Writing **Custom Exceptions** for robust error handling (e.g., `ValidationException`, `DuplicatedIDException`). 
* Utilizing **Dependency Injection** by passing validators and repositories to services. 
* Ensuring code reliability through **Unit Testing** (embedded in the modules). 

## 📊 Sample Data
The repository includes a `data/` directory with pre-populated text files to demonstrate the application's functionality immediately:
* **students.txt**: A list of 15 sample students with unique IDs.
* **disciplines.txt**: Real-world academic subjects from the UBB Computer Science curriculum.
* **grades.txt**: A diverse set of grades used to showcase the **Top 20%** statistics and average calculations.

You can start the app and immediately run option `12` (Top 20% Students) or `10` (List Student Grades) to see the system in action.

## 🏁 How to Run Locally
1. Clone the repository: 
   `git clone https://github.com/username/UBB-Student-Manager.git`
2. Ensure you have the data directory and `.txt` files in place. 
3. Run the application:
   `python msin.py`


---
*Developed as part of the Fundamentals of Programming curriculum at UBB (Cluj-Napoca).*
