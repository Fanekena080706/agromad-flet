import flet as ft
from pages.stores.store import users, connector
from pages.accueil.home import accueil_page
from pages.categories.data.gestion import data

def login_page(page: ft.Page):
    
    page.bgcolor = "#ffffff"
    page.padding = 10  
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def navigete_to_register(e):
        page.go("/register")
 
    def navigete_to_welcome(e):
        page.go("/")

    

    back_icon = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_size=20,
        on_click=navigete_to_welcome,
        bgcolor="#ffffff",
        style=ft.ButtonStyle(
            color="#000000",  
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
        color="#2e7d32",
        font_family="Georgia",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    login = ft.Text(
        "Connexion",
        size=17,
        color="#2e7d32",
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        font_family="Georgia",
        italic=True,
    )

    logo =ft.Image(src="images/logo1.png", width=50, height=50)
        
        
    
    last_name =ft.Container(
        border=ft.border.only(bottom=ft.BorderSide(width=1, color=ft.colors.BLACK)),
        content=ft.TextField(
            label="Nom",
            hint_text="Entrez votre nom",
            color=ft.colors.BLACK,
            bgcolor="#cff4d2",
            filled=True,
            border=ft.InputBorder.NONE,
        ),
        width=300,
        expand=True
    )
    first_name =ft.Container(
        border=ft.border.only(bottom=ft.BorderSide(width=1, color=ft.colors.BLACK)),
        content=ft.TextField(
            label="Prénom",
            hint_text="Entrez votre prénom",
            color=ft.colors.BLACK,
            bgcolor="#cff4d2",
            filled=True,
            border=ft.InputBorder.NONE,
        ),
        width=300,
        expand=True
    )

    password_field = ft.Container(
        border=ft.border.only(bottom=ft.BorderSide(width=1, color=ft.colors.BLACK)),
        content=ft.TextField(
            label="Mot de passe",
            hint_text="Entrer votre mot de passe",
            color=ft.colors.BLACK,
            bgcolor="#cff4d2",
            filled=True,
            password=True,
            can_reveal_password=True,
            border=ft.InputBorder.NONE,
        ),
        width=300,
        expand=True,
    )

    message = ft.Text(color="red")

    def connexion(e):
        if last_name.content.value and first_name.content.value and password_field.content.value:
            for user in data["utilisateurs"]:
                if user["last_name"] == last_name.content.value and user["first_name"] == first_name.content.value and user["password"] == password_field.content.value:
                    connector.append(user)
                    #connector=user #,, apesaina rehefa manova identite ilay utilisateur, rehefa misy fonctionalité "modifier utilisateur" @zay tonga de miova daholo ny info rehetra rehefa manova identite ilay utilisateur
                    page.go("/accueil/home")
                    return
            message.value = "Nom, prénom ou mot de passe incorrect"
            page.update()
            return
        else:
            message.value = "Veuillez remplir tous les champs"
            page.update()
            return
        #message.value = "Connexion réussie"

    login_button = ft.ElevatedButton(
        text="Connexion",
        width=200,
        height=40,
        bgcolor="#2e7d32",
        color="#ffffff",
        on_click=connexion,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
    )

    signup_text = ft.Row(
        controls=[
            ft.Text(
                "Vous n'avez pas de compte? ",
                color="#000000",
                size=14,
                ),
            ft.TextButton(
                text="Créer un compte",
                on_click=navigete_to_register,
                style=ft.ButtonStyle(
                    color="#1b5e20",
                    
                ),
            ),
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    formulaire = ft.Container(
        content=ft.Column(
            [
                logo, 
                ft.Row([ft.Icon(name=ft.icons.PERSON,size=40,color="#424242"),last_name],alignment=ft.MainAxisAlignment.START,expand=True),
                ft.Row([ft.Icon(name=ft.icons.PERSON_4_SHARP,size=40,color="#424242"),first_name],alignment=ft.MainAxisAlignment.START,expand=True),
                ft.Row([ft.Icon(name=ft.icons.LOCK,size=40,color="#424242"),password_field],alignment=ft.MainAxisAlignment.START,expand=True),
                message,
                login_button,
                signup_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#fff8e1",
        padding=20,
        margin=10,
        border_radius=5,
        width=400,
        height=420,
        opacity=0.8,
        shadow=ft.BoxShadow(blur_radius=20, color="#4d6453", offset=(2, 4)),
        expand=True,
        animate_opacity=ft.Animation(300, "easeInOut"),
        animate=ft.animation.Animation(300, "easeInOut"),
    )
    login_container = ft.Column(
        [
                 
            ft.Divider(height=30, color="transparent"),
            ft.Row([back_icon, title,logo_ispm], alignment=ft.MainAxisAlignment.SPACE_AROUND,),
            #ft.Divider(height=3, color="transparent"),
            formulaire,
            ft.Divider(height=150, color="transparent"),  
            ft.Divider(height=150, color="transparent"),  
            ft.Divider(height=150, color="transparent"),    
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    centered_container = ft.Stack(
        controls=[
            #ft.Image(src="images/bg7.jpeg", width=float('inf'), height=float('inf'), fit=ft.ImageFit.COVER, border_radius=20, opacity=1, expand=True),
            
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
                    colors=["#f7fffc","#f7fffc"],
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                ),
                expand=True,
                blur=ft.Blur(1.5, 1.5),
            )
        ],
    )

    main_container = ft.Container(
        content=centered_container,
        #expand=True,
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




