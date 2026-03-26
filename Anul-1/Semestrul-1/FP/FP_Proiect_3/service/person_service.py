import random
from domain.person import Person


class PersonService:
    def __init__(self, person_repo, validator):
        """
        Initializes the PersonService.
        :param person_repo: Repository for person data.
        :param validator: Validator for person entities.
        """
        self._repo = person_repo
        self._validator = validator

    def add_person(self, person_id: str, name: str, address: str):
        """Validates and adds a new person to the repository."""
        self._validator.validate(person_id, name, address)
        person = Person(person_id, name, address)
        self._repo.store(person_id, person)

    def update_person(self, person_id: str, name: str, address: str):
        """Updates an existing person's details."""
        self._validator.validate(person_id, name, address)
        person = self._repo.find_by_id(person_id)
        person.set_name(name)
        person.set_address(address)

    def remove_person(self, person_id: str):
        """Removes a person by their ID."""
        self._repo.remove(person_id)

    def find_by_id(self, person_id: str):
        """Retrieves a person by ID."""
        return self._repo.find_by_id(person_id)

    def generate_random_persons(self, count: int):
        """Generates a specified number of random persons."""
        first_names = ["Ana", "Andrei", "Ion", "Maria", "Tudor", "Elena", "Victor"]
        last_names = ["Popescu", "Georgescu", "Ionescu", "Dumitrescu", "Lupu"]
        cities = ["Cluj-Napoca", "Bucuresti", "Timisoara", "Iasi", "Sibiu"]

        while count > 0:
            p_id = str(random.randint(1, 10000))
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            address = f"Str. {random.randint(1, 100)}, {random.choice(cities)}"
            try:
                self.add_person(p_id, name, address)
                count -= 1
            except ValueError:
                continue

    def get_all_sorted_by_id(self):
        """Returns all persons sorted by their ID."""
        return sorted(self._repo.get_all(), key=lambda p: p.get_id())