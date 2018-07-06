# erna.soraya.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
#renata
cidade = "https://media.wsimag.com/attachments/87d7e431ded78e4f143c7e84db3e01a694a8276e/store/fill/1020/574/cc1c81d29f191e0dd08e953179b0d2d3baa88ab791485adf5c60ca97fdd2/Chongqing-China-Tempestade-sobre-a-cidade.jpg"
linkaviao = "http://i.imgur.com/geBGkhx.png"
#Help!!!
def historia():
     cenacidade = Cena(img = "https://media.wsimag.com/attachments/87d7e431ded78e4f143c7e84db3e01a694a8276e/store/fill/1020/574/cc1c81d29f191e0dd08e953179b0d2d3baa88ab791485adf5c60ca97fdd2/Chongqing-China-Tempestade-sobre-a-cidade.jpg")
     aviao = Elemento(img = linkaviao,tit = "Aviao", style = dict (top = 260, left = 150, height = 60, width = 60))
     aviao.entra(cenacidade)
     cenacidade.vai()
historia()