# Jacqueline
from _spy.vitollino.main import Cena, Elemento, Texto

ZUMBI ="https://images.vexels.com/media/users/3/149934/isolated/preview/37d8e9ddd0a5a330004d4a8f0b6ef8fb-sereia-criatura-aqu-tica-silueta-by-vexels.png"

def Historia():
    ILHA = Cena(img ="https://ogimg.infoglobo.com.br/in/21993934-fe0-499/FT1086A/652/x06_10_2017.-Jornal-O-Globo.-Ilha-Grande-4.jpg.pagespeed.ic.NPxcsQST9i.jpg")
    zumbi9= Elemento(img=ZUMBI,tit="Sereia",style=dict(left=150, top=60, width=60,height=200))
    zumbi9.entra(ILHA)
    ILHA.vai ()
Historia()
