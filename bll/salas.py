from dal.db import Db

def listar():
    sql = '''SELECT IdSala, NombreSala, Tipo, Capacidad
            from Salas'''
    result = Db.consultar(sql)
    return result


def obtener_id(id):
    sql = '''SELECT IdSala, NombreSala, Tipo, Capacidad
            from Salas
        WHERE IdSala = ?;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def existe(sala):
    sql = "SELECT COUNT(*) FROM Salas WHERE Sala = ? ;"
    parametros = (sala,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1


def agregar(nombresala, tipo, capacidad):    
    sql = "INSERT INTO Salas(NombreSala, Tipo, Capacidad) VALUES(?, ?, ?);"
    parametros = (nombresala, tipo, capacidad)
    Db.ejecutar(sql, parametros)

def actualizar(id, nombresala, tipo, capacidad):    
    sql = "UPDATE Salas SET NombreSala = ?, Tipo = ?, Capacidad = ? WHERE IdSala = ? ;"
    parametros = (id, nombresala, tipo, capacidad)
    Db.ejecutar(sql, parametros) 