import asyncio

import flet as ft

def home_page(page: ft.Page):
    page.title = "Home Page"

    def button_clicked(e):
        snack_bar = ft.SnackBar(content = ft.Text(f"Clicked: {e.control.content}"))
        page.show_dialog(snack_bar)

    def logout_clicked(e):
        page.session.store.remove("user")
        asyncio.create_task(page.push_route("/login"))

    body = ft.Column(
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            ft.Text("Welcome Home!", size = 28, weight = ft.FontWeight.BOLD),
            ft.Text("Choose an option:"),

            ft.Button("Profile", on_click = button_clicked),
            ft.Button("Settings", on_click = button_clicked),
            ft.Button("Logout", on_click = logout_clicked),
        ],
    )

    return ft.View(
        route = "/home",
        controls = [
            body
        ],
    )