import sl4a

class Form:

    droid = sl4a.Android()

    def __init__(self):
       self.droid.eventClearBuffer()
  
    def entrada_qr(self):
       ret = None
       datos = self.droid.scanBarcode().result
       if datos:
          ret = datos['extras']['SCAN_RESULT']
       return ret

    def menu(self, lista, titulo):    
       self.droid.dialogCreateAlert(titulo)
       self.droid.dialogSetItems(lista)
       self.droid.dialogShow()
       resul = self.droid.dialogGetResponse().result       
       if 'item' in resul:
          return resul['item']
       else:
          return -1
    
    def salida(self):
       self.droid.dialogCreateAlert('Desarrollado por','Daniel Cruz 2015')
       self.droid.dialogSetPositiveButtonText('Ok')
       self.droid.dialogShow()
       
    def busca(self):    
       dato = self.droid.dialogGetInput('Autor, titulo o estado').result
       if dato:
          return dato
       else:
          return None