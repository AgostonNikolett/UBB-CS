import unittest
from domain.person import Person
from domain.event import Event
from domain.participant import Participant

class TestDomain(unittest.TestCase):

    # --- Tests for Person Entity ---

    def test_create_person(self):
        """Tests the initialization and getters of Person."""
        p = Person("p1", "Alice", "Str. Florilor 10")
        self.assertEqual(p.get_id(), "p1")
        self.assertEqual(p.get_name(), "Alice")
        self.assertEqual(p.get_address(), "Str. Florilor 10")

    def test_person_setters(self):
        """Tests the setter methods of Person."""
        p = Person("p1", "Alice", "Str. Florilor 10")
        p.set_name("Alice Brown")
        p.set_address("Str. Primăverii 5")
        self.assertEqual(p.get_name(), "Alice Brown")
        self.assertEqual(p.get_address(), "Str. Primăverii 5")

    def test_person_serialization(self):
        """Tests to_file_string, from_file_string and __str__ for Person."""
        p = Person("p1", "Alice", "Cluj")
        expected_str = "p1,Alice,Cluj"
        self.assertEqual(p.to_file_string(), expected_str)

        # Test valid restoration
        p_restored = Person.from_file_string(expected_str)
        self.assertEqual(p_restored.get_id(), "p1")
        self.assertEqual(p_restored.get_name(), "Alice")

        # Test invalid restoration (ValueError)
        with self.assertRaises(ValueError):
            Person.from_file_string("invalid,data")

        # Test __str__
        self.assertIn("Alice", str(p))
        self.assertIn("p1", str(p))

    # --- Tests for Event Entity ---

    def test_create_event(self):
        """Tests the initialization and getters of Event."""
        e = Event("e1", "2024-12-01", "18:00", "Party")
        self.assertEqual(e.get_id(), "e1")
        self.assertEqual(e.get_date(), "2024-12-01")
        self.assertEqual(e.get_time(), "18:00")
        self.assertEqual(e.get_description(), "Party")
        self.assertEqual(e.get_participant_count(), 0)

    def test_event_setters(self):
        """Tests the setter methods of Event."""
        e = Event("e1", "2024-12-01", "18:00", "Party")
        e.set_date("2024-12-25")
        e.set_time("20:00")
        e.set_description("Christmas Dinner")
        self.assertEqual(e.get_date(), "2024-12-25")
        self.assertEqual(e.get_description(), "Christmas Dinner")

    def test_event_participant_counter(self):
        """Tests incrementing and decrementing the participant counter."""
        e = Event("e1", "2024-12-01", "18:00", "Party")
        e.update_participant_count(5)
        self.assertEqual(e.get_participant_count(), 5)

        e.update_participant_count(-2)
        self.assertEqual(e.get_participant_count(), 3)

        # Test floor at 0 (cannot have negative participants)
        e.update_participant_count(-10)
        self.assertEqual(e.get_participant_count(), 0)

    def test_event_serialization(self):
        """Tests serialization and string representation for Event."""
        e = Event("e1", "2024-05-10", "12:00", "Workshop")
        csv_line = "e1,2024-05-10,12:00,Workshop"
        self.assertEqual(e.to_file_string(), csv_line)

        e_restored = Event.from_file_string(csv_line)
        self.assertEqual(e_restored.get_description(), "Workshop")

        with self.assertRaises(ValueError):
            Event.from_file_string("not,enough,parts")

        self.assertIn("Workshop", str(e))

    # --- Tests for Participant (Registration) Entity ---

    def test_participant_logic(self):
        """Tests the Participant link entity."""
        part = Participant("p1", "e1")
        self.assertEqual(part.get_person_id(), "p1")
        self.assertEqual(part.get_event_id(), "e1")

        csv_line = "p1,e1"
        self.assertEqual(part.to_file_string(), csv_line)

        part_restored = Participant.from_file_string(csv_line)
        self.assertEqual(part_restored.get_person_id(), "p1")

        with self.assertRaises(ValueError):
            Participant.from_file_string("only_one_part")

        self.assertIn("p1", str(part))
        self.assertIn("e1", str(part))