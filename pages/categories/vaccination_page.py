import flet as ft

def get_vaccination_content():
    
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
    )
    text2 =ft.Text(
        "La vaccination joue un rôle clé dans la prévention des maladies infectieuses en élevage. Elle permet de protéger non seulement l'animal vacciné, mais aussi le troupeau dans son ensemble, en réduisant la propagation des agents pathogènes.",
        size=12,
        font_family="Georgia",
        expand=True,
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
                    ft.DataCell(ft.Text(vaccin["nom"],color="white",weight="bold")),
                    ft.DataCell(ft.Text(vaccin["date"],color="white",weight="bold")),
                    ft.DataCell(ft.Text(vaccin["prochaine"],color="white",weight="bold")),
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
            ft.Text("Gestion des Vaccinations", size=25, weight="bold", color="#83e85a"),
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
                        ft.Text("Types des vaccinations", size=16, weight="bold", color="white", font_family="Georgia"),
                        ft.Container(
                            height=300,  # Hauteur fixe pour scroll vertical
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        [
                                            ft.DataTable(
                                                columns=[
                                                    ft.DataColumn(ft.Text("Image", color="black", font_family="Georgia")),
                                                    ft.DataColumn(ft.Text("Nom du vaccin", color="black", font_family="Georgia")),
                                                    ft.DataColumn(ft.Text("Periode de\nVaccination", color="black", font_family="Georgia")),
                                                    ft.DataColumn(ft.Text("Description", color="black", font_family="Georgia")),
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
                                                                    content=ft.Text(v["nom"], color="white", weight="bold"),
                                                                    padding=10
                                                                )
                                                            ),
                                                            ft.DataCell(
                                                                ft.Container(
                                                                    content=ft.Text(v["periode"], color="white", weight="bold"),
                                                                    padding=10
                                                                )
                                                            ),
                                                            ft.DataCell(
                                                                ft.Container(
                                                                    content=ft.Text(v["desc"], color="white", weight="bold"),
                                                                    padding=10
                                                                )
                                                            ),
                                                        ]
                                                    ) for v in vaccinations
                                                ],
                                                column_spacing=10,
                                                heading_row_color=ft.colors.BLUE_GREY,
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
                            border=ft.border.all(1, ft.colors.GREEN),
                            border_radius=10,
                        ),
                    ],
                    spacing=20,
                ),
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
            
            ft.Divider(height=30, color="transparent"),
            
            # Tableau des vaccins
            # Tableau des vaccins avec défilement horizontal
            ft.Container(
                height=300,  # Hauteur fixe pour le conteneur
                content=ft.Column(
                    [
                        ft.Text("Historique des vaccinations", size=16, weight="bold",color="white",font_family="Georgia"),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.DataTable(
                                        columns=[
                                            ft.DataColumn(ft.Text("Nom du vaccin",color="black",font_family="Georgia")),
                                            ft.DataColumn(ft.Text("Date administration",color="black",font_family="Georgia")),
                                            ft.DataColumn(ft.Text("Prochaine dose",color="black",font_family="Georgia")),
                                            ft.DataColumn(ft.Text("Statut",color="black",font_family="Georgia")),
                                            ft.DataColumn(ft.Text("Actions",color="black",font_family="Georgia")),
                                        ],
                                        rows=rows,
                                        column_spacing=20,  # Espacement entre colonnes
                                        heading_row_color=ft.colors.BLUE_GREY,
                                        data_row_min_height=40,
                                        width=800,  # Largeur totale du tableau
                                    )
                                ],
                                scroll=ft.ScrollMode.AUTO,  # Activation du défilement horizontal
                            ),
                            padding=10,
                            border=ft.border.all(1, ft.colors.WHITE24),
                            border_radius=10,
                        )
                    ],
                    spacing=10
                ),
                bgcolor=ft.colors.with_opacity(0.6, ft.colors.WHITE12),
                border_radius=10,
            ),
            
            ft.Divider(height=20, color="transparent"),
            
            # Formulaire d'ajout
            ft.Text("Nouvelle Vaccination", size=18, weight="bold",color="white"),
            ft.Column(
                controls=[
                    ft.Dropdown(
                        options=[ft.dropdown.Option(a["id"]) for a in animaux],
                        label="Animal",
                        width=200,
                        color="white",
                        border_color=ft.colors.WHITE,
                        border_width=1,
                        border_radius=5,
                    ),
                    ft.Dropdown(
                        options=[
                            ft.dropdown.Option("Fièvre Aphteuse"),
                            ft.dropdown.Option("Brucellose"),
                            ft.dropdown.Option("Charbon"),
                        ],
                        label="Type de vaccin",
                        width=200,
                        color="white",
                        border_color=ft.colors.WHITE,
                        border_width=1,
                    ),
                    ft.TextField(label="Date", width=150,color="white",border_color=ft.colors.WHITE,border_width=1,border_radius=5),
                    ft.TextField(label="Prochaine dose", width=150,color="white",border_color=ft.colors.WHITE,border_width=1,border_radius=5),
                ],
                spacing=20,
            ),
            ft.ElevatedButton(
                "Enregistrer",
                icon=ft.icons.SAVE,
                on_click=save_vaccination,
            ),
            
            # Calendrier des vaccins
            ft.Divider(height=30, color="transparent"),
            ft.Text("Calendrier Vaccinal", size=18, weight="bold",color="white"),
            ft.Container(
                content=ft.Text("Calendrier visuel des vaccins à venir", italic=True),
                padding=20,
                bgcolor=ft.colors.with_opacity(0.5, ft.colors.WHITE10),
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



