import datetime
from repository.package_operations import add_package_to_list, delete_package_by_id
from service.package_service import perform_undo, filter_by_price_and_location
from utils.display_utils import display_all_packages


def batch_mode(packages: list, undo_list: list):
    """
    Handles multiple commands entered as a single line, separated by ';'.
    Supported syntax:
    - add dd.mm.yyyy/dd.mm.yyyy location price
    - delete id
    - filter location price
    - undo
    - show
    """
    print("\n=== BATCH MODE ENABLED ===")
    print("Example: add 01.05.2024/10.05.2024 rome 1200; show; undo")

    while True:
        cmd_input = input("batch-shell> ").strip().lower()
        if cmd_input == 'q':
            break

        commands = cmd_input.split(";")

        for full_cmd in commands:
            parts = full_cmd.strip().split(" ")
            action = parts[0]

            try:
                if action == "add":
                    # Syntax: add 01.01.2024/10.01.2024 paris 500
                    dates = parts[1].split("/")
                    start = datetime.datetime.strptime(dates[0], "%d.%m.%Y")
                    end = datetime.datetime.strptime(dates[1], "%d.%m.%Y")
                    location = parts[2]
                    price = float(parts[3])
                    add_package_to_list(packages, start, end, location, price, undo_list)
                    print(f"Success: Added package to {location.capitalize()}")

                elif action == "delete":
                    # Syntax: delete 5
                    pkg_id = int(parts[1])
                    delete_package_by_id(packages, pkg_id)
                    print(f"Success: Package {pkg_id} deleted.")

                elif action == "filter":
                    # Syntax: filter london 1000
                    location = parts[1]
                    price = float(parts[2])
                    removed = filter_by_price_and_location(packages, location, price, undo_list)
                    print(f"Success: Filtered {removed} packages.")

                elif action == "undo":
                    packages = perform_undo(packages, undo_list)
                    print("Success: Undo performed.")

                elif action == "show":
                    display_all_packages(packages)

                else:
                    print(f"Unknown command: {action}")

            except (IndexError, ValueError, Exception) as e:
                print(f"Error executing '{action}': {e}")