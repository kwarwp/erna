# mariahduarte
from _spy.vitollino.main import Cena, Elemento, Texto

GOKU ="https://i.ytimg.com/vi/jEjtNGZnsak/hqdefault.jpg"
def Historia():
    cenaTeatro = Cena(img ="http://1.bp.blogspot.com/-aGwacYjRKw8/T-St9kEVvMI/Avs/ximTg6O8XUA/s1600/ESCENARIOS29+%282%.jpg")
    goku = Elemento(img= GOKU,
           tit ="Goku",
           style = dict(left=150, top=60,width=60, height=200))
    goku.entra(cenaTeatro)
    txtGoKu=Texto (cenaTeatro, "Hello")
    goku=GoKutxt
    cenaTeatro.vai()
Historia()