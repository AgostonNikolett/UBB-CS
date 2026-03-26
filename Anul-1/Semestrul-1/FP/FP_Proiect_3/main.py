from repository.event_repository import EventFileRepository
from repository.participant_repository import ParticipantFileRepository
from repository.base_repository import InMemoryRepository
from repository.person_repository import PersonFileRepository

from validators.person_validator import PersonValidator
from validators.event_validator import EventValidator
from validators.registration_validator import RegistrationValidator

from service.person_service import PersonService
from service.event_service import EventService
from service.registration_service import RegistrationService

from ui.console_person import PersonMenu
from ui.console_event import EventMenu
from ui.console_registration import RegistrationMenu
from ui.console import UI


def initialize_app():
    print("Welcome! Select Storage Mode:")
    print("1. In-Memory (Session only)")
    print("2. File Persistent (Saves to .txt)")

    choice = input("Choice: ").strip()

    if choice == "2":
        person_repo = PersonFileRepository("data/persons.txt")
        event_repo = EventFileRepository("data/events.txt")
        part_repo = ParticipantFileRepository("data/registrations.txt")
    else:
        print("Running in Memory Mode...")
        person_repo = InMemoryRepository()
        event_repo = InMemoryRepository()
        part_repo = ParticipantFileRepository("data/temp.txt")

    # Validators
    p_val = PersonValidator()
    e_val = EventValidator()
    r_val = RegistrationValidator()

    # Services
    p_service = PersonService(person_repo, p_val)
    e_service = EventService(event_repo, e_val)
    r_service = RegistrationService(part_repo, person_repo, event_repo, r_val)

    # UI Layers
    p_menu = PersonMenu(p_service)
    e_menu = EventMenu(e_service)
    r_menu = RegistrationMenu(r_service)

    return UI(p_menu, e_menu, r_menu)


if __name__ == "__main__":
    app = initialize_app()
    app.start()