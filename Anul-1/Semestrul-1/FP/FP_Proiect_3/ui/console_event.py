from utils.prints import print_events_table

class EventMenu:
    def __init__(self, event_service):
        self.event_service = event_service

    def print_event_menu(self):
        print("\nEvent Management")
        print("1.  Add Event")
        print("2.  List Events")
        print("3.  Modify Event")
        print("4.  Delete Event")
        print("5.  Find Event")
        print("RE. Add Random Events")
        print("Q.  Back to Main Menu")

    def handle_event_menu(self):
        while True:
            self.print_event_menu()
            option = input("Choose an option: ").lower()
            if option == "1":
                self.handle_add_event()
            elif option == "2":
                self.handle_list_events()
            elif option == "3":
                self.handle_update_event()
            elif option == "4":
                self.handle_delete_event()
            elif option == "5":
                self.handle_find_event()
            elif option == "re":
                self.handle_add_random_events()
            elif option == "q":
                break
            else:
                print("Invalid option. Please try again.")
    

    def handle_add_event(self):
        try:
            event_id = input("Enter Event ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            time = input("Enter Time (HH:MM): ")
            description = input("Enter Description: ")
            self.event_service.add_event(event_id, date, time, description)
            print("Event added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_list_events(self):
        events = self.event_service.list_all_events()
        if not events:
            print("No events found.")
        else:
            print_events_table(events)

    def handle_update_event(self):
        try:
            event_id = input("Enter Event ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            time = input("Enter Time (HH:MM): ")
            description = input("Enter Description: ")
            self.event_service.update_event(event_id, date, time, description)
            print("Event updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_delete_event(self):
        try:
            event_id = input("Enter Event ID to delete: ")
            self.event_service.remove_event(event_id)
            print("Event deleted successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_find_event(self):
        try:
            event_id = input("Enter Event ID to finde: ")
            event = self.event_service.find_event_by_id(event_id)
            print(event)
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_add_random_events(self):
        try:
            number_of_events = int(input("Number of events to add:"))
            self.event_service.add_random_events(number_of_events)
            print("Events added successfully.")
        except ValueError as e:
            print(f"Error: {e}")