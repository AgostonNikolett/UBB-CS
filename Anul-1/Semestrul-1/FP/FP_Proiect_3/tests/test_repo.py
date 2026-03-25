import unittest
from repository.repo_person import PersonRepository
from repository.repo_event import EventRepository
from repository.repo_participant import ParticipantRepository
from domain.person import Person
from domain.event import Event
from domain.participant import Participant

class TestEventRepository(unittest.TestCase):

    def setUp(self):
        """Initialize the repository and sample data for testing."""
        self.repo = EventRepository()
        self.event1 = Event("101", "2024-12-25", "18:00", "Christmas Party")
        self.event2 = Event("102", "2024-12-31", "20:00", "New Year's Eve")

    def test_add_event(self):
        """Test adding an event to the repository."""
        self.repo.add_event(self.event1)
        self.assertIn("101", self.repo._events)
        self.assertEqual(self.repo.find_event_by_id("101"), self.event1)

        # Test adding a duplicate event
        with self.assertRaises(ValueError) as context:
            self.repo.add_event(self.event1)
        self.assertEqual(str(context.exception), "Event with ID 101 already exists.")

    def test_remove_event(self):
        """Test removing an event from the repository."""
        self.repo.add_event(self.event1)
        self.repo.remove_event("101")
        self.assertNotIn("101", self.repo._events)

        # Test removing a non-existent event
        with self.assertRaises(ValueError) as context:
            self.repo.remove_event("999")
        self.assertEqual(str(context.exception), "Event with ID 999 does not exist.")

    def test_update_event(self):
        """Test updating an existing event."""
        self.repo.add_event(self.event1)
        self.repo.update_event("101", "2024-12-24", "17:00", "Christmas Eve Party")
        updated_event = self.repo.find_event_by_id("101")
        self.assertEqual(updated_event.get_date(), "2024-12-24")
        self.assertEqual(updated_event.get_time(), "17:00")
        self.assertEqual(updated_event.get_description(), "Christmas Eve Party")

        # Test updating a non-existent event
        with self.assertRaises(ValueError) as context:
            self.repo.update_event("999", "2024-01-01", "00:00", "Non-existent Event")
        self.assertEqual(str(context.exception), "Event with ID 999 does not exist.")

    def test_find_event_by_id(self):
        """Test finding an event by its ID."""
        self.repo.add_event(self.event1)
        found_event = self.repo.find_event_by_id("101")
        self.assertEqual(found_event, self.event1)

        # Test finding a non-existent event
        with self.assertRaises(ValueError) as context:
            self.repo.find_event_by_id("999")
        self.assertEqual(str(context.exception), "Event with ID 999 does not exist.")

    def test_get_all_events(self):
        """Test retrieving all events from the repository."""
        self.repo.add_event(self.event1)
        self.repo.add_event(self.event2)
        all_events = self.repo.get_all_events()
        self.assertEqual(len(all_events), 2)
        self.assertIn(self.event1, all_events)
        self.assertIn(self.event2, all_events)

