import flet as ft

def login_page(page: ft.Page):
    
    page.bgcolor = "#ffffff"
    page.padding = 10  
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def navigete_to_register(e):
        page.go("/register")
 
    def navigete_to_accueil(e):
        page.go("/accueil/home")

    def navigete_to_welcome(e):
        page.go("/")

    back_icon = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_size=20,
        on_click=navigete_to_welcome,
        bgcolor="#f3f9f9f2",
        style=ft.ButtonStyle(
            color="#2fc8ff",  
        ),
        width=34,
        height=34,
        opacity=0.7,
        
    )
 
    logo_ispm=ft.Image(
        src="images/ISPM.png",
        width=65,
        height=65,
        border_radius=50
    )

    title = ft.Text(
        "AgroMad",
        size=30,
        color="#ffffff",
        font_family="Georgia",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    login = ft.Text(
        "Connexion",
        size=25,
        color="#83e85a",
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        font_family="Georgia",
        italic=True,
    )

    email_field = ft.TextField(
        label="Email",
        hint_text="Entrez votre email",
        border_color="#ffffff",
        color=ft.colors.WHITE,
        border_radius=30,
        bgcolor="#2f3a4b",
        width=400,
        filled=True,
    )

    password_field = ft.TextField(
        label="Mot de passe",
        hint_text="Entrez votre mot de passe",
        border_color="#ffffff",
        border_radius=30,
        color=ft.colors.WHITE,
        bgcolor="#2f3a4b",
        width=400,
        filled=True,
        password=True,
        can_reveal_password=True,
    )


    login_button = ft.ElevatedButton(
        text="Connexion",
        width=200,
        height=40,
        bgcolor="#83e85a",
        color="#ffffff",
        on_click=navigete_to_accueil,
    )

    signup_text = ft.Row(
        controls=[
            ft.Text(
                "Vous n'avez pas de compte? ",
                color=ft.colors.WHITE,
                size=14,
                ),
            ft.TextButton(
                text="Créer un compte",
                on_click=navigete_to_register,
                style=ft.ButtonStyle(
                    color="#83e85a",
                    
                ),
            ),
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    formulaire = ft.Container(
        content=ft.Column(
            [
                email_field,
                password_field,
                login_button,
                signup_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#21334d",
        padding=20,
        margin=10,
        border_radius=ft.border_radius.only(top_left=0, top_right=40, bottom_left=40,bottom_right=0),
        width=400,
        height=300,
        opacity=0.8,
        shadow=ft.BoxShadow(blur_radius=20, color="#2f3a4b", offset=(2, 4)),
        expand=True,
        animate_opacity=ft.Animation(300, "easeInOut"),
        animate=ft.animation.Animation(300, "easeInOut"),
    )
    login_container = ft.Column(
        [
                 
            ft.Divider(height=5, color="transparent"),
            ft.Row([back_icon, title,logo_ispm], alignment=ft.MainAxisAlignment.SPACE_AROUND,),
            ft.Divider(height=3, color="transparent"),
            login, 
            formulaire,
            ft.Divider(height=20, color="transparent"),  
            ft.Divider(height=20, color="transparent"),  
            ft.Divider(height=10, color="transparent"),    
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    centered_container = ft.Stack(
        controls=[
            #ft.Image(src="images/bg11.jpg", width=450, height=900, fit=ft.ImageFit.COVER,border_radius=20,opacity=0.4),
            
            ft.Container(
                content=ft.Column(
                    [
                        login_container,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
                alignment=ft.alignment.center, 
                padding=0,  
                border_radius=20, 
                #width=450,  
                #height=900,
                gradient=ft.LinearGradient(
                    colors=["#5c6afd","#111827"],
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
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
        "/login",
        [
            main_container,
        ]
    )
def main(page:ft.Page):
    page.add(login_page(page))




