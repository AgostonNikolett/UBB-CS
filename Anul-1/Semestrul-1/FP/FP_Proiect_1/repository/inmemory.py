from domain.validators import CRUDException

class RepositoryException(CRUDException):
    """Excepție de bază pentru erorile de stocare."""
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg

class DuplicatedIDException(RepositoryException):
    """Se aruncă atunci când un ID există deja în sistem."""
    def __init__(self):
        super().__init__("ID duplicat: O entitate cu acest ID există deja.")

class InMemoryRepository:
    """Clasă de bază pentru stocarea în memorie folosind un dicționar."""
    def __init__(self):
        self._items = {}

    def store(self, entity):
        if entity.get_id() in self._items:
            raise DuplicatedIDException()
        self._items[entity.get_id()] = entity

    def find(self, entity_id):
        return self._items.get(entity_id, None)

    def remove(self, entity_id):
        if entity_id not in self._items:
            raise RepositoryException(f"Entitatea cu ID {entity_id} nu a fost găsită.")
        return self._items.pop(entity_id)

    def update(self, entity_id, new_entity):
        if entity_id not in self._items:
            raise RepositoryException(f"Entitatea cu ID {entity_id} nu a fost găsită.")
        self._items[entity_id] = new_entity

    def get_all(self):
        return list(self._items.values())

    def size(self):
        return len(self._items)

class StudentRepository(InMemoryRepository):
    pass

class DisciplinaRepository(InMemoryRepository):
    pass

class NotaRepository:
    """Notele au o logică de stocare ușor diferită (listă, nu dicționar după ID)."""
    def __init__(self):
        self._grades = []

    def store(self, grade):
        # Verificăm dacă studentul are deja notă la acea disciplină
        for g in self._grades:
            if g.get_student() == grade.get_student() and g.get_disciplina() == grade.get_disciplina():
                raise RepositoryException("Nota a fost deja alocată pentru acest student la această materie.")
        self._grades.append(grade)

    def get_all(self, student):
        """Returnează toate notele unui student specific."""
        return [g for g in self._grades if g.get_student() == student]

    def get_all_for_dis(self, disc_name):
        """Returnează toate notele pentru o disciplină specifică."""
        return [g for g in self._grades if g.get_disciplina() == disc_name]

    def size(self):
        return len(self._grades)