from personagem import Personagem, Heroi,Vilao

personagem1 = Personagem("Valentina Vortex", 100, "Avançado")
heroi1 = Heroi ("Lady Destino", 60, "Intermediário", "Pablo", 50) 
vilao1= Vilao ("Rainha do Terror", 80, "Lendário", 70)

print("Personagem:")
personagem1.detalhes()
personagem1.receberDano(10)
personagem1.verificarVida()
print("-" * 50)
print("Heroi:")
heroi1.detalhes()
heroi1.executarHabilidades("Controle do Tempo", 25)
heroi1.recarregarEnergia(10)
print("-" *50)
print("Vilão:")
vilao1.detalhes()
vilao1.planejarArmadilha("Furar o pneu do carro")

