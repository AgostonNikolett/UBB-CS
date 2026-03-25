import unittest
from unittest.mock import MagicMock
from validator.validator_event import EventValidator
from validator.validator_participant import ParticipantValidator
from validator.validator_person import PersonValidator

class TestEventValidator(unittest.TestCase):

    def setUp(self):
        """Set up the EventValidator and mock dependencies."""
        self.validator = EventValidator()
        self.mock_event_repo = MagicMock()

    def test_validate_event_success(self):
        """Test successful validation of an event."""
        event_id = "1"
        date = "2023-12-01"
        time = "15:30"
        description = "Tech Conference"

        # Call the validate_event method
        result = self.validator.validate_event(event_id, date, time, description, self.mock_event_repo)

        # Verify that the method returns True for valid inputs
        self.assertTrue(result)

    def test_validate_event_invalid_date_format(self):
        """Test validation fails for an invalid date format."""
        event_id = "1"
        date = "01-12-2023"  # Invalid format
        time = "15:30"
        description = "Tech Conference"

        with self.assertRaises(ValueError) as context:
            self.validator.validate_event(event_id, date, time, description, self.mock_event_repo)

        self.assertEqual(str(context.exception), "Invalid date format. Please use YYYY-MM-DD.")

    def test_validate_event_invalid_time_format(self):
        """Test validation fails for an invalid time format."""
        event_id = "1"
        date = "2023-12-01"
        time = "3:30 PM"  # Invalid format
        description = "Tech Conference"

        with self.assertRaises(ValueError) as context:
            self.validator.validate_event(event_id, date, time, description, self.mock_event_repo)

        self.assertEqual(str(context.exception), "Invalid time format. Please use HH:MM.")

    def test_validate_event_empty_description(self):
        """Test validation fails for an empty description."""
        event_id = "1"
        date = "2023-12-01"
        time = "15:30"
        description = "   "  # Empty after stripping whitespace

        with self.assertRaises(ValueError) as context:
            self.validator.validate_event(event_id, date, time, description, self.mock_event_repo)

        self.assertEqual(str(context.exception), "Event description cannot be empty.")

class TestParticipantValidator(unittest.TestCase):

    def setUp(self):
        """Set up the ParticipantValidator and mock dependencies."""
        self.validator = ParticipantValidator()
        self.mock_participant_repo = MagicMock()
        self.mock_person_repo = MagicMock()
        self.mock_event_repo = MagicMock()

    def test_validate_participant_success(self):
        """Test successful validation of a participant."""
        person_id = "1"
        event_id = "10"

        # Mocking repositories
        self.mock_person_repo.find_person_by_id.return_value = MagicMock()  # Person exists
        self.mock_event_repo.find_event_by_id.return_value = MagicMock()   # Event exists
        self.mock_participant_repo.get_all_participants.return_value = []  # No participants yet

        # Call the validate_participant method
        result = self.validator.validate_participant(person_id, event_id,
                                                     self.mock_participant_repo,
                                                     self.mock_person_repo,
                                                     self.mock_event_repo)

        # Verify the method returns True for valid input
        self.assertTrue(result)

    def test_validate_participant_person_does_not_exist(self):
        """Test validation fails if the person does not exist."""
        person_id = "1"
        event_id = "10"

        # Mocking repositories
        self.mock_person_repo.find_person_by_id.side_effect = ValueError("Person does not exist")
        self.mock_event_repo.find_event_by_id.return_value = MagicMock()
        self.mock_participant_repo.get_all_participants.return_value = []

        with self.assertRaises(ValueError) as context:
            self.validator.validate_participant(person_id, event_id,
                                                self.mock_participant_repo,
                                                self.mock_person_repo,
                                                self.mock_event_repo)

        self.assertEqual(str(context.exception), "Person with ID 1 does not exist.")

    def test_validate_participant_event_does_not_exist(self):
        """Test validation fails if the event does not exist."""
        person_id = "1"
        event_id = "10"

        # Mocking repositories
        self.mock_person_repo.find_person_by_id.return_value = MagicMock()  # Person exists
        self.mock_event_repo.find_event_by_id.side_effect = ValueError("Event does not exist")
        self.mock_participant_repo.get_all_participants.return_value = []

        with self.assertRaises(ValueError) as context:
            self.validator.validate_participant(person_id, event_id,
                                                self.mock_participant_repo,
                                                self.mock_person_repo,
                                                self.mock_event_repo)

        self.assertEqual(str(context.exception), "Event with ID 10 does not exist.")

    def test_validate_participant_already_registered(self):
        """Test validation fails if the person is already registered for the event."""
        person_id = "1"
        event_id = "10"

        # Mocking repositories
        self.mock_person_repo.find_person_by_id.return_value = MagicMock()  # Person exists
        self.mock_event_repo.find_event_by_id.return_value = MagicMock()   # Event exists
        self.mock_participant_repo.get_all_participants.return_value = [
            MagicMock(get_person_id=lambda: "1", get_event_id=lambda: "10")  # Already registered
        ]

        with self.assertRaises(ValueError) as context:
            self.validator.validate_participant(person_id, event_id,
                                                self.mock_participant_repo,
                                                self.mock_person_repo,
                                                self.mock_event_repo)

        self.assertEqual(str(context.exception),
                         "Person with ID 1 is already registered for Event with ID 10.")

class TestPersonValidator(unittest.TestCase):
    def setUp(self):
        """Set up the PersonValidator and mock dependencies."""
        self.validator = PersonValidator()
        self.mock_person_repo = MagicMock()

    def test_validate_person_success(self):
        """Test successful validation of a person."""
        person_id = "1"
        name = "John Doe"
        address = "123 Main Street"

        # Mocking the repository (no specific calls needed for this test)
        self.mock_person_repo.find_person_by_id.return_value = MagicMock()  # Assume the person exists

        # Call the validate_person method
        result = self.validator.validate_person(person_id, name, address, self.mock_person_repo)

        # Verify the method returns True for valid input
        self.assertTrue(result)

    def test_validate_person_empty_name(self):
        """Test validation fails if the name is empty."""
        person_id = "1"
        name = ""
        address = "123 Main Street"

        # Mocking the repository (not used here)
        self.mock_person_repo.find_person_by_id.return_value = MagicMock()

        with self.assertRaises(ValueError) as context:
            self.validator.validate_person(person_id, name, address, self.mock_person_repo)

        self.assertEqual(str(context.exception), "Name and address cannot be empty.")

    def test_validate_person_empty_address(self):
        """Test validation fails if the address is empty."""
        person_id = "1"
        name = "John Doe"
        address = ""

        # Mocking the repository (not used here)
        self.mock_person_repo.find_person_by_id.return_value = MagicMock()

        with self.assertRaises(ValueError) as context:
            self.validator.validate_person(person_id, name, address, self.mock_person_repo)

        self.assertEqual(str(context.exception), "Name and address cannot be empty.")

    def test_validate_person_empty_name_and_address(self):
        """Test validation fails if both name and address are empty."""
        person_id = "1"
        name = ""
        address = ""

        # Mocking the repository (not used here)
        self.mock_person_repo.find_person_by_id.return_value = MagicMock()

        with self.assertRaises(ValueError) as context:
            self.validator.validate_person(person_id, name, address, self.mock_person_repo)

        self.assertEqual(str(context.exception), "Name and address cannot be empty.")