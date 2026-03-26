import os
from domain.participant import Participant


class ParticipantFileRepository:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._participants = []
        self._load_data()

    def _load_data(self):
        if not os.path.exists(self._file_path): return 
        with open(self._file_path, 'r') as f:
            for line in f:
                if line.strip():
                    self._participants.append(Participant.from_file_string(line))

    def _save_data(self):
        with open(self._file_path, 'w') as f:
            for p in self._participants: 
                f.write(p.to_file_string() + '\n')


    def add_registration(self, participant: Participant):
        """Registers a person to an event."""
        # Verificăm dacă nu este deja înregistrat
        for p in self._participants:
            if p.get_person_id() == participant.get_person_id() and \
                p.get_event_id() == participant.get_event_id():
                raise ValueError("Person is already registered for this event.")


        self._participants.append(participant)
        self._save_data()


    def remove_registration(self, person_id: str, event_id: str):
        """Unregisters a person from an event."""
        initial_len = len(self._participants)
        self._participants = [
            p for p in self._participants
            if not (p.get_person_id() == person_id and p.get_event_id() == event_id)
        ]

        if len(self._participants) == initial_len:
            raise ValueError("Registration not found.")
        self._save_data()


    def get_all(self):
        return self._participants