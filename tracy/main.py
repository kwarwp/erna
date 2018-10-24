# DANIEL
from _spy.vitollino.main import Cena, Elemento,Texto

CACADOR="http://1.bp.blogspot.com/-0kys80OhYn4/U955vuWvpKI/AAAAAAAAZU4/LoppJ0dcKJA/s1600/guardioesdagalaxia_sess%C3%A3o+cr%C3%ADtica.png"
def Historia():
    cenaFloresta=Cena(img="https://beira.pt/coolkids/wp-content/uploads/sites/7/2014/08/universo.png")
    cacador = Elemento(img= CACADOR,
              tit ="Caçador",
              style = dict(left=165,top=60, width=60, height=200))
    cacador.entra(cenaFloresta)
    txtcacador = Texto (cenaFloresta, "Hello")
    cacador.vai = txtcacador.vai
    cenaFloresta.vai()
Historia()