import unittest
from service.services import StudentService, DisciplinaService, NotaService
from repository.inmemory import StudentRepository, DisciplinaRepository, NotaRepository
from domain.validators import StudentValidator, DisciplinaValidator, NotaValidator


class TestService(unittest.TestCase):
    def setUp(self):
        self.rs = StudentRepository()
        self.rd = DisciplinaRepository()
        self.rn = NotaRepository()
        self.ss = StudentService(StudentValidator(), self.rs)
        self.sd = DisciplinaService(DisciplinaValidator(), self.rd)
        self.sn = NotaService(NotaValidator(), self.rn, self.rs, self.rd)

    def test_student_service(self):
        self.ss.create("1", "Alice")
        self.ss.create("2", "Bob")
        self.assertEqual(len(self.ss.search("Ali")), 1)
        self.assertEqual(len(self.ss.search("")), 2)
        self.ss.update("1", "Alicia")
        self.ss.remove("2")
        self.assertEqual(len(self.ss.get_all()), 1)

    def test_discipline_service(self):
        self.sd.create("1", "FP", "Istvan")
        results = self.sd.search("")
        self.assertEqual(len(results), 1)
        self.assertEqual(len(self.sd.search("FP")), 1)
        self.assertEqual(len(self.sd.search("")), 1)
        self.sd.update("1", "OOP", "Bazil")
        self.sd.remove("1")

    def test_nota_service(self):
        self.ss.create("1", "Alice")
        self.sd.create("1", "FP", "Istvan")

        # Success
        self.sn.assign_grade("1", "1", 10)
        self.assertEqual(len(self.sn.get_student_grades("1")), 1)
        self.assertEqual(len(self.sn.get_discipline_grades("FP")), 1)

        # Failures
        with self.assertRaises(ValueError):
            self.sn.assign_grade("99", "1", 10)
        with self.assertRaises(ValueError):
            self.sn.assign_grade("1", "99", 10)
        with self.assertRaises(ValueError):
            self.sn.get_student_grades("99")

    def test_top_students(self):
        # Create 5 students to test 20% (1 student)
        for i in range(5):
            sid = str(i)
            self.ss.create(sid, f"S{i}")
            self.sd.create(sid, f"D{i}", "P")
            self.sn.assign_grade(sid, sid, 5 + i)  # Grades: 5, 6, 7, 8, 9

        top = self.sn.get_top_students()
        self.assertEqual(len(top), 1)
        self.assertEqual(top[0][0].get_nume(), "S4")