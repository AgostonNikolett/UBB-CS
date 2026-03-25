import unittest
import os
from repository.inmemory import StudentRepository, DuplicatedIDException, RepositoryException, NotaRepository
from repository.file import StudentFileRepository, DisciplinaFileRepository, NoteFileRepository
from domain.entities import Student, Disciplina, Nota


class TestRepository(unittest.TestCase):
    def test_in_memory(self):
        repo = StudentRepository()
        s = Student("1", "Alice")
        repo.store(s)
        self.assertEqual(repo.size(), 1)
        with self.assertRaises(DuplicatedIDException):
            repo.store(s)

        self.assertEqual(repo.find("1"), s)
        self.assertIsNone(repo.find("2"))

        repo.update("1", Student("1", "Bob"))
        self.assertEqual(repo.find("1").get_nume(), "Bob")
        with self.assertRaises(RepositoryException):
            repo.update("99", s)

        repo.remove("1")
        with self.assertRaises(RepositoryException):
            repo.remove("1")

        with self.assertRaises(RepositoryException) as re:
            repo.remove("ID_INEXISTENT")
        error_msg = str(re.exception)

    def test_nota_repository(self):
        repo = NotaRepository()
        s = Student("1", "A")
        n = Nota(s, "FP", 10)
        repo.store(n)
        with self.assertRaises(RepositoryException):  # Duplicate grade for same student/disc
            repo.store(n)
        self.assertEqual(len(repo.get_all(s)), 1)
        self.assertEqual(len(repo.get_all_for_dis("FP")), 1)

    def test_file_repositories(self):
        # Test paths
        fs, fd, fn = "tests/data/ts.txt", "tests/data/td.txt", "tests/data/tn.txt"

        filename = "data/non_existent.txt"
        if os.path.exists(filename): os.remove(filename)
        repo = StudentFileRepository(filename)

        # Cleanup if exists
        for f in [fs, fd, fn]:
            if os.path.exists(f): os.remove(f)

        # Student File Repo (covers FileNotFoundError via pass in __load)
        repo_s = StudentFileRepository(fs)
        repo_s.store(Student("1", "Alice"))
        repo_s.update("1", Student("1", "Bob"))
        repo_s.remove("1")

        # Disciplina File Repo
        repo_d = DisciplinaFileRepository(fd)
        repo_d.store(Disciplina("1", "FP", "Istvan"))
        repo_d.remove("1")

        # Note File Repo
        repo_s.store(Student("1", "Alice"))
        repo_n = NoteFileRepository(fn, repo_s, repo_d)
        repo_n.store(Nota(Student("1", "Alice"), "FP", 10))

        # Reload to check persistence
        repo_n2 = NoteFileRepository(fn, repo_s, repo_d)
        self.assertEqual(repo_n2.size(), 1)