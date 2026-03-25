from domain.entities import Student, Disciplina, Nota

class StudentService:
    def __init__(self, validator, repository):
        self.__val = validator
        self.__repo = repository

    def create(self, student_id, nume):
        """Validates and stores a new student."""
        st = Student(student_id, nume)
        self.__val.validate_student(st)
        self.__repo.store(st)
        return st

    def remove(self, student_id):
        """Removes student by ID."""
        return self.__repo.remove(student_id)

    def update(self, student_id, nume_nou):
        """Updates an existing student's information."""
        st_nou = Student(student_id, nume_nou)
        self.__val.validate_student(st_nou)
        self.__repo.update(student_id, st_nou)

    def search(self, criteriu=""):
        """Returns a list of students whose names contain the criterion."""
        all_students = self.__repo.get_all()
        if not criteriu:
            return all_students
        return [st for st in all_students if criteriu.lower() in st.get_nume().lower()]

    def get_all(self):
        return self.__repo.get_all()


class DisciplinaService:
    def __init__(self, validator, repository):
        self.__val = validator
        self.__repo = repository

    def create(self, disc_id, nume_disc, nume_profesor):
        """Validates and stores a new discipline."""
        disc = Disciplina(disc_id, nume_disc, nume_profesor)
        self.__val.validate_disciplina(disc)
        self.__repo.store(disc)
        return disc

    def remove(self, disc_id):
        return self.__repo.remove(disc_id)

    def update(self, disc_id, nume_disc, nume_profesor):
        disc_nou = Disciplina(disc_id, nume_disc, nume_profesor)
        self.__val.validate_disciplina(disc_nou)
        self.__repo.update(disc_id, disc_nou)

    def search(self, criteriu=""):
        all_disc = self.__repo.get_all()
        if not criteriu:
            return all_disc
        return [d for d in all_disc if criteriu.lower() in d.get_disciplina().lower()]

    def get_all(self):
        return self.__repo.get_all()


class NotaService:
    def __init__(self, validator, nota_repo, student_repo, disc_repo):
        self.__val = validator
        self.__nota_repo = nota_repo
        self.__student_repo = student_repo
        self.__disc_repo = disc_repo

    def assign_grade(self, student_id, disc_id, valoare_nota):
        """Assigns a grade after validating student and discipline existence."""
        student = self.__student_repo.find(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")

        discipline = self.__disc_repo.find(disc_id)
        if not discipline:
            raise ValueError(f"Discipline with ID {disc_id} not found.")

        nota_obj = Nota(student, discipline.get_disciplina(), valoare_nota)
        self.__val.validate_nota(nota_obj)
        self.__nota_repo.store(nota_obj)
        return nota_obj

    def get_student_grades(self, student_id):
        student = self.__student_repo.find(student_id)
        if not student:
            raise ValueError("Student not found.")
        return self.__nota_repo.get_all(student)

    def get_discipline_grades(self, disc_name):
        return self.__nota_repo.get_all_for_dis(disc_name)

    def get_top_students(self):
        """Calculates the top 20% students by average grade."""
        all_students = self.__student_repo.get_all()
        averages = []

        for st in all_students:
            grades = self.__nota_repo.get_all(st)
            if grades:
                avg = sum([g.get_nota() for g in grades]) / len(grades)
                averages.append((st, avg))

        # Sort by average descending
        averages.sort(key=lambda x: x[1], reverse=True)

        # Take top 20%
        nr_top = max(1, len(averages) // 5)
        return averages[:nr_top]