from dal.db import Db

def listar():
    sql = '''select f.IdFuncion, p.NombrePelicula, p.Idioma, s.NombreSala, f.Fecha, F.Hora, s.Tipo, p.Clasificacion
            from Funciones f INNER JOIN Salas s, Peliculas p
        WHERE f.IdSala = s.IdSala AND f.IdPelicula = p.IdPelicula AND f.Activa = 1;'''
    result = Db.consultar(sql)
    return result

def listar_peliculas():
    sql = '''SELECT p.IdPelicula, p.NombrePelicula
            FROM Peliculas p
            Where p.Activa = 1;'''
    result = Db.consultar(sql)
    return result

def listar_salas():
    sql = '''SELECT s.IdSala, s.NombreSala
            FROM Salas s
            Where s.Activo = 1;''' 
    result = Db.consultar(sql)
    return result

def obtener_id(id):
    sql = '''SELECT NombrePelicula, Genero, Idioma, Clasificacion
            from Peliculas
        WHERE IdPelicula = ? AND Activa = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result