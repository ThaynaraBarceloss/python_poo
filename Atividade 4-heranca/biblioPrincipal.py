from biblioteca import Biblioteca, Livro, Revista

biblioteca1 = Biblioteca("Orgulho e Preconceito", "Jane Austen", 1813, 424)
livro = Livro ( "Dom Casmurro", "Machado de Assis", 1899, 346 )
revista = Revista ("Revista Veja", "Roberto Civita", 1997, 30)
print("\n")
biblioteca1.detalhes()
livro.detalhes()
livro.calcularIdadeItem()
livro.verificarTamanho()

print("-" *50)

revista.detalhes()
revista.calcularIdadeItem()
revista.verificarEdicao()
