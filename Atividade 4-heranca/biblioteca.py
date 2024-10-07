import datetime
class Biblioteca:
    def __init__ (self, titulo,  autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao 
        self._numeroPagina = numeroPagina 

    def detalhes(self):
        print(f"O item {self._titulo} do autor {self._autor} do ano {self._anoPublicacao} tem {self._numeroPagina} páginas")

    def calcularIdadeItem(self):
         anoAtual = datetime.datetime.now()
         idade = anoAtual.year - self._anoPublicacao
         if idade > 70:
             print(f"O item {self._titulo} do ano {self._anoPublicacao} é antigo com a idade de {idade} anos")
         elif 30 >= idade and idade <= 70:
            print(f"O item {self._titulo} do ano {self._anoPublicacao} é recente com a idade de {idade} anos")
         else:
             print(f"O item {self._titulo} do ano {self._anoPublicacao} é contemporâneo com a idade de {idade} anos")


class Livro (Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina >= 300 :
            print(f"O {self._titulo}  tem {self._numeroPagina} páginas e é longo com mais de 300 páginas")
        else:
            self._numeroPagina <= 300
            print(f"O {self.titulo}  tem {self._numeroPagina} páginas e é curto com menos de 300 páginas")

class Revista (Biblioteca):
    def verificarEdicao(self):
        if self._anoPublicacao <= 1998:
            print(f" A revista {self._titulo} do ano de {self._anoPublicacao} é uma edição especial ")

        else:
            self._anoPublicacao >= 1998
            print(f" A revista {self._titulo} do ano de {self._anoPublicacao} não é uma edição especial")


