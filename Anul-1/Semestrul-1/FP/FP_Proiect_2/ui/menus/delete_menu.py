from repository.package_operations import delete_packages_by_destination, delete_packages_by_price
from utils.io_utils import read_number

def package_deletion_menu(packages: list, undo_list: list):
    while True:
        print("\n--- Deletion Menu ---")
        print("1. Delete packages by destination")
        print("2. Delete packages by price (greater than X)")
        print("B. Back")

        option = input("Select option: ").strip().lower()
        if option == '1':
            dest = input("Destination to remove: ").strip().lower()
            delete_packages_by_destination(packages, dest, undo_list)
            print(f">>> All packages to {dest} have been removed.")
        elif option == '2':
            limit = read_number("Price limit: ", float, "Must be a number.")
            delete_packages_by_price(packages, limit, undo_list)
            print(f">>> Packages more expensive than {limit} removed.")
        elif option == 'b':
            break