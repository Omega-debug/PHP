from teste.testStudent import testStudentiSetteri, testStudent
from teste.testStudentService import testAdaugaStudentService, testModificaStudentService, testStergeStudentService
from teste.testStudentiRepository import testAdaugaStudentRepository, testModificaStudentRepository, \
    testStergeStudentRepository


def TestAll():
    testStudent()
    testStudentiSetteri()

    testAdaugaStudentRepository()
    testModificaStudentRepository()
    testStergeStudentRepository()

    testAdaugaStudentService()
    testModificaStudentService()
    testStergeStudentService()

