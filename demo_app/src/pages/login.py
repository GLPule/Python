import flet as ft
import asyncio
from components.reset_password import reset_password
import json
import os
from pathlib import Path

def get_assets_dir() -> Path:
    default_assets_dir = Path(__file__).parent / "assets" # fallback for local runs
    return Path(os.environ.get("FLET_ASSETS_DIR", str(default_assets_dir))).resolve()

'''def load_users():
    default_path = get_assets_dir()

    with open(f"{default_path}/data/users.json", "r") as f:
        return json.load(f)

USERS = load_users()

def check_username(username):
    for user in USERS["users"]:
        if user["username"].lower() == username.lower():
            return user
        
    return None'''

def load_users():
    file_path = get_assets_dir() / "data" / "users.json"

    if not file_path.exists():
        return {"users": []}

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def check_username(username):
    # Reload users from the JSON file every time
    users_data = load_users()

    for user in users_data["users"]:
        if user["username"].strip().lower() == username.strip().lower():
            return user

    return None

def login_page(page: ft.Page) -> ft.View:
    page.tittle = "Login Page"
    page.window.height = 750
    page.window.width = 450

    user = {
        "username": "user1",
        "password": "pass1"
    }

    #===========================================================Functions==================================================================
    # Login Button
    def login_click(e):
        if not username_textfield.value:
            username_textfield.helper = "Username cannot be left empty"
            username_textfield.update()
            return
        else:
            username_textfield.helper = None
            username_textfield.update()
        
        if not password_textfield.value:
           password_textfield.helper = "Password cannot be left empty"
           password_textfield.update()
           return
        else:
           password_textfield.helper = None
           password_textfield.update()

        user = check_username(username_textfield.value)

        if user is None:
            error_text.visible = True
            error_text.value = "Username not found"
            error_text.update()
            return
        
        if user["password"] != password_textfield.value:
            error_text.visible = True
            error_text.value = "Incorrect password"
            error_text.update()
            return

        error_text.visible = False
        error_text.update()

        page.session.store.set("user", user)

        asyncio.create_task(page.push_route("/home"))

    # Forgot Password Link
    def on_forgot_password(e):
        page.show_dialog(reset_password(page))

    #========================================================Layout Components=============================================================
    # Login Text
    login_text = ft.Container(
        padding = ft.Padding(0,20,0,30),
        content = ft.Text(
            "Login",
            size = 40,
            weight = ft.FontWeight.BOLD,
            color = "#0084a8"
        )
    )

    # Username
    username_label = ft.Row(
        controls = [
            ft.Icon(
                icon = ft.Icons.PERSON,
                color = "#0084a8"
            ),
            ft.Text(
                "Username",
                color = "#0084a8",
                size = 15,
                weight = ft.FontWeight.BOLD,
            )
        ]
    )

    username_textfield = ft.TextField(
        hint_text = "Username",
        text_style = ft.TextStyle(
            color = "#0084a8"
        ),
        border_color = "#0084a8",
        focused_border_color = "#0084a8",
        border_radius = ft.BorderRadius.all(10),
        helper_style = ft.TextStyle(
            color = ft.Colors.RED
        )
    )

    # Password
    password_label = ft.Row(
        controls = [
            ft.Icon(
                icon = ft.Icons.LOCK,
                color = "#0084a8"
            ),
            ft.Text(
                "Password",
                color = "#0084a8",
                size = 15,
                weight = ft.FontWeight.BOLD,
            )
        ]
    )

    password_textfield = ft.TextField(
        hint_text = "Password",
        text_style = ft.TextStyle(
            color = "#0084a8"
        ),
        border_color = "#0084a8",
        focused_border_color = "#0084a8",
        border_radius = ft.BorderRadius.all(10),
        password = True,
        can_reveal_password = True,
        helper_style = ft.TextStyle(
            color = ft.Colors.RED
        )
    )

    # Remember Me & Forgot password
    fp_text = ft.Row(
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,

        controls = [
            ft.Checkbox(
                label = "Keep me logged in",
                label_style = ft.TextStyle(
                    color = "#0084a8"
                ),
            ),
            ft.GestureDetector(
                content = ft.Text(
                    "Forgot Password",
                    weight = ft.FontWeight.BOLD,
                    color = "#0084a8"
                ),
                on_tap = on_forgot_password
            )
        ]
    )

    # Error Message
    error_text = ft.Text(
        "Invalid username or password",
        size = 15,
        weight = ft.FontWeight.BOLD,
        color = ft.Colors.RED,
        visible = False,
    )

    # Login button
    login_button = ft.Container(
        padding = ft.Padding(0,20,0,0),

        content = ft.Button(
            content = "Login",
            bgcolor = "#0084a8",
            color = "#ffffff",
            height = 40,
            width = page.width,
            on_click = login_click        
        )
    )

    # Sign Up link
    signup_text = ft.Container(
        padding = ft.Padding(0,20,0,0),
        alignment = ft.Alignment.CENTER,

        content = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,

                controls = [
                ft.Text(
                    "Don't have an account?",
                    size = 15,
                    color = "#0084a8"
                ),
                ft.GestureDetector(
                    on_tap = lambda e : asyncio.create_task(page.push_route("/register")),
                    content = ft.Text(
                        "Sign Up",
                        size = 15,
                        weight = ft.FontWeight.BOLD,
                        color = "#0084a8"
                    )
                ),
            ]
        )
    )

    body = ft.Container(
        expand = True,
        bgcolor = "#0084a8",
        alignment = ft.Alignment.CENTER,

        content = ft.Container(
            height = page.height * 0.8,
            width = page.width * 0.8,
            bgcolor = ft.Colors.WHITE,
            border_radius = ft.BorderRadius.all(20),
            padding = ft.Padding(40,40,40,40),

            content = ft.Column(
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,

                controls = [
                    login_text,
                    username_label,
                    username_textfield,
                    password_label,
                    password_textfield,
                    fp_text,
                    error_text,
                    login_button,
                    signup_text
                ]
            )
        )
    )

    return ft.View(
        route = "/login",
        controls = [
            body
        ],
    )
