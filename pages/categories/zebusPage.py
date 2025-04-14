import flet as ft
from flet import *
import time
from pages.categories.vaccination_page import get_vaccination_content

def zebus_page(page: ft.Page):
    page.title = "AgroMad - Gestion d'Élevage"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10

    def navigate_home(e):
        page.go("/accueil/home")
    
    # page isakarazany
    def get_page_content(page_name):
        contents = {
            "Vaccination": get_vaccination_content(),
            "Alimentation": ft.Text("Contenu Alimentation", size=30, color="black"),
            "Santé": ft.Text("Contenu Santé", size=30, color="black"),
            "Reproduction": ft.Text("Contenu Reproduction", size=30, color="black"),
            "Production": ft.Text("Contenu Production", size=30, color="black"),
            "Ventes": ft.Text("Contenu Ventes", size=30, color="black"),
            "Inventaire": ft.Text("Contenu Inventaire", size=30, color="black"),
            "Rapports": ft.Text("Contenu Rapports", size=30, color="black")
        }
        return contents.get(page_name, ft.Text("Page non trouvée", size=30, color="black"))

    def animate_opacity(duration):
        return ft.animation.Animation(duration, "easeInOut")
     
    current_page = ft.Text("Vaccination")
    content_area = ft.Container(
        content=get_page_content(current_page.value),
        alignment=ft.alignment.center,
        expand=True,
        animate_opacity=animate_opacity(300)
    )

    def change_page(e):
        content_area.opacity = 0.7
        page.update()
        
        time.sleep(0.3)  
        
        current_page.value = e.control.data
        content_area.content = get_page_content(current_page.value)
        
        content_area.opacity = 1
        page.update()
        
        for item in nav_bar.controls:
            if item.data == current_page.value:
                item.border = ft.border.only(bottom=ft.border.BorderSide(3, "Green"))
            else:
                item.border = None
        page.update()

    # Données des types
    type_data = [
        {"type": "Vaccination", "icon": ft.icons.VACCINES},
        {"type": "Alimentation", "icon": ft.icons.RESTAURANT},
        {"type": "Santé", "icon": ft.icons.HEALTH_AND_SAFETY},
        {"type": "Reproduction", "icon": ft.icons.FAMILY_RESTROOM},
        {"type": "Production", "icon": ft.icons.FACTORY},
        {"type": "Ventes", "icon": ft.icons.SELL},
        {"type": "Inventaire", "icon": ft.icons.INVENTORY},
        {"type": "Rapports", "icon":ft.icons.INSERT_CHART},
    ]

    # Barre de navigation
    nav_items = []
    for type in type_data:
        nav_item = ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        border=ft.border.all(2, "#83e85a"),
                        border_radius=50,
                        content=ft.IconButton(
                            icon=type["icon"],
                            data=type["type"],
                            on_click=change_page,
                        )
                    ),
                    ft.Text(
                        type["type"],
                        color="#83e85a",
                        size=12,
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                    )
                ],
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            data=type["type"],
            on_click=change_page,
            padding=10,
            border=ft.border.only(bottom=ft.border.BorderSide(3, "#83e85a")) if type["type"] == current_page.value else None,
            animate=ft.animation.Animation(300, "easeInOut"),
        )
        nav_items.append(nav_item)

    nav_bar = ft.Row(
        controls=nav_items,
        scroll=True,
        spacing=20,
    )

    # Conteneur principal
    toot_container = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_size=20,
                            on_click=navigate_home,
                            bgcolor="#f3f9f9",
                            style=ft.ButtonStyle(color="#2fc8ff"),
                            width=34,
                            height=34,
                            opacity=0.7,
                        ),
                        ft.Text(
                            "AgroMad",
                            size=30,
                            color="#f3f9f9",
                            weight=ft.FontWeight.BOLD,
                            expand=True,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Image(
                            src="images/ISPM.png",
                            width=65,
                            height=65,
                            border_radius=50
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(
                    content=nav_bar,
                    padding=ft.padding.only(top=20, bottom=20),
                ),
                ft.Divider(color="white24", height=1),
                ft.Container(
                    content=content_area,
                    expand=True,
                )
            ],
            spacing=0,
            expand=True,
        ),
        
        border_radius=20,
        padding=20,
        expand=True,
    )

    centered_container = ft.Stack(
        controls=[
            #ft.Image(src="images/bg12.jpg", width=450, height=900, fit=ft.ImageFit.COVER,border_radius=20,opacity=1),
            
            ft.Container(
                content=ft.Column(
                    [
                        toot_container,
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
        "/categories/zebus",
        [
            main_container,
        ]
    )
def main(page:ft.Page):
    page.add(zebus_page(page))