class Calculadora :
    def __init__(self,num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def somar (self ):
        resultadoSoma = self.__num1 + self.__num2
        print(f"A soma do {self.__num1} + {self.__num2} é igual a {resultadoSoma}")

    def subtrair (self):
        resultadoSubstracao =self.__num1 - self.__num2
        print (f"A subtração do {self.__num1} - {self.__num2} é igual a {resultadoSubstracao}")

    def multiplicar (self):
        resultadoMultiplicacao = self.__num1 * self.__num2
        print(f"A multiplicação do {self.__num1} X {self.__num2} é igual a {resultadoMultiplicacao}")
        
    def dividir (self ):
        if self.__num2 < 0:
            print("Informe um valor diferente de zero")
        else:
            resultadoDivicao = self.__num1 / self.__num2
            print(f"A divisão de {self.__num1} / {self.__num2} é igual a {resultadoDivicao}")

    def potencia(self):
        if self.__num1 > 0 and self.__num2 >= 0:
            resultadoPotencia = self.__num1 ** self.__num2
            print(f"{self.__num1} elevado à potência de {self.__num2} é: {resultadoPotencia}")
        else:
            print("Erro: num1 deve ser maior que zero e num2 não pode ser negativo.")

    def verificar(self, valor):
       if valor % 2 == 0:
          print("O valor é par")
       else:
          print("O valor é impar")
