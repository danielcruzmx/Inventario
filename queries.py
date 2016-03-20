q_select = '''
      select *
      from articulos
      where codigo = %s
'''

q_lista = '''
      select *
      from articulos
'''

q_max_id = '''
      select max(id) + 1 as id
      from articulos
'''

q_upd = '''
      update articulos
      set estado = :estado
      where codigo = %s
'''

q_busca = '''
      select *
      from articulos
      where (upper(titulo) like '%s'
      or upper(autor) like '%s'
      or upper(estado) like '%s')
'''

q_ins = '''
      insert into articulos(
     	id,
     	categoria,
     	titulo,
      autor,
      codigo,
     	editorial,
      estado)
      values (
       		:id,
       		:categoria,
       		:titulo,
       		:autor,
       		:codigo,
       		:editorial,
       		:estado)
'''     
  
q_crea = ''' create table articulos(
  	      id integer primary key,
  	      categoria text,
  	      titulo text,
  	      autor text,
  	      codigo text,
  	      editorial text,
  	      estado text)
'''


#
#   'categoria' : 'libros',
#   'autor' : 'Arturo Fernandez Montoro' ,
#   'titulo' : 'Python 3 al descubierto',
#   'editorial' : 'Alfaomega',
#   'codigo' : '9786077077183'
#
