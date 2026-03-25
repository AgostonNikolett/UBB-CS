import random
from domain.validators import ValidationException
from repository.inmemory import RepositoryException


def print_menu():
    print("\n" + "="*45)
    print("     STUDENT & GRADE MANAGEMENT SYSTEM")
    print("="*45)
    print("  1. Add Student          5. Add Discipline")
    print("  2. Remove Student       6. Remove Discipline")
    print("  3. Search Student       7. Search Discipline")
    print("  4. Update Student       8. Update Discipline")
    print("-" * 45)
    print("  9. Assign Grade        10. List Student Grades")
    print(" 11. List Disc. Grades   12. Top 20% Students")
    print("-" * 45)
    print(" 13. Generate Students   14. Generate Disciplines")
    print("  0. Exit")
    print("="*45)


class ConsoleUI:
    def __init__(self, st_service, disc_service, nota_service):
        """
        Initialize the User Interface.
        :param st_service: StudentService
        :param disc_service: DisciplinaService
        :param nota_service: NotaService
        """
        self.__st_service = st_service
        self.__disc_service = disc_service
        self.__nota_service = nota_service

    # --- Student Operations ---
    def __ui_add_student(self):
        sid = input("Student ID: ").strip()
        name = input("Student Name: ").strip()
        self.__st_service.create(sid, name)
        print(">>> Student added successfully.")

    def __ui_remove_student(self):
        sid = input("Student ID to remove: ").strip()
        st = self.__st_service.remove(sid)
        print(f">>> Student {st.get_nume()} was removed.")

    def __ui_search_student(self):
        criterion = input("Name contains: ").strip()
        results = self.__st_service.search(criterion)
        if not results:
            print(">>> No students found.")
            return
        print(f"\n{'ID':<10} | {'Name':<20}")
        print("-" * 33)
        for st in results:
            print(f"{st.get_id():<10} | {st.get_nume():<20}")

    def __ui_update_student(self):
        sid = input("Existing Student ID: ").strip()
        new_name = input("New Name: ").strip()
        self.__st_service.update(sid, new_name)
        print(">>> Data updated successfully.")

    # --- Discipline Operations ---
    def __ui_add_discipline(self):
        did = input("Discipline ID: ").strip()
        name = input("Discipline Name: ").strip()
        professor = input("Professor Name: ").strip()
        self.__disc_service.create(did, name, professor)
        print(">>> Discipline added successfully.")

    def __ui_remove_discipline(self):
        did = input("Discipline ID to remove: ").strip()
        disc = self.__disc_service.remove(did)
        print(f">>> Discipline {disc.get_disciplina()} was removed.")

    def __ui_search_discipline(self):
        criterion = input("Discipline name contains: ").strip()
        results = self.__disc_service.search(criterion)
        if not results:
            print(">>> No disciplines found.")
            return
        print(f"\n{'ID':<10} | {'Subject':<20} | {'Professor':<15}")
        print("-" * 50)
        for d in results:
            print(f"{d.get_id():<10} | {d.get_disciplina():<20} | {d.get_nume():<15}")

    # --- Grade Operations ---
    def __ui_assign_grade(self):
        sid = input("Student ID: ").strip()
        did = input("Discipline ID: ").strip()
        try:
            value = float(input("Grade (1-10): "))
            self.__nota_service.assign_grade(sid, did, value)
            print(">>> Grade assigned successfully.")
        except ValueError:
            print("[ERROR] Grade must be a numerical value.")

    def __ui_list_student_grades(self):
        sid = input("Student ID: ").strip()
        grades = self.__nota_service.get_student_grades(sid)
        if not grades:
            print(">>> No grades found for this student.")
            return
        print(f"\nGrades for student: {grades[0].get_student().get_nume()}")
        print(f"{'Discipline':<20} | {'Grade':<5}")
        print("-" * 28)
        for g in grades:
            print(f"{g.get_disciplina():<20} | {g.get_nota():<5}")

    def __ui_top_students(self):
        top = self.__nota_service.get_top_students()
        if not top:
            print(">>> Not enough data for statistics.")
            return
        print(f"\n{'Student':<20} | {'Average':<10}")
        print("-" * 33)
        for st, average in top:
            print(f"{st.get_nume():<20} | {average:<10.2f}")

    # --- Data Generation ---
    def __ui_generate_students(self):
        names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George"]
        for _ in range(5):
            sid = str(random.randint(100, 999))
            name = random.choice(names)
            try:
                self.__st_service.create(sid, name)
            except (ValidationException, RepositoryException):
                continue
        print(">>> 5 random students generated.")

    def start(self):
        """Entry point for the console UI loop."""
        commands = {
            "1": self.__ui_add_student,
            "2": self.__ui_remove_student,
            "3": self.__ui_search_student,
            "4": self.__ui_update_student,
            "5": self.__ui_add_discipline,
            "6": self.__ui_remove_discipline,
            "7": self.__ui_search_discipline,
            "9": self.__ui_assign_grade,
            "10": self.__ui_list_student_grades,
            "12": self.__ui_top_students,
            "13": self.__ui_generate_students
        }

        while True:
            print_menu()
            option = input("Select option: ").strip()

            if option == "0":
                print("Exiting application. Goodbye!")
                break

            if option in commands:
                try:
                    commands[option]()
                except (ValidationException, RepositoryException, ValueError) as e:
                    print(f"\n[ERROR] {e}")
            else:
                print("\n[!] Invalid option. Please try again.")