from academia import aluno

nomeAluno = input("Informe o seu nome: ")
idadeAluno = int(input("Informe a sua idade: "))
pesoAluno =float(input("Informe o seu peso: "))
alturaAluno = float(input("Informe a sua altura: "))

aluno1 = aluno(nomeAluno,idadeAluno,alturaAluno,pesoAluno)
aluno1.exibirDados()
aluno1.calcularImc()

