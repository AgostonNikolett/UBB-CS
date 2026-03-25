from utils.prints import print_persons_table

class PersonMenu:
    def __init__(self, person_service):
        self.person_service = person_service

    def print_person_menu(self):
        print("\nPerson Management")
        print("1.  Add Person")
        print("2.  List Persons")
        print("3.  Modify Person")
        print("4.  Delete Person")
        print("5.  Find Person")
        print("RP. Add Random Persons")
        print("Q.  Back to Main Menu")

    def handle_person_menu(self):
        while True:
            self.print_person_menu()
            option = input("Choose an option: ").lower()
            if option == "1":
                self.handle_add_person()
            elif option == "2":
                self.handle_list_persons()
            elif option == "3":
                self.handle_update_person()
            elif option == "4":
                self.handle_delete_person()
            elif option == "5":
                self.handle_find_person()
            elif option == "rp":
                self.handle_add_random_persons()
            elif option == "q":
                break
            else:
                print("Invalid option. Please try again.")

    
    def handle_add_person(self):
        try:
            person_id = input("Enter Person ID: ")
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            self.person_service.add_person(person_id, name, address)
            print("Person added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_list_persons(self):
        persons = self.person_service.list_all_persons()
        if not persons:
            print("No persons found.")
        else:
            print_persons_table(persons)
    
    def handle_update_person(self):
        try:
            person_id = input("Enter Person ID: ")
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            self.person_service.update_person(person_id, name, address)
            print("Person updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_delete_person(self):
        try:
            person_id = input("Enter Person ID to delete: ")
            self.person_service.remove_person(person_id)
            print("Person deleted successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_find_person(self):
        try:
            person_id = input("Enter Person ID to finde: ")
            person = self.person_service.find_person_by_id(person_id)
            print(person)
        except ValueError as e:
            print(f"Error: {e}")

    def handle_add_random_persons(self):
        try:
            number_of_persons = int(input("Number of persons to add:"))
            self.person_service.add_random_persons(number_of_persons)
            print("Persons added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
 