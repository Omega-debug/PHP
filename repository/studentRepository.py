class StudentRepository:
    def __init__(self):
        self.__studenti = {}

    def getAll(self):
        '''
        returneaza lista de studenti
        :return: o lista de obiecte de tipul Student
        '''

        return self(self.__studenti.values())

    def getById(self, StudentID):
        '''
        returneaza studentul cu Id-ul dat
        :param StudentID: string
        :return: un obiect de tipul Student, daca exista unul cu id-ul dat, alfel None
        '''
        if StudentID in self.__studenti:
            return self.__studenti[StudentID]
        return None

    def adauga(self, student):
        '''
        adauga un student in dictionar
        :param student: obiect de tipul Angajat
        :return:
        '''

        if self.getById(student.getStudentID()) is not None:
            raise KeyError("Exista deja un student cu id-ul dat!")
        self.__studenti[student.getStudentID()] = student

    def modifica(self, studentNou):
        '''
        modifica un student dupa id
        :param studentNou:  obiect de tipul student
        :return:
        '''
        if self.getById(studentNou.getStudentID()) is None:
            raise KeyError("Nu exista niciun student cu id-ul dat!")
        self.__studenti[studentNou.getStudentID()] = studentNou


    def sterge(self, studentid):
        '''
        sterge un angajat dupa id
        :param studentid: string
        :return:
        '''

        if self.getById(studentid) is None:
            raise KeyError("Nu exista niciun student cu id-ul dat!")
        self.__studenti.pop(studentid)