class UI:
    def __init__(self, person_menu, event_menu, reg_menu):
        self._person_menu = person_menu
        self._event_menu = event_menu
        self._reg_menu = reg_menu

    def start(self):
        while True:
            print("\n=== EVENT MANAGEMENT SYSTEM ===")
            print("1. Person Management")
            print("2. Event Management")
            print("3. Registrations & Reports")
            print("Q. Exit")

            choice = input("Select category: ").strip().lower()
            if choice == "1":
                self._person_menu.handle_menu()
            elif choice == "2":
                self._event_menu.handle_menu()
            elif choice == "3":
                self._reg_menu.handle_menu()
            elif choice == "q":
                print("Exiting application...")
                break
            else:
                print("Invalid category choice.")