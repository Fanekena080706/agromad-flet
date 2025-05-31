import flet as ft
from datetime import date
from pages.categories.data.gestion import ajouter_production, data, save_data, ajouter_production_user,supprimer_production_user
from pages.stores.store import connector

def get_production_page(page: ft.Page):

    for c in connector:
        email_connector = c["email"]

    
    message = ft.Text("")
    liste_journaliere = ft.Column()

    def supprimer_prod_user_click(jour, id_boeuf):
        supprimer_production_user(jour, id_boeuf)
        afficher_productions_usser()
        page.update()

    # Actualiser les enregistrements du jour
    def afficher_productions_usser():
        liste_journaliere.controls.clear()
        for a in data["utilisateurs"]:
            if a["email"] == email_connector:
                for b in a["boeufs"]:
                    if b["actif"] and b["production"]:
                        liste_journaliere.controls.append(
                            ft.Text(f"Production du boeuf {b['id']}({b['nom']})", size=18, weight="bold", color="#ffffff", font_family="Georgia")
                        )
                        for jour in b["production"]:
                            liste_journaliere.controls.append(
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(f"      Date: {jour}:", size=15, weight="bold", color="#FFAF75", font_family="Arial"),
                                            ft.Column(
                                                controls=[
                                                    ft.Text(f"   Litres: {prod['litres']}", size=14, color="#5a89f8", font_family="Georgia")
                                                    for prod in b["production"][jour]
                                                ],
                                                spacing=5,
                                            ),
                                            ft.Row([
                                                ft.IconButton(
                                                    icon=ft.icons.DELETE,
                                                    icon_color="red",
                                                    on_click=lambda e, id_boeuf=b["id"]:supprimer_prod_user_click(jour, id_boeuf),
                                                )
                                            ], alignment=ft.MainAxisAlignment.END)
                                        ],
                                        spacing=7,
                                    ),
                                    border_radius=10,
                                    bgcolor="#3E3E3E",
                                    margin=10,
                                    padding=ft.padding.only(left=10, right=10, top=0, bottom=10),
                                    alignment=ft.alignment.center
                                )
                            )
        

    # Quand on clique sur "Ajouter"
    def enregistrer(e):
        if dropdown_boeufs.value and litres_field.value:
            try:
                litres = float(litres_field.value)
                ajouter_production_user(dropdown_boeufs.value, litres)
                message.value = "✔️ Lait enregistré"
                dropdown_boeufs.value = None
                litres_field.value = ""
                afficher_productions_usser()
                toggle_form(False)
            except ValueError:
                message.value = "❌ Entrez un nombre valide"
        else:
            message.value = "❗ Tous les champs sont obligatoires"
        page.update()


    def toggle_form(visible):
        dropdown_boeufs.visible = visible
        litres_field.visible = visible
        message.visible = visible
        form_container.visible = visible
        page.update()

    # Dropdown avec les bœufs actifs
    dropdown_boeufs = ft.Dropdown(
        label="Choisir un bœuf",
        options=[
            ft.dropdown.Option(b["id"]) for b in connector[0]["boeufs"] if b["actif"]
        ],
        width=300,
        visible=True,
        menu_height=200,
        color="#ffffff",
    )

    litres_field = ft.TextField(label="Litres de lait", width=200,visible=True, color="#ffffff")

    form_container = ft.Container(
        content=ft.Column(
            controls=[
                dropdown_boeufs,
                litres_field,
                message,
                ft.Row([
                    ft.ElevatedButton("Annuler", on_click=lambda e: toggle_form(False), bgcolor="#e57373", color="white"),
                    ft.ElevatedButton("Ajouter", on_click=enregistrer, bgcolor="#4CAF50", color="white"),
                ], spacing=10),
            ],
            spacing=10
        ),
        bgcolor="#292a2e",
        padding=20,
        border_radius=10,
        visible=False,
        width=350,
        top=40,
        left=20,
        expand=False
    )

    afficher_productions_usser()

    add_button = ft.IconButton(
        icon=ft.icons.ADD,
        icon_color="white",
        bgcolor="#5ab6e8",
        tooltip="Ajouter une production",
        on_click=lambda e: toggle_form(True)
    )

    content = ft.Stack(
        controls=[
            ft.Column(
                controls=[
                    ft.Row([
                        ft.Text("Production de lait", size=20, weight="bold",color="#5ab6e8"),
                        add_button,
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Divider(),
                    liste_journaliere,
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
                alignment=ft.MainAxisAlignment.START,
            ),
            form_container,
        ],
        height=1000,
    )

    return content