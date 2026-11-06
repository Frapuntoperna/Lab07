from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        #IL PROBLEMA è QUA, CE DA CAPIRE BENE QUALE DELLE 3 LISTE DERIVANTI DAI DAO DEVE PASSARE NEL CONTROLLER PER ESSERE
        #STAMPATA
        libri_filtrati_biblioteca=self._biblioteca_dao.get_libri_filtro_biblioteca(biblioteca)
        libri_filtrati_biblioteca_e_genere=self._biblioteca_dao.get_libri_filtro_biblioteca_e_genere(biblioteca, genere)
        libri_filtrati_genere=self._libro_dao.get_libri_filtro_genere(genere)
        libri_non_filtrati=self._libro_dao.get_libri_totali()

        lista_libri_da_mostrare=[]

        if libri_filtrati_biblioteca is not None and biblioteca is not None:
            lista_libri_da_mostrare=libri_filtrati_biblioteca

        elif libri_filtrati_genere is not None and genere is not None:
            lista_libri_da_mostrare=libri_filtrati_genere

        elif libri_filtrati_biblioteca_e_genere is not None and biblioteca is not None and genere is not None:
            lista_libri_da_mostrare=libri_filtrati_biblioteca_e_genere

        elif lista_libri_da_mostrare is not None and genere is None and biblioteca is None:
            lista_libri_da_mostrare=libri_non_filtrati

        print(lista_libri_da_mostrare)


        return lista_libri_da_mostrare


    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        lista_generi=[]
        for libro in self._libro_dao.get_libri_totali():
            if libro.genere not in lista_generi:
                lista_generi.append(libro.genere)
        return lista_generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        lista_biblioteche=self._biblioteca_dao.get_biblioteche_totali()
        return lista_biblioteche

    def get_biblioteca_selezionata(self, nome_biblioteca):
        biblioteca=nome_biblioteca
        self._biblioteca_dao.get_libri_filtro_biblioteca(biblioteca)

    def get_biblioteca_e_genere_selezionati(self, nome_biblioteca, nome_genere):
        genere=nome_genere
        biblioteca=nome_biblioteca
        self._biblioteca_dao.get_libri_filtro_biblioteca_e_genere(biblioteca, genere)

    def get_genere_selezionato(self, nome_genere):
        genere=nome_genere
        self._libro_dao.get_libri_filtro_genere(genere)
