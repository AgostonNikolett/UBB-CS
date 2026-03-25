class PersonRepository:
    def __init__(self):
        self._persons = {}

    # Adds a new Person to the repository
    def add_person(self, person):
        if person.get_person_id() in self._persons:
            raise ValueError(f"Person with ID {person.get_person_id()} already exists.")
        self._persons[person.get_person_id()] = person

    # Removes a Person from the repository by its person_id
    def remove_person(self, person_id):
        if person_id not in self._persons:
            raise ValueError(f"Person with ID {person_id} does not exist.")
        del self._persons[person_id]

    # Updates an existing Person in the repository
    def update_person(self, person_id, name, address):
        if person_id not in self._persons:
            raise ValueError(f"Person with ID {person_id} does not exist.")
        self._persons[person_id].set_name(name)
        self._persons[person_id].set_address(address)

    # Finds and retrieves a Person by its perosn_id
    def find_person_by_id(self, person_id):
        if person_id not in self._persons:
            raise ValueError(f"Person with ID {person_id} does not exist.")
        return self._persons[person_id]

    # Returns a list of all Persons objects in the repository
    def get_all_persons(self):
        return list(self._persons.values())
