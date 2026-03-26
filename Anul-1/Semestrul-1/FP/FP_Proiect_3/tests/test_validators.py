import unittest
from validators.person_validator import PersonValidator
from validators.event_validator import EventValidator
from validators.registration_validator import RegistrationValidator
from repository.base_repository import InMemoryRepository
from repository.participant_repository import ParticipantFileRepository
from domain.person import Person
from domain.event import Event
from domain.participant import Participant
import os


class TestValidators(unittest.TestCase):

    def setUp(self):
        self.person_val = PersonValidator()
        self.event_val = EventValidator()
        self.reg_val = RegistrationValidator()

        self.person_repo = InMemoryRepository()
        self.event_repo = InMemoryRepository()
        self.part_file = "test_val_reg.txt"
        self.part_repo = ParticipantFileRepository(self.part_file)

    def tearDown(self):
        if os.path.exists(self.part_file):
            os.remove(self.part_file)

    # --- Teste PersonValidator ---

    def test_person_validator_success(self):
        # Date corecte
        try:
            self.person_val.validate("p1", "John Doe", "Cluj-Napoca")
        except ValueError:
            self.fail("validate() raised ValueError unexpectedly!")

    def test_person_validator_failures(self):
        # Cazul: ID gol
        with self.assertRaises(ValueError) as cm:
            self.person_val.validate(" ", "John", "Cluj")
        self.assertIn("Person ID cannot be empty", str(cm.exception))

        # Cazul: Toate câmpurile goale (verifică concatenarea erorilor)
        with self.assertRaises(ValueError) as cm:
            self.person_val.validate("", "", "")
        self.assertTrue(len(str(cm.exception).split('\n')) >= 3)

    # --- Teste EventValidator ---

    def test_event_validator_success(self):
        # Date corecte
        try:
            self.event_val.validate("e1", "2024-12-01", "18:00", "Tech Conference")
        except ValueError:
            self.fail("validate() raised ValueError unexpectedly!")

    def test_event_validator_formats(self):
        # Format dată invalid
        with self.assertRaises(ValueError) as cm:
            self.event_val.validate("e1", "01-12-2024", "18:00", "Desc")
        self.assertIn("Invalid date format", str(cm.exception))

        # Format timp invalid
        with self.assertRaises(ValueError) as cm:
            self.event_val.validate("e1", "2024-12-01", "6 PM", "Desc")
        self.assertIn("Invalid time format", str(cm.exception))

        # Descriere goală
        with self.assertRaises(ValueError) as cm:
            self.event_val.validate("e1", "2024-12-01", "18:00", " ")
        self.assertIn("Event description cannot be empty", str(cm.exception))

    def test_event_validator_empty_id(self):
        v = EventValidator()

        # Test cu string gol
        with self.assertRaises(ValueError) as cm:
            v.validate("", "2024-01-01", "12:00", "Description")
        self.assertIn("Event ID cannot be empty", str(cm.exception))

        # Test cu string format doar din spații (pentru a verifica .strip())
        with self.assertRaises(ValueError) as cm:
            v.validate("   ", "2024-01-01", "12:00", "Description")
        self.assertIn("Event ID cannot be empty", str(cm.exception))

    # --- Teste RegistrationValidator ---

    def test_registration_validator_logic(self):
        # Setup: Adăugăm o persoană și un eveniment
        person = Person("p1", "John", "Cluj")
        event = Event("e1", "2024-12-01", "10:00", "Meeting")
        self.person_repo.store("p1", person)
        self.event_repo.store("e1", event)

        # 1. Succes: Înregistrare validă
        try:
            self.reg_val.validate("p1", "e1", self.part_repo, self.person_repo, self.event_repo)
        except ValueError:
            self.fail("Registration validation failed unexpectedly")

        # 2. Eroare: Persoană inexistentă
        with self.assertRaises(ValueError) as cm:
            self.reg_val.validate("p99", "e1", self.part_repo, self.person_repo, self.event_repo)
        self.assertIn("Person with ID p99 does not exist", str(cm.exception))

        # 3. Eroare: Eveniment inexistent
        with self.assertRaises(ValueError) as cm:
            self.reg_val.validate("p1", "e99", self.part_repo, self.person_repo, self.event_repo)
        self.assertIn("Event with ID e99 does not exist", str(cm.exception))

        # 4. Eroare: Înregistrare duplicat
        self.part_repo.add_registration(Participant("p1", "e1"))
        with self.assertRaises(ValueError) as cm:
            self.reg_val.validate("p1", "e1", self.part_repo, self.person_repo, self.event_repo)
        self.assertIn("Conflict: Person p1 is already registered", str(cm.exception))