import random
from datetime import datetime, timedelta
from domain.event import Event

class EventService:
    def __init__(self, event_repo, validator):
        """
        Initializes the EventService.
        :param event_repo: Repository for event data.
        :param validator: Validator for event entities.
        """
        self._repo = event_repo
        self._validator = validator

    def add_event(self, event_id: str, date: str, time: str, description: str):
        """Validates and adds a new event."""
        self._validator.validate(event_id, date, time, description)
        event = Event(event_id, date, time, description)
        self._repo.store(event_id, event)

    def update_event(self, event_id: str, date: str, time: str, description: str):
        """Updates event details."""
        self._validator.validate(event_id, date, time, description)
        event = self._repo.find_by_id(event_id)
        event.set_date(date)
        event.set_time(time)
        event.set_description(description)

    def remove_event(self, event_id: str):
        """Removes an event by ID."""
        self._repo.remove(event_id)

    def find_by_id(self, event_id: str):
        """Finds an event by ID."""
        return self._repo.find_by_id(event_id)

    def generate_random_events(self, count: int):
        """Generates random events for testing purposes."""
        descriptions = ["Tech Conference", "AI Summit", "Workshop Python", "Music Festival"] 
        while count > 0:
            e_id = str(random.randint(1, 10000)) 
            date = (datetime.now() + timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d") 
            time = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}" 
            desc = random.choice(descriptions) 
            try:
                self.add_event(e_id, date, time, desc)
                count -= 1
            except ValueError:
                continue

    def get_all_sorted_by_id(self):
        """Returns all events sorted numerically by ID."""
        return sorted(self._repo.get_all(), key=lambda e: e.get_id())