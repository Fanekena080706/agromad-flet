import flet as ft

def get_alimentaton_content():

    image = ft.Image(
        src="assets/images/exemple1.jpg",
        width=120,
        height=120,
        border_radius=20,
    )

    text = ft.Text(
        "La nécessité de certains vaccins dépend des conditions locales ou du niveau d'exposition aux maladies. Des rappels réguliers sont recommandés pour assurer une protection continue. Il est essentiel de suivre les directives du vétérinaire selon le protocole en vigueur.",
        size=12,
        font_family="Georgia",
        expand=True,
    )


    content = ft.Column(
        controls=[
            ft.Text("Gestion d'alimentation", size=25, width="bold", color="#83e85a"),
            ft.Divider(height=10, color="transparent"),
            ft.Row([image, text],alignment=ft.MainAxisAlignment.START,width=400),
            ft.Divider(height=10, color="transparent"),
            ft.Row([image, text],alignment=ft.MainAxisAlignment.START,width=400),
            ft.Row([image, text],alignment=ft.MainAxisAlignment.START,width=400),
            ft.Row([image, text],alignment=ft.MainAxisAlignment.START,width=400),
        ],
        scroll="auto",
        expand=True,
    )

    return  content