from utils.display_utils import print_persons_table, print_events_table, print_registrations_table

class RegistrationMenu:
    def __init__(self, registration_service):
        self._service = registration_service

    def _print_menu(self):
        print("\n--- Registration & Reports ---")
        print("1. Register Person to Event")
        print("2. Unregister Person from Event")
        print("3. Show Events for a Person (Sorted)")
        print("4. Show Persons for an Event (Sorted)")
        print("5. Report: Most Active Persons")
        print("6. Report: Top 20% Events by Attendance")
        print("B. Back")

    def handle_menu(self):
        while True:
            self._print_menu()
            option = input("Choose option: ").strip().lower()
            if option == "1": self._handle_register()
            elif option == "2": self._handle_unregister()
            elif option == "3": self._handle_person_events()
            elif option == "4": self._handle_event_participants()
            elif option == "5": self._handle_most_active()
            elif option == "6": self._handle_top_events()
            elif option in ["b", "q"]: break

    def _handle_register(self):
        try:
            p_id = input("Person ID: ")
            e_id = input("Event ID: ")
            self._service.register_to_event(p_id, e_id)
            print("Success: Registration complete.")
        except ValueError as e: print(f"Error: {e}")

    def _handle_unregister(self):
        try:
            p_id = input("Person ID: ")
            e_id = input("Event ID: ")
            self._service.unregister_from_event(p_id, e_id)
            print("Success: Person unregistered.")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_person_events(self):
        try:
            p_id = input("Person ID: ")
            events = self._service.get_person_events_sorted(p_id)
            if not events: print("No events found for this person.")
            else: print_events_table(events)
        except ValueError as e: print(f"Error: {e}")

    def _handle_event_participants(self):
        try:
            e_id = input("Enter Event ID: ")
            participants = self._service.get_event_participants_sorted(e_id)
            if not participants: print("No participants for this event.")
            else: print_persons_table(participants)
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_most_active(self):
        persons = self._service.get_most_active_persons()
        if not persons: print("No registration data available.")
        else:
            print("\n--- Most Active Persons ---")
            print_persons_table(persons)

    def _handle_top_events(self):
        events = self._service.get_top_events()
        if not events: print("No event data available.")
        else:
            print("--- Top 20% Events by Attendance ---")
            print_events_table(events)