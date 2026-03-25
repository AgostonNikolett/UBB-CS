class UI:
    def __init__(self, person_menu, event_menu, participant_menu):
        self.person_menu = person_menu
        self.event_menu = event_menu
        self.participant_menu = participant_menu

    def print_main_menu(self):
        print("\nMain Menu")
        print("1. Person Management")
        print("2. Event Management")
        print("3. Participant Management")
        print("Q. Quit")

    def start(self):
        while True:
            self.print_main_menu()
            option = input("Choose an option: ").lower()
            if option == "1":
                self.person_menu.handle_person_menu()
            elif option == "2":
                self.event_menu.handle_event_menu()
            elif option == "3":
                self.participant_menu.handle_participant_menu()
            elif option == "q":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
