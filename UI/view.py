import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO

        self.tendina_biblioteche_sezione_2 = ft.Dropdown(label='Biblioteca', on_select=self.controller.funzione_select_biblioteche, height=200)
        self.tendina_biblioteche_sezione_2.options.append(ft.DropdownOption(key='Nessun Filtro', text='Nessun Filtro'))
        for b in self.controller.popola_dropdown_biblioteche():
            self.tendina_biblioteche_sezione_2.options.append(ft.DropdownOption(key=b, text=b))

        self.tendina_generi_sezione_2 = ft.Dropdown(label='Genere',on_select=self.controller.funzione_select_generi_e_biblioteche, height=200)
        self.tendina_generi_sezione_2.options.append(ft.DropdownOption(key='Nessun Filtro', text='Nessun Filtro'))
        for g in self.controller.popola_dropdown_generi():
            self.tendina_generi_sezione_2.options.append(ft.DropdownOption(key=g, text=g))


        self.riga_sezione_2 = ft.Row(spacing= 120, controls=[self.tendina_biblioteche_sezione_2, self.tendina_generi_sezione_2], alignment=ft.MainAxisAlignment.CENTER)
        # Sezione 3: Libri
        # TODO
        self.bottone_mostra_sezione_3=ft.Button(content='Mostra Libro', on_click=self.controller.funzione_bottone_mostra) #aggiungere funzione on_click
        self.contenitore_libri_sezione_3=ft.ListView(expand=True, spacing=5, padding=10)

        self.riga_prima_sezione_3=ft.Row(spacing=80, controls=[self.bottone_mostra_sezione_3], alignment=ft.MainAxisAlignment.CENTER)
        self.riga_seconda_sezione_3=ft.Row(controls=[self.contenitore_libri_sezione_3], alignment=ft.MainAxisAlignment.CENTER)
        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            self.riga_sezione_2,
            ft.Divider(),
            # Sezione 3: Libri
            # TODO
            self.riga_prima_sezione_3,
            self.riga_seconda_sezione_3,
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
