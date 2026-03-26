import unittest
from utils.sortare import generic_sort
from domain.person import Person

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.data = [64, 34, 25, 12, 22, 11, 90]
        self.people = [
            Person("3", "Zaharia", "Cluj"),
            Person("1", "Abel", "Turda"),
            Person("2", "Mihai", "Dej")
        ]

    def test_quick_sort_basic(self):
        # Test Quick Sort implicit
        result = generic_sort(self.data, method='quick')
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])

    def test_gnome_sort_basic(self):
        # Test Gnome Sort
        result = generic_sort(self.data, method='gnome')
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])

    def test_sort_reversed(self):
        # Test reverse=True
        result = generic_sort(self.data, method='quick', reverse=True)
        self.assertEqual(result, [90, 64, 34, 25, 22, 12, 11])

    def test_sort_with_key(self):
        # Sortare obiecte Person după nume (alfabetic)
        result = generic_sort(self.people, method='quick', key=lambda p: p.get_name())
        self.assertEqual(result[0].get_name(), "Abel")
        self.assertEqual(result[-1].get_name(), "Zaharia")

    def test_sort_invalid_method(self):
        # Testare ramură de eroare pentru metodă inexistentă
        with self.assertRaises(ValueError):
            generic_sort(self.data, method='invalid_method')

    def test_gnome_sort_edge_cases(self):
        # Test listă goală și listă cu un element pentru Gnome Sort
        self.assertEqual(generic_sort([], method='gnome'), [])
        self.assertEqual(generic_sort([1], method='gnome'), [1])