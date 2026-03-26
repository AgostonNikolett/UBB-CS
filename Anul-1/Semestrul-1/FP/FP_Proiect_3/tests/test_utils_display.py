import unittest
from io import StringIO
import sys
from utils.display_utils import print_events_table, print_persons_table, print_registrations_table
from domain.event import Event
from domain.person import Person
from domain.participant import Participant

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output # Redirecționăm print-ul

    def tearDown(self):
        sys.stdout = sys.__stdout__ # Resetăm consola

    def test_print_events(self):
        e = Event("e1", "2024-05-20", "10:00", "Workshop Python")
        print_events_table([e])
        output = self.held_output.getvalue()
        self.assertIn("e1", output)
        self.assertIn("Workshop Python", output)
        self.assertIn("20-05-2024", output) # Verificăm formatarea datei

    def test_print_persons(self):
        p = Person("p1", "Andrei Pop", "Str. Eroilor")
        print_persons_table([p])
        output = self.held_output.getvalue()
        self.assertIn("p1", output)
        self.assertIn("Andrei Pop", output)

    def test_print_registrations(self):
        reg = Participant("p1", "e1")
        print_registrations_table([reg])
        output = self.held_output.getvalue()
        self.assertIn("p1", output)
        self.assertIn("e1", output)

    def test_print_event_invalid_date_format(self):
        from domain.event import Event
        e = Event("e1", "invalid-date", "10:00", "Desc")
        from utils.display_utils import print_events_table
        print_events_table([e])