import flet as ft
from pages.stores.store import users 
from pages.categories.data.gestion import ajouter_utilisateur, data

def register_page(page: ft.Page):
    page.bgcolor = "#ffffff"
    page.padding = 0  
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 

    def navigate_to_login(e):
        page.go("/login")

    back_icon = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_size=20,
        on_click=navigate_to_login,
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
    signUp = ft.Text(
        "Inscription",
        size=17,
        color="#2e7d32",
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        font_family="Georgia",
        italic=True,
    )

    logo =ft.Image(src="images/logo1.png", width=50, height=50)

        
    
    
    last_name_field = ft.Container(
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

    first_name_field = ft.Container(
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


    email_field = ft.Container(
        border=ft.border.only(bottom=ft.BorderSide(width=1, color=ft.colors.BLACK)),
        content=ft.TextField(
            label="Email",
            hint_text="Entrez votre email",
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

    confirm_password_field = ft.Container(
        border=ft.border.only(bottom=ft.BorderSide(width=1, color=ft.colors.BLACK)),
        content=ft.TextField(
            label="Confirmation du mot de passe",
            hint_text="Confirme votre mot de passe",
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


    def inscription(e):
        last_name = last_name_field.content.value
        first_name = first_name_field.content.value
        email = email_field.content.value
        password = password_field.content.value
        confirm_password = confirm_password_field.content.value

        if not last_name or not first_name or not email or not password or not confirm_password:
            message.value = "Tous les champs sont obligatoires."
            page.update()
            return

        if password != confirm_password:
            message.value = "Les mots de passe ne correspondent pas."
            page.update()
            return

        if any(user["email"] == email for user in data["utilisateurs"]):
            message.value = "Cet email a déjà un compte."
            page.update()
            return

        ajouter_utilisateur(email, last_name, first_name, password)

        #message.value = "Inscription réussie !"
        page.update()
        page.go("/login")

    signup_button = ft.ElevatedButton(
        text="S'inscrire",
        width=200,
        height=40,
        bgcolor="#2e7d32",
        color="#ffffff",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
        on_click=inscription,
    )


    formulaire = ft.Container(
        content=ft.Column(
            [
                logo, 
                ft.Row([ft.Icon(name=ft.icons.PERSON,size=40,color="#424242"),last_name_field],alignment=ft.MainAxisAlignment.START,expand=True),
                ft.Row([ft.Icon(name=ft.icons.PERSON_4_SHARP,size=40,color="#424242"),first_name_field],alignment=ft.MainAxisAlignment.START,expand=True),
                ft.Row([ft.Icon(name=ft.icons.EMAIL,size=40,color="#424242"),email_field],alignment=ft.MainAxisAlignment.START,expand=True),
                ft.Row([ft.Icon(name=ft.icons.LOCK,size=40,color="#424242"),password_field],alignment=ft.MainAxisAlignment.START,expand=True),
                ft.Row([ft.Icon(name=ft.icons.VERIFIED_USER,size=40,color="#424242"),confirm_password_field],alignment=ft.MainAxisAlignment.START,expand=True),
                message,
                signup_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#fff8e1",
        padding=20,
        margin=10,
        border_radius=5,
        width=400,
        height=470,
        shadow=ft.BoxShadow(blur_radius=20, color="#4d6453", offset=(2, 4)),
        opacity=0.8,
    )

    signup_container = ft.Column(
        [
            ft.Divider(height=30, color="transparent"),  
            ft.Row([back_icon,title,logo_ispm], alignment=ft.MainAxisAlignment.SPACE_AROUND), 
            
            #ft.Divider(height=5, color="transparent"),  
             
            formulaire,
            ft.Divider(height=150, color="transparent"),  
            ft.Divider(height=150, color="transparent"),  
            ft.Divider(height=50, color="transparent"),  
            
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
                        signup_container,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                )
            )
        ]
    )

    main_container = ft.Container(
        content=centered_container,
        #expand=True,  
        alignment=ft.alignment.center, 
    )

    return ft.View(
        "register",
        [
            main_container
        ]
    )

def main(page: ft.Page):
    page.add(register_page(page))


