import flet as ft
from pages.stores.store import connector
from pages.categories.data.gestion import ajouter_vaccination,data

def get_vaccination_content(page: ft.Page):
    
    image1=ft.Image(
        src="assets/images/exemple1.jpg",
        width=120,
        height=120,
        border_radius=20,
    )
    image2=ft.Image(
        src="assets/images/exemple2.jpg",
        width=120,
        height=120,
        border_radius=20,
    )

    text1 =ft.Text(
        "La nécessité de certains vaccins dépend des conditions locales ou du niveau d'exposition aux maladies. Des rappels réguliers sont recommandés pour assurer une protection continue. Il est essentiel de suivre les directives du vétérinaire selon le protocole en vigueur.",
        size=12,
        font_family="Georgia",
        expand=True,
        color="#000000"
    )
    text2 =ft.Text(
        "La vaccination joue un rôle clé dans la prévention des maladies infectieuses en élevage. Elle permet de protéger non seulement l'animal vacciné, mais aussi le troupeau dans son ensemble, en réduisant la propagation des agents pathogènes.",
        size=12,
        font_family="Georgia",
        expand=True,
        color="#000000"
    )
    # Données de vaccination (exemple)
    vaccins = [
        {"nom": "Fièvre Aphteuse", "date": "15/06/24", "prochaine": "15/12/24", "effectue": True},
        {"nom": "Brucellose", "date": "01/05/24", "prochaine": "01/11/24", "effectue": False},
        {"nom": "Charbon", "date": "10/04/24", "prochaine": "10/10/24", "effectue": True},
    ]
    
    # Liste des animaux
    animaux = [
        {"id": "BOV-001", "nom": "Bella", "age": "3 ans"},
        {"id": "BOV-002", "nom": "Luna", "age": "2 ans"},
        {"id": "BOV-003", "nom": "Daisy", "age": "4 ans"},
    ]

    vaccinations = [
        {
            "nom":"BVD (Diarrhée Virale Bovine).", 
            "periode":"Veau : 6-8 semaines, rappel après 4 semaines",
            "desc":"Protège contre un virus qui affaiblit le système immunitaire et provoque des diarrhées graves.",
            "image":"assets/images/1bvd.jpg",
        },
        {
            "nom":"FCO (Fièvre Catarrhale Ovine chez bovins).", 
            "periode":"À partir de 3 mois",
            "desc":"Vaccin contre la 'maladie de la langue bleue', transmise par des moucherons.",
            "image":"assets/images/2fco.jpg",
        },
        {
            "nom":"Brucellose", 
            "periode":"Femelle : entre 3 et 8 mois",
            "desc":"Maladie zoonotique grave ; vaccination obligatoire dans certains pays.",
            "image":"assets/images/3brucelose.jpg",
        },
        {
            "nom":"Fièvre Aphteuse", 
            "periode":"	2-3 mois puis rappels annuels",
            "desc":"Très contagieuse ; affecte les sabots et la bouche. Vaccination préventive.",
            "image":"assets/images/4alphteuse.jpg",
        },
        {
            "nom":"Clostridioses (Charbon symptomatique, entérotoxémies...).", 
            "periode":"2 mois, rappel 4-6 semaines après",
            "desc":"Regroupe plusieurs maladies bactériennes graves souvent mortelles.",
            "image":"assets/images/5clostri.jpg",
        },
        {
            "nom":"Leptospirose", 
            "periode":"4-6 mois, puis rappel annuel",
            "desc":"Zoonose transmise par l'urine contaminée ; affecte les reins et la reproduction.",
            "image":"assets/images/6leptos.jpg",
        },
        {
            "nom":"Paratuberculose", 
            "periode":"2-4 semaines ",
            "desc":"Infection bactérienne chronique ; vaccination recommandée dans les zones à risque.(facultatif, selon la région)",
            "image":"assets/images/7paratuber.jpg",
        },
        {
            "nom":"Pasteurellose", 
            "periode":"3 mois, puis rappels tous les 6 mois si nécessaire",
            "desc":"Infection respiratoire sévère ; fréquente en élevage intensif.",
            "image":"assets/images/8pasteurellose.jpg",
        },
        {
            "nom":"VRSB + PI3 (Virus Respiratoire Syncytial Bovin + Parainfluenza). ", 
            "periode":"3-6 semaines",
            "desc":"Prévient les maladies respiratoires chez les jeunes veaux. (intra-nasal ou injectable)",
            "image":"assets/images/9pi3.jpg",
        },
        {
            "nom":"Rage", 
            "periode":"souvent vers 3 mois, puis tous les ans",
            "desc":"Selon la zone, Rage est un vaccin obligatoire dans certaines régions ; protection contre la rage.",
            "image":"assets/images/10rage.jpg",
        },
    ]

    # pour ajouter une vaccination
    
    id_bouef = ft.Dropdown(
                        options=[ft.dropdown.Option(a["id"]) for a in connector[0]["boeufs"]],
                        label="Animal",
                        width=200,
                        color="#000000",
                        border_color=ft.colors.BLACK,
                        border_width=1,
                        border_radius=5,
                    )
    type_vaccin = ft.Dropdown(
                        options=[
                            ft.dropdown.Option("Fièvre Aphteuse"),
                            ft.dropdown.Option("Brucellose"),
                            ft.dropdown.Option("Charbon"),
                            ft.dropdown.Option("Rage"),
                            ft.dropdown.Option("VRSB + PI3"),
                            ft.dropdown.Option("BVD"),
                            ft.dropdown.Option("Leptospirose"),
                            ft.dropdown.Option("FCO"),
                            ft.dropdown.Option("Paratuberculose"),
                            ft.dropdown.Option("Leptospirose"),
                        ],
                        label="Type de vaccin",
                        width=200,
                        color="#000000",
                        border_color=ft.colors.BLACK,
                        border_width=1,
                    )

    date = ft.TextField(label="Date", width=150,color="#000000",border_color=ft.colors.BLACK,border_width=1,border_radius=5)
    message = ft.Text("", color= "#f6a75c" )

    def ajouter_vacc_click(e):
        # Récupération des valeurs du formulaire
        id_boeuf = id_bouef.value
        type_vaccin_value = type_vaccin.value
        date_value = date.value
        
        if not id_boeuf or not type_vaccin_value or not date_value:
            message.value = "Tous les champs sont obligatoires."
            page.update()
            return
        # Ajout de la vaccination
        ajouter_vaccination(id_boeuf, date_value, type_vaccin_value)
        
        # Réinitialisation du formulaire
        id_bouef.value = ""
        type_vaccin.value = ""
        date.value = ""
        message.value = "Vaccination ajoutée avec succès."
        page.update()
    
    # Création des lignes du tableau
    rows = []
    for vaccin in vaccins:
        status_icon = ft.Icon(
            name=ft.icons.CHECK_CIRCLE if vaccin["effectue"] else ft.icons.WARNING,
            color=ft.colors.GREEN if vaccin["effectue"] else ft.colors.ORANGE
        )
        
        rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(vaccin["nom"],color="#000000",weight="bold")),
                    ft.DataCell(ft.Text(vaccin["date"],color="#000000",weight="bold")),
                    ft.DataCell(ft.Text(vaccin["prochaine"],color="#000000",weight="bold")),
                    ft.DataCell(status_icon),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.icons.EDIT,
                            on_click=lambda e, v=vaccin: edit_vaccin(e, v),
                        ),
                    ),
                    
                ],
                
            )
        )

    
    # Contenu principal
    content = ft.Column(
        controls=[
            ft.Text("Gestion des Vaccinations", size=25, weight="bold", color="#2e7d32"),
            ft.Divider(height=10, color="transparent"),
            #images
            ft.Row([image1,text1], alignment=ft.MainAxisAlignment.START,width=400,),
            ft.Divider(height=10, color="transparent"),
            ft.Row([text2,image2], alignment=ft.MainAxisAlignment.START,width=400,),
            ft.Divider(height=10, color="transparent"),

            ft.Container(
                height=400,
                content=ft.Column(
                    [
                        ft.Text("Types des vaccinations", size=16, weight="bold", color="#2e7d32", font_family="Georgia"),
                        ft.Container(
                            height=300,  # Hauteur fixe pour scroll vertical
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        [
                                            ft.DataTable(
                                                columns=[
                                                    ft.DataColumn(ft.Text("Image", color="#000000", font_family="Georgia")),
                                                    ft.DataColumn(ft.Text("Nom du vaccin", color="#000000", font_family="Georgia")),
                                                    ft.DataColumn(ft.Text("Periode de\nVaccination", color="#000000", font_family="Georgia")),
                                                    ft.DataColumn(ft.Text("Description", color="#000000", font_family="Georgia")),
                                                ],
                                                rows=[
                                                    ft.DataRow(
                                                        cells=[
                                                            ft.DataCell(
                                                                ft.Container(
                                                                    content=ft.Image(v["image"], width=80, height=80, border_radius=20),
                                                                    padding=10
                                                                )
                                                            ),
                                                            ft.DataCell(
                                                                ft.Container(
                                                                    content=ft.Text(v["nom"], color="#000000", weight="bold"),
                                                                    padding=10
                                                                )
                                                            ),
                                                            ft.DataCell(
                                                                ft.Container(
                                                                    content=ft.Text(v["periode"], color="#000000", weight="bold"),
                                                                    padding=10
                                                                )
                                                            ),
                                                            ft.DataCell(
                                                                ft.Container(
                                                                    content=ft.Text(v["desc"], color="#000000", weight="bold"),
                                                                    padding=10
                                                                )
                                                            ),
                                                        ]
                                                    ) for v in vaccinations
                                                ],
                                                column_spacing=10,
                                                heading_row_color="#9AE283",
                                                data_row_min_height=80,
                                                data_row_max_height=120,
                                                width=600,
                                            )
                                        ],
                                        scroll=ft.ScrollMode.ALWAYS,
                                    ),
                                ],
                                scroll=True,
                                expand=True
                            ),
                            padding=10,
                            border=ft.border.all(1, ft.colors.BLUE),
                            border_radius=10,
                        ),
                    ],
                    spacing=20,
                ),
                bgcolor=ft.colors.with_opacity(0.6, "#C5E0BD"),
            ),


            # Cartes statistiques
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Vaccins effectués", size=12),
                                ft.Text("24", size=20, weight="bold"),
                            ],
                            alignment="center",
                            horizontal_alignment="center",
                        ),
                        padding=20,
                        width=100,
                        height=100,
                        bgcolor=ft.colors.with_opacity(0.9, ft.colors.GREEN),
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Vaccins en retard", size=12),
                                ft.Text("3", size=20, weight="bold"),
                            ],
                            alignment="center",
                            horizontal_alignment="center",
                        ),
                        padding=20,
                        width=100,
                        height=100,
                        bgcolor=ft.colors.with_opacity(0.9, ft.colors.RED),
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Prochains vaccins", size=12),
                                ft.Text("5", size=20, weight="bold"),
                            ],
                            alignment="center",
                            horizontal_alignment="center",
                        ),
                        padding=20,
                        width=100,
                        height=100,
                        bgcolor=ft.colors.with_opacity(0.9, ft.colors.BLUE),
                        border_radius=10,
                    ),
                ],
                spacing=20,
            ),
            
            
            ft.Divider(height=20, color="transparent"),
            
            # Formulaire d'ajout
            ft.Text("Nouvelle Vaccination", size=18, weight="bold",color="#000000"),
            ft.Column(
                controls=[
                    message,
                    id_bouef,
                    type_vaccin,
                    date,
                   
                ],
                spacing=20,
            ),
            ft.ElevatedButton(
                "Enregistrer",
                icon=ft.icons.SAVE,
                on_click=lambda e: ajouter_vacc_click(e),
                bgcolor="#4CAF50",
                color="black",
            ),
            
            # Calendrier des vaccins
            ft.Divider(height=30, color="transparent"),
            ft.Text("Calendrier Vaccinal", size=18, weight="bold",color="#000000"),
            ft.Container(
                content=ft.Text("Calendrier visuel des vaccins à venir", italic=True),
                padding=20,
                bgcolor=ft.colors.with_opacity(0.5, "#2B2B2B"),
                border_radius=10,
                alignment=ft.alignment.center,
                height=200,
            ),
        ],
        scroll="auto",
        expand=True,
    )
    
    return content

# Fonctions de gestion
def edit_vaccin(e, vaccin):
    print(f"Édition du vaccin: {vaccin['nom']}")

def save_vaccination(e):
    print("Nouvelle vaccination enregistrée")



