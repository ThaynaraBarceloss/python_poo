class Pessoa:
    #atributos
    nome = "Fulano"
    peso = 71
    escolaridade = "Ensino Médio"

    #métodos 
    def falar(self, texto):
        print(f"Tenho algo pra te dizer: {texto}")


#Criando os objetos
pessoa1 = Pessoa()
print(pessoa1.nome)
pessoa1.falar("Boa tarde, hoje é segunda-feira")