class TestParticipantRepository(unittest.TestCase):

    def setUp(self):
        """Initialize the repository and sample participants for testing."""
        self.repo = ParticipantRepository()
        self.participant1 = Participant("1", "101")
        self.participant2 = Participant("2", "101")
        self.participant3 = Participant("1", "102")

    def test_add_participant(self):
        """Test adding a participant to the repository."""
        self.repo.add_participant(self.participant1)
        self.repo.add_participant(self.participant2)
        all_participants = self.repo.get_all_participants()
        self.assertEqual(len(all_participants), 2)
        self.assertIn(self.participant1, all_participants)
        self.assertIn(self.participant2, all_participants)

    def test_remove_participant(self):
        """Test removing a participant from the repository."""
        self.repo.add_participant(self.participant1)
        self.repo.add_participant(self.participant2)
        self.repo.remove_participant("1", "101")
        remaining_participants = self.repo.get_all_participants()
        self.assertEqual(len(remaining_participants), 1)
        self.assertNotIn(self.participant1, remaining_participants)
        self.assertIn(self.participant2, remaining_participants)

        # Test removing a non-existent participant (should not raise an error)
        self.repo.remove_participant("3", "999")
        self.assertEqual(len(self.repo.get_all_participants()), 1)

    def test_find_participants_by_event(self):
        """Test finding all participants for a specific event."""
        self.repo.add_participant(self.participant1)
        self.repo.add_participant(self.participant2)
        event_participants = self.repo.find_participants_by_event("101")
        self.assertEqual(len(event_participants), 2)
        self.assertIn(self.participant1, event_participants)
        self.assertIn(self.participant2, event_participants)

        # Test for an event with no participants
        event_participants = self.repo.find_participants_by_event("999")
        self.assertEqual(len(event_participants), 0)

    def test_find_participants_by_person(self):
        """Test finding all events a specific person participates in."""
        self.repo.add_participant(self.participant1)
        self.repo.add_participant(self.participant3)
        person_participants = self.repo.find_participants_by_person("1")
        self.assertEqual(len(person_participants), 2)
        self.assertIn(self.participant1, person_participants)
        self.assertIn(self.participant3, person_participants)

        # Test for a person not registered for any events
        person_participants = self.repo.find_participants_by_person("999")
        self.assertEqual(len(person_participants), 0)

    def test_get_all_participants(self):
        """Test retrieving all participants from the repository."""
        self.repo.add_participant(self.participant1)
        self.repo.add_participant(self.participant2)
        self.repo.add_participant(self.participant3)
        all_participants = self.repo.get_all_participants()
        self.assertEqual(len(all_participants), 3)
        self.assertIn(self.participant1, all_participants)
        self.assertIn(self.participant2, all_participants)
        self.assertIn(self.participant3, all_participants)

class TestPersonRepository(unittest.TestCase):

    def setUp(self):
        """Initialize the repository and sample person data for testing."""
        self.repo = PersonRepository()
        self.person1 = Person("1", "John Doe", "123 Main St")
        self.person2 = Person("2", "Jane Smith", "456 Elm St")
        self.person3 = Person("3", "Alice Johnson", "789 Oak St")

    def test_add_person(self):
        """Test adding a person to the repository."""
        self.repo.add_person(self.person1)
        self.repo.add_person(self.person2)
        all_persons = self.repo.get_all_persons()
        self.assertEqual(len(all_persons), 2)
        self.assertIn(self.person1, all_persons)
        self.assertIn(self.person2, all_persons)

    def test_add_person_duplicate_id(self):
        """Test adding a person with a duplicate ID should raise an error."""
        self.repo.add_person(self.person1)
        with self.assertRaises(ValueError):
            self.repo.add_person(self.person1)

    def test_remove_person(self):
        """Test removing a person from the repository."""
        self.repo.add_person(self.person1)
        self.repo.add_person(self.person2)
        self.repo.remove_person("1")
        all_persons = self.repo.get_all_persons()
        self.assertEqual(len(all_persons), 1)
        self.assertNotIn(self.person1, all_persons)
        self.assertIn(self.person2, all_persons)

    def test_remove_person_non_existent(self):
        """Test removing a non-existent person should raise an error."""
        with self.assertRaises(ValueError):
            self.repo.remove_person("999")

    def test_update_person(self):
        """Test updating a person's name and address."""
        self.repo.add_person(self.person1)
        self.repo.update_person("1", "Johnathan Doe", "101 New St")
        updated_person = self.repo.find_person_by_id("1")
        self.assertEqual(updated_person.get_name(), "Johnathan Doe")
        self.assertEqual(updated_person.get_address(), "101 New St")

    def test_update_person_non_existent(self):
        """Test updating a non-existent person should raise an error."""
        with self.assertRaises(ValueError):
            self.repo.update_person("999", "New Name", "New Address")

    def test_find_person_by_id(self):
        """Test finding a person by ID."""
        self.repo.add_person(self.person1)
        self.repo.add_person(self.person2)
        found_person = self.repo.find_person_by_id("1")
        self.assertEqual(found_person, self.person1)

    def test_find_person_by_id_non_existent(self):
        """Test finding a non-existent person should raise an error."""
        with self.assertRaises(ValueError):
            self.repo.find_person_by_id("999")

    def test_get_all_persons(self):
        """Test retrieving all persons from the repository."""
        self.repo.add_person(self.person1)
        self.repo.add_person(self.person2)
        all_persons = self.repo.get_all_persons()
        self.assertEqual(len(all_persons), 2)
        self.assertIn(self.person1, all_persons)
        self.assertIn(self.person2, all_persons)