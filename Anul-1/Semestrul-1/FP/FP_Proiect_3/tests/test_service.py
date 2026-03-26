import unittest
import os
from service.person_service import PersonService
from service.event_service import EventService
from service.registration_service import RegistrationService
from repository.base_repository import InMemoryRepository
from repository.participant_repository import ParticipantFileRepository
from validators.person_validator import PersonValidator
from validators.event_validator import EventValidator
from validators.registration_validator import RegistrationValidator
from domain.person import Person
from domain.event import Event


class TestService(unittest.TestCase):

    def setUp(self):
        """Initializes the service layer with in-memory and temporary file repos."""
        self.person_repo = InMemoryRepository()
        self.event_repo = InMemoryRepository()
        self.part_file = "test_service_reg.txt"
        self.part_repo = ParticipantFileRepository(self.part_file)

        self.person_val = PersonValidator()
        self.event_val = EventValidator()
        self.reg_val = RegistrationValidator()

        self.person_service = PersonService(self.person_repo, self.person_val)
        self.event_service = EventService(self.event_repo, self.event_val)
        self.reg_service = RegistrationService(
            self.part_repo, self.person_repo, self.event_repo, self.reg_val
        )

    def tearDown(self):
        if os.path.exists(self.part_file):
            os.remove(self.part_file)

    # --- PersonService Tests ---

    def test_person_service_operations(self):
        self.person_service.add_person("p1", "John", "Cluj")
        self.assertEqual(len(self.person_service.get_all_sorted_by_id()), 1)

        self.person_service.update_person("p1", "John Doe", "Gherla")
        self.assertEqual(self.person_service.find_by_id("p1").get_name(), "John Doe")

        self.person_service.remove_person("p1")
        self.assertEqual(len(self.person_service.get_all_sorted_by_id()), 0)

    def test_random_person_generation(self):
        # We test that it successfully adds the requested number of persons
        self.person_service.generate_random_persons(5)
        self.assertEqual(len(self.person_service.get_all_sorted_by_id()), 5)

    # --- EventService Tests ---

    def test_event_service_operations(self):
        self.event_service.add_event("e1", "2024-01-01", "12:00", "New Year")
        self.assertEqual(len(self.event_service.get_all_sorted_by_id()), 1)

        self.event_service.update_event("e1", "2024-01-01", "13:00", "Party")
        self.assertEqual(self.event_service.find_by_id("e1").get_time(), "13:00")

        self.event_service.remove_event("e1")
        self.assertEqual(len(self.event_service.get_all_sorted_by_id()), 0)

    def test_random_event_generation(self):
        self.event_service.generate_random_events(3)
        self.assertEqual(len(self.event_service.get_all_sorted_by_id()), 3)

    # --- RegistrationService & Reports Tests ---

    def test_registration_and_counter(self):
        # Setup entities
        self.person_service.add_person("p1", "User", "Addr")
        self.event_service.add_event("e1", "2024-05-05", "10:00", "Meeting")

        # Register
        self.reg_service.register_to_event("p1", "e1")
        event = self.event_service.find_by_id("e1")
        self.assertEqual(event.get_participant_count(), 1)

        # Unregister
        self.reg_service.unregister_from_event("p1", "e1")
        self.assertEqual(event.get_participant_count(), 0)

    def test_sorting_reports(self):
        self.person_service.add_person("p1", "Zaharia", "Addr")
        self.person_service.add_person("p2", "Abel", "Addr")
        self.event_service.add_event("e1", "2024-01-01", "10:00", "Workshop")

        self.reg_service.register_to_event("p1", "e1")
        self.reg_service.register_to_event("p2", "e1")

        # Test participants sorted alphabetically
        participants = self.reg_service.get_event_participants_sorted("e1")
        self.assertEqual(participants[0].get_name(), "Abel")
        self.assertEqual(participants[1].get_name(), "Zaharia")

    def test_most_active_persons_report(self):
        self.person_service.add_person("p1", "Active", "Addr")
        self.person_service.add_person("p2", "Passive", "Addr")
        self.event_service.add_event("e1", "2024-01-01", "10:00", "E1")
        self.event_service.add_event("e2", "2024-01-02", "11:00", "E2")

        self.reg_service.register_to_event("p1", "e1")
        self.reg_service.register_to_event("p1", "e2")
        self.reg_service.register_to_event("p2", "e1")

        active = self.reg_service.get_most_active_persons()
        self.assertEqual(len(active), 1)
        self.assertEqual(active[0].get_id(), "p1")

        # Empty case
        temp_file = "empty_test.txt"
        try:
            empty_part_repo = ParticipantFileRepository(temp_file)
            empty_reg_service = RegistrationService(
                empty_part_repo, self.person_repo, self.event_repo, self.reg_val
            )
            self.assertEqual(empty_reg_service.get_most_active_persons(), [])
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

    def test_top_events_report(self):
        # Create 5 events (20% of 5 is 1 event)
        for i in range(1, 6):
            self.event_service.add_event(f"e{i}", "2024-01-01", "10:00", f"Desc{i}")
            self.person_service.add_person(f"p{i}", f"Name{i}", "Addr")

        # Make e3 the most popular
        self.reg_service.register_to_event("p1", "e3")
        self.reg_service.register_to_event("p2", "e3")
        self.reg_service.register_to_event("p3", "e1")

        top_events = self.reg_service.get_top_events()
        self.assertEqual(len(top_events), 1)
        self.assertEqual(top_events[0].get_id(), "e3")

    def test_get_person_events_sorted(self):
        self.person_service.add_person("p1", "John Doe", "Cluj")

        self.event_service.add_event("e1", "2024-12-01", "10:00", "B Conference")
        self.event_service.add_event("e2", "2024-11-01", "10:00", "A Workshop")
        self.event_service.add_event("e3", "2024-10-01", "10:00", "B Conference")

        self.reg_service.register_to_event("p1", "e1")
        self.reg_service.register_to_event("p1", "e2")
        self.reg_service.register_to_event("p1", "e3")

        sorted_events = self.reg_service.get_person_events_sorted("p1")

        self.assertEqual(len(sorted_events), 3)
        self.assertEqual(sorted_events[0].get_id(), "e2")
        self.assertEqual(sorted_events[0].get_description(), "A Workshop")
        self.assertEqual(sorted_events[1].get_id(), "e3")
        self.assertEqual(sorted_events[2].get_id(), "e1")