import flet as ft
import asyncio
from pages.login import login_page
from pages.register import register_page
from pages.home import home_page

def main(page: ft.Page):
    page.window.height = 750
    page.window.width = 450

    def on_route_change():
        page.views.clear()


        global pgr
        pgr = page.route

        match pgr:
            case "/" | "/login":
                page.views.append(login_page(page))
            case "/home":
                page.views.append(home_page(page))
            case "/register":
                page.views.append(register_page(page))
            case _:
                page.views.append(login_page(page)) 

        page.update()

    async def view_pop(e):
        if e.view is not None:
            page.view.remove(e.view)
        top_view = page.view[-1]
        await page.push_route(top_view.route)

    page.on_route_change = on_route_change
    page.on_view_pop = view_pop

    on_route_change()

if __name__ == "__main__":
    ft.run(main)