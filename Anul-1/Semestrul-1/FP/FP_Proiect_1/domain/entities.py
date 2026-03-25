class Student:
    """Represents a student entity."""
    def __init__(self, id_student, nume):
        self.__id = id_student
        self.__nume = nume

    def get_id(self): return self.__id
    def get_nume(self): return self.__nume

    def __str__(self):
        return f"{self.__id} {self.__nume}"

    def __eq__(self, other):
        if not isinstance(other, Student): return False
        return self.__id == other.__id


class Disciplina:
    """Represents a discipline (subject) entity."""
    def __init__(self, id_disciplina, disciplina, nume_profesor):
        self.__id = id_disciplina
        self.__disciplina = disciplina
        self.__nume_profesor = nume_profesor

    def get_id(self): return self.__id
    def get_disciplina(self): return self.__disciplina
    def get_nume(self): return self.__nume_profesor

    def __str__(self):
        return f"{self.__id} {self.__disciplina} ({self.__nume_profesor})"

    def __eq__(self, other):
        if not isinstance(other, Disciplina): return False
        return self.__id == other.__id


class Nota:
    """Represents a grade assigned to a student for a discipline."""
    def __init__(self, student, disciplina, valoare_nota):
        self.__st = student
        self.__dis = disciplina
        self.__nota = valoare_nota

    def get_student(self): return self.__st
    def get_disciplina(self): return self.__dis
    def get_nota(self): return self.__nota

    def __str__(self):
        return f"Student: {self.__st.get_nume()} | Disc: {self.__dis} | Grade: {self.__nota}"

    def __eq__(self, other):
        if not isinstance(other, Nota): return False
        return self.__st == other.__st and self.__dis == other.__dis