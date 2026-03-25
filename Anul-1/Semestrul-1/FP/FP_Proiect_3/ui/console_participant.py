from utils.prints import print_participants_table
from utils.prints import print_events_table
from utils.prints import print_persons_table

class ParticipantMenu:
    def __init__(self, participant_service):
        self.participant_service = participant_service

    def print_participant_menu(self):
        print("\nParticipant Management")
        print("1.   Register Person to Event")
        print("2.   List Persons whit Events")
        print("3.   Show Events for a Person")
        print("4.   Show Persons for an Event")
        print("5.   Show Top Persons")
        print("6.   Show Top Events")
        print("RPE. Register Random Persons to Events")
        print("Q.   Back to Main Menu")

    def handle_participant_menu(self):
        while True:
            self.print_participant_menu()
            option = input("Choose an option: ").lower()
            if option == "1":
                self.handle_register_person_to_event()
            elif option == "2":
                self.handle_list_participants()
            elif option == "3":
                self.handle_show_events_for_person()
            elif option == "4":
                self.handle_show_persons_for_event()
            elif option == "5":
                self.handle_show_top_participants()
            elif option == "6":
                self.handle_show_top_events()
            elif option == "rpe":
                self.handle_register_random_persons_to_events()
            elif option == "q":
                break
            else:
                print("Invalid option. Please try again.")

     
    def handle_register_person_to_event(self):
        try:
            person_id = input("Enter Person ID: ")
            event_id = input("Enter Event ID: ")
            self.participant_service.register_person_to_event(person_id, event_id)
            print("Person registered to event successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_list_participants(self):
        participants = self.participant_service.list_all_participants()
        if not participants:
            print("No persons registeried to events found.")
        else:
            print_participants_table(participants)
     
    def handle_show_events_for_person(self):
        try:
            person_id = input("Enter Person ID: ")
            events = self.participant_service.get_person_events(person_id)
            if not events:
                print("This person is not registered for any events.")
            else:
                print("Events for the person:")
                print_events_table(events)
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_show_persons_for_event(self):
        try:
            event_id = input("Enter Event ID: ")
            persons = self.participant_service.get_event_persons(event_id)
            if not persons:
                print("This event dose note have any participants.")
            else:
                print("Participants for the event:")
                print_persons_table(persons)
        except ValueError as e:
            print(f"Error: {e}")

    def handle_show_top_participants(self):
        participants = self.participant_service.get_most_active_persons()
        if not participants:
            print("No participants found.")
        else:
            print("Top participants:")
            print_persons_table(participants)
    
    def handle_show_top_events(self):
        events = self.participant_service.get_top_events_by_participants()
        if not events:
            print("No events found.")
        else:
            print("Top events:")
            print_events_table(events)

    def handle_register_random_persons_to_events(self):
        try:
            number_of_participants = int(input("Number of participants to add:"))
            self.participant_service.register_random_persons_to_events(number_of_participants)
            print("Participants added successfully.")
        except ValueError as e:
            print(f"Errpr: {e}")