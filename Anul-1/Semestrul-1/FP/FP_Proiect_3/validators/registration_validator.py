class RegistrationValidator:
    """
    Validator for registrations (participants).
    Verifies existence of linked entities and prevents duplicates.
    """
    def validate(self, person_id: str, event_id: str, part_repo, person_repo, event_repo):
        """
        Validates if a registration can be performed.
        :raises ValueError: If links are missing or registration already exists.
        """
        # Check if person exists in the system
        try:
            person_repo.find_by_id(person_id)
        except ValueError:
            raise ValueError(f"Registration failed: Person with ID {person_id} does not exist.") 

        # Check if event exists in the system
        try:
            event_repo.find_by_id(event_id)
        except ValueError:
            raise ValueError(f"Registration failed: Event with ID {event_id} does not exist.") 

        # Prevent duplicate registrations for the same person-event pair
        registrations = part_repo.get_all()
        for reg in registrations:
            if reg.get_person_id() == person_id and reg.get_event_id() == event_id: 
                raise ValueError(f"Conflict: Person {person_id} is already registered for Event {event_id}.") 