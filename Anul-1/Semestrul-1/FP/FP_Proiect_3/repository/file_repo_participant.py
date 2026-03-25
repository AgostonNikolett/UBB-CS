import os 
from repository.repo_participant import ParticipantRepository
from domain.participant import Participant

class ParticipantFileRepository(ParticipantRepository):
    def __init__(self, filename):
        ParticipantRepository.__init__(self)
        self._filename = filename
        self._load_from_file()

    def _save_to_file(self):
        """Saves all participants to the file."""
        with open(self._filename, 'w') as file:
            for participant in self._participants:
                file.write(participant.to_string() + '\n')

    def _load_from_file(self):
        """Loads all participants from the file."""
        if not os.path.exists(self._filename):
            return
        with open(self._filename, 'r') as file:
            for line in file:
                if line.strip():
                    participant = Participant.from_string(line)
                    self._participants[participant.get_participant_id()] = participant
    
    # Register a person to an event
    def add_participant(self, participant):
        ParticipantRepository.add_participant(self, participant)
        self._save_to_file()

    # Unregister a person from an event
    def remove_participant(self, person_id, event_id):
        ParticipantRepository.remove_participant(self, person_id, event_id)
        self._save_to_file()

    # Find all persons participating to an event
    def find_participants_by_event(self, event_id):
        return ParticipantRepository.find_participants_by_event(self, event_id)

    # Find all events that a person participates to
    def find_participants_by_person(self, person_id):
        return ParticipantRepository.find_participants_by_person(self, person_id)

    # Returns a list of all Participant objects in the repository
    def get_all_participants(self):
        return ParticipantRepository.get_all_participants(self)