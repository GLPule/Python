import flet as ft

def home_page(page: ft.Page) -> ft.View:

    async def go_to_settings(e):
        await page.push_route("/settings")
        page.update()

    async def go_to_profile(e):
        await page.push_route("/profile")
        page.update()


    app_bar = ft.AppBar(
        title = "Home",
        center_title = True,
        actions = [
            ft.TextButton(
                content = "Settings",
                on_click = go_to_settings
            ),
            ft.IconButton(
                icon = ft.Icons.PERSON,
                on_click = go_to_profile
            ),
        ]
    )

    body = ft.Container(
        bgcolor = ft.Colors.ORANGE,
        alignment = ft.Alignment.CENTER,
        expand = True,
        height = page.height,
        width = page.width,

        content = ft.Text(
            value = "Welcome Home",
            size = 50,
            style = ft.TextStyle(color = ft.Colors.WHITE)
        )
    )

    return ft.View(
        route = "/home",
        appbar = app_bar,
        controls = [
            body
        ]    
    )