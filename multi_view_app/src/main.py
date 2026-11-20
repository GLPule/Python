import flet as ft
from pages.home import home_page
from pages.error import error_page
from pages.settings import settings_page
from pages.profile import profile_page


def main(page: ft.Page):
    page.title = "Multi_View_App"
   
    def on_route_change():
        page.views.clear()

        global pgr
        pgr = page.route

        match pgr:
            case "/" | "/home":
                page.views.append(home_page(page))
            case "/settings":
                page.views.append(settings_page(page))
            case "/profile":
                page.views.append(profile_page(page))
            case _:
                page.views.append(error_page(page)) 

        page.update()

    page.on_route_change = on_route_change

    on_route_change()

if __name__ == "__main__":
    ft.run(main)
