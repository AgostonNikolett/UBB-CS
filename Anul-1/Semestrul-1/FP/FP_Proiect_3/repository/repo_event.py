class EventRepository:
    def __init__(self):
        self._events = {}

    # Adds a new Event to the repository
    def add_event(self, event):
        if event.get_event_id() in self._events:
            raise ValueError(f"Event with ID {event.get_event_id()} already exists.")
        self._events[event.get_event_id()] = event

    # Removes an Event from the repository by its event_id
    def remove_event(self, event_id):
        if event_id not in self._events:
            raise ValueError(f"Event with ID {event_id} does not exist.")
        del self._events[event_id]

    # Updates an existing Event in the repository
    def update_event(self, event_id, date, time, description):
        if event_id not in self._events:
            raise ValueError(f"Event with ID {event_id} does not exist.")
        event = self._events[event_id]
        event.set_date(date)
        event.set_time(time)
        event.set_description(description)

    # Finds and retrieves an Event by its event_id
    def find_event_by_id(self, event_id):
        if event_id not in self._events:
            raise ValueError(f"Event with ID {event_id} does not exist.")
        return self._events[event_id]

    # Returns a list of all Event objects in the repository
    def get_all_events(self):
        return list(self._events.values())
