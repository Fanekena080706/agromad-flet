import flet as ft
from datetime import date
from pages.categories.data.gestion import ajouter_vente, data, ajouter_vente_user, supprimer_vente_user
from pages.stores.store import connector

def get_ventes_page(page: ft.Page):
    jour = str(date.today())

    for c in connector:
        email_connector = c["email"]


    vente_jornaliere = ft.Column()

    def supprimer_vente_user_click(jour):
        supprimer_vente_user(jour)
        afficher_ventes_journaliere()
        page.update()

    def afficher_ventes_journaliere():
        vente_jornaliere.controls.clear()
        for a in data["utilisateurs"]:
            if a["email"] == email_connector:
                for b in a["ventes"]:
                    vente = a["ventes"][b]
                    vente_jornaliere.controls.append(
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(f"Date: {b}", size=15, weight="bold", color="#FFAF75", font_family="Arial"),
                                    ft.Text(f"Litres vendus: {vente['litres_vendus']:,.2f} L", size=14, color="#5a85e8", font_family="Georgia"),
                                    ft.Text(f"Prix par litre: {vente['prix_litre']:,.2f} Ar", size=14, color="#5a85e8", font_family="Georgia"),
                                    ft.Text(f"Revenu: {vente['revenu']:,.2f} Ar", size=14, color="#5a85e8", font_family="Georgia"),
                                    ft.Row([
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            icon_color="red",
                                            on_click=lambda e, jour=b: supprimer_vente_user_click(jour),
                                        )
                                    ], alignment=ft.MainAxisAlignment.END)
                                ],
                                spacing=5,
                            ),
                            border_radius=10,
                            bgcolor="#3E3E3E",
                            margin=10,
                            padding=ft.padding.only(left=10, right=10, top=0, bottom=10),
                            alignment=ft.alignment.center
                        )
                    )


    afficher_ventes_journaliere()

    def toggle_form(visible):
        form_container.visible = litres_field.visible= prix_field.visible = visible
        page.update()

    litres_field = ft.TextField(label="Litres vendus", width=200, color="#ffffff", bgcolor="#1B1B1B", visible=False)
    prix_field = ft.TextField(label="Prix par litre (Ar)", width=200, color="#ffffff", bgcolor="#1B1B1B", keyboard_type=ft.KeyboardType.NUMBER, visible=False)
    message = ft.Text("", color="red", visible=False)
    revenu_field = ft.Text("")

    def enregistrer_vente(e):
        if litres_field.value and prix_field.value:
            try:
                litres = float(litres_field.value)
                prix = float(prix_field.value)
                ajouter_vente_user(litres, prix, jour)
                revenu = litres * prix
                revenu_field.value = f"💰 Revenu du jour : {revenu:,.0f} Ar"
                litres_field.value = ""
                prix_field.value = ""
                toggle_form(False),
                afficher_ventes_journaliere()
                page.update()
            except ValueError:
                message.value = "❌ Champs numériques invalides"
        else:
            message.value = "❗ Tous les champs sont obligatoires"
        page.update()

    form_container = ft.Container(
        content=ft.Column(
            controls=[
                message,
                litres_field,
                prix_field,
                ft.Row([
                    ft.ElevatedButton("Annuler", on_click=lambda e: toggle_form(False), bgcolor="#e57373", color="white"),
                    ft.ElevatedButton("Enregistrer", on_click=enregistrer_vente, bgcolor="#4CAF50", color="white"),
                ], spacing=5),
            ]
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

    enregistrer_btn = ft.IconButton(
        icon=ft.icons.SAVE,
        icon_color="white",
        bgcolor="#5ab6e8",
        on_click=lambda e: toggle_form(True),
    )
    


    content = ft.Stack(
        controls=[
            ft.Column(
                controls=[
                    ft.Row([
                        ft.Text("Ventes de lait", size=20, weight="bold", color="#5ab6e8"),
                        enregistrer_btn,
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Divider(),
                    message,
                    vente_jornaliere,
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