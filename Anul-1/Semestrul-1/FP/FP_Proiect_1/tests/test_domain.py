import unittest
from domain.entities import Student, Disciplina, Nota
from domain.validators import StudentValidator, DisciplinaValidator, NotaValidator, ValidationException


class TestDomain(unittest.TestCase):
    def test_entities(self):
        # Student
        s = Student("1", "Alice")
        self.assertEqual(str(s), "1 Alice")
        self.assertEqual(s, Student("1", "Diff"))
        self.assertNotEqual(s, "not a student")

        # Disciplina
        d = Disciplina("1", "FP", "Istvan")
        self.assertEqual(str(d), "1 FP (Istvan)")
        self.assertEqual(d, Disciplina("1", "Other", "Other"))
        self.assertNotEqual(d, 5)

        # Nota
        n = Nota(s, "FP", 10.0)
        self.assertEqual(n.get_student(), s)
        self.assertEqual(n.get_disciplina(), "FP")
        self.assertEqual(n.get_nota(), 10.0)
        self.assertIn("Student: Alice", str(n))
        self.assertEqual(n, Nota(s, "FP", 9.0))
        self.assertNotEqual(n, s)

    def test_validators(self):
        # Student Validator
        sv = StudentValidator()
        sv.validate_student(Student("1", "Alice"))
        with self.assertRaises(ValidationException) as ve:
            sv.validate_student(Student("", ""))
        msgs = ve.exception.get_msgs()
        self.assertEqual(len(msgs), 2)

        # Disciplina Validator
        dv = DisciplinaValidator()
        dv.validate_disciplina(Disciplina("1", "FP", "Istvan"))
        with self.assertRaises(ValidationException):
            dv.validate_disciplina(Disciplina("", "", ""))

        # Nota Validator
        nv = NotaValidator()
        nv.validate_nota(Nota(None, None, "10"))
        with self.assertRaises(ValidationException):  # Out of range
            nv.validate_nota(Nota(None, None, 11))
        with self.assertRaises(ValidationException):  # Not numeric
            nv.validate_nota(Nota(None, None, "abc"))