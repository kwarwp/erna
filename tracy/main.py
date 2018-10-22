# DANIEL
from _spy.vitollino.main import Cena, Elemento,Texto

CACADOR="https://2.bp.blogspot.com/-proH1UNc9Yw/V1ShJQ0HsMI/AAAAAAAAGF4/dSBPvEvXwDYFgEi1jLNlIcnc6JwKhmtawCLcB/s1600/o-ca%25C3%25A7ador-e-a-rainha-do-gelo-poshhterk.png"
def Historia():
    cenaFloresta=Cena(img="http://homeroreis.com/wp-content/uploads/2015/10/floresta.jpg")
    cacador = Elemento(img= CACADOR,
              tit ="Caçador",
              style = dict(left=150, top=60, width=60, height=200))
    cacador.entra(cenaFloresta)
    txtcacador = Texto (cenaFloresta, "Hello")
    cacador.vai = txtcacador.vai
    cenaFloresta.vai()
Historia()