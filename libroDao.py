from queries import *
from data import BDatos

class LibroDao:

  bd = BDatos()
    
  def crea_tabla(self):
    self.bd.result(q_crea,{})

  def existe_isbn(self, isbn):
    query = q_select % isbn
    self.bd.result(query,{})
    if self.bd.row:
       return self.bd.row[0]
    else:
       return None

  def max_id(self):
    self.bd.result(q_max_id,{})
    if self.bd.row:
       return self.bd.row[0]
    else:
       return None

  def lista(self):
    self.bd.result(q_lista,{})
    if self.bd.row:
       return self.bd.row
    else:
       return []

  def act_estado(self, isbn, estado):
    query = q_upd % isbn
    self.bd.result(query, estado)

  def insert(self, data):
    self.bd.result(q_ins, data)
    
  def busca(self, dato):
    query = q_busca % (dato, dato, dato)
    self.bd.result(query,{})
    if self.bd.row:
       return self.bd.row  
    else:
       return[] 
