import sqlite3

class BDatos:

    s_path = '/storage/emulated/0/com.hipipal.qpyplus/projects3/AppInventario/stock.db3'

    def __init__(self):
      self.row = []

    def result(self, query, param):
      self.row = []
      try:
        db = sqlite3.connect(self.s_path)
        cur = db.cursor()
        cur.execute(query, param)
        res = self.dictfetchall(cur)        
        if res:
          self.row = res
        else:
          self.row = []
        db.commit()
        db.close()
      except:
        print(" Except BD ")

    def dictfetchall(self,cursor):
      desc = cursor.description
      return [
       dict(zip([col[0] for col in desc], row))
       for row in cursor.fetchall()
      ]  