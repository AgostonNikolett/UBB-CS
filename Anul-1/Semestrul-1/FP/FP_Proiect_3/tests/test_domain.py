import unittest
from domain.person import Person
from domain.event import Event
from domain.participant import Participant

class TestEvent(unittest.TestCase):

    def setUp(self):
        # Set up a sample event for use in multiple tests
        self.event = Event("101", "2024-12-25", "18:00", "Christmas Party")

    def test_constructor(self):
        self.assertEqual(self.event.get_event_id(), "101")
        self.assertEqual(self.event.get_date(), "2024-12-25")
        self.assertEqual(self.event.get_time(), "18:00")
        self.assertEqual(self.event.get_description(), "Christmas Party")
        self.assertEqual(self.event.get_participant_count(), 0)

    def test_getters_and_setters(self):
        # Test setters and getters for date
        self.event.set_date("2024-12-31")
        self.assertEqual(self.event.get_date(), "2024-12-31")

        # Test setters and getters for time
        self.event.set_time("20:00")
        self.assertEqual(self.event.get_time(), "20:00")

        # Test setters and getters for description
        self.event.set_description("New Year's Eve Party")
        self.assertEqual(self.event.get_description(), "New Year's Eve Party")

    def test_participant_count(self):
        # Test incrementing participant count
        self.event.increment_participant_count()
        self.assertEqual(self.event.get_participant_count(), 1)

        # Test decrementing participant count
        self.event.decrement_participant_count()
        self.assertEqual(self.event.get_participant_count(), 0)

        # Ensure participant count does not go negative
        self.event.decrement_participant_count()
        self.assertEqual(self.event.get_participant_count(), 0)

    def test_to_string(self):
        # Test the to_string method
        expected_string = "101,2024-12-25,18:00,Christmas Party"
        self.assertEqual(self.event.to_string(), expected_string)

    def test_from_string(self):
        # Test the from_string static method
        event_string = "102,2024-12-31,20:00,New Year's Eve Party"
        event = Event.from_string(event_string)
        self.assertEqual(event.get_event_id(), "102")
        self.assertEqual(event.get_date(), "2024-12-31")
        self.assertEqual(event.get_time(), "20:00")
        self.assertEqual(event.get_description(), "New Year's Eve Party")
        self.assertEqual(event.get_participant_count(), 0)

    def test_from_string_invalid(self):
        # Test invalid string format
        with self.assertRaises(ValueError):
            Event.from_string("Invalid,string")

    def test_str_method(self):
        # Test the __str__ method
        expected_output = ("Event ID: 101, Time: 18:00, Date: 2024-12-25, "
                           "Description: Christmas Party, Participants: 0")
        self.assertEqual(str(self.event), expected_output)

    def tearDown(self):
        # Clean up resources if needed
        pass

class TestParticipant(unittest.TestCase):

    def setUp(self):
        # Set up a sample participant for use in multiple tests
        self.participant = Participant("1", "101")

    def test_constructor(self):
        # Test the constructor initializes attributes correctly
        self.assertEqual(self.participant.get_person_id(), "1")
        self.assertEqual(self.participant.get_event_id(), "101")

    def test_getters(self):
        # Test getter methods
        self.assertEqual(self.participant.get_person_id(), "1")
        self.assertEqual(self.participant.get_event_id(), "101")

    def test_to_string(self):
        # Test the to_string method
        expected_string = "1,101"
        self.assertEqual(self.participant.to_string(), expected_string)

    def test_from_string(self):
        # Test the from_string static method
        participant_string = "2,102"
        participant = Participant.from_string(participant_string)
        self.assertEqual(participant.get_person_id(), "2")
        self.assertEqual(participant.get_event_id(), "102")

    def test_from_string_invalid(self):
        # Test invalid string format
        with self.assertRaises(ValueError):
            Participant.from_string("Invalid,string,format")

    def test_str_method(self):
        # Test the __str__ method
        expected_output = "Person ID: 1, Event ID: 101"
        self.assertEqual(str(self.participant), expected_output)

    def tearDown(self):
        # Clean up resources if needed
        pass

class TestPerson(unittest.TestCase):

    def setUp(self):
        # Set up a sample person for use in multiple tests
        self.person = Person("1", "John Doe", "123 Main St")

    def test_constructor(self):
        # Test the constructor initializes attributes correctly
        self.assertEqual(self.person.get_person_id(), "1")
        self.assertEqual(self.person.get_name(), "John Doe")
        self.assertEqual(self.person.get_address(), "123 Main St")

    def test_getters(self):
        # Test getter methods
        self.assertEqual(self.person.get_person_id(), "1")
        self.assertEqual(self.person.get_name(), "John Doe")
        self.assertEqual(self.person.get_address(), "123 Main St")

    def test_setters(self):
        # Test setter methods
        self.person.set_name("Jane Doe")
        self.person.set_address("456 Oak St")
        self.assertEqual(self.person.get_name(), "Jane Doe")
        self.assertEqual(self.person.get_address(), "456 Oak St")

    def test_to_string(self):
        # Test the to_string method
        expected_string = "1,John Doe,123 Main St"
        self.assertEqual(self.person.to_string(), expected_string)

    def test_from_string(self):
        # Test the from_string static method
        person_string = "2,Jane Smith,789 Elm St"
        person = Person.from_string(person_string)
        self.assertEqual(person.get_person_id(), "2")
        self.assertEqual(person.get_name(), "Jane Smith")
        self.assertEqual(person.get_address(), "789 Elm St")

    def test_from_string_invalid(self):
        # Test invalid string format
        with self.assertRaises(ValueError):
            Person.from_string("Invalid,string")

    def test_str_method(self):
        # Test the __str__ method
        expected_output = "Person ID: 1, Name: John Doe, Address: 123 Main St"
        self.assertEqual(str(self.person), expected_output)

    def tearDown(self):
        # Clean up resources if needed
        pass