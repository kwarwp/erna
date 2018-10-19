#Feliphe
from _spy.vitollino.main import Cena, Elemento, Texto

ZUMBI ="https://cdn.pixabay.com/photo/2017/01/09/14/59/zombie-1966751_960_720.png"

def Historia():
    CEMITERIO = Cena(img ="http://www.jomagazin.cz/wp-content/uploads/2015/01/angel-cemetery-cross-fog-gothic-favim.com-263560.jpg")
    zumbi = Elemento(img =ZUMBI,tit="Zumbi",style=dict(left = 180, top = 40, heigth = 40, width = 170)
    zumbi.entra(CEMITERIO)
    CEMITERIO.vai ()
Historia()