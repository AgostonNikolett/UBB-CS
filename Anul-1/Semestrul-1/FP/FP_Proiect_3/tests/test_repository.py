import unittest
import os
from repository.base_repository import InMemoryRepository
from repository.person_repository import PersonFileRepository
from repository.event_repository import EventFileRepository
from repository.participant_repository import ParticipantFileRepository
from domain.person import Person
from domain.event import Event
from domain.participant import Participant

class TestRepository(unittest.TestCase):

    def setUp(self):
        """Prepare filenames for file-based repository testing."""
        self.person_file = "test_persons.txt"
        self.event_file = "test_events.txt"
        self.part_file = "test_participants.txt"
        # Ensure clean state before each test
        self._cleanup_files()

    def tearDown(self):
        """Clean up temporary files after each test."""
        self._cleanup_files()

    def _cleanup_files(self):
        for f in [self.person_file, self.event_file, self.part_file]:
            if os.path.exists(f):
                os.remove(f)

    # --- Tests for InMemoryRepository (Base) ---

    def test_in_memory_operations(self):
        """Tests basic CRUD operations in memory."""
        repo = InMemoryRepository()

        # Test Store
        repo.store("1", "item1")
        self.assertEqual(len(repo.get_all()), 1)
        self.assertEqual(repo.find_by_id("1"), "item1")

        # Test Duplicate ID error
        with self.assertRaises(ValueError):
            repo.store("1", "item2")

        # Test Find Non-existent
        with self.assertRaises(ValueError):
            repo.find_by_id("99")

        # Test Remove
        removed = repo.remove("1")
        self.assertEqual(removed, "item1")
        self.assertEqual(len(repo.get_all()), 0)

        # Test Remove Non-existent
        with self.assertRaises(ValueError):
            repo.remove("99")

    # --- Tests for PersonFileRepository ---

    def test_person_file_repository(self):
        """Tests persistence for Person entities."""
        repo = PersonFileRepository(self.person_file)
        p = Person("p1", "John", "Cluj")

        # Add and check file existence
        repo.add(p)
        self.assertTrue(os.path.exists(self.person_file))

        # Update and check
        repo.update("p1", "John Doe", "Bucuresti")
        updated_p = repo.find_by_id("p1")
        self.assertEqual(updated_p.get_name(), "John Doe")

        # Reload from file to test persistence [cite: 1, 3]
        new_repo = PersonFileRepository(self.person_file)
        self.assertEqual(len(new_repo.get_all()), 1)
        self.assertEqual(new_repo.find_by_id("p1").get_name(), "John Doe")

        # Delete
        repo.delete("p1")
        self.assertEqual(len(repo.get_all()), 0)

    # --- Tests for EventFileRepository ---

    def test_event_file_repository(self):
        """Tests persistence for Event entities."""
        repo = EventFileRepository(self.event_file)
        e = Event("e1", "2024-10-10", "10:00", "Meeting")

        repo.add(e)
        repo.update("e1", "2024-11-11", "11:00", "Workshop")

        # Reload to verify [cite: 1]
        new_repo = EventFileRepository(self.event_file)
        restored = new_repo.find_by_id("e1")
        self.assertEqual(restored.get_description(), "Workshop")

        repo.delete("e1")
        self.assertEqual(len(repo.get_all()), 0)

    # --- Tests for ParticipantFileRepository ---

    def test_participant_file_repository(self):
        """Tests the special list-based participant persistence."""
        repo = ParticipantFileRepository(self.part_file)
        part = Participant("p1", "e1")

        # Add registration
        repo.add_registration(part)
        self.assertEqual(len(repo.get_all()), 1)

        # Test Duplicate Registration [cite: 5]
        with self.assertRaises(ValueError):
            repo.add_registration(Participant("p1", "e1"))

        # Reload to verify [cite: 2]
        new_repo = ParticipantFileRepository(self.part_file)
        self.assertEqual(len(new_repo.get_all()), 1)

        # Remove registration
        repo.remove_registration("p1", "e1")
        self.assertEqual(len(repo.get_all()), 0)

        # Remove Non-existent registration [cite: 5]
        with self.assertRaises(ValueError):
            repo.remove_registration("p1", "e1")