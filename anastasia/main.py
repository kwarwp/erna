from _spy.vitollino.main import Cena, Elemento, Texto
# Raphael
oceano = "https://mardehistorias.files.wordpress.com/2010/11/oceano.jpg"
nemo = "http://www.araguaiaaquarios.com.br/loja/modules/possequence/images/image_1.jpg"
#Glub Glub
def historia():
   cenaoceano = Cena(img = "https://mardehistorias.files.wordpress.com/2010/11/oceano.jpg")
   nemo = Elemento(img=linkdonemo,
                  tit="nemo",
                  style = dict (top = 150, left = 60, height = 60, width = 200))
   cenaoceano.vai()
historia()