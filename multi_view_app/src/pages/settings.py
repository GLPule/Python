import flet as ft

def settings_page(page: ft.Page) -> ft.View:

    async def on_back(e):
        await page.push_route("/home")
        page.update()

    app_bar = ft.AppBar(
        title = "Settings",
        center_title = True,
        leading = ft.Button(
            content = ft.Row(
                controls = [
                    ft.Icon(icon = ft.Icons.ARROW_BACK),
                    ft.Text(value = "Back")
                ],
            ),
            align = ft.Alignment.CENTER,
            on_click = on_back
        )
    )

    body = ft.Container(
        bgcolor = ft.Colors.BLUE,
        alignment = ft.Alignment.CENTER,
        expand = True,
        height = page.height,
        width = page.width,

        content = ft.Text(
            value = "These are your settings",
            size = 50,
            style = ft.TextStyle(color = ft.Colors.WHITE)
        )
    )

    return ft.View(
        route = "/settings",
        appbar = app_bar,
        controls = [
            body
        ]    
    )