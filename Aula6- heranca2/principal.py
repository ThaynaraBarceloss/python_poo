from pessoa import Pessoa,Aluno, Professor

pessoa1 = Pessoa("Thaynara", 17)
aluno1 = Aluno("Maria", 20, 3456)
professor1 = Professor("Pablo", 24, "Matemática")

pessoa1.info()
print("-" * 50)

aluno1.info()
aluno1.estudar()
print("-" * 50)
professor1.info()
professor1.ensinar()
