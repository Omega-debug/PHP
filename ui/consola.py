from service.StudentService import StudentService


class Consola:
    def __init__(self, studentService: StudentService):
        self.__studentService = studentService

    def adaugaStudent(self):
        try:
            studentid = input("dati id-ul studentului: ")
            nume = input("Dati numele studentului")
            self.__studentService.adauga(studentid, nume)
        except KeyError as e:
            print(e)

    def modificaStudent(self):
        try:
            studentid = input("dati id-ul studentului care trebuie modificat: ")
            numeNou = input("dati numele nou studentului: ")
            self.__studentService.modifica(studentid, numeNou)
        except KeyError as e:
            print(e)

    def sterge(self):
        try:
            studentid = input("dati id-ul studentului de sters")
            self.__studentService.sterge(studentid)
        except KeyError as e:
            print(e)

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def printMeniu(self):
        print("1. Adauga student")
        print("2. Modifica student")
        print("3. Sterge student")
        print("a. Afiseaza toti studentii")
        print("x. Iesire")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("dati optiunea: ")
            if optiune == "1":
                self.adaugaStudent()
            elif optiune == "2":
                self.modificaStudent()
            elif optiune == "3":
                self.sterge()
            elif optiune == "a":
                self.afiseaza(self.__studentService.getAllStudenti())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reincercati!")