from repository.studentRepository import StudentRepository
from service.StudentService import StudentService
from ui.consola import Consola


def main():
    studentRepository = StudentRepository()
    studentService = StudentService(studentRepository)
    consola = Consola(StudentService)

    consola.meniu()

main()