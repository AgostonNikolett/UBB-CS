class ParticipantValidator:
    def validate_participant(self, person_id, event_id, participant_repo, person_repo, event_repo):
        
        # Ensure the person exists
        try:
            person = person_repo.find_person_by_id(person_id)
        except ValueError:
            raise ValueError(f"Person with ID {person_id} does not exist.")
        
        # Ensure the event exists
        try:
            event = event_repo.find_event_by_id(event_id)
        except ValueError:
            raise ValueError(f"Event with ID {event_id} does not exist.")
        
        # Ensure the person is not already registered for the event
        if any(
            p.get_person_id() == person_id and p.get_event_id() == event_id
            for p in participant_repo.get_all_participants()
            ):
            raise ValueError(f"Person with ID {person_id} is already registered for Event with ID {event_id}.")
        
        return True
