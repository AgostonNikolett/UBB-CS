class Person:
    """Represents a person in the management system."""

    def __init__(self, person_id: str, name: str, address: str):
        self._person_id = person_id
        self._name = name
        self._address = address

    # Getters
    def get_id(self) -> str: return self._person_id
    def get_name(self) -> str: return self._name
    def get_address(self) -> str: return self._address

    # Setters
    def set_name(self, name: str): self._name = name
    def set_address(self, address: str): self._address = address

    def to_file_string(self) -> str:
        """Converts object to CSV format for file storage."""
        return f"{self._person_id},{self._name},{self._address}"

    @staticmethod
    def from_file_string(line: str) -> 'Person':
        """Creates a Person instance from a CSV line."""
        parts = line.strip().split(',')
        if len(parts) != 3:
            raise ValueError("Invalid format for Person data.")
        return Person(parts[0], parts[1], parts[2])

    def __str__(self) -> str:
        return f"ID: {self._person_id} | Name: {self._name} | Address: {self._address}"