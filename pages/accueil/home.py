import flet as ft
from pages.stores.store import connector, users

def accueil_page(page: ft.Page):
    page.horizontal_alignment = page.vertical_alignment = "center"

    def navigate_to_login(e):
        connector.clear()
        toggle_form(False)
        page.go("/login")

    def navigate_zebus(e):
        page.go("/categories/zebus")

    def navigate(e):
        page.go("/accueil/home")

    title = ft.Text(
        "AgroMad",
        size=30,
        color="#2e7d32",
        weight=ft.FontWeight.BOLD,
        italic=True,
        text_align=ft.TextAlign.CENTER,
        font_family="Georgia"
    )

    logo_ispm=ft.Image(
        src="images/ISPM.png",
        width=55,
        height=55,
        border_radius=50
    )

    logo = ft.Container(
        content=ft.Image(src="images/logo1.png", width=55, height=55),
        
        border_radius=50,
        bgcolor="#ffffff",
        padding=5,
    )

    email_connector = ft.Container(
        content=ft.Text(
            connector[0]["email"][0].upper(),  # Get the first letter of the email and convert to uppercase
            size=20,
            color="#2e7d32",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        ),
        bgcolor="#E8EAE6",
        border_radius=50,
        border=ft.border.all(2, "#2e7d32"),
        height=40,
        width=40,
        alignment=ft.alignment.center,
        on_click=lambda e: toggle_form(True),
    )

    utilistateur = ft.Container(
        content=ft.Text(
            connector[0]["last_name"].capitalize() + " " + connector[0]["first_name"].capitalize(),
            size=21,
            color="#424242",
            font_family="Georgia",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
            italic=True,
        )
    )

    vide = ft.Text(
        "    ",
    )

    def toggle_form(visible):
        email_info.visible = nom_info.visible = letters_info.visible = btn_deconnected.visible = btn_annuler.visible = form_container.visible = visible
        page.update()

    email_info=ft.Text(connector[0]["email"], visible=False, color="#353535", size=20, font_family="Georgia")
    nom_info=ft.Text(connector[0]["last_name"].capitalize() + " " + connector[0]["first_name"].capitalize(), visible=False, color="#353535", size=20, font_family="Georgia")
    letters_info=ft.Container(
        content=ft.Text(
            connector[0]["email"][0].upper(),  # Get the first letter of the email and convert to uppercase
            size=20,
            color="#E6EAF1",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        ),
        bgcolor="blue",
        border_radius=50,
        border=ft.border.all(2, "#E6EAF1"),
        height=40,
        width=40,
        alignment=ft.alignment.center,
        visible=False,
    )

    btn_deconnected = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.LOGOUT,
                    icon_size=20,
                    on_click=navigate_to_login,
                    icon_color="#E6EAF1",
                ),
                ft.Text(
                    "Déconnexion",
                    size=12,
                    color="#E6EAF1",
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        on_click=navigate_to_login,
        visible=False,
        bgcolor="#FA213E",
        border_radius=5,
        padding=5,
        width=200,
    )

    btn_annuler = ft.IconButton(
        icon=ft.icons.CANCEL,
        icon_size=30,
        on_click=lambda e: toggle_form(False),
        visible=False,
        icon_color="#444444",
    )

    form_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row([btn_annuler],alignment=ft.MainAxisAlignment.END,),
                letters_info,
                email_info,
                nom_info,
                btn_deconnected,
            ],alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#d7f5e9",
        border_radius=10,
        width=300,
        height=250,
        expand=True,
        top=50,
        left=20,
        visible=False,
    )
   
    #colors = [ft.colors.with_opacity(0.5,ft.colors.BLUE_100), ft.colors.with_opacity(0.8,ft.colors.YELLOW_100),ft.colors.with_opacity(0.8,ft.colors.GREEN_100),ft.colors.with_opacity(0.8,ft.colors.RED_100),ft.colors.with_opacity(0.8,ft.colors.PINK_100),ft.colors.with_opacity(0.8,ft.colors.ORANGE_100)]
    colors = ["#529455","#529455","#529455"]

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
        for i in range(0, len(categories_data), 3):
            row_categories = categories_data[i:i+3]
            row = ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src=cat["icon"], width=30, height=30),
                                ft.Text(cat["name"], text_align=ft.TextAlign.CENTER, size=14,color="#ffffff", weight=ft.FontWeight.BOLD,),
                                
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        
                            
                        ),
                        margin=5,
                        padding=5,
                        alignment=ft.alignment.center,
                        bgcolor=colors[(i + j) % len(colors)],
                        width=170,
                        height=100,
                        border_radius=16,
                        on_click=cat["lien"],
                        shadow=ft.BoxShadow(blur_radius=5, color="#2f3a4b", offset=(2, 4)),
                        expand=True,
                    )
                    for j,cat in enumerate(row_categories)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=5,
                
            )
            rows.append(row)

        return ft.Column(rows, spacing=5, scroll="auto", expand=True)

    categories_container = ft.Container(
        content=ft.Column(
            [
                #generate_categories()
            ],
            scroll="auto",
            expand=True,
        ),
        padding=10,
        expand=True,
        bgcolor="#d3d3d3",
        border_radius=5,
        margin=10,
    )

    
    navigation_bar = ft.Container(
        content=ft.NavigationBar(
            bgcolor="#424242",
            height=100,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icon(ft.icons.PERSON, color="#ffffff", size=40,) ),
                ft.NavigationBarDestination(icon=ft.Icon(ft.icons.HOME, color="#ffffff", size=40)  ),
                ft.NavigationBarDestination(icon=ft.Icon(ft.icons.NOTIFICATIONS, color="#ffffff", size=40)  ),
            ],
            on_change=lambda e: change_categories(e.control.selected_index),
            selected_index=1,
            indicator_color="#2cb977",
            indicator_shape=ft.RoundedRectangleBorder(
                radius=20,
            ),
        ),
        border_radius=20,
        alignment=ft.alignment.top_center,
        padding=2,
    )

    def change_categories(selected_index):
        if selected_index == 0:
            categories_container.content = ft.Text("", size=20, color="#2cb977")
        elif selected_index == 1:
            categories_container.content = generate_categories()
        elif selected_index == 2:
            categories_container.content = ft.Text("", size=20, color="#2cb977")
        page.update()

    change_categories(1)

    accueil_container = ft.Column(
        [
            ft.Divider(height=30, color="transparent"), 
            ft.Row([logo,title,logo_ispm], alignment=ft.MainAxisAlignment.SPACE_AROUND,),
            ft.Divider(height=3, color="#d6d6d6"), 
            ft.Row([utilistateur,vide,email_connector], alignment=ft.MainAxisAlignment.SPACE_AROUND,),
            #title,"#020202"
            #email_connector,
            ft.Divider(height=3, color="#d6d6d6"), 
            categories_container,
            navigation_bar,
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
                    colors=["#f7fffc","#f7fffc"],
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                )
            ),
            form_container,
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


