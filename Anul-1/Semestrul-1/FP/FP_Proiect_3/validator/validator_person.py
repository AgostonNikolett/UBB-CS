class PersonValidator:
    def validate_person(self, person_id, name, address, person_repo):
        """
        # Ensure the person exists
        try:
            person = person_repo.find_person_by_id(person_id)
        except ValueError:
            raise ValueError(f"Person with ID {person_id} does not exist.")
        """
        # Ensure name and address is not empty
        if not name or not address:
            raise ValueError("Name and address cannot be empty.")
        return True
