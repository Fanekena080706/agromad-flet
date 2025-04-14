import flet as ft
from pages.welcome import welcome_page
from pages.login import login_page
from pages.register import register_page
from pages.accueil.home import accueil_page
from pages.categories.zebusPage import zebus_page

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(welcome_page(page))
        elif page.route == "/login":
            page.views.append(login_page(page))
        elif page.route == "/register":
            page.views.append(register_page(page))
        elif page.route == "/accueil/home":
            page.views.append(accueil_page(page))
        elif page.route == "/categories/zebus":
            page.views.append(zebus_page(page))
        page.update()
    
    page.on_route_change = route_change
    page.go("/")
    
ft.app(target=main)

