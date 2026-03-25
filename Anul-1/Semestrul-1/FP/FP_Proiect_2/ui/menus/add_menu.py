from repository.package_operations import add_package_to_list, update_package_service
from utils.io_utils import read_date, read_number


def print_add_menu():
    print("\n--- Addition & Modification Menu ---")
    print("1. Add a new travel package")
    print("2. Modify an existing package")
    print("B. Back to main menu")


def ui_add_package(packages: list, undo_list: list):
    """Reads data from console and calls the service to add a package."""
    arrival = read_date("%d %m %Y", "Invalid date format.")
    departure = read_date("%d %m %Y", "Invalid date format.")
    location = input("Location: ").strip().lower()
    price = read_number("Price: ", float, "Price must be a positive number.")

    try:
        add_package_to_list(packages, arrival, departure, location, price, undo_list)
        print(">>> Package added successfully.")
    except Exception as e:
        print(f"[ERROR] {e}")


def ui_modify_package(packages: list, undo_list: list):
    """Reads ID and new data to update an existing package."""
    pkg_id = read_number("Enter Package ID to modify: ", int, "ID must be an integer.")
    arrival = read_date("%d %m %Y", "Invalid date format.")
    departure = read_date("%d %m %Y", "Invalid date format.")
    location = input("New Location: ").strip().lower()
    price = read_number("New Price: ", float, "Price must be a positive number.")

    try:
        update_package_service(packages, pkg_id, arrival, departure, location, price, undo_list)
        print(">>> Package modified successfully.")
    except Exception as e:
        print(f"[ERROR] {e}")


def package_addition_menu(packages: list, undo_list: list):
    while True:
        print_add_menu()
        option = input("Select option: ").strip().lower()
        if option == '1':
            ui_add_package(packages, undo_list)
        elif option == '2':
            ui_modify_package(packages, undo_list)
        elif option == 'b':
            break