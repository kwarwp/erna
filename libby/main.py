from _spy.vitollino.main import Cena, Elemento, Texto
# Lana
lugar = "https://media-cdn.tripadvisor.com/media/photo-s/12/f8/68/3d/big-bus-paris-hop-on.jpg"
linkpassaros = https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjX7I2gzYrcAhXFf5AKHYPfByMQjRx6BAgBEAU&url=http%3A%2F%2Fbemfacilpng.blogspot.com%2F2015%2F05%2Fpassaros-png.html&psig=AOvVaw0Drf1_1EWA-AN3_TzV-nb5&ust=1530970918980391
#piupiupiupiu
def historia():
     Cenalugar = Cena(img = "https://media-cdn.tripadvisor.com/media/photo-s/12/f8/68/3d/big-bus-paris-hop-on.jpg")   
     passaros = Elemento(img = linkpassaros, tit = "passaros", style = dict (top =  100,left =  160,height = 100, width = 100))
     txtpassaros = Texto(Cenalugar, "HELP!!!”)
     passaros.vai = txtpassaros.vai
     passaros.entra(Cenalugar)
     Cenalugar.vai()
historia()
