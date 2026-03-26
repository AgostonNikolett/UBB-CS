from service.service_person import PersonService
from service.service_event import EventService
from service.service_participant import ParticipantService

from repository.repo_person import PersonRepository
from repository.repo_event import EventRepository
from repository.repo_participant import ParticipantRepository

from repository.file_repo_person import PersonFileRepository
from repository.file_repo_event import EventFileRepository
from repository.file_repo_participant import ParticipantFileRepository

from validator.validator_person import PersonValidator
from validator.validator_event import EventValidator
from validator.validator_participant import ParticipantValidator
from ui.console_person import PersonMenu
from ui.console_event import EventMenu
from ui.console_participant import ParticipantMenu
from ui.console import UI
import unittest

def run_all_tests():
    print("Running all tests...")
    # Discover and run all tests in the 'tests' directory
    loader = unittest.TestLoader()
    suite = loader.discover('tests') 
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("All tests passed successfully!\n")
    else:
        print(f"Some tests failed. Total Failures: {len(result.failures)}\n")

def print_main_menu():
    print("\nModel repository")
    print("1. In Memori Repository")        
    print("2. File Repository")
    print("Q. Quit")

def main():
    # Run tests before starting the UI
    run_all_tests()
    
    # Initialize repositories
    print_main_menu()
    option = input("Choose an option: ").lower()
    
    if option == "1":
        person_repo = PersonRepository()
        event_repo = EventRepository()
        participant_repo = ParticipantRepository()
        
    elif option == "2":
        person_repo = PersonFileRepository("data/person_file.txt")
        event_repo = EventFileRepository("data/event_file.txt")
        participant_repo = ParticipantFileRepository("data/participant_file.txt")

    # Initialize validators
    person_val = PersonValidator()
    event_val = EventValidator()
    participant_val = ParticipantValidator()
    
    # Initialize services
    person_service = PersonService(person_repo, person_val)
    event_service = EventService(event_repo, event_val)
    participant_service = ParticipantService(participant_repo, person_repo, event_repo, participant_val)
    
    # Initialize console
    person_menu = PersonMenu(person_service)
    event_menu = EventMenu(event_service)
    participant_menu = ParticipantMenu(participant_service)
    
    # Initialize UI
    ui = UI(person_menu, event_menu, participant_menu)
    
    # Start the application
    ui.start()
    

if __name__ == "__main__":
    main()
    