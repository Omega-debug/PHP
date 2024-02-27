from domeniu.angajat import Student
from repository.studentRepository import StudentRepository


def testAdaugaStudentRepository():
    studentRepository = StudentRepository()
    student = Student("1", "Maria")

    studentRepository.adauga(student)

    studenti = studentRepository.getAll()
    assert len(studenti) == 1
    assert studenti[0].getStudentID == "1"

    try:
        studentRepository.adauga(student)
        assert False
    except KeyError:
        ...

def testModificaStudentRepository():
        studentRepository = StudentRepository()
        student = Student("1", "Maria")
        studentNou1 = Student("1", "Mihai")
        studentNou2 = Student("2", "Ionel")
        studentRepository.adauga(student)

        studentRepository.modifica(studentNou1)

        studenti = studentRepository.getAll()
        assert studenti[0].getNume == "Mihai"

        try:
            studentRepository.modifica(studentNou2)
            assert False
        except KeyError:
            ...

def testStergeStudentRepository():
    studentRepository = StudentRepository()
    student = Student("1", "ana")
    studentRepository.adauga(student)

    studentRepository.sterge("1")

    assert len(studentRepository.getAll()) == 0

    try:
        studentRepository.sterge("!")
        assert False
    except KeyError:
        ...