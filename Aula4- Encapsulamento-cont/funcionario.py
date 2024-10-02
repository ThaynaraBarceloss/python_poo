class Funcionario:
    def __init__(self, nome, salario = 1000):
        self.__nome = nome
        self.__salario = salario

    def getNome(self):
        return self.__nome
    
    def setNome(self, valor):
        self.__nome = valor #Alterar


    #Iremos utilizar um recurso único do python para acessar atributos privados
    
    #Criando um get personalizado
    @property #esse item irá criar um get "mais amigável"
    def salario(self):
        return self.__salario
    
    @salario.setter #Irá criar um set para o atributo de forma  "mais amigável"
    def salario(self, valor):
        if valor >0:
            self.__salario = valor 
        else:
            print("Você não pode ter un salário negativo")