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
    
|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Glaucio Santos** <glaucio75@ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

    
from _spy.vitollino.main import Cena, Elemento,STYLE
from julia.main import IlhaProibida as Ilha
#from julia import main as jmain
#from anastasia import main as amain
STYLE["width"] = 800
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg" 
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"

#class IlhaProibida(jmain.IlhaProibida):
#class IlhaProibida(Ilha):
"""essas chamadas de parâmetros tem por fim herdar as classes que estão em outros códigos que eu quero usar 
"""


class IlhaProibida:
    """Representa a classe principal do jogo

Terrenos
   Locais onde o peão pode ficar
    """

    def __init__(self):
        self.oceano = oceano = Cena(IMAGEM).vai()
        info_terrenos = [PORTAO_BRONZE, PALACIO_CORAL, PORTAO_BRONZE, PALACIO_CORAL]
        self.terrenos = [Terreno(cena=oceano, posy=50, posx = px*110+10, local=lc)
        for px, lc in enumerate(info_terrenos)]
        self.peao = Peao(self)
        self.terrenos[1].ocupa(self.peao)
        """
        portao = Elemento(PORTAO_BRONZE, X=10, Y=50, W=100, H=100, tit = "Portão de Bronze", cena=oceano)
        palacio = Elemento(PALACIO_CORAL, x= 120, Y=50, W=100, H=100, cena=oceano)
        self.peao = Peao(oceano)
        """
    def direita(self, terreno):
        """Move o peao para a direita.
    
    :param terreno:: O terreno aonde está o peão
    :return: O terreno para onde vai
        """
    
    aqui = self.terrenos.index(terreno)
    return self.terrenos[aqui+1]
    
class Terreno:
    def __init__(self, local, x= posx, y= posy, w = 100, h = 100,
    cena = cena)
    self.peao = None
    self.posx, self.posy = posx, posy
    
    def ocupa(self, peao):
        self.peao = peao
        peao.mover(self.posx, self)

  
class Peao:
    """Marcador usado para definir a posição do jogador nos terrenos.
    """
    
    def __init__(self, ilha):
        self.peao = Elemento(PAWN, x=20, y=20, w=80, h=80,
        cena=ilha.oceano, vai=self.move)
        self.terreno = None
        self.ilha = ilha
        #self.peao.vai = self.move
    
    def move(self, ev=None): #Corrigir: não está condizente!
        terreno_destino = self.ilha.direita(0) #(self.terreno)
        self.peao.y = 300
    
    def move_(self, ev=None):  # Corrigir: não está condizente!
        terreno_destino = self.ilha.direita(self.terreno)
        #self.peao.x = 170
        terreno_destino.ocupa(self)  
         
    def mover(self, x, terreno):
        self.terreno = terreno
        self.peao.x = x
    
        
if __name__== "__main__"
    #print((amain.__name__))
    IlhaProibida()
    #IlhaProibida()