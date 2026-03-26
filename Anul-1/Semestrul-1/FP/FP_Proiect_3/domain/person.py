class Person:
    # Constructor to initialize the person's attributes
    def __init__(self, person_id, name, address):
        self.person_id = person_id
        self.name = name
        self.address = address

    # Getter method to retrieve the person's ID
    def get_person_id(self):
        return self.person_id

    # Getter method to retrieve the person's name
    def get_name(self):
        return self.name

    # Getter method to retrieve the person's address
    def get_address(self):
        return self.address

    # Setter method to update the person's name
    def set_name(self, name):
        self.name = name

    # Setter method to update the person's address
    def set_address(self, address):
        self.address = address

    def to_string(self):
        """Converts the Person object to a string suitable for saving to a file."""
        return f"{self.person_id},{self.name},{self.address}"

    @staticmethod
    def from_string(person_str):
        """Creates a Person object from a string."""
        parts = person_str.strip().split(',')
        if len(parts) != 3:
            raise ValueError("Invalid person string format.")
        return Person(parts[0], parts[1], parts[2])
    

    def __str__(self):
        return f"Person ID: {self.person_id}, Name: {self.name}, Address: {self.address}"