from _spy.vitollino.main import Cena, Elemento, Texto
#Tassiane 
ceu = "https://png.pngtree.com/thumb_back/fw800/back_pic/03/56/29/24579dee6c24b45.jpg"
linkparis = "http://www.freepngimg.com/download/paris/24125-5-paris-picture.png"
#Bonne nuit
def historia():
     cenaceu = Cena(img = "https://png.pngtree.com/thumb_back/fw800/back_pic/03/56/29/24579dee6c24b45.jpg")
     paris = Elemento(img = linkparis, tit = 'Paris', style = dict (top = 10, left = 30, height = 30, width = 50))
     paris.entra(cenaceu)
     cenaceu.vai()
historia() 