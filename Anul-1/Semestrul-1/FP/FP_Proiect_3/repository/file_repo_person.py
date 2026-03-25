import os 
from repository.repo_person import PersonRepository
from domain.person import Person

class PersonFileRepository(PersonRepository):
    def __init__(self, filename):
        PersonRepository.__init__(self)
        self._filename = filename
        self._load_from_file()

    def _save_to_file(self):
        """Saves all persons to the file."""
        with open(self._filename, 'w') as file:
            for person in self._persons.values():
                file.write(person.to_string() + '\n')

    def _load_from_file(self):
        """Loads all persons from the file."""
        if not os.path.exists(self._filename):
            return
        with open(self._filename, 'r') as file:
            for line in file:
                if line.strip():
                    person = Person.from_string(line)
                    self._persons[person.get_person_id()] = person
    
    # Adds a new Person to the repository
    def add_person(self, person):
        PersonRepository.add_person(self, person)
        self._save_to_file()

    # Removes a Person from the repository by its person_id
    def remove_person(self, person_id):
        PersonRepository.remove_person(self, person_id)
        self._save_to_file()

    # Updates an existing Person in the repository
    def update_person(self, person_id, name, address):
        PersonRepository.update_person(self, person_id, name, address)
        self._save_to_file()

    # Finds and retrieves a Person by its perosn_id
    def find_person_by_id(self, person_id):
        return PersonRepository.find_person_by_id(self, person_id)

    # Returns a list of all Persons objects in the repository
    def get_all_persons(self):
        return PersonRepository.get_all_persons(self)