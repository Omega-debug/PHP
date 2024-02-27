from domeniu.angajat import Student
from repository.studentRepository import StudentRepository


class StudentService:
    def __init__(self, studentRepository: StudentRepository):
        self.__studentRepository = studentRepository

    def getAllStudenti(self):
        '''
        returneaza lista de studenti
        :return: o lista de obiecte de tipul student
        '''
        return self.__studentRepository.getAll()

    def adauga(self, studentid, nume):
        '''
        adauga un student
        :param studentid: string
        :param nume: string
        :return:
        '''
        student = Student(studentid, nume)
        self.__studentRepository.adauga(student)

    def modifica(self, studentid, numeNou):
        '''
        modifica un student
        :param studentid: string
        :param numeNou: string
        :return:
        '''
        studentNou = Student(studentid, numeNou)
        self.__studentRepository.modifica(studentNou)

    def sterge(self, studentid):
        '''
        sterge un student dupa id
        :param studentid: string
        :return:
        '''
        self.__studentRepository.sterge(studentid)
