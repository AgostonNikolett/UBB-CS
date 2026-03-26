class Event:
    """Represents an organized event."""

    def __init__(self, event_id: str, date: str, time: str, description: str):
        self._event_id = event_id
        self._date = date
        self._time = time
        self._description = description
        self._participant_count = 0

    # Getters
    def get_id(self) -> str: return self._event_id
    def get_date(self) -> str: return self._date
    def get_time(self) -> str: return self._time
    def get_description(self) -> str: return self._description
    def get_participant_count(self) -> int: return self._participant_count

    # Setters
    def set_date(self, date: str): self._date = date
    def set_time(self, time: str): self._time = time
    def set_description(self, desc: str): self._description = desc

    def update_participant_count(self, delta: int):
        """Updates the count of participants (positive for add, negative for remove)."""
        self._participant_count = max(0, self._participant_count + delta)

    def to_file_string(self) -> str:
        return f"{self._event_id},{self._date},{self._time},{self._description}"

    @staticmethod
    def from_file_string(line: str) -> 'Event':
        parts = line.strip().split(',')
        if len(parts) != 4:
            raise ValueError("Invalid format for Event data.")
        return Event(parts[0], parts[1], parts[2], parts[3])

    def __str__(self) -> str:
        return (f"Event {self._event_id}: {self._description} "
                f"on {self._date} at {self._time} ({self._participant_count} attending)")