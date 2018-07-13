from _spy.vitollino.main import Cena, Elemento, Texto
#Alexandre
AMBIENTE3 = "https://i.imgur.com/rkX57B2.png"
linkpessoa = "http://3.bp.blogspot.com/-4SsFci7nC_Q/VmsgYxu3EdI/AAAAAAAAPzo/1pjiUbLTJSs/s1600/Estrela%2B5.png"
# bom dia 
def historia():
     cenaAMBIENTE3 = Cena(img = "https://i.imgur.com/rkX57B2.png")
     pessoa = Elemento(img = linkpessoa, tit = "Pessoa", style = dict (top = 60, left = 150, height = 200, width = 60))
     txtpessoa = Texto(cenaAMBIENTE3,"Bom Dia")
     pessoa.vai = txtpessoa.vai
     pessoa.entra(cenaAMBIENTE3)
     cenaAMBIENTE3.vai()
historia()

