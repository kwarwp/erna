from _spy.vitollino.main import Cena, Elemento, Texto
#Tassiane 
ambiente4 = "https://i.imgur.com/Ei24vcD.png"
linkparis = "http://www.freepngimg.com/download/paris/24125-5-paris-picture.png"
#Bonne nuit
def historia():
     ambiente4 = Cena(img = "https://i.imgur.com/Ei24vcD.png")
     paris = Elemento(img = linkparis, tit = 'Paris', style = dict (top = 50, left = 30, height = 50, width = 40))
     txtparis = Texto(ambiente4 This is our digital environment)
     paris.vai = txtparis.vai
     paris.entra(ambiente4)
     ambiente4.vai()
historia()   