# erna.soraya.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
#renata
ambiente9 = "https://i.imgur.com/38Sq4Jm.png"
linkaviao = "http://3.bp.blogspot.com/-4SsFci7nC_Q/VmsgYxu3EdI/AAAAAAAAPzo/1pjiUbLTJSs/s1600/Estrela%2B5.png"
#Help!!!
def historia():
     cenaambiente9= Cena(img = "https://i.imgur.com/38Sq4Jm.png")
     aviao = Elemento(img = linkaviao,tit = "Aviao", style = dict (top = 260, left = 150, height = 60, width = 60))
     txtaviao = Texto(ambiente9, "Feel free to those a computer. The teacher is on her way")

     aviao.vai=txtaviao.vai
     aviao.entra(ambiente9)
     cenaambiente9.vai()
historia()