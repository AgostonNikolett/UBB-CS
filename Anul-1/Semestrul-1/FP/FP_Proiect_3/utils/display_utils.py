from datetime import datetime


def print_events_table(events: list):
    """Prints a formatted table of events."""
    header = f"{'Event ID':<12} | {'Date':<12} | {'Time':<8} | {'Description':<25} | {'Attendees'}"
    print("\n" + header)
    print("-" * len(header))

    for event in events:
        # Convert date to a more readable format (DD-MM-YYYY)
        try:
            raw_date = event.get_date()
            formatted_date = datetime.strptime(raw_date, "%Y-%m-%d").strftime("%d-%m-%Y")
        except:
            formatted_date = event.get_date()

        print(f"{event.get_id():<12} | {formatted_date:<12} | {event.get_time():<8} | "
              f"{event.get_description():<25} | {event.get_participant_count()}")
    print("-" * len(header) + "\n")


def print_persons_table(persons: list):
    """Prints a formatted table of persons."""
    header = f"{'Person ID':<12} | {'Full Name':<25} | {'Address'}"
    print("\n" + header)
    print("-" * len(header))

    for person in persons:
        print(f"{person.get_id():<12} | {person.get_name():<25} | {person.get_address()}")
    print("-" * len(header) + "\n")


def print_registrations_table(registrations: list):
    """Prints simple ID-based links between persons and events."""
    header = f"{'Person ID':<15} | {'Event ID':<15}"
    print("\n" + header)
    print("-" * len(header))

    for reg in registrations:
        print(f"{reg.get_person_id():<15} | {reg.get_event_id():<15}")
    print("-" * len(header) + "\n")