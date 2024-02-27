from domeniu.angajat import Student


def testStudent():
    student = Student("1", "Maria")

    assert student.getIdAngajat() == "1"
    assert student.getNume() == "Maria"

def testStudentiSetteri():
    student = Student("1", "Maria")

    student.setStudentID("2")
    assert student.getStudentID() == "2"

    student.setNume("Alexandra")
    assert student.getNume() == "Alexandra"


