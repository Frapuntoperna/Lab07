import mysql

from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_libri_totali(self):
        cnx = DBConnect.get_connection()

        query = 'SELECT * FROM LIBRO'

        cursor = cnx.cursor()
        cursor.execute(query)

        lista_risultato_libri = []

        for g in cursor:
            libro = Libro(*g)
            lista_risultato_libri.append(libro)

        cursor.close()
        cnx.close()

        return lista_risultato_libri

    def get_libri_filtro_genere(self, genere):
        cnx = DBConnect.get_connection()
        query = 'SELECT * FROM LIBRO where genere = %s'

        cursor=cnx.cursor()
        cursor.execute(query, (genere,))

        lista_libri_filtro_genere = []

        for l in cursor:
            libro=Libro(*l)
            lista_libri_filtro_genere.append(libro)



        cursor.close()
        cnx.close()

        return lista_libri_filtro_genere
