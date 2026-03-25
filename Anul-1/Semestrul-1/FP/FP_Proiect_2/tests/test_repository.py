import unittest
from datetime import datetime

from domain.travel_package import get_id
from repository.package_operations import (
    add_package_to_list, get_package_by_id, update_package_service,
    delete_package_by_id, delete_packages_by_destination, delete_packages_by_price
)


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.packages = []
        self.undo_list = []
        self.d1 = datetime(2024, 1, 1)
        self.d2 = datetime(2024, 1, 5)

    def test_add_and_get(self):
        add_package_to_list(self.packages, self.d1, self.d2, "rome", 100, self.undo_list)
        self.assertEqual(len(self.packages), 1)
        self.assertEqual(get_package_by_id(self.packages, 1)[3], "rome")

        with self.assertRaises(Exception):
            get_package_by_id(self.packages, 99)

    def test_add_package_validation_failure(self):
        packages = []
        bad_arrival = datetime(2024, 10, 10)
        bad_departure = datetime(2024, 10, 1)

        with self.assertRaises(Exception):
            add_package_to_list(packages, bad_arrival, bad_departure, "invalid", 100)

        self.assertEqual(len(packages), 0)

    def test_delete_operations(self):
        add_package_to_list(self.packages, self.d1, self.d2, "rome", 100)
        add_package_to_list(self.packages, self.d1, self.d2, "paris", 200)

        # Delete by ID
        delete_package_by_id(self.packages, 1)
        self.assertEqual(len(self.packages), 1)
        with self.assertRaises(Exception):
            delete_package_by_id(self.packages, 99)

        # Delete by destination
        delete_packages_by_destination(self.packages, "paris")
        self.assertEqual(len(self.packages), 0)

        # Delete by price
        add_package_to_list(self.packages, self.d1, self.d2, "london", 500)
        delete_packages_by_price(self.packages, 100)  # Threshold 100, London is 500
        self.assertEqual(len(self.packages), 0)

    def test_update(self):
        add_package_to_list(self.packages, self.d1, self.d2, "rome", 100)
        update_package_service(self.packages, 1, self.d1, self.d2, "milan", 150)
        self.assertEqual(self.packages[0][3], "milan")