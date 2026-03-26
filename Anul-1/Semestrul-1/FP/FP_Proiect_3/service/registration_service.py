from domain.participant import Participant
from utils.sortare import generic_sort


class RegistrationService:
    def __init__(self, part_repo, person_repo, event_repo, validator):
        """
        Coordinates registrations and reporting.
        """
        self._part_repo = part_repo
        self._person_repo = person_repo
        self._event_repo = event_repo
        self._validator = validator

    def register_to_event(self, person_id: str, event_id: str):
        """Registers a person to an event and increments event counter."""
        self._validator.validate(person_id, event_id, self._part_repo, self._person_repo, self._event_repo)
        participant = Participant(person_id, event_id)
        self._part_repo.add_registration(participant)

        # Update the counter in the Event entity
        event = self._event_repo.find_by_id(event_id)
        event.update_participant_count(1)

    def unregister_from_event(self, person_id: str, event_id: str):
        """Removes a registration and decrements event counter."""
        self._part_repo.remove_registration(person_id, event_id)
        event = self._event_repo.find_by_id(event_id)
        event.update_participant_count(-1)

    def get_event_participants_sorted(self, event_id: str):
        """Returns persons for an event, sorted alphabetically."""
        registrations = [r for r in self._part_repo.get_all() if r.get_event_id() == event_id]
        persons = [self._person_repo.find_by_id(r.get_person_id()) for r in registrations]
        return generic_sort(persons, method='quick', key=lambda p: p.get_name())

    def get_person_events_sorted(self, person_id: str):
        """Returns events for a person, sorted by description and date."""
        registrations = [r for r in self._part_repo.get_all() if r.get_person_id() == person_id]
        events = [self._event_repo.find_by_id(r.get_event_id()) for r in registrations]
        return generic_sort(events, method='gnome', key=lambda e: (e.get_description(), e.get_date()))

    def get_most_active_persons(self):
        """Finds persons registered for the most events."""
        counts = {}
        for r in self._part_repo.get_all():
            p_id = r.get_person_id()
            counts[p_id] = counts.get(p_id, 0) + 1

        if not counts: return []
        max_reg = max(counts.values())
        active_ids = [p_id for p_id, count in counts.items() if count == max_reg]
        return [self._person_repo.find_by_id(p_id) for p_id in active_ids]


    def get_top_events(self):
        """Returns top 20% events by attendance."""
        events = self._event_repo.get_all()
        sorted_events = sorted(events, key=lambda e: e.get_participant_count(), reverse=True)

        limit = max(1, int(0.2 * len(sorted_events)))
        return sorted_events[:limit]