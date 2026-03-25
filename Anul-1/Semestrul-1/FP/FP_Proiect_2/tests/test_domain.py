import unittest
from datetime import datetime
from domain.travel_package import create_package, get_id, get_arrival_date, get_departure_date, get_location, get_price, \
    modify_package
from domain.validators import validate_package


class TestDomain(unittest.TestCase):
    def test_package_entity(self):
        arrival = datetime(2024, 5, 1)
        departure = datetime(2024, 5, 10)
        p = create_package(1, arrival, departure, "paris", 500.0)

        self.assertEqual(get_id(p), 1)
        self.assertEqual(get_arrival_date(p), arrival)
        self.assertEqual(get_departure_date(p), departure)
        self.assertEqual(get_location(p), "paris")
        self.assertEqual(get_price(p), 500.0)

        modify_package(p, arrival, departure, "london", 600.0)
        self.assertEqual(get_location(p), "london")
        self.assertEqual(get_price(p), 600.0)

    def test_validator(self):
        arrival = datetime(2024, 5, 1)
        departure = datetime(2024, 5, 10)
        p_ok = create_package(1, arrival, departure, "paris", 500.0)

        # Test valid
        self.assertTrue(validate_package(p_ok, []))

        # Test duplicate ID
        with self.assertRaises(Exception) as ex:
            validate_package(p_ok, [p_ok])
        self.assertIn("ID already exists", str(ex.exception))

        # Test invalid dates
        p_bad_date = create_package(2, departure, arrival, "paris", 500.0)
        with self.assertRaises(Exception) as ex:
            validate_package(p_bad_date, [])
        self.assertIn("Departure date cannot be earlier", str(ex.exception))