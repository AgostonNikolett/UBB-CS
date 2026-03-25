import unittest
from datetime import datetime

from domain.travel_package import create_package
from utils.display_utils import display_all_packages

class TestUtils(unittest.TestCase):
    def test_display_empty(self):
        # We just call it to ensure it covers the 'if not packages' branch
        display_all_packages([])
        display_all_packages(None)

    def test_display_with_actual_data(self):
        p1 = create_package(1, datetime(2024, 1, 1), datetime(2024, 1, 10), "london", 500.0)
        p2 = create_package(2, datetime(2024, 2, 1), datetime(2024, 2, 10), "paris", 600.0)
        packages = [p1, p2]

        display_all_packages(packages)

        display_all_packages("not a list")