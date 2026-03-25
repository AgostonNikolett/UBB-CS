from ui.menus.add_menu import package_addition_menu
from ui.menus.search_menu import package_search_menu
from ui.menus.filter_menu import package_filtering_menu
from ui.menus.report_menu import package_reports_menu
from ui.menus.delete_menu import package_deletion_menu
from service.package_service import perform_undo
from utils.io_utils import clear_screen
from utils.display_utils import display_all_packages


def print_main_menu():
    """
    Displays the primary navigation menu.
    """
    print("\n=== TRAVEL PACKAGE MANAGEMENT SYSTEM ===")
    print("1. Add / Modify Packages")
    print("2. Delete Packages")
    print("3. Search Packages")
    print("4. Package Reports")
    print("5. Filter Packages")
    print("6. Undo Last Operation")
    print("A. Display All Packages")
    print("Q. Exit")
    print("========================================")


def main_menu(packages: list, undo_list: list):
    """
    Main execution loop for the CLI.
    :param packages: The shared list of travel packages.
    :param undo_list: The stack for undo operations.
    """
    clear_screen()
    while True:
        print_main_menu()
        cmd = input("Select an option: ").strip().lower()

        if cmd == '1':
            clear_screen()
            package_addition_menu(packages, undo_list)
        elif cmd == '2':
            clear_screen()
            package_deletion_menu(packages, undo_list)
        elif cmd == '3':
            clear_screen()
            package_search_menu(packages)
        elif cmd == '4':
            clear_screen()
            package_reports_menu(packages)
        elif cmd == '5':
            clear_screen()
            package_filtering_menu(packages, undo_list)
        elif cmd == '6':
            try:
                packages = perform_undo(packages, undo_list)
                clear_screen()
                print("Undo successful!")
                display_all_packages(packages)
            except Exception as e:
                print(f"[ERROR] {e}")
        elif cmd == 'a':
            clear_screen()
            display_all_packages(packages)
        elif cmd == 'q':
            print("Exiting application...")
            break
        else:
            print("Invalid command! Please try again.")