import ast
import sys

def str_to_dict(cadena):
  ret = {}
  if cadena:
    cad = cadena.replace('\n',' ').replace('\r',' ')
    ret = ast.literal_eval(cad)
  return ret     

def dict_to_list(dic):
  lista = []
  for key, value in dic.items():
     temp = key + ': ' + str(value)
     lista.append(temp)
  return lista

def cls_screen(self):
  sys.stdout.flush()
  