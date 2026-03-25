import unittest
from unittest.mock import Mock
from service.service_person import PersonService
from service.service_event import EventService
from service.service_participant import ParticipantService
from domain.person import Person
from domain.event import Event
from domain.participant import Participant

class TestEventService(unittest.TestCase):
    def setUp(self):
        # Set up the mocks for repository and validator
        self.event_repo_mock = Mock()
        self.validator_mock = Mock()

        # Instantiate EventService with mocked dependencies
        self.event_service = EventService(self.event_repo_mock, self.validator_mock)

        # Example Event for tests
        self.event_id = "123"
        self.event_date = "2024-06-20"
        self.event_time = "14:30"
        self.event_description = "Workshop Python"
        self.event = Event(self.event_id, self.event_date, self.event_time, self.event_description)

    def test_add_event_valid(self):
        # Validator accepts the event
        self.validator_mock.validate_event.return_value = True

        # Call add_event
        self.event_service.add_event(self.event_id, self.event_date, self.event_time, self.event_description)

        # Verify that the repo's add_event method was called with the correct Event
        self.event_repo_mock.add_event.assert_called_once()
        called_event = self.event_repo_mock.add_event.call_args[0][0]
        self.assertEqual(called_event.get_event_id(), self.event_id)
        self.assertEqual(called_event.get_date(), self.event_date)
        self.assertEqual(called_event.get_time(), self.event_time)
        self.assertEqual(called_event.get_description(), self.event_description)

    def test_add_event_invalid(self):
        # Validator rejects the event
        self.validator_mock.validate_event.return_value = False

        # Call add_event
        self.event_service.add_event(self.event_id, self.event_date, self.event_time, self.event_description)

        # Verify add_event was not called on the repo
        self.event_repo_mock.add_event.assert_not_called()

    def test_update_event_valid(self):
        # Validator accepts the updated event
        self.validator_mock.validate_event.return_value = True

        # Call update_event
        self.event_service.update_event(self.event_id, self.event_date, self.event_time, self.event_description)

        # Verify the repo's update_event was called
        self.event_repo_mock.update_event.assert_called_once_with(
            self.event_id, self.event_date, self.event_time, self.event_description
        )

    def test_remove_event(self):
        # Call remove_event
        self.event_service.remove_event(self.event_id)

        # Verify the repo's remove_event was called
        self.event_repo_mock.remove_event.assert_called_once_with(self.event_id)

    def test_find_event_by_id(self):
        # Mock repository to return a specific event
        self.event_repo_mock.find_event_by_id.return_value = self.event

        # Call find_event_by_id
        result = self.event_service.find_event_by_id(self.event_id)

        # Verify the repo's find_event_by_id was called
        self.event_repo_mock.find_event_by_id.assert_called_once_with(self.event_id)

        # Verify the returned event
        self.assertEqual(result, self.event)

    def test_add_random_events(self):
        # Mock the validator to always accept events
        self.validator_mock.validate_event.return_value = True

        # Mock repo's add_event to simulate adding events
        self.event_repo_mock.add_event = Mock()

        # Call add_random_events
        self.event_service.add_random_events(5)

        # Verify that add_event was called exactly 5 times
        self.assertEqual(self.event_repo_mock.add_event.call_count, 5)

    def test_list_all_events(self):
        # Mock events in the repository
        event1 = Event("2", "2024-06-21", "15:00", "Event 1")
        event2 = Event("1", "2024-06-20", "14:00", "Event 2")
        event3 = Event("3", "2024-06-22", "16:00", "Event 3")

        # Mock repository to return unsorted events
        self.event_repo_mock.get_all_events.return_value = [event1, event2, event3]

        # Call list_all_events
        sorted_events = self.event_service.list_all_events()

        # Verify that the returned events are sorted by event_id
        self.assertEqual([e.get_event_id() for e in sorted_events], ["1", "2", "3"])

