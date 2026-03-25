# Travel Agency Management System

This is a Python-based application designed to manage travel packages for a tourism agency. The project demonstrates a strong command of **Procedural Programming**, **Modular Design**, and **Advanced Sorting Algorithms**.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Data Structures:** Lists and Dictionaries (Procedural approach)
* **Algorithms:** QuickSort (In-place partitioning)
* **Testing:** Unittest & Coverage.py
* **Version Control:** Git/GitHub

## 🏗 Architectural Layers
The project is organized into clear modules to ensure separation of concerns:
* **Domain:** Defines the travel package entity and its basic getters/setters.
* **Repository:** Handles data collection management (Create, Read, Update, Delete).
* **Service:** Implements complex business logic (Averages, Intervals, Filtering).
* **UI:** Dual-mode interface supporting both a **Standard Menu** and a **Batch Command Shell**.
* **Utils:** Helper modules for I/O validation, sorting, and undo state management.

## 📈 Testing & Code Quality
Reliability is ensured through rigorous unit testing, covering all logical edge cases.

* **Code Coverage:** **100%** (verified with `coverage.py`)
* **Test Suite:** Comprehensive tests for Domain, Repository, Service, and Utility modules.
* **Robustness:** Input validation for dates (datetime objects) and numeric values.

### Running Tests
To verify the 100% code coverage locally:
1. Install dependencies: `pip install coverage`
2. Run tests: `coverage run -m unittest discover tests`
3. View report: `coverage report -m`

## 🚀 Features
* **Package Management:** Full CRUD operations with auto-generated IDs.
* **Advanced Search:** Find packages within specific date intervals or price ranges.
* **Statistical Reports:** Calculate average prices per destination and generate sorted offers.
* **Smart Filtering:** Bulk remove packages based on destination, price, or specific months.
* **Undo System:** Revert any destructive operation (Delete/Filter) to the previous state.
* **Batch Mode:** Execute multiple commands in a single line (e.g., `add ...; show; undo`).

## 🧠 What I Learned
Through this project, I practiced:
* **In-place List Manipulation:** Using slice assignment (`packages[:]`) for efficient filtering.
* **Algorithm Implementation:** Writing a custom **QuickSort** to handle entity sorting by price.
* **State Preservation:** Implementing an **Undo** mechanism using a stack-based approach.
* **Shell-like Parsing:** Developing a command parser for the **Batch Mode** interface.

## 💻 How to Run Locally
1. Clone the repository: 
   `git clone https://github.com/username/Travel-Agency-Manager.git`
2. Run the application:
   `python main.py`

---
*Developed as part of the Fundamentals of Programming curriculum at UBB (Cluj-Napoca).*