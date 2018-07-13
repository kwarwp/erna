from _spy.vitollino.main import Cena, Elemento, Texto
# Luciane
ambiente7 = "https://i.imgur.com/YEk25am.png"
linkcarro = "http://www.vpowerautomoveis.com.br/home/imgs/carro_top4.png"
# cheguei
def historia():
     cenaambiente7 = Cena(img = "https://i.imgur.com/YEk25am.png")
     carro = Elemento(img = linkcarro, tit = "Carro", style = dict (top = 220, left = 150, height = 200, width = 60))
     txtcarro = Texto(cenaambiente7, "turn left and go up the ramp")
     carro.vai = txtcarro.vai
     carro.entra(cenaambiente7)
     cenaambiente7.vai()
historia()