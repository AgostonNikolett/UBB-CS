from datetime import datetime

def print_events_table(events):
    print(f"{'ID Eveniment':<15}{'Data':<15}{'Timp':<10}{'Descriere':<30}{'Participanti'}")
    print("=" * 70) 

    for event in events:
        formatted_date = datetime.strptime(event.get_date(), "%Y-%m-%d").strftime("%d-%m-%Y")
        print(f"{event.get_event_id():<15}{formatted_date:<15}{event.get_time():<10}{event.get_description():<30}{event.get_participant_count()}")
        
    print("=" * 70) 

def print_persons_table(persons):
    print(f"{'ID Persoana':<15}{'Nume':<25}{'Adresa'}")
    print("=" * 50)  

    for person in persons:
        print(f"{person.get_person_id():<15}{person.get_name():<25}{person.get_address()}")
        
    print("=" * 50) 

def print_participants_table(participants):
    print(f"{'ID Persoana':<15}{'ID Eveniment'}")
    print("=" * 50)  

    for participant in participants:
        print(f"{participant.get_person_id():<15}{participant.get_event_id()}")
        
    print("=" * 50)