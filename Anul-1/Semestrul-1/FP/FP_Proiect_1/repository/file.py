from domain.entities import Student, Disciplina, Nota
from repository.inmemory import StudentRepository, DisciplinaRepository, NotaRepository


class StudentFileRepository(StudentRepository):
    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    sid, name = line.split(";")
                    super().store(Student(sid, name))
        except FileNotFoundError:
            pass # Fișierul va fi creat la prima salvare

    def __save_to_file(self):
        with open(self.__file_path, "w") as f:
            for st in self.get_all():
                f.write(f"{st.get_id()};{st.get_nume()}\n")

    def store(self, st):
        super().store(st)
        self.__save_to_file()

    def remove(self, sid):
        st = super().remove(sid)
        self.__save_to_file()
        return st

    def update(self, sid, st_nou):
        super().update(sid, st_nou)
        self.__save_to_file()


class DisciplinaFileRepository(DisciplinaRepository):
    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    disciplina_id, disciplina_name, prof = line.split(";")
                    super().store(Disciplina(disciplina_id, disciplina_name, prof))
        except FileNotFoundError:
            pass

    def __save_to_file(self):
        with open(self.__file_path, "w") as f:
            for d in self.get_all():
                f.write(f"{d.get_id()};{d.get_disciplina()};{d.get_nume()}\n")

    def store(self, disc):
        super().store(disc)
        self.__save_to_file()

    def remove(self, did):
        d = super().remove(did)
        self.__save_to_file()
        return d


class NoteFileRepository(NotaRepository):
    def __init__(self, file_path, student_repo, disc_repo):
        super().__init__()
        self.__file_path = file_path
        self.__st_repo = student_repo
        self.__ds_repo = disc_repo
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    sid, disc_name, val = line.split(",")
                    student = self.__st_repo.find(sid)
                    if student:
                        # Reconstruim obiectul Nota folosind entitatea Student găsită
                        super().store(Nota(student, disc_name, float(val)))
        except FileNotFoundError:
            pass

    def __save_to_file(self):
        with open(self.__file_path, "w") as f:
            for g in self._grades:
                f.write(f"{g.get_student().get_id()},{g.get_disciplina()},{g.get_nota()}\n")

    def store(self, grade):
        super().store(grade)
        self.__save_to_file()