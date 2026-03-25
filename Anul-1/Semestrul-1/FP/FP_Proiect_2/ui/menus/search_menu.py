from service.package_service import search_packages_in_interval
from utils.display_utils import display_all_packages
from utils.io_utils import read_date


def package_search_menu(packages: list):
    while True:
        print("\n--- Search Menu ---")
        print("1. Search packages within a time interval")
        print("2. Search by destination and max price")
        print("B. Back")

        option = input("Select option: ").strip().lower()
        if option == '1':
            start = read_date("%d %m %Y", "Invalid date.")
            end = read_date("%d %m %Y", "Invalid date.")
            results = search_packages_in_interval(packages, start, end)
            display_all_packages(results)
        elif option == 'b':
            break