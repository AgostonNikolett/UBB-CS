from datetime import datetime

class EventValidator:
    """
    Validator for Event entities.
    Checks date formats (YYYY-MM-DD) and time formats (HH:MM).
    """
    def validate(self, event_id: str, date: str, time: str, description: str):
        """
        Validates event attributes.
        :raises ValueError: If formats are invalid or fields are empty.
        """
        errors = []

        if not event_id.strip():
            errors.append("Event ID cannot be empty.")

        # Validate Date format: YYYY-MM-DD
        try:
            datetime.strptime(date, "%Y-%m-%d") 
        except ValueError:
            errors.append("Invalid date format. Expected YYYY-MM-DD.") 

        # Validate Time format: HH:MM
        try:
            datetime.strptime(time, "%H:%M") 
        except ValueError:
            errors.append("Invalid time format. Expected HH:MM.") 

        if not description.strip():
            errors.append("Event description cannot be empty.") 

        if errors:
            raise ValueError("\n".join(errors))