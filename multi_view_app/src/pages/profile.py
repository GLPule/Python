import flet as ft

def profile_page(page: ft.Page) -> ft.View:

    async def on_back(e):
        await page.push_route("/home")
        page.update()

    app_bar = ft.AppBar(
        title = "Profile",
        center_title = True,
        leading = ft.Button(
            # content = ft.Row(
            #     ft.Icon(icon = ft.Icons.ARROW_BACK),
            # ),
            icon = ft.Icons.ARROW_BACK,
            align = ft.Alignment.CENTER,
            on_click = on_back
        )
    )

    body = ft.Container(
        bgcolor = ft.Colors.BROWN,
        alignment = ft.Alignment.CENTER,
        expand = True,
        height = page.height,
        width = page.width,

        content = ft.Text(
            value = "This is your profile",
            size = 50,
            style = ft.TextStyle(color = ft.Colors.WHITE)
        )
    )

    return ft.View(
        route = "/profile",
        appbar = app_bar,
        controls = [
            body
        ]    
    )