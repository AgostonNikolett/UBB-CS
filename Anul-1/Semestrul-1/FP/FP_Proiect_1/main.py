import os
from domain.validators import StudentValidator, DisciplinaValidator, NotaValidator
from repository.file import StudentFileRepository, DisciplinaFileRepository, NoteFileRepository
from service.services import StudentService, DisciplinaService, NotaService
from ui.console import ConsoleUI

def ensure_data_dir():
    """
    Creates the 'data' directory if it doesn't exist to prevent FileNotFoundError.
    """
    if not os.path.exists('data'):
        os.makedirs('data')

def run_app():
    """
        Initializes the layers of the application and starts the UI.
        Uses Dependency Injection to connect Validators -> Repositories -> Services -> UI.
        """
    ensure_data_dir()

    # 1. Initialize Validators
    student_validator = StudentValidator()
    discipline_validator = DisciplinaValidator()
    grade_validator = NotaValidator()

    # 2. Initialize Repositories
    student_repo = StudentFileRepository("data/students.txt")
    discipline_repo = DisciplinaFileRepository("data/disciplines.txt")
    grade_repo = NoteFileRepository("data/grades.txt", student_repo, discipline_repo)

    # 3. Initialize Services
    student_service = StudentService(student_validator, student_repo)
    discipline_service = DisciplinaService(discipline_validator, discipline_repo)
    grade_service = NotaService(grade_validator, grade_repo, student_repo, discipline_repo)

    # 4. Initialize and Start UI
    ui = ConsoleUI(student_service, discipline_service, grade_service)
    ui.start()

if __name__ == "__main__":
    try:
        run_app()
    except Exception as e:
        print(f"CRITICAL ERROR: The application failed to start. {e}")