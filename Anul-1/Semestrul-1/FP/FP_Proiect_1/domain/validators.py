class CRUDException(Exception):
    """Base exception for application errors."""
    pass


class ValidationException(CRUDException):
    """Exception raised when entity validation fails."""

    def __init__(self, msgs):
        self.__msgs = msgs

    def get_msgs(self):
        return self.__msgs

    def __str__(self):
        return ", ".join(self.__msgs)


class StudentValidator:
    def validate_student(self, st):
        errors = []
        if not st.get_id(): errors.append("ID cannot be empty")
        if not st.get_nume(): errors.append("Name cannot be empty")
        if errors:
            raise ValidationException(errors)


class DisciplinaValidator:
    def validate_disciplina(self, dis):
        errors = []
        if not dis.get_id(): errors.append("ID cannot be empty")
        if not dis.get_disciplina(): errors.append("Discipline name cannot be empty")
        if not dis.get_nume(): errors.append("Professor name cannot be empty")
        if errors:
            raise ValidationException(errors)


class NotaValidator:
    def validate_nota(self, nota_obj):
        errors = []
        try:
            valoare = float(nota_obj.get_nota())
            if valoare < 1 or valoare > 10:
                errors.append("Grade must be between 1 and 10")
        except ValueError:
            errors.append("Grade must be a numeric value")

        if errors:
            raise ValidationException(errors)