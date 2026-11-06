import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown_biblioteche(self):
        lista_biblioteche=self._model.get_biblioteche()

        return lista_biblioteche

    def popola_dropdown_generi(self):
        lista_generi=self._model.get_generi()
        return lista_generi

    # CALLBACKS DROPDOWN
    # TODO
    def funzione_select_biblioteche(self):
        self._model.get_biblioteca_selezionata(self._view.tendina_biblioteche_sezione_2.value)

    def funzione_select_generi_e_biblioteche(self):
        self._model.get_biblioteca_e_genere_selezionati(self._view.tendina_biblioteche_sezione_2.value, self._view.tendina_generi_sezione_2.value)
        self._model.get_genere_selezionato(self._view.tendina_generi_sezione_2.value)

    # AZIONE: MOSTRA LIBRI
    # TODO
    def funzione_bottone_mostra(self):
        biblioteca=self._view.tendina_biblioteche_sezione_2.value
        genere=self._view.tendina_generi_sezione_2.value
        self._view.contenitore_libri_sezione_3.controls.append(ft.Text(f'{self._model.get_libri_filtrati(biblioteca, genere)}'))

