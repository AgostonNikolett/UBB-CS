import os 
from repository.repo_event import EventRepository
from domain.event import Event

class EventFileRepository(EventRepository):
    def __init__(self, filename):
        EventRepository.__init__(self)
        self._filename = filename
        self._load_from_file()

    def _save_to_file(self):
        """Saves all events to the file."""
        with open(self._filename, 'w') as file:
            for event in self._events.values():
                file.write(event.to_string() + '\n')

    def _load_from_file(self):
        """Loads all events from the file."""
        if not os.path.exists(self._filename):
            return
        with open(self._filename, 'r') as file:
            for line in file:
                if line.strip():
                    event = Event.from_string(line)
                    self._events[event.get_event_id()] = event

    # Adds a new Event to the repository
    def add_event(self, event):
        EventRepository.add_event(self, event)
        self._save_to_file()

    # Removes an Event from the repository by its event_id
    def remove_event(self, event_id):
        EventRepository.remove_event(self, event_id)
        self._save_to_file()

    # Updates an existing Event in the repository
    def update_event(self, event_id, date, time, description):
        EventRepository.update_event(self, event_id, date, time, description)
        self._save_to_file()
        
    # Finds and retrieves an Event by its event_id
    def find_event_by_id(self, event_id):
        return EventRepository.find_event_by_id(self, event_id)

    # Returns a list of all Event objects in the repository
    def get_all_events(self):
        return EventRepository.get_all_events(self)