class TestParticipantService(unittest.TestCase):
    def setUp(self):
        # Set up mocks for repositories and validator
        self.participant_repo_mock = Mock()
        self.person_repo_mock = Mock()
        self.event_repo_mock = Mock()
        self.validator_mock = Mock()

        # Instantiate ParticipantService with mocks
        self.participant_service = ParticipantService(
            self.participant_repo_mock,
            self.person_repo_mock,
            self.event_repo_mock,
            self.validator_mock
        )

        # Example objects for testing
        self.person_id = "P1"
        self.event_id = "E1"
        self.participant = Participant(self.person_id, self.event_id)
        self.mock_event = Mock()
        self.mock_event.get_event_id.return_value = self.event_id

    def test_register_person_to_event_valid(self):
        # Validator accepts the registration
        self.validator_mock.validate_participant.return_value = True
        self.event_repo_mock.find_event_by_id.return_value = self.mock_event

        # Call register_person_to_event
        self.participant_service.register_person_to_event(self.person_id, self.event_id)

        # Assertions
        self.participant_repo_mock.add_participant.assert_called_once()
        self.mock_event.increment_participant_count.assert_called_once()

    def test_register_person_to_event_invalid(self):
        # Validator rejects the registration
        self.validator_mock.validate_participant.return_value = False

        # Call register_person_to_event
        self.participant_service.register_person_to_event(self.person_id, self.event_id)

        # Verify add_participant is not called
        self.participant_repo_mock.add_participant.assert_not_called()

    def test_unregister_person_from_event(self):
        # Mock the find_event_by_id to return a mock event
        self.event_repo_mock.find_event_by_id.return_value = self.mock_event

        # Call unregister_person_from_event
        self.participant_service.unregister_person_from_event(self.person_id, self.event_id)

        # Assertions
        self.participant_repo_mock.remove_participant.assert_called_once_with(self.person_id, self.event_id)
        self.mock_event.decrement_participant_count.assert_called_once()

    def test_register_random_persons_to_events(self):
        # Mock persons, events, and participants
        mock_person = Mock()
        mock_person.get_person_id.return_value = "P1"
        mock_event = Mock()
        mock_event.get_event_id.return_value = "E1"

        self.person_repo_mock.get_all_persons.return_value = [mock_person]
        self.event_repo_mock.get_all_events.return_value = [mock_event]
        self.participant_repo_mock.get_all_participants.return_value = []

        # Validator accepts all registrations
        self.validator_mock.validate_participant.return_value = True
        mock_event.increment_participant_count = Mock()

        # Call register_random_persons_to_events
        self.participant_service.register_random_persons_to_events(1)

        # Assertions
        self.participant_repo_mock.add_participant.assert_called_once()

    def test_get_event_persons(self):
        # Mock participants for a specific event
        participant1 = Participant("P1", "E1")
        participant2 = Participant("P2", "E1")
        self.participant_repo_mock.find_participants_by_event.return_value = [participant1, participant2]

        # Mock persons
        mock_person1 = Mock()
        mock_person1.get_person_id.return_value = "P1"
        mock_person1.get_name.return_value = "Alice"

        mock_person2 = Mock()
        mock_person2.get_person_id.return_value = "P2"
        mock_person2.get_name.return_value = "Bob"

        self.person_repo_mock.find_person_by_id.side_effect = lambda pid: mock_person1 if pid == "P1" else mock_person2

        # Call get_event_persons
        result = self.participant_service.get_event_persons("E1")

        # Assertions: sorted by name
        self.assertEqual([person.get_name() for person in result], ["Bob", "Alice"])

    def test_get_person_events(self):
        # Mock participants for a specific person
        participant1 = Participant("P1", "E1")
        participant2 = Participant("P1", "E2")
        self.participant_repo_mock.find_participants_by_person.return_value = [participant1, participant2]

        # Mock events
        mock_event1 = Mock()
        mock_event1.get_event_id.return_value = "E1"
        mock_event1.get_description.return_value = "Date"
        mock_event1.get_date.return_value = "2024-06-20"
        mock_event1.get_time.return_value = "12:00"

        mock_event2 = Mock()
        mock_event2.get_event_id.return_value = "E2"
        mock_event2.get_description.return_value = "Christmas"
        mock_event2.get_date.return_value = "2024-12-25"
        mock_event2.get_time.return_value = "18:00"

        # Mock the event repository's behavior
        self.event_repo_mock.find_event_by_id.side_effect = lambda eid: mock_event1 if eid == "E1" else mock_event2

        # Call get_person_events
        result = self.participant_service.get_person_events("P1")

        # Assertions: sorted first by description, then date and time
        self.assertEqual(
            [event.get_description() for event in result],
            ["Christmas", "Date"]  # Sorted alphabetically by description
        )
        self.assertEqual(
            [event.get_event_id() for event in result],
            ["E2", "E1"]  # Ensures correct events are returned in the expected order
        )

    def test_get_most_active_persons(self):
        # Mock participants
        participant1 = Participant("P1", "E1")
        participant2 = Participant("P1", "E2")
        participant3 = Participant("P2", "E1")

        self.participant_repo_mock.get_all_participants.return_value = [participant1, participant2, participant3]

        # Mock persons
        mock_person1 = Mock()
        mock_person1.get_person_id.return_value = "P1"
        mock_person1.get_name.return_value = "Alice"

        mock_person2 = Mock()
        mock_person2.get_person_id.return_value = "P2"
        mock_person2.get_name.return_value = "Bob"

        self.person_repo_mock.find_person_by_id.side_effect = lambda pid: mock_person1 if pid == "P1" else mock_person2

        # Call get_most_active_persons
        result = self.participant_service.get_most_active_persons()

        # Assertions: P1 is the most active
        self.assertEqual([person.get_person_id() for person in result], ["P1"])

    def test_get_top_events_by_participants(self):
        # Mock participants
        participant1 = Participant("P1", "E1")
        participant2 = Participant("P2", "E1")
        participant3 = Participant("P3", "E2")

        self.participant_repo_mock.get_all_participants.return_value = [participant1, participant2, participant3]

        # Mock events
        mock_event1 = Mock()
        mock_event1.get_event_id.return_value = "E1"
        mock_event2 = Mock()
        mock_event2.get_event_id.return_value = "E2"

        self.event_repo_mock.find_event_by_id.side_effect = lambda eid: mock_event1 if eid == "E1" else mock_event2

        # Call get_top_events_by_participants
        result = self.participant_service.get_top_events_by_participants()

        # Assertions: Top 20% includes E1
        self.assertEqual([event.get_event_id() for event in result], ["E1"])

    def test_list_all_participants(self):
        # Mock participants
        participant1 = Participant("P1", "E1")
        participant2 = Participant("P2", "E2")
        self.participant_repo_mock.get_all_participants.return_value = [participant1, participant2]

        # Call list_all_participants
        result = self.participant_service.list_all_participants()

        # Assertions
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].get_person_id(), "P1")
        self.assertEqual(result[1].get_person_id(), "P2")

