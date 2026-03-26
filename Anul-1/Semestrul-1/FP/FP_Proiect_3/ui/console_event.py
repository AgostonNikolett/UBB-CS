from utils.display_utils import print_events_table

class EventMenu:
    def __init__(self, event_service):
        self._service = event_service

    def _print_menu(self):
        print("\n--- Event Management ---")
        print("1. Add Event")
        print("2. List All Events")
        print("3. Modify Event")
        print("4. Delete Event")
        print("5. Find Event by ID")
        print("6. Generate Random Events")
        print("B. Back to Main Menu")

    def handle_menu(self):
        while True:
            self._print_menu()
            option = input("Choose option: ").strip().lower()
            if option == "1": self._handle_add()
            elif option == "2": self._handle_list()
            elif option == "3": self._handle_update()
            elif option == "4": self._handle_delete()
            elif option == "5": self._handle_find()
            elif option == "6": self._handle_random()
            elif option in ["b", "q"]: break
            else: print("Invalid option.")

    def _handle_add(self):
        try:
            e_id = input("Event ID: ")
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time (HH:MM): ")
            desc = input("Description: ")
            self._service.add_event(e_id, date, time, desc)
            print("Success: Event added.")
        except ValueError as e: print(f"Error: {e}")

    def _handle_list(self):
        events = self._service.get_all_sorted_by_id()
        if not events: print("No events found.")
        else: print_events_table(events)

    def _handle_update(self):
        try:
            e_id = input("Enter Event ID to modify: ")
            date = input("New Date (YYYY-MM-DD): ")
            time = input("New Time (HH:MM): ")
            desc = input("New Description: ")
            self._service.update_event(e_id, date, time, desc)
            print("Success: Event updated.")
        except ValueError as e: print(f"Error: {e}")

    def _handle_delete(self):
        try:
            e_id = input("Enter Event ID to delete: ")
            self._service.remove_event(e_id)
            print("Success: Event removed.")
        except ValueError as e: print(f"Error: {e}")

    def _handle_find(self):
        try:
            e_id = input("Enter Event ID to find: ")
            event = self._service.find_event_by_id(e_id)
            print(f"Found: {event}")
        except ValueError as e: print(f"Error: {e}")

    def _handle_random(self):
        try:
            count = int(input("How many events? "))
            self._service.generate_random_events(count)
            print(f"Generated {count} events.")
        except ValueError as e: print(f"Error: {e}")