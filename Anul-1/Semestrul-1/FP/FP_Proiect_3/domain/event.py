import datetime

class Event:
    # Constructor to initialize the event's attributes
    def __init__(self, event_id, date, time, description):
        self.event_id = event_id
        self.date = date
        self.time = time
        self.description = description
        self.participant_count = 0

    # Getter method to retrieve the event's ID
    def get_event_id(self):
        return self.event_id

    # Getter method to retrieve the event's date
    def get_date(self):
        return self.date

    # Getter method to retrieve the event's time
    def get_time(self):
        return self.time
    
    # Getter method to retrieve the event's description
    def get_description(self):
        return self.description

    # Getter method for participant count
    def get_participant_count(self):
        return self.participant_count

    # Setter method to update the event's date
    def set_date(self, date):
        self.date = date

    # Setter method to update the event's time
    def set_time(self, time):
        self.time = time

    # Setter method to update the event's description
    def set_description(self, description):
        self.description = description

    # Method to increase participant count
    def increment_participant_count(self):
        self.participant_count += 1

    # Method to decrease participant count
    def decrement_participant_count(self):
        if self.participant_count > 0:
            self.participant_count -= 1

    def to_string(self):
        """Converts the Event object to a string suitable for saving to a file."""
        return f"{self.event_id},{self.date},{self.time},{self.description}"

    @staticmethod
    def from_string(event_str):
        """Creates an Event object from a string."""
        parts = event_str.strip().split(',')
        if len(parts) != 4:
            raise ValueError("Invalid event string format.")
        return Event(parts[0], parts[1], parts[2], parts[3])
    
    def __str__(self):
        return (f"Event ID: {self.event_id}, Time: {self.time}, Date: {self.date}, "
                f"Description: {self.description}, Participants: {self.participant_count}")
