from _spy.vitollino.main import Cena, Elemento, Texto
#Breno celso
tristeza = "http://clinicaintervir.com.br/wp-content/uploads/2018/01/imagem-depress%C3%A3o-750x480.jpg"
nomeferro = "https://png.pngtree.com/element_pic/16/12/27/f8d3f37ac40656a40836942a56f8fa53.jpg"
#um carro bateu em um pilar de ferro e esposa ficou muito triste
def historia():
       cenaTristreza = Cena(img = "http://clinicaintervir.com.br/wp-content/uploads/2018/01/imagem-depress%C3%A3o-750x480.jpg")
       nomeferro = Elemento(img = "https://png.pngtree.com/element_pic/16/12/27/f8d3f37ac40656a40836942a56f8fa53.jpg", tit = "Destruiçaõ", style = dict (top =60, left =150, height =200, width =60))
       nomeferro.entrar(cenaTristeza)
       cenaTristreza.vai()
      
historia()