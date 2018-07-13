from _spy.vitollino.main import Cena, Elemento, Texto
#Alexandre
AMBIENTE3 = "https://i.imgur.com/rkX57B2.png"
linkpessoa = "http://www.trackandfield.com.br/wordpress/wp-content/uploads/2014/10/Screen-Shot-2014-10-15-at-4.38.02-PM.png"
# bom dia 
def historia():
     cenaAMBIENTE3 = Cena(img = "https://i.imgur.com/rkX57B2.png")
     pessoa = Elemento(img = linkpessoa, tit = "Pessoa", style = dict (top = 60, left = 150, height = 200, width = 60))
     txtpessoa = Texto(cenaAMBIENTE3,"Bom Dia")
     pessoa.vai = txtpessoa.vai
     pessoa.entra(cenaAMBIENTE3)
     cenaAMBIENTE3.vai()
historia()

