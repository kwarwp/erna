#bruno
from _spy.vitollino.main import Cena, Elemento, Texto

ZUMBI ="https://images.vexels.com/media/users/3/137945/isolated/preview/fbeb505577b4a8b8b87018f254d43c7e--cone-do-transporte-de-barco-by-vexels.png"

def Historia():
    ILHA = Cena(img ="https://ogimg.infoglobo.com.br/in/21993934-fe0-499/FT1086A/652/x06_10_2017.-Jornal-O-Globo.-Ilha-Grande-4.jpg.pagespeed.ic.NPxcsQST9i.jpg")
    zumbi9= Elemento(img=ZUMBI,tit="ZUMBI",style=dict(left=150, top=60, width=60,height=200))
    zumbi9.entra(ILHA)
    ILHA.vai ()
Historia()