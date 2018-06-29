
{'date': 'Fri Jun 29 2018 11:43:35.926 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 8
    historia()
  module <module> line 7
    cenacastelo = Cena(img = "https://upload.wikimedia.org/wikipedia/commons/8/88/Castelo_de_Guimar%C3%A3es_%28Portugal%29.jpg")
TypeError: 'module' object is not callable
'''},