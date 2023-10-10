# erna.courtney.main.py
#__author__glaucio

""" Página de entrada do jogo Ilha Proibida.
..codeauthor:: Glaucio <glaucio75@ufrj.br>

Changelog
---------
..versionadded:: 23.10
    Classes Ilha, Terreno, Peao(10).

..versionadded:: 23.09
    Versão Inicial (26).
    
"""
    
from _spy.vitollino.main import Cena, Elemento,STYLE
from julia.main import IlhaProibida as Ilha
from julia import main as jmain
from anastasia import main as amain
STYLE["width"] = 800
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg" 
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"

#class IlhaProibida(jmain.IlhaProibida):
#class IlhaProibida(Ilha):
"""essas chamadas de parâmetros é para herdar as classes que estão em outros códigos que eu quero usar 
"""
class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, X=10, Y=50, W=100, H=100, tit = "Portão de Bronze", cena=oceano)
        palacio = Elemento(PALACIO_CORAL, x= 120, Y=50, W=100, H=100, cena=oceano)
        self.peao = Peao(oceano)
        
    

  
class Peao:
    """Marcador usado para definir a posição do jogador nos terrenos.
    """
    
    def __init__(self, oceano):
        self.peao = Elemento(PAWN, x=20, y=20, w=80, h=80, cena=oceano, vai=self.move)
    
    def move(self, ev=None):
        self.peao.x = 150
        
if __name__== "__main__"
    #IlhaProibida()
