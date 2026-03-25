from domain.participant import Participant
import random
from utils.sortare import generic_sort


class ParticipantService:
    def __init__(self, participant_repo, person_repo, event_repo, validator):
        self.participant_repo = participant_repo
        self.person_repo = person_repo
        self.event_repo = event_repo
        self.validator = validator

    # Register a person to an event
    def register_person_to_event(self, person_id, event_id):
        if self.validator.validate_participant(person_id, event_id, self.participant_repo, self.person_repo, self.event_repo):
            participant = Participant(person_id, event_id)
            self.participant_repo.add_participant(participant)

            # Update participant count in the event
            event = self.event_repo.find_event_by_id(event_id)
            event.increment_participant_count()

    # Unregister a person from an event
    def unregister_person_from_event(self, person_id, event_id):
        self.participant_repo.remove_participant(person_id, event_id)
        
        # Update participant count in the event
        event = self.event_repo.find_event_by_id(event_id)
        event.decrement_participant_count()

    # Register random persons to random events
    def register_random_persons_to_events(self, number_of_participants):
        persons = self.person_repo.get_all_persons() 
        events = self.event_repo.get_all_events()
        participants = self.participant_repo.get_all_participants()

        if not persons or not events:
            raise ValueError("There must be at least one person and one event to register participants.")

        max_participants = len(persons)*len(events) - len(participants)
        if number_of_participants > max_participants:
            raise ValueError(f"{'There are not enough persons and events to register. Max = '} {max_participants}")
        
        while number_of_participants > 0:
            # Randomly select a person and an event
            person = random.choice(persons)
            event = random.choice(events)
            person_id = person.get_person_id()
            event_id = event.get_event_id()

            if self.validator.validate_participant(person_id, event_id, self.participant_repo, self.person_repo, self.event_repo):
                participant = Participant(person_id, event_id)
                self.participant_repo.add_participant(participant)

                # Update participant count in the event
                event = self.event_repo.find_event_by_id(event_id)
                event.increment_participant_count()
                    
                number_of_participants -= 1

    # Get all participants for an event
    def get_event_persons(self, event_id):
        event_participants = self.participant_repo.find_participants_by_event(event_id)
        persons = [
            self.person_repo.find_person_by_id(participant.get_person_id())
            for participant in event_participants
        ]
        
        # Sort the list of persons by their name
        return generic_sort(persons, method='quick', key=lambda person: person.get_name(), reversed=True)

    # Get all events a person is registered for
    # Complexitate: O(N + P^2), unde:
    # N = numarul total de participari (perechi persoana - eveniment)
    # P = numarul evenimentelor persoanei
    # sortare Gnome Sort - O(P^2) in cel mai rau caz
    #                    - O(P) in cel mai bun caz
    def get_person_events(self, person_id):
        person_events = self.participant_repo.find_participants_by_person(person_id)
        events = [
            self.event_repo.find_event_by_id(participant.get_event_id())
            for participant in person_events
        ]

        # Sort the list of events first by description alphabetically, then by date
        return generic_sort(events, method='gnome', key=lambda event: (event.get_description(), event.get_date(), event.get_time()))


    # Find persons registered for the most events
    def get_most_active_persons(self):
        person_event_count = {}
        for participant in self.participant_repo.get_all_participants():
            person_id = participant.get_person_id()
            if person_id not in person_event_count:
                person_event_count[person_id] = 0
            person_event_count[person_id] += 1

        max_count = max(person_event_count.values(), default=0)
        return [
            self.person_repo.find_person_by_id(person_id)
            for person_id, count in person_event_count.items()
            if count == max_count
        ]

    # Find the top 20% of events by participant count
    def get_top_events_by_participants(self):
        event_participant_count = {}

        # Count participants for each event
        for participant in self.participant_repo.get_all_participants():
            event_id = participant.get_event_id()
            if event_id not in event_participant_count:
                event_participant_count[event_id] = 0
            event_participant_count[event_id] += 1

        # Sort events by participant count in descending order
        sorted_events = sorted(
            event_participant_count.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # Calculate the number of events in the top 20%
        top_20_percent_count = max(1, int(0.2 * len(sorted_events)))

        # Select the top 20% events
        top_events = sorted_events[:top_20_percent_count]

        # Retrieve and return the event objects for the top events
        return [
            self.event_repo.find_event_by_id(event_id)
            for event_id, _ in top_events
        ]

    # List all participants
    def list_all_participants(self):
        return self.participant_repo.get_all_participants()
