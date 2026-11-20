import flet as ft

def error_page(page: ft.Page) -> ft.View:

    body = ft.Container(
        bgcolor = ft.Colors.RED,
        expand = True,
        height = page.height,
        width = page.width,

        content = ft.Text(
            value = "Page Not Found",
            size = 50,
            style = ft.TextStyle(color = ft.Colors.WHITE)
        )
    )

    return ft.View(
        route = "/error_404",
        controls = [
            body
        ]    
    )