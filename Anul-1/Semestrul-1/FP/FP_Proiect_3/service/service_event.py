from domain.event import Event
import random 
from datetime import datetime, timedelta

class EventService:
    def __init__(self, event_repo, validator):
        self.event_repo = event_repo
        self.validator = validator

    # Add an event
    def add_event(self, event_id, date, time, description):
        if self.validator.validate_event(event_id, date, time, description, self.event_repo):
            event = Event(event_id, date, time, description)
            self.event_repo.add_event(event)

    # Update an event
    def update_event(self, event_id, date, time, description):
        if self.validator.validate_event(event_id, date, time, description, self.event_repo):
            self.event_repo.update_event(event_id, date, time, description)

    # Remove an event
    def remove_event(self, event_id):
        self.event_repo.remove_event(event_id)

    # Find an event by its ID
    def find_event_by_id(self, event_id):
        return self.event_repo.find_event_by_id(event_id)

    # Add random events
    def add_random_events(self, number_of_events):
        descriptions = ["Conferinta Tehnologie", "Workshop Python", "Gala Premiilor", "Christmas Party", "Hackathon", "AI Summit", "Blockchain Conference",
            "Birthday Party", "Music Festival", "Art Exposition", "Virtual Reality Expo", "Startup Pitch Night", "Artificial Intelligence Workshop",
            "Gaming Convention", "Film Screening & Discussion", "Marathon Charity Run", "Cultural Heritage Day", "Space Exploration Seminar",
            "E-Sports Championship", "Yoga and Wellness Retreat", "Creative Writing Workshop", "Sustainable Living Fair", "Public Speaking Coaching",
            "Culinary Arts Showcase", "Investment Strategies Forum", "Robotics Demonstration", "Cybersecurity Training", "Community Volunteering Event",
            "Literary Festival", "Social Media Marketing Seminar", "Renewable Energy Conference", "Data Science Meetup", "Climate Change Awareness Campaign"
            ]

        while number_of_events > 0:
            event_id = str(random.randint(0, 10000))

            # Generate a random date
            today = datetime.today()
            random_days = random.randint(0, 365)
            date = (today + timedelta(days=random_days)).strftime("%Y-%m-%d")

            # Generate a random time
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            time = f"{hour:02}:{minute:02}"

            description = random.choice(descriptions)

            if self.validator.validate_event(event_id, date, time, description, self.event_repo):
                event = Event(event_id, date, time, description)
                self.event_repo.add_event(event)
                number_of_events -= 1

    # List all events
    def list_all_events(self):
        events = self.event_repo.get_all_events()
        sorted_events = sorted(events, key=lambda event: int(event.get_event_id()))
        return sorted_events

