class Participant:
    """Represents the link between a Person and an Event (Registration)."""

    def __init__(self, person_id: str, event_id: str):
        self._person_id = person_id
        self._event_id = event_id

    def get_person_id(self) -> str:
        return self._person_id

    def get_event_id(self) -> str:
        return self._event_id

    def to_file_string(self) -> str:
        """CSV format: person_id,event_id"""
        return f"{self._person_id},{self._event_id}"

    @staticmethod
    def from_file_string(line: str) -> 'Participant':
        parts = line.strip().split(',')
        if len(parts) != 2:
            raise ValueError("Invalid format for Participant data.")
        return Participant(parts[0], parts[1])

    def __str__(self) -> str:
        return f"Person {self._person_id} is registered for Event {self._event_id}"