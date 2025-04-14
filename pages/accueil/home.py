import flet as ft

def accueil_page(page: ft.Page):
    page.horizontal_alignment = page.vertical_alignment = "center"

    def navigate_to_login(e):
        page.go("/login")
    def navigate_zebus(e):
        page.go("/categories/zebus")

    def navigate(e):
        page.go("/accueil/home")
    
    back_icon = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_size=30,
        on_click=navigate_to_login
    )

    title = ft.Text(
        "AgroMad",
        size=40,
        color="#ffffff",
        weight=ft.FontWeight.BOLD,
        italic=True,
        text_align=ft.TextAlign.CENTER,
    )

    logo_ispm=ft.Image(
        src="images/ISPM.png",
        width=65,
        height=65,
        border_radius=50
    )

    
    texte = ft.Text(
        "Catégories",
        size=18,
        color="#83e85a",
        italic=True,    
        text_align=ft.TextAlign.CENTER,
    )

   
    #colors = [ft.colors.with_opacity(0.5,ft.colors.BLUE_100), ft.colors.with_opacity(0.8,ft.colors.YELLOW_100),ft.colors.with_opacity(0.8,ft.colors.GREEN_100),ft.colors.with_opacity(0.8,ft.colors.RED_100),ft.colors.with_opacity(0.8,ft.colors.PINK_100),ft.colors.with_opacity(0.8,ft.colors.ORANGE_100)]
    colors = ["#263142","#2f3a4b","#21334d"]

    def generate_categories():
        categories_data = [
            {"name": "Zebus", "icon": "images/cow.png","lien":navigate_zebus},
            {"name": "Volailles", "icon": "images/chicken.png","lien":navigate},
            {"name": "Porcs", "icon": "images/pig.png","lien":navigate},
            {"name": "Chèvres", "icon": "images/sheep.png","lien":navigate},
            {"name": "Moutons", "icon": "images/animals.png","lien":navigate},
            {"name": "Lapins", "icon": "images/rabbit.png","lien":navigate},
        ]

        rows = []
        for i in range(0, len(categories_data), 2):
            row_categories = categories_data[i:i+2]
            row = ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src=cat["icon"], width=40, height=40),
                                ft.Text(cat["name"], text_align=ft.TextAlign.CENTER, size=14,color="#83e85a", weight=ft.FontWeight.BOLD,),
                                
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        
                            
                        ),
                        margin=5,
                        padding=5,
                        alignment=ft.alignment.center,
                        bgcolor=colors[(i + j) % len(colors)],
                        width=170,
                        height=140,
                        border_radius=16,
                        on_click=cat["lien"],
                        shadow=ft.BoxShadow(blur_radius=20, color=colors[(i + j) % len(colors)], offset=(8, 12)),
                        expand=True,
                    )
                    for j,cat in enumerate(row_categories)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                
            )
            rows.append(row)

        return ft.Column(rows, spacing=5)

    categories_container = ft.Container(
        content=ft.Column(
            [
                generate_categories()
            ],
            scroll="auto",
            expand=True,
        ),
        padding=10,
        expand=True,
        bgcolor="transparent",
        border_radius=10,
    )

    
    navigation_bar = ft.Container(
        content=ft.NavigationBar(
            bgcolor="#217301",
            height=100,
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Profil"),
                ft.NavigationBarDestination(icon=ft.icons.HOME, label="Accueil"),
                ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Paramètres"),
            ],
            on_change=lambda e: change_categories(e.control.selected_index),
            selected_index=1,
        
        ),
        border_radius=20,
    )

    def change_categories(selected_index):
        if selected_index == 0:
            categories_container.content = ft.Text("Profil", size=20, color="#2cb977")
        elif selected_index == 1:
            categories_container.content = generate_categories()
        elif selected_index == 2:
            categories_container.content = ft.Text("Paramètres", size=20, color="#2cb977")
        page.update()


    accueil_container = ft.Column(
        [
            ft.Divider(height=10, color="transparent"), 
            ft.Row([back_icon,title,logo_ispm], alignment=ft.MainAxisAlignment.SPACE_AROUND,),
            #title,
            texte,
            ft.Divider(height=3, color="#539756"), 
            categories_container,
            navigation_bar
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    
    centered_container = ft.Stack(
        controls=[
            #ft.Image(src="images/bg12.jpg", width=450, height=900, fit=ft.ImageFit.COVER,border_radius=20,opacity=1),
            
            ft.Container(
                content=ft.Column(
                    [
                        accueil_container,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center, 
                padding=0,  
                border_radius=20, 
                #width=450,  
                #height=900,
                gradient=ft.LinearGradient(
                    colors=["#5c6afd","#111827","#111827"],
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                )
            )
        ]
    )

    main_container = ft.Container(
        content=centered_container,
        expand=True, 
        alignment=ft.alignment.center, 
    )

    
    return ft.View(
        "/accueil/home",
        #bgcolor="#E8F6F3",
        controls=[
            main_container,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        
    )

def main(page: ft.Page):
    page.add(accueil_page(page))


