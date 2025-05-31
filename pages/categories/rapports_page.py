import flet as ft
from datetime import date
from pages.categories.data.gestion import total_lait_produit, total_vendu, lait_restant, data, supprimer_production, supprimer_vente, supprimer_boeuf, total_lait_produit_user, total_vendu_user, lait_restant_user
from pages.stores.store import connector

def get_rapports_page(page: ft.Page):
    jour = str(date.today())

    for c in connector:
        email_connector = c["email"]

    # Affichage des totaux
    total_lait = total_lait_produit_user()
    total_vendu_value = total_vendu_user()
    lait_restant_value = lait_restant_user()

    # Afficher les productions
    def afficher_productions():
        productions_column.controls.clear()
        for a in data["utilisateurs"]:
            if a["email"] == email_connector:
                for b in a["production"]:
                    for prod in a["production"][b]:
                        productions_column.controls.append(
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(f"Date: {b}", size=15, weight="bold", color="#FFAF75", font_family="Arial"),
                                        ft.Text(f"Boeuf: {prod.get('id_boeuf', prod.get('id', ''))}", size=14, color="#5a85e8", font_family="Georgia"),
                                        ft.Text(f"Litres produits: {prod['litres']:,.2f} L", size=14, color="#5a85e8", font_family="Georgia"),
                                        ft.Row([
                                            ft.Text(f"{email_connector}", size=10, color="#e0e1e4", font_family="Georgia"),
                                        ], alignment=ft.MainAxisAlignment.END)
                                    ],
                                    spacing=5,
                                ),
                                border_radius=10,
                                bgcolor="#3E3E3E",
                                margin=2,
                                padding=ft.padding.only(left=10, right=10, top=0, bottom=10),
                                alignment=ft.alignment.center,
                                width=180,
                                expand=True,
                            )
                        )


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
                                    ft.Text(f"Date: {b}", size=15, weight="bold", color="#D79C72", font_family="Arial"),
                                    ft.Text(f"Litres vendus: {vente['litres_vendus']:,.2f} L", size=14, color="#5a85e8", font_family="Georgia"),
                                    ft.Text(f"Prix/L: {vente['prix_litre']:,.2f} Ar", size=14, color="#5a85e8", font_family="Georgia"),
                                    ft.Text(f"Revenu: {vente['revenu']:,.2f} Ar", size=14, color="#5a85e8", font_family="Georgia"),
                                    ft.Row([
                                        ft.Text(f"{email_connector}", size=10, color="#ffffff", font_family="Georgia"),
                                    ], alignment=ft.MainAxisAlignment.END),
                                ],
                                spacing=5,
                            ),
                            border_radius=10,
                            bgcolor="#3E3E3E",
                            margin=2,
                            padding=ft.padding.only(left=10, right=10, top=0, bottom=10),
                            alignment=ft.alignment.center,
                            width=180,
                            expand=True,
                        )
                    )               


    productions_column = ft.Column(alignment=ft.MainAxisAlignment.START)
    vente_jornaliere = ft.Column(alignment=ft.MainAxisAlignment.START)

    afficher_productions()
    afficher_ventes_journaliere()

    content = ft.Column(
        controls=[
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Column([  # <-- fix: wrap the two rows in a Column
                            ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Text(str(total_lait), size=16, weight="bold", color="#ffffff", font_family="Georgia"),
                                        alignment=ft.alignment.center,
                                        width=80,
                                        height=80,
                                        bgcolor="#06070B77",
                                        border_radius=50,
                                        border=ft.border.all(4, "#265FB4"),
                                    ),
                                    ft.Container(
                                        content=ft.Text(str(total_vendu_value), size=16, weight="bold", color="#ffffff", font_family="Georgia"),
                                        alignment=ft.alignment.center,
                                        width=80,
                                        height=80,
                                        bgcolor="#06070B77",
                                        border_radius=50,
                                        border=ft.border.all(4, "#27B63C"),
                                    ),
                                    ft.Container(
                                        content=ft.Text(str(lait_restant_value), size=16, weight="bold", color="#ffffff", font_family="Georgia"),
                                        alignment=ft.alignment.center,
                                        width=80,
                                        height=80,
                                        bgcolor="#06070B77",
                                        border_radius=50,
                                        border=ft.border.all(4, "#ca2c2c"),
                                    ),
                                ], alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            ),
                            ft.Row(
                                [
                                    ft.Text("Total lait produit(L)", size=13, color="#ffffff", font_family="Georgia"),
                                    ft.Text("Total lait vendu(Ar)", size=13, color="#ffffff", font_family="Georgia"),
                                    ft.Text("Lait restant(L)", size=13, color="#ffffff", font_family="Georgia"),
                                ], alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            ),
                        ])
                    ),
                    ft.Divider(),
                    ft.Row([
                        ft.Text("Productions", size=15, weight="bold", color="#ffffff", font_family="Georgia"),
                        ft.Text("Ventes journalières", size=15, weight="bold", color="#ffffff", font_family="Georgia"),
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    ft.Row([productions_column,vente_jornaliere], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    ft.Divider(),
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
                alignment=ft.MainAxisAlignment.START,
            ),
        ],
        height=1000,
    )

    return content