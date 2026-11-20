import asyncio
import flet as ft
import json
import os
from pathlib import Path

def get_assets_dir() -> Path:
    default_assets_dir = Path(__file__).parent / "assets" # fallback for local runs
    return Path(os.environ.get("FLET_ASSETS_DIR", str(default_assets_dir))).resolve()

def load_user():
    fill_path = get_assets_dir() / "data" / "users.json"
    if not fill_path.exists():
        return {"users": []}

    with open(fill_path, "r") as f:
        return json.load(f)

USERS = load_user()

def add_users(user):
    #Update existing user
    for i, existing in enumerate(USERS["users"]):
        if existing["username"].lower() == user["username"].lower():
            USERS["users"][i] = user
            break

    else:
        #Runs if the loop completes without hitting break
        USERS["users"].append(user)

    file_path = get_assets_dir() / "data" / "users.json"
    file_path.parent.mkdir(parents = True, exist_ok = True)

    with open(file_path, "w") as f:
        json.dump(USERS, f, indent = 2)

def check_username(username):
    for user in USERS["users"]:
        if user["username"].lower() == username.lower():
            return user
    return None

def register_page(page: ft.Page):
    page.tittle = "Registration Page"

    #===========================================================Functions==================================================================
    def accept_terms(e):
        terms_checkbox.value = True
        terms_dialog.open = False
        page.update()

    def open_terms(e):
        terms_dialog.open = True
        page.update()

    def decline_terms(e):
        terms_checkbox.value = False
        terms_dialog.open = False
        page.update()

    def handle_register(e):
        u_val = username.value.strip() if username.value else ""
        f_val = fullname.value.strip() if fullname.value else ""
        p_val = password.value or ""
        cp_val = confirm_password.value or ""

        if not u_val or not f_val or not p_val:
            error_message.value = "Please fill in all fields"
            error_message.visible = True
            page.update()
            return

        if check_username(u_val):
            error_message.value = "Username already exists"
            error_message.visible = True
            page.update()
            return

        if p_val != cp_val:
            error_message.value = "Passwords do not match"
            error_message.visible = True
            page.update()
            return

        if not terms_checkbox.value:
            error_message.value = "You must agree to the terms & conditions"
            error_message.visible = True
            page.update()
            return

        # Build and append user data
        new_user = {
            "username": u_val,
            "fullname": f_val,
            "password": p_val  # Note: Consider hashing passwords before storing
        }

        add_users(new_user)

        # Clear fields and show success state
        error_message.visible = False
        username.value = ""
        fullname.value = ""
        password.value = ""
        confirm_password.value = ""
        terms_checkbox.value = False

        page.show_dialog(ft.SnackBar(ft.Text("Account registered successfully!")))
        page.update()

    def field_with_label(label, icon, field):
        return ft.Column(
            spacing=5,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Row(
                    spacing=8,
                    controls=[
                        ft.Icon(
                            icon,
                            color="#0084a8",
                            size=20,
                        ),
                        ft.Text(
                            label,
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color="#0084a8",
                        ),
                    ],
                ),
                field,
            ],
        )

    #========================================================Layout Components=============================================================
    username = ft.TextField(
        hint_text = "Username",
        text_style = ft.TextStyle(color = "#0084a8"),
        # width = page.width * 0.5,
        border_color = "#0084a8",
        focused_border_color = "#0084a8",
        border_radius = ft.BorderRadius.all(10),
        content_padding = ft.Padding(10, 10, 10, 10)
    )

    fullname = ft.TextField(
        hint_text = "Enter your fullname",
        text_style = ft.TextStyle(color = "#0084a8"),
        # width = page.width * 0.5,
        border_color = "#0084a8",
        focused_border_color = "#0084a8",
        border_radius = ft.BorderRadius.all(10),
        content_padding = ft.Padding(10, 10, 10, 10)
    )

    password = ft.TextField(
        hint_text = "Password",
        password = True,
        can_reveal_password = True,
        text_style = ft.TextStyle(color = "#0084a8"),
        # width = page.width * 0.5,
        border_color = "#0084a8",
        focused_border_color = "#0084a8",
        border_radius = ft.BorderRadius.all(10),
        content_padding = ft.Padding(10, 10, 10, 10)
    )

    confirm_password = ft.TextField(
        hint_text = "Confirm Password",
        password = True,
        can_reveal_password = True,
        text_style = ft.TextStyle(color = "#0084a8"),
        # width = page.width * 0.5,
        border_color = "#0084a8",
        focused_border_color = "#0084a8",
        border_radius = ft.BorderRadius.all(10),
        content_padding = ft.Padding(10, 10, 10, 10)
    )

    error_message = ft.Text(
        "",
        size = 15,
        weight = ft.FontWeight.BOLD,
        color = "#ff0000",
        visible = False
    )

    terms_checkbox = ft.Checkbox(value = False)


    terms_dialog = ft.AlertDialog(
        modal = True,
        title = ft.Text("Terms & Conditions", color = "#0084a8", weight = ft.FontWeight.BOLD),
        content = ft.Container(
            width = 400,
            height = 220,
            content = ft.Column(
                scroll = ft.ScrollMode.AUTO,
                controls = [
                    ft.Text(
                        "1. Introduction\n"
                        "Welcome to our platform. By creating an accoint, you agree to comply with our service policies.\n\n"
                        "2. User Responsibilities\n"
                        "You are responsible for maintaining the confidentiality of your account password and activity.\n\n"
                        "3. Privacy & Data Use\n"
                        "We collect necessary information strictly to improve user experience and deliver service features.\n\n"
                        "4. Account Termination\n"
                        "We reserve thr right to suspend accounts that violate our community standards.",
                        color = "#FFFBFB",
                        size = 14
                    )
                ],
            ),
        ),
        actions = [
            ft.TextButton("Decline", on_click = decline_terms),
            ft.Button(
                "Accept",
                bgcolor = "#0084a8",
                color = "#ffffff",
                on_click = accept_terms,
            ),
        ],
        actions_alignment = ft.MainAxisAlignment.END,
    )

    page.overlay.append(terms_dialog)

    async def go_to_login(e):
        await page.push_route("/login")
        

    # Registration button
    register_button = ft.Button(
        content="Create Account",
        width=250,
        height=45,
        bgcolor="#0084a8",
        color="#ffffff",
        on_click=handle_register,
    )

    # Main registration card
    body = ft.Container(
        expand=True,
        bgcolor="#0084a8",
        alignment=ft.Alignment.CENTER,
        padding=20,
        content=ft.Container(
            # height=page.height * 0.9 if page.height else 700,
            # width=min(page.width * 0.5, 550) if page.width else 450,
            height = page.height * 0.9,
            width = page.width * 0.8,
            bgcolor="#ffffff",
            border_radius=ft.BorderRadius.all(20),
            padding=ft.Padding(40, 30, 40, 30),

            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
                spacing=15,

                controls=[
                    # ================= Heading =================
                    ft.Text(
                        "Create Account",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="#0084a8",
                    ),

                    ft.Text(
                        "Register to get started",
                        size=15,
                        color="#666666",
                    ),

                    # ================= Username =================
                    field_with_label(
                        "Username",
                        ft.Icons.PERSON,
                        username,
                    ),

                    # ================= Full Name =================
                    field_with_label(
                        "Full Name",
                        ft.Icons.BADGE,
                        fullname,
                    ),

                    # ================= Password =================
                    field_with_label(
                        "Password",
                        ft.Icons.LOCK,
                        password,
                    ),

                    # ================= Confirm Password =================
                    field_with_label(
                        "Confirm Password",
                        ft.Icons.LOCK_RESET,
                        confirm_password,
                    ),

                    # ================= Terms & Conditions =================
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            terms_checkbox,

                            ft.Text(
                                "I agree to the",
                                size=13,
                                color="#333333",
                            ),

                            ft.GestureDetector(
                                on_tap=open_terms,
                                content=ft.Text(
                                    "Terms & Conditions",
                                    size=13,
                                    weight=ft.FontWeight.BOLD,
                                    color="#0084a8",
                                ),
                            ),
                        ],
                    ),

                    # ================= Error Message =================
                    error_message,

                    # ================= Register Button =================
                    ft.Button(
                        content="Create Account",
                        width=250,
                        height=45,
                        bgcolor="#0084a8",
                        color="#ffffff",
                        on_click=handle_register,
                    ),

                    # ================= Divider =================
                    ft.Divider(
                        height=20,
                        color="#dddddd",
                    ),

                    # ================= Login Navigation =================
                    ft.Container(
                        padding=ft.Padding(0, 10, 0, 0),
                        alignment=ft.Alignment.CENTER,

                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5,

                            controls=[
                                ft.Text(
                                    "Already have an account?",
                                    size=14,
                                    color="#0084a8",
                                ),

                                ft.GestureDetector(
                                    on_tap=lambda e: asyncio.create_task(
                                        page.push_route("/login")
                                    ),

                                    content=ft.Text(
                                        "Log in",
                                        size=14,
                                        weight=ft.FontWeight.BOLD,
                                        color="#0084a8",
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),
    )

    # ================= Display Page =================
    return ft.View(
        route = "/register",
        controls = [
            body
        ],
    )

    