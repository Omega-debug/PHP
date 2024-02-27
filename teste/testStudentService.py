from repository.studentRepository import StudentRepository
from service.StudentService import StudentService


def testAdaugaStudentService():
    studentRepository = StudentRepository()
    studentService = StudentService()

    studentService.adauga("1", "Ana")

    studenti = studentService.getAllStudenti()
    assert len(studenti) == 1
    assert studenti[0].getStudentID == "1"

    try:
        studentService.adauga("1", "Ion")
        assert False
    except KeyError:
        ...

def testModificaStudentService():
    studentRepository = StudentRepository()
    studentService = StudentService(studentRepository)

    studentService.adauga("1", "Ana")
    studentService.modifica("1", "Paul")

    studenti = studentRepository.getAll()
    assert studenti[0].getNume =="Paul"

    try:
        studentService.modifica("2", "Ion")
        assert False
    except KeyError:
        ...

def testStergeStudentService():
    studentRepository = StudentRepository()
    studentService = StudentService(studentRepository)

    studentService.adauga("1", "Ana")
    studentService.sterge("1")

    studenti = studentService.getAllStudenti()
    assert len(studenti) == 0

    try:
        studentService.sterge("1")
        assert False
    except KeyError:
        ...