from domain.person import Person
import random
class PersonService:
    def __init__(self, person_repo, validator):
        self.person_repo = person_repo
        self.validator = validator

    # Add a person
    def add_person(self, person_id, name, address):
        if self.validator.validate_person(person_id, name, address, self.person_repo):
            person = Person(person_id, name, address)
            self.person_repo.add_person(person)

    # Update a person
    def update_person(self, person_id, name, address):
        if self.validator.validate_person(person_id, name, address, self.person_repo):
            self.person_repo.update_person(person_id, name, address)

    # Remove a person
    def remove_person(self, person_id):
        self.person_repo.remove_person(person_id)

    # Find a person by their ID
    def find_person_by_id(self, person_id):
        return self.person_repo.find_person_by_id(person_id)

    # Add random persons
    def add_random_persons(self, number_of_persons):
        # Define lists for components of an address
        street_names = [
            "Mihail Kogalniceanu", "Bistritei", "Fabricii", "Florilor", 
            "Libertatii", "Transilvaniei", "Mihai Viteazul", "Unirii", 
            "Privighetorii", "Stefan cel Mare", "Eroilor", "Ciresilor"
        ]
        cities = [
            "Cluj-Napoca", "Bucuresti", "Timisoara", "Brasov", 
            "Constanta", "Iasi", "Oradea", "Craiova", 
            "Sibiu", "Alba Iulia", "Galati", "Ploiesti"
        ]
        first_names = [
            "Ana", "Andrei", "Ion", "Mihai", "Maria", "Tudor", "Mihaela", "Ionel", "Cezar", "Alex", 
            "Iulia", "Oana", "Elena", "Victor", "Mariana", "Cristian", "Adriana"
        ]
        last_names = [
            "Popescu", "Georgescu", "Eminescu", "Voinea", "Preda", "Dumitrescu", 
            "Vasile", "Iliescu", "Radu", "Barbu", "Marinescu", "Stoica", "Lupu"
        ]
    
        while number_of_persons != 0:
            person_id = str(random.randint(0, 10000))

            # Generate a random name by combining a first name and a last name
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            name = f"{first_name} {last_name}"
        
            # Generate a random address by combining a street name, number, and city
            street = random.choice(street_names)
            house_number = random.randint(1, 200)  
            city = random.choice(cities)
            address = f"Str. {street} {house_number} {city}"
            if self.validator.validate_person(person_id, name, address, self.person_repo):
                person = Person(person_id, name, address)
                self.person_repo.add_person(person)
                number_of_persons -= 1

    def list_all_persons(self):
        persons = self.person_repo.get_all_persons()
        sorted_persons = sorted(persons, key=lambda person: int(person.get_person_id()))
        return sorted_persons
