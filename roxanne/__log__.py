
{'date': 'Fri Jul 13 2018 10:17:42.241 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 4
  ferro "https://png.pngtree.com/element_pic/16/12/27/f8d3f37ac40656a40836942a56f8fa53.jpg"
         ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Jul 13 2018 10:18:22.512 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 9
    historia()
  module <module> line 7
    cenatristreza = Cena(img = "http://f.i.uol.com.br/fotografia/2016/05/02/606604-970x600-1.jpg")
TypeError: 'module' object is not callable
'''},