from _spy.vitollino.main import Cena, Elemento, Texto
#Alexandre
praia = "https://beachpark.com.br/mobile/wp-content/themes/beachpark/img/praia/apresentacao.jpg"
linkpessoa = "http://www.trackandfield.com.br/wordpress/wp-content/uploads/2014/10/Screen-Shot-2014-10-15-at-4.38.02-PM.png"
# bom dia 
def historia():
     cenapraia = Cena(img = "https://beachpark.com.br/mobile/wp-content/themes/beachpark/img/praia/apresentacao.jpg")
     pessoa = Elemento(img = linkpessoa, tit = "Pessoa", style = dict (top = 60, left = 150, height = 200, width = 60))
     txtpessoa = Texto(cenapraia,"Bom Dia")
     pessoa.vai = txtpessoa.vai
     pessoa.entra(cenapraia)
     cenapraia.vai()
historia()

