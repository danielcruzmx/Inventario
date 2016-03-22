from libroDao import LibroDao

class Libro:
  
  lib = LibroDao()
  stock = {'estado':'en stock'}
  prest = {'estado':'prestamo'}

  def __init__(self, datos):
    if type(datos) is dict:
      self.data = datos
    else:
      self.data = {}
   
  def existe_libro(self):
    ret = False
    if self.data:
      res = self.lib.existe_isbn(self.data['cve_isbn'])
      if res:
         self.data = res
         ret = True
    return ret
  
  def catalogo(self):
     return self.lib.lista()
  
  def agrega(self):
    if self.data:
       res = self.lib.max_id()
       if res:
         self.data.update(res)
         self.data.update(self.stock)
         self.lib.insert(self.data)
        
  def actualiza(self):
    if self.data:
      isbn = self.data['cve_isbn']
      if self.data['estado'] == 'en stock':
         self.lib.act_estado(isbn, self.prest)
      else:
         self.lib.act_estado(isbn, self.stock)
               
  def busca(self, dato):
     param = '%' + dato.upper() + '%'
     return self.lib.busca(param)
     
  def crea(self):
     self.lib.crea_tabla()
