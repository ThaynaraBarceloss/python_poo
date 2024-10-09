from produto import Produto,Eletronico

produto1 = Produto("Armário", 758.99)
eletronico1= Eletronico("Smartphone", 1544.99, 220)

produto1.descrever()
produto1.calcularDesconto(10)

eletronico1.descrever()
eletronico1.calcularDesconto(30)