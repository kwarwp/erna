from _spy.vitollino.main import Cena, Elemento, Texto
#Matheus
ambiente2 = "http://2.bp.blogspot.com/-QfJCgBGjGLI/U7sgKKLbRWI/AAAAAAAAZEE/RXU-xgjdPlg/s1600/ZQHFqWr.jpg"
linkhokage = "https://i.pinimg.com/originals/39/02/44/390244b135c00088e1b8b7871d45957a.png"
#Olá eu sou o kakashi, o sexto hokage da aldeia da folha
def historia ():
     cenaambiente2 = Cena(img = "http://2.bp.blogspot.com/-QfJCgBGjGLI/U7sgKKLbRWI/AAAAAAAAZEE/RXU-xgjdPlg/s1600/ZQHFqWr.jpg")
     hokage = Elemento(img = linkhokage, tit = "Hokage", style = dict (top = 60, left = 160, height = 800, width = 60))
     txthokage = Texto(cenaambiente2, "Olá!!! Eu sou o kakashi, o sexto hokage da aldeia da folha")
     hokage.vai = txthokage.vai
     hokage.entra(cenaambiente2)
     cenaambiente2.vai()
historia()