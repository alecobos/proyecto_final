from dal.db import Db

def listar():
    sql = '''SELECT IdSala, NombreSala, Tipo, Capacidad
            from Salas'''
    result = Db.consultar(sql)
    return result