from _spy.vitollino.main import Cena, Elemento, Texto
#Tassiane 
ceu = "https://png.pngtree.com/thumb_back/fw800/back_pic/03/56/29/24579dee6c24b45.jpg"
linkparis = "http://www.freepngimg.com/download/paris/24125-5-paris-picture.png"
#Bonne nuit
def historia():
     cenaceu = Cena(img = "https://png.pngtree.com/thumb_back/fw800/back_pic/03/56/29/24579dee6c24b45.jpg")
     paris = Elemento(img = linkparis, tit = 'Paris', style = dict (top = 200, left = 200, height = 200, width = 80))
     paris.entra(cenaceu)
     cenaceu.vai()
historia() 