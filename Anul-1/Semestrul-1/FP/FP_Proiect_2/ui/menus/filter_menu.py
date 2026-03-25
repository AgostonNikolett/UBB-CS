from service.package_service import filter_by_price_and_location
from utils.io_utils import read_number

def package_filtering_menu(packages: list, undo_list: list):
    while True:
        print("\n--- Filtering Menu ---")
        print("1. Keep only specific destination OR lower than price")
        print("B. Back")

        option = input("Select option: ").strip().lower()
        if option == '1':
            dest = input("Target destination: ").strip().lower()
            price = read_number("Price threshold: ", float, "Invalid price.")
            removed = filter_by_price_and_location(packages, dest, price, undo_list)
            print(f">>> Filter applied. {removed} packages were removed.")
        elif option == 'b':
            break