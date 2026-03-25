import unittest
from datetime import datetime
from service.package_service import (
    search_packages_in_interval, get_average_price_by_destination,
    filter_by_price_and_location, perform_undo
)
from repository.package_operations import add_package_to_list
from utils.sort_utils import quick_sort_by_price


class TestService(unittest.TestCase):
    def setUp(self):
        self.packages = []
        self.undo_list = []
        self.d1 = datetime(2024, 1, 1)
        self.d2 = datetime(2024, 1, 10)

    def test_search_and_stats(self):
        add_package_to_list(self.packages, datetime(2024, 1, 2), datetime(2024, 1, 5), "rome", 100)
        add_package_to_list(self.packages, datetime(2024, 1, 15), datetime(2024, 1, 20), "rome", 200)

        # Search in interval
        results = search_packages_in_interval(self.packages, datetime(2024, 1, 1), datetime(2024, 1, 10))
        self.assertEqual(len(results), 1)

        # Average price
        avg = get_average_price_by_destination(self.packages, "rome")
        self.assertEqual(avg, 150.0)
        self.assertEqual(get_average_price_by_destination(self.packages, "unknown"), 0.0)

    def test_filter_and_undo(self):
        add_package_to_list(self.packages, self.d1, self.d2, "rome", 100, self.undo_list)
        filter_by_price_and_location(self.packages, "paris", 50, self.undo_list)
        # Rome != Paris AND 100 > 50 -> Should be deleted
        self.assertEqual(len(self.packages), 0)

        # Undo
        self.packages = perform_undo(self.packages, self.undo_list)
        self.assertEqual(len(self.packages), 1)

        with self.assertRaises(Exception):
            perform_undo(self.packages, [])

    def test_sorting(self):
        add_package_to_list(self.packages, self.d1, self.d2, "A", 300)
        add_package_to_list(self.packages, self.d1, self.d2, "B", 100)
        add_package_to_list(self.packages, self.d1, self.d2, "C", 200)

        quick_sort_by_price(self.packages, 0, len(self.packages) - 1)
        self.assertEqual(self.packages[0][4], 100)
        self.assertEqual(self.packages[2][4], 300)