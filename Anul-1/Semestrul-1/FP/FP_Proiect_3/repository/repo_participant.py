class ParticipantRepository:
    def __init__(self):
        self._participants = []

    # Register a person to an event
    def add_participant(self, participant):
        self._participants.append(participant)

    # Unregister a person from an event
    def remove_participant(self, person_id, event_id):
        self._participants = [
            p for p in self._participants
            if not (p.get_person_id() == person_id and p.get_event_id() == event_id)
        ]

    # Find all persons participating at an event
    def find_participants_by_event(self, event_id):
        return [p for p in self._participants if p.get_event_id() == event_id]

    # Find all events that a person participates in
    def find_participants_by_person(self, person_id):
        return [p for p in self._participants if p.get_person_id() == person_id]

    # Returns a list of all Participant objects in the repository
    def get_all_participants(self):
        return self._participants
