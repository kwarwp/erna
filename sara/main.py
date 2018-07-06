from _spy.vitollino.main import Cena, Elemento, Texto
# Luciane
castelo = "https://upload.wikimedia.org/wikipedia/commons/8/88/Castelo_de_Guimar%C3%A3es_%28Portugal%29.jpg"
linkcarro = "http://www.vpowerautomoveis.com.br/home/imgs/carro_top4.png"
# cheguei
def historia():
     cenacastelo = Cena(img = "https://upload.wikimedia.org/wikipedia/commons/8/88/Castelo_de_Guimar%C3%A3es_%28Portugal%29.jpg")
     carro = Elemento(img = linkcarro, tit = "Carro", style = dict (top = 60, left = 150, height = 200, width = 100))
     carro.entra(cenacastelo)
     cenacastelo.vai()
historia()