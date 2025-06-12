import flet as ft
from pages.categories.data.gestion import ajouter_boeuf, data, supprimer_boeuf, supprimer_boeuf_user
from pages.categories.data.data_stote import save_data
from pages.stores.store import connector

def get_boeufs_page(page: ft.Page):

    for c in connector:
        email_connector = c["email"]
    # Zone pour afficher la liste permanente
    boeufs_list = ft.Column()
    
    # Message de retour
    message = ft.Text("",color="red")

    def supprimer_boeuf_click(id):
        supprimer_boeuf_user(id)
        load_boeufs()
        page.update()
    
    # Fonction pour charger la liste des bœufs
    def load_boeufs():
        boeufs_list.controls.clear()
        for a in data["utilisateurs"]:
           
           #print(connector["email"])
            if a["email"] == email_connector:
                for b in a["boeufs"][:]:
                    if b["actif"]:
                        rows_vacin = []
                        nbVacin = len(b["vacination"])
                        for v in range(0, len(b["vacination"]), 1):
                            row_vacin = b["vacination"][v:v+1]
                            row = ft.Row(
                                [
                                    ft.Text(f"✔️-{cat["type"]} ", color="#5a85e8", size=15, font_family="Georgia", italic=True,)
                                for j, cat in enumerate(row_vacin)
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                height=30,
                                expand=True
                            )
                            rows_vacin.append(row)
                            
                        boeufs_list.controls.append(
                            ft.Container(
                                content=ft.Column([
                                    ft.Row([
                                        ft.Column([
                                            ft.Text(f"ID: {b['id']}", color="#5a85e8", size=22, font_family="Georgia"),
                                            ft.Text(f"Nom: {b['nom']}", color="#5a85e8", size=22, font_family="Georgia"),
                                            ft.Container(
                                                content=ft.Text(f"🐄 {b['race']}", color="#F9ECEC", size=17, weight="bold"),
                                                bgcolor="#9AE283",  
                                                padding=2,
                                                border_radius=3,
                                                width=150,
                                                height=50,
                                                alignment=ft.alignment.center,
                                            ),
                                        
                                            ft.Container(
                                                content=ft.Text(f"Sexe:{b['sexe']}", color="#EEE4E4", size=17, weight="bold"),
                                                bgcolor="#2e7d32",  
                                                padding=2,
                                                border_radius=3,
                                                width=150,
                                                height=50,
                                                alignment=ft.alignment.center,
                                            ),
                                        ]),
                                        ft.Column([
                                            ft.Text(f"{nbVacin} Vacin effectuée:", color="#FFAF75", size=15, weight="bold"),
                                            ft.Column(rows_vacin, scroll=ft.ScrollMode.AUTO, expand=True,alignment=ft.MainAxisAlignment.START),
                                        ]),
                                    ], alignment= ft.MainAxisAlignment.SPACE_AROUND, expand=True),
                                    ft.Row([
                                        ft.Text(f"{email_connector}", size=10, color="#313132", font_family="Georgia"),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            icon_color="red",
                                            tooltip="Supprimer",
                                            on_click=lambda e, id=b["id"]: supprimer_boeuf_click(id)
                                        ),
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                    
                                ],
                                alignment= ft.MainAxisAlignment.START,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                expand=True
                                ),
                                
                                bgcolor="#C5E0BD",  # Couleur de fond
                                padding=10,
                                border_radius=5,
                                margin=ft.margin.only(bottom=5), # Marge entre les éléments
                                height=250,
                                width=400,
                            ),
                        )
                    else:
                        rows_vacin = []
                        nbVacin = len(b["vacination"])
                        for v in range(0, len(b["vacination"]), 1):
                            row_vacin = b["vacination"][v:v+1]
                            row = ft.Row(
                                [
                                    ft.Text(f"✔️-{cat["type"]} ", color="#5a85e8", size=15, font_family="Georgia", italic=True,)
                                for j, cat in enumerate(row_vacin)
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                height='auto',
                                expand=True
                            )
                            rows_vacin.append(row)
                            
                        boeufs_list.controls.append(
                            ft.Container(
                                content=ft.Column([
                                    
                                    ft.Row([
                                        ft.Column([
                                            ft.Text(f"ID: {b['id']}", color="#5a85e8", size=22, font_family="Georgia"),
                                            ft.Text(f"Nom: {b['nom']}", color="#5a85e8", size=22, font_family="Georgia"),
                                            ft.Container(
                                                content=ft.Text(f"🐄 {b['race']}", color="#F9ECEC", size=17, weight="bold"),
                                                bgcolor="#9AE283",  
                                                padding=2,
                                                border_radius=3,
                                                width=150,
                                                height=50,
                                                alignment=ft.alignment.center,
                                            ),
                                        
                                            ft.Container(
                                                content=ft.Text(f"Sexe:{b['sexe']}", color="#EEE4E4", size=17, weight="bold"),
                                                bgcolor="#2e7d32",  
                                                padding=2,
                                                border_radius=3,
                                                width=150,
                                                height=50,
                                                alignment=ft.alignment.center,
                                            ),
                                        ]),
                                        ft.Column([
                                            ft.Text(f"{nbVacin} Vacin effectuée:", color="#FFAF75", size=15, weight="bold"),
                                            ft.Column(rows_vacin, scroll=ft.ScrollMode.AUTO, expand=True,alignment=ft.MainAxisAlignment.START),
                                        ]),
                                    ], alignment= ft.MainAxisAlignment.SPACE_AROUND, expand=True),


                                    ft.Row([
                                        ft.Text(f"{email_connector}", size=10, color="#313132", font_family="Georgia"),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            icon_color="red",
                                            tooltip="Supprimer",
                                            on_click=lambda e, id=b["id"]: supprimer_boeuf_click(id)
                                        ),
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                ],
                                alignment= ft.MainAxisAlignment.START,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                expand=True
                                ),
                                bgcolor="#C5E0BD",  # Couleur de fond
                                padding=10,
                                border_radius=5,
                                margin=ft.margin.only(bottom=5), # Marge entre les éléments
                                height=250,
                                width=400,
                            ),
                        )
        page.update()
    
    # Fonction appelée au clic sur "Ajouter"
    def ajouter_click(e):
        if id_field.value:
            ajouter_boeuf(id_field.value, nom_field.value, race_field.value, sexe_field.value, True if sexe_field.value == "femelle" else False)
            id_field.value = nom_field.value = race_field.value = sexe_field.value = ""
            toggle_form(False)
            load_boeufs()
        else:
            message.value = "ID obligatoire !"
        page.update()
    
    # Fonction pour afficher/masquer le formulaire
    def toggle_form(show):
        id_field.visible = nom_field.visible = race_field.visible =sexe_field.visible= show
        form_container.visible = show
        form_container.expand=show
        page.update()
    
    # Champs de formulaire (initialement invisibles)
    id_field = ft.TextField(label="ID du bœuf", visible=False, color="#000000")
    nom_field = ft.TextField(label="Nom du bœuf", visible=False, color="#000000")
    race_field = ft.TextField(label="Race", visible=False, color="#000000")
    sexe_field = ft.Dropdown(
        label="Sexe",
        options=[
            ft.dropdown.Option("femelle"),
            ft.dropdown.Option("male"),
        ],
        visible=False,
        color="#000000",
    )
    
    # Conteneur pour le formulaire flottant
    form_container = ft.Container(
        content=ft.Column(
            controls=[
                message,
                id_field,
                nom_field,
                race_field,
                sexe_field,
                ft.Row([
                    ft.ElevatedButton("Annuler", on_click=lambda e: toggle_form(False), bgcolor="#e57373", color="white"),
                    ft.ElevatedButton("Ajouter", on_click=ajouter_click, bgcolor="#4CAF50", color="white"),
                ], spacing=10),
            ],
            spacing=10
        ),
        bgcolor="#929292",
        padding=20,
        border_radius=10,
        visible=False,
        width=350,
        top=10,
        left=15,
        expand=False
    )
    
    # Charger initialement la liste
    load_boeufs()
    
    # Bouton d'ajout
    add_button = ft.IconButton(
        icon=ft.icons.ADD,
        icon_color="white",
        bgcolor="#2e7d32",
        tooltip="Ajouter un bœuf",
        on_click=lambda e: toggle_form(True)
    )
    
    content = ft.Stack(
        controls=[
            ft.Column(
                controls=[
                    ft.Row([
                        ft.Text("Liste des bœufs", size=25, weight="bold", color="#2e7d32"),
                        add_button
                    ], alignment="spaceBetween"),
                    ft.Divider(),
                    boeufs_list,
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




