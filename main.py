from utils import *
from libro import Libro
from view import Form

__author__ = 'Daniel Cruz <danielcruzmx@hotmail.com>'

s_opc = [ 'Consulta, agrega libro', 
          'Prestamo, devolucion',
          'Ver catalogo',
          'Busca libro',
          'Salir'
        ]

if __name__ == '__main__':
  f = Form()
  l = Libro({})
  l.crea()
  while True:
    opc = f.menu(s_opc, 'Opciones')
    if opc != 4:
     l = Libro({})
     if opc in (0,1):
       s = str_to_dict(f.entrada_qr())
       l = Libro(s)
       if l.existe_libro():
          if opc == 1:
            l.actualiza()
       else:
          l.agrega()
       l.existe_libro()
       f.menu(dict_to_list(l.data), 'Titulo')
     if opc == 2:
       tit = []
       cat = l.catalogo()
       for d in cat:
          tit.append(d['titulo'])
       elem = f.menu(tit, 'Catalogo')   
       if elem != -1:
         lib = cat[elem]
         f.menu(dict_to_list(lib),'Titulo')
     if opc == 3:
       dat = f.busca()
       if dat:
         tit = []
         cat = l.busca(dat)
         for d in cat:
            tit.append(d['titulo'])
         if tit == []:
            tit.append('No hay elementos')
            f.menu(tit,'Titulo')
         else:
            elem = f.menu(tit, 'Catalogo')
            if elem != -1:
               lib = cat[elem]
               f.menu(dict_to_list(lib), 'Titulo')
    else:
       break
  f.salida()
