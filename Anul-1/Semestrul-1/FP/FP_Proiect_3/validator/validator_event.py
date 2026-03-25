from datetime import datetime

class EventValidator:
    def validate_event(self, event_id, date, time, description, event_repo):
        
        # Check if the date is in a valid format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
        # Check if the time is in a valid format (HH:MM)
        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            raise ValueError("Invalid time format. Please use HH:MM.")
        
        # Ensure description is not empty
        if not description.strip():
            raise ValueError("Event description cannot be empty.")
        
        return True