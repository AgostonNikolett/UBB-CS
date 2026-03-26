from utils.display_utils import print_persons_table

class PersonMenu:
    def __init__(self, person_service):
        self._service = person_service

    def _print_menu(self):
        print("\n--- Person Management ---")
        print("1. Add Person")
        print("2. List All Persons")
        print("3. Modify Person")
        print("4. Delete Person")
        print("5. Find Person by ID")
        print("6. Generate Random Persons")
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
            p_id = input("ID: ")
            name = input("Name: ")
            address = input("Address: ")
            self._service.add_person(p_id, name, address)
            print("Success: Person added.")
        except ValueError as e: print(f"Error: {e}")

    def _handle_list(self):
        persons = self._service.get_all_sorted_by_id()
        if not persons: print("No persons in system.")
        else: print_persons_table(persons)

    def _handle_update(self):
        try:
            p_id = input("Enter ID to modify: ")
            name = input("New Name: ")
            address = input("New Address: ")
            self._service.update_person(p_id, name, address)
            print("Success: Person updated.")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_delete(self):
        try:
            p_id = input("Enter ID to delete: ")
            self._service.remove_person(p_id)
            print("Success: Person removed.")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_find(self):
        try:
            p_id = input("Enter ID to find: ")
            person = self._service.find_by_id(p_id)
            print(f"Found: {person}")
        except ValueError as e: print(f"Error: {e}")

    def _handle_random(self):
        try:
            count = int(input("How many persons to generate? "))
            self._service.generate_random_persons(count)
            print(f"Success: Generated {count} persons.")
        except ValueError as e: print(f"Error: {e}")