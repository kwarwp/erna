# mariahduarte
from _spy.vitollino.main import Cena, Elemento, Texto

GOKU ="http://img01.deviantart.net/01b7/i/2016/350/d/7/goku_universo_survival_dbs_by_jaredsongohan-daru6yn.png"
def Historia():
    cenaTeatro = Cena(img ="https://supygirls.readthedocs.io/en/latest/_images/DungeonWall.jpg")
    goku = Elemento(img= GOKU,
           tit ="Goku",
           style = dict(left=100, top=157,width=60, height=200))
    goku.entra(cenaTeatro)
    txtgoku=Texto (cenaTeatro, "Hello")
    goku.vai=txtgoku.vai
    cenaTeatro.vai()
Historia()