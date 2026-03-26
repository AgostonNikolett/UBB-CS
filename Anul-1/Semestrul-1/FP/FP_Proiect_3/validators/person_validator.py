class PersonValidator:
    """
    Validator for Person entities.
    Ensures data consistency and presence of mandatory fields.
    """

    def validate(self, person_id: str, name: str, address: str):
        """
        Validates the attributes of a person.
        :raises ValueError: If any field is empty or logically incorrect.
        """
        errors = []

        if not person_id.strip():
            errors.append("Person ID cannot be empty.")

        if not name.strip():
            errors.append("Name cannot be empty.")

        if not address.strip():
            errors.append("Address cannot be empty.")

        if errors:
            raise ValueError("\n".join(errors))