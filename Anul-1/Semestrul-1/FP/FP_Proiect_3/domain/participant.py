class Participant:
    # Constructor to initialize the participants's attributes
    def __init__(self, person_id, event_id):
        self.person_id = person_id
        self.event_id = event_id

    # Getter method to retrieve the person's ID
    def get_person_id(self):
        return self.person_id

    # Getter method to retrieve the event's ID
    def get_event_id(self):
        return self.event_id

    def to_string(self):
        """Converts the Participant object to a string suitable for saving to a file."""
        return f"{self.person_id},{self.event_id}"

    @staticmethod
    def from_string(participant_str):
        """Creates a Participant object from a string."""
        parts = participant_str.strip().split(',')
        if len(parts) != 2:
            raise ValueError("Invalid participant string format.")
        return Participant(parts[0], parts[1])
    
    def __str__(self):
        return f"Person ID: {self.person_id}, Event ID: {self.event_id}"
