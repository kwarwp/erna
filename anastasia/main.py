from _spy.vitollino.main import Cena, Elemento, Texto
# Raphael
oceano = "https://mardehistorias.files.wordpress.com/2010/11/oceano.jpg"
nemo = "http://www.araguaiaaquarios.com.br/loja/modules/possequence/images/image_1.jpg"
#Glub Glub
def historia():
   cenaoceano = Cena(img="https://mardehistorias.files.wordpress.com/2010/11/oceano.jpg")              
   nemo = Elemento(img="http://www.araguaiaaquarios.com.br/loja/modules/possequence/images/image_1.jpg",
                  tit="nemo",
                  style = dict (top = 180, left = 40, height = 40, width = 170))
   nemo.entra(cenaoceano)
   txtNemo = Texto(cenaoceano,
                  "Glub Glub")
   nemo.vai = txtNemo.vai
   cenaoceano.vai()
historia()