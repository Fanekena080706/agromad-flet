import flet as ft


def welcome_page(page: ft.Page):
    page.window_icon = 'assets/icon.png'
    page.padding = 0
    page.title = "AgroMad"
    page.bgcolor = "#2cb977"  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Variables pour suivre l'état actuel
    current_text_index = 0
    texts = [
        "Avec Agromad, gérez votre élevage d'animaux femelles en toute simplicité. Suivez les cycles de reproduction, planifiez les soins et améliorez la productivité de votre ferme, le tout depuis votre smartphone.",
        "Suivez les cycles de reproduction de vos animaux femelles et recevez des alertes pour ne rien manquer.\nPlanifiez les périodes de reproduction et maximisez la productivité de votre troupeau.",
        "Conservez un historique détaillé de chaque animal pour une gestion optimale de votre élevage."
    ]

    
    def navigate_to_login(e):
        page.go("/login")

    
    def navigate_to_intro(e):
        nonlocal current_text_index
        current_text_index += 1
        
        if current_text_index < len(texts):
            # Animation de fondu pour le texte
            agro_text.opacity = 0
            agro_text.update()
            
            agro_text.value = texts[current_text_index]
            
            # Animation d'apparition
            agro_text.opacity = 1
            agro_text.update()
            
            # Si c'est le dernier texte, changer le bouton
            if current_text_index == len(texts) - 1:
                but.text = "Commencer"
                but.update()
            progress_bar.value = (current_text_index + 1) / len(texts)
            progress_bar.update()
        else:
            # Animation de transition vers la page de login
            main_container.opacity = 0
            main_container.offset = ft.transform.Offset(3, 1)
            main_container.update()
            navigate_to_login(e)

    

    def animate_text():
        # Configurer les propriétés d'animation APRÈS que le contrôle est ajouté à la page
        agro_text.opacity = 0
        agro_text.offset = ft.transform.Offset(0.4, 0.9)
        agro_text.animate_opacity = ft.Animation(500, "easeInOut")
        agro_text.animate_offset = ft.Animation(700, "easeOutBack")
        page.update()
        
        agro_text.opacity = 1
        agro_text.offset = ft.transform.Offset(0, 0)
        page.update()

    textAgro = ft.Text(
        "AgroMad",
        size=30,
        color="#205072",
        weight=ft.FontWeight.BOLD,
        font_family="Georgia",
    )
    textVide = ft.Text(
        "    ",
    )

    logo_ispm=ft.Image(
        src="images/ISPM.png",
        width=65,
        height=65,
        border_radius=50,
    )
    logo = ft.Column(
        controls=[
            ft.Image(src="images/logo1.png", width=150, height=150),
            textAgro,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    welcome = ft.Text(
        "Bienvenue sur",
        size=25,
        weight=ft.FontWeight.BOLD,
        color="#ffffff",
        font_family="Arial",
        italic=True,
    )

    agro_text = ft.Text(
        texts[0],
        size=15,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER,
        italic=True,
        font_family="Georgia",
        opacity=1,
        animate_opacity=ft.Animation(300, "easeInOut"),
        offset=ft.transform.Offset(0, 0),
        animate_offset=ft.Animation(500, "easeOutBack"),
    )

    image1=ft.Image(
        src="assets/images/exemple1.jpg",
        width=120,
        height=75,
        border_radius=10,
    )

    image2=ft.Image(
        src="assets/images/exemple2.jpg",
        width=120,
        height=75,
        border_radius=10,
    )

    progress_bar = ft.ProgressBar(
        value=(current_text_index + 1) / len(texts),
        width=300,
        color="#56C596"
    )

    but = ft.ElevatedButton(
        text="Suivant",
        width=200,
        height=40,
        bgcolor="#205072",
        color="#ffffff",
        animate_scale=ft.Animation(200, "easeInOut"),
        on_click=navigate_to_intro,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
        
    )

    contText = ft.Container(
        content=ft.Column(
            [
                #ft.Row([image1,image2], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                agro_text,
                progress_bar,
                #ft.Divider(height=50, color="transparent"),
                #but,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        padding=0,
        width=420,
        height=250,
        opacity=1,
        margin=20,
        #expand=True,
        bgcolor="#cff4d2",
        shadow=[
            ft.BoxShadow(
                blur_radius=1,
                spread_radius=1,
                color="#7be495",
                offset=ft.Offset(2,2),
            )
        ],
        alignment=ft.alignment.center,
        border_radius=20,
        animate_opacity=ft.Animation(500, "easeInOut"),
    )

    welcome_container =ft.Column(
        [
            ft.Divider(height=20, color="transparent"),
            ft.Row([textVide,textVide,logo_ispm], alignment=ft.MainAxisAlignment.END),
            logo,
            contText,
            but,
            ft.Divider(height=50, color="transparent"),
            ft.Divider(height=50, color="transparent"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    

    centered_container = ft.Stack(
        controls=[
            ft.Image(src="images/bg7.jpeg", width=float('inf'), height=float('inf'), fit=ft.ImageFit.COVER, border_radius=20, opacity=1, expand=True),
            
            ft.Container(
                content=ft.Column(
                    [
                        welcome_container,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center, 
                padding=10,  
                border_radius=20, 
                #width=450,  
                #height=900,
                blur=ft.Blur(1.5,1.5),
                #gradient=ft.LinearGradient(
                    #colors=["#cff4d2", "#7be495"],
                    #begin=ft.alignment.top_center,
                    #end=ft.alignment.bottom_center,
                #),
                expand=True,
            )
        ]
    )

    main_container = ft.Container(
        content=centered_container,
        expand=True,  
        alignment=ft.alignment.center, 
        border_radius=20,
        animate_opacity=ft.Animation(500, "easeInOut"),
        animate_offset=ft.Animation(500, "easeInOut"),
        offset=ft.transform.Offset(0, 0),
    )

    # Lancer l'animation initiale du texte
    animate_text()

    view = ft.View(
        "/",
        [
            main_container
        ]
    )

    # Lancer l'animation après un petit délai pour s'assurer que la page est chargée
    def on_view_loaded(e):
        animate_text()
        page.update()

    view.on_load = on_view_loaded

    return view



