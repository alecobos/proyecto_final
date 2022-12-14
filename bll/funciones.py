from dal.db import Db

def listar():
    sql = '''select f.IdFuncion, p.NombrePelicula, p.Idioma, s.NombreSala, f.Fecha, F.Hora, s.Tipo, p.Clasificacion
from Funciones f INNER JOIN Salas s, Peliculas p
WHERE f.IdSala = s.IdSala AND f.IdPelicula = p.IdPelicula'''
    result = Db.consultar(sql)
    return result