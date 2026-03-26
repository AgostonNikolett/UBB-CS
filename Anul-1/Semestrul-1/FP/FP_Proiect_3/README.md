# Event Management System

This is a Python-based application designed to manage persons, events, and their respective registrations. The project demonstrates a solid understanding of **Layered Architecture (Separation of Concerns)** and **Object-Oriented Programming (OOP)** principles.

## 🚀 Tech Stack
* **Language:** Python 3.x
* **Persistence:** File I/O (custom `.txt` formatted storage)
* **Testing:** Unittest & Coverage.py
* **Algorithms:** Generic implementation of **Quick Sort** and **Gnome Sort**

## 🏗️ Architectural Layers
The project is structured into distinct layers to ensure maintainability and scalability:
* **Domain:** Defines the core entities (`Person`, `Event`, `Participant`) and their internal validation logic.
* **Repository:** Manages data storage, offering both **In-Memory** and **File-Based** persistence.
* **Service (Controller):** Implements business logic, coordinates data flow, and calculates statistical reports.
* **Validators:** Ensures data integrity (e.g., ISO date/time formats, unique IDs) before storage.
* **UI:** A modular command-line interface (CLI) for user interaction.

## 📊 Testing & Code Quality
A major focus of this project is reliability. The application achieves nearly total code coverage through a comprehensive suite of unit tests.

* **Code Coverage:** **99%** (verified with `coverage.py`)
* **Test Suite:** Includes tests for Domain, Repository, Service, Validators, and Utils.
* **Error Handling:** Robust exception handling for duplicated IDs, invalid formats, or non-existent entities.

### Running Tests
To verify the code coverage locally, follow these steps:
1. Install coverage: `pip install coverage`
2. Run tests: `coverage run -m unittest discover tests`
3. View report: `coverage report -m`

## ✨ Features
* **Person Management:** Full CRUD (Create, Read, Update, Delete) operations and search by ID.
* **Event Management:** Strict validation for ISO formats: Date (YYYY-MM-DD) and Time (HH:MM).
* **Registration System:** Register persons to events with automatic participant count updates.
* **Advanced Reports:** * List events for a specific person (sorted by description and date).
    * Identify **Most Active Persons** (those with the highest number of registrations).
    * **Top 20% Events** report based on participant attendance.
* **Random Generators:** Tools to quickly populate the database with random person and event data.
* **Generic Sorting:** Custom sorting utility capable of sorting any entity by any key.

## 💡 What I Learned
Through this project, I practiced:
* **Separation of Concerns:** Decoupling business logic from the user interface.
* **Dependency Injection:** Passing validators and repositories to services as parameters.
* **Algorithm Implementation:** Writing and testing generic sorting algorithms (Quick Sort & Gnome Sort).
* **Robustness:** Using `try...except` blocks and custom validation to ensure application stability against invalid input.

## 🏃 How to Run Locally
1. Clone the repository.
2. Ensure the `data/` directory exists with the required `.txt` files.
3. Run the application:
   `python main.py`

---
*Developed as part of the Fundamentals of Programming (FP) curriculum at UBB (Cluj-Napoca).*