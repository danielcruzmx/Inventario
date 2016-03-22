q_select = '''
      select *
      from articulos
      where cve_isbn = %s
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
      where cve_isbn = %s
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
      cve_isbn,
     	editorial,
      estado)
      values (
       		:id,
       		:categoria,
       		:titulo,
       		:autor,
       		:cve_isbn,
       		:editorial,
       		:estado)
'''     
  
q_crea = ''' create table articulos(
  	      id integer primary key,
  	      categoria text,
  	      titulo text,
  	      autor text,
  	      cve_isbn text,
  	      editorial text,
  	      estado text)
'''


#
#   'categoria' : 'libros',
#   'autor' : 'Arturo Fernandez Montoro' ,
#   'titulo' : 'Python 3 al descubierto',
#   'editorial' : 'Alfaomega',
#   'cve_isbn' : '9786077077183'
#