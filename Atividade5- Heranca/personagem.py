class Personagem:
    def __init__(self, nome,vida, rank):
        self._nome = nome
        self._vida = vida
        self._rank = rank

    def receberDano(self,dano):
        self._vida= self._vida - dano
        print(f"Quantidade de danos: {dano}")

    def verificarVida(self):
        if self._vida >= 1:
         print(f"O personagem está vivo")
        else:
         self._vida <=0
         print(f"O personagem está morto")

    def detalhes(self):
        print(f"Nome do(a) personagem : {self._nome} \nQuantidade de vidas:{self._vida} \nRank:{self._rank} ")

class Heroi(Personagem):
    def __init__(self, nome,vida,rank, identidadeSecreta, energia):
        super().__init__(nome,vida,rank)
        self._identidadeSecreta = identidadeSecreta
        self._energia = energia

    def detalhes(self):
       print(f"Nome do(a) Heroi : {self._nome} \nQuantidade de vidas:{self._vida} \nRank:{self._rank} \nIdentidade Secreta: {self._identidadeSecreta} \nQuantidade de energia: {self._energia} ")
       
    def executarHabilidades(self,tipoHabilidade,energiaConsumida):
       self._tipoHabilidade = tipoHabilidade 
       self._energia = self._energia - energiaConsumida
       print(f"Habilidade do(a) Heroi:{self._tipoHabilidade} \nEnergia consumida {energiaConsumida}")

    def recarregarEnergia(self,aumentoEnergia):
       self._energia = self._energia + aumentoEnergia
       print(f"Energia recarregada:{aumentoEnergia} \nEnergia total:{self._energia}")

class Vilao(Personagem):
   def __init__(self,nome,vida,rank,malicia ):
      super().__init__(nome,vida,rank)
      self._malicia = malicia 

   def detalhes(self):
       print(f"Nome do(a) Vilão :{self._nome} \nQuantidade de vidas:{self._vida} \nRank:{self._rank} \nMalícia do vilão:{self._malicia} ")

   def desferirGolpe(self,tipoGolpe):
      self.tipoGolpe = tipoGolpe

   def planejarArmadilha(self,tipoArmadilha):
      self._tipoArmadilha = tipoArmadilha
      print(f"O vilão está planejando uma armadilha:{self._tipoArmadilha}")
       
  