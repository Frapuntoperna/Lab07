from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca
from model.libro_DTO import Libro

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_biblioteche_totali(self):

        cnx=DBConnect.get_connection()
        if cnx is not None:
            query='SELECT * FROM BIBLIOTECA'

            cursor=cnx.cursor()
            cursor.execute(query)

            self.lista_risultato_biblioteche=[]

            for b in cursor:

                biblioteca=Biblioteca(*b)
                self.lista_risultato_biblioteche.append(biblioteca.nome)

            cursor.close()
            cnx.close()

        return self.lista_risultato_biblioteche

    def get_libri_filtro_biblioteca(self, biblioteca):

        cnx = DBConnect.get_connection()

        if cnx is not None:
            query = 'SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca FROM LIBRO L, BIBLIOTECA B WHERE B.id=L.id_biblioteca AND B.nome = %s'

            cursor = cnx.cursor()
            cursor.execute(query, (biblioteca,))

            self.lista_libri_filtro_biblioteca_e_genere=[]

            for l in cursor:
                l=Libro(*l)
                self.lista_libri_filtro_biblioteca_e_genere.append(l)

            cursor.close()
            cnx.close()

        return self.lista_libri_filtro_biblioteca_e_genere


    def get_libri_filtro_biblioteca_e_genere(self, biblioteca, genere):

        cnx = DBConnect.get_connection()

        if cnx is not None:
            query = 'SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca FROM LIBRO L, BIBLIOTECA B WHERE B.id=L.id_biblioteca AND B.nome = %s AND l.genere = %s'

            cursor = cnx.cursor()
            cursor.execute(query, (biblioteca, genere))

            self.lista_libri_filtro_biblioteca=[]

            for l in cursor:
                l=Libro(*l)
                self.lista_libri_filtro_biblioteca.append(l)

            cursor.close()
            cnx.close()

        return self.lista_libri_filtro_biblioteca