class TestPersonService(unittest.TestCase):
    def setUp(self):
        # Mock the repository and validator
        self.person_repo_mock = Mock()
        self.validator_mock = Mock()

        # Create an instance of PersonService with mocks
        self.person_service = PersonService(self.person_repo_mock, self.validator_mock)

        # Example person data
        self.person_id = "123"
        self.name = "John Doe"
        self.address = "Str. Mihail Kogalniceanu 10 Cluj-Napoca"
        self.person = Person(self.person_id, self.name, self.address)

    def test_add_person_valid(self):
        # Validator accepts the person
        self.validator_mock.validate_person.return_value = True

        # Call add_person
        self.person_service.add_person(self.person_id, self.name, self.address)

        # Check that add_person was called on the repository
        self.person_repo_mock.add_person.assert_called_once()
        self.validator_mock.validate_person.assert_called_once_with(
            self.person_id, self.name, self.address, self.person_repo_mock
        )

    def test_add_person_invalid(self):
        # Validator rejects the person
        self.validator_mock.validate_person.return_value = False

        # Call add_person
        self.person_service.add_person(self.person_id, self.name, self.address)

        # Ensure add_person is not called on the repository
        self.person_repo_mock.add_person.assert_not_called()

    def test_update_person_valid(self):
        # Validator accepts the updated person data
        self.validator_mock.validate_person.return_value = True

        # Call update_person
        self.person_service.update_person(self.person_id, self.name, self.address)

        # Verify update_person was called
        self.person_repo_mock.update_person.assert_called_once_with(
            self.person_id, self.name, self.address
        )
        self.validator_mock.validate_person.assert_called_once_with(
            self.person_id, self.name, self.address, self.person_repo_mock
        )

    def test_remove_person(self):
        # Call remove_person
        self.person_service.remove_person(self.person_id)

        # Verify remove_person was called on the repository
        self.person_repo_mock.remove_person.assert_called_once_with(self.person_id)

    def test_find_person_by_id(self):
        # Mock find_person_by_id to return a person
        self.person_repo_mock.find_person_by_id.return_value = self.person

        # Call find_person_by_id
        result = self.person_service.find_person_by_id(self.person_id)

        # Assertions
        self.assertEqual(result, self.person)
        self.person_repo_mock.find_person_by_id.assert_called_once_with(self.person_id)

    def test_add_random_persons(self):
        # Mock the validator to accept any random person
        self.validator_mock.validate_person.return_value = True

        # Mock repository add_person to simply pass
        self.person_repo_mock.add_person.return_value = None

        # Call add_random_persons
        self.person_service.add_random_persons(2)

        # Assertions
        self.assertEqual(self.validator_mock.validate_person.call_count, 2)
        self.assertEqual(self.person_repo_mock.add_person.call_count, 2)

    def test_list_all_persons(self):
        # Mock repository to return a list of persons
        person1 = Person("123", "Alice Doe", "Str. Libertatii 5 Cluj-Napoca")
        person2 = Person("456", "Bob Smith", "Str. Florilor 8 Bucuresti")
        self.person_repo_mock.get_all_persons.return_value = [person2, person1]

        # Call list_all_persons
        result = self.person_service.list_all_persons()

        # Verify sorting by ID
        self.assertEqual(result, [person1, person2])  # Sorted by IDs: 123, 456
        self.person_repo_mock.get_all_persons.assert_called_once()