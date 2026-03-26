import os
from repository.base_repository import InMemoryRepository
from domain.person import Person
from domain.event import Event

class PersonFileRepository(InMemoryRepository):
    def __init__(self, file_path: str):
        super().__init__()
        self._file_path = file_path
        self._load_data()

    def _load_data(self):
        if not os.path.exists(self._file_path): return
        with open(self._file_path, 'r') as f:
            for line in f:
                if line.strip():
                    person = Person.from_file_string(line)
                    super().store(person.get_id(), person)

    def _save_data(self):
        with open(self._file_path, 'w') as f:
            for person in self.get_all():
                f.write(person.to_file_string() + '\n')

    def add(self, person: Person):
        super().store(person.get_id(), person)
        self._save_data()

    def update(self, person_id: str, name: str, address: str):
        person = self.find_by_id(person_id)
        person.set_name(name)
        person.set_address(address)
        self._save_data()

    def delete(self, person_id: str):
        super().remove(person_id)
        self._save_data()