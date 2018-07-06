
{'date': 'Fri Jul 06 2018 10:11:43.620 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 7
  Cenalugar = Cena(img = "https://media-cdn.tripadvisor.com/media/photo-s/12/f8/68/3d/big-bus-paris-hop-on.jpg" 
                                                                                                                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Jul 06 2018 10:32:08.983 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 9
  passarinho.entrar(cenalugar)
  ^
IndentationError: unexpected indent
'''},
{'date': 'Fri Jul 06 2018 10:35:54.223 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 9
  passarinho.entra(cenalugar)
  ^
IndentationError: unexpected indent
'''},
{'date': 'Fri Jul 06 2018 10:36:38.78 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 11
    historia()
  module <module> line 9
    passarinho.entra(cenalugar)
NameError: name 'passarinho' is not defined
'''},