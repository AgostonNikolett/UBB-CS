from ui.console import main_menu
from ui.batch_mode import batch_mode
from utils.io_utils import clear_screen


def start():
    """
    Main entry point for the Travel Agency Manager application.
    Initializes the package list and the undo stack.
    """
    packages = []
    undo_list = []

    clear_screen()
    print("Welcome to Travel Agency Manager v2.0")
    print("Choose operation mode:")
    print("1. Standard Menu Mode")
    print("2. Batch/Command Mode")

    choice = input("Choice: ").strip()

    if choice == '1':
        main_menu(packages, undo_list)
    elif choice == '2':
        batch_mode(packages, undo_list)
    else:
        print("Invalid choice. Defaulting to Menu Mode...")
        main_menu(packages, undo_list)


if __name__ == "__main__":
    start()