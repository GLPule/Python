import flet as ft
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

def update_users(user):
    # Update global User
    for i, existing in enumerate(USERS["users"]):
        if existing["username"] == user["username"]:
            USERS["users"][i] = user
            break

    # Update file in folder

    default_path = get_assets_dir()

    with open(f"{default_path}/data/users.json", "w") as f:
        json.dump(USERS, f, indent = 2)

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
    users_data = load_users()

    for user in users_data["users"]:
        if user["username"].strip().lower() == username.strip().lower():
            return user

    return None


def update_users(user):
    # Always load the latest data
    users_data = load_users()

    updated = False

    for i, existing in enumerate(users_data["users"]):
        if existing["username"].strip().lower() == user["username"].strip().lower():
            users_data["users"][i] = user
            updated = True
            break

    if not updated:
        raise ValueError("User not found. Password was not updated.")

    file_path = get_assets_dir() / "data" / "users.json"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(users_data, f, indent=2)

def reset_password(page: ft.Page):
    
    #===========================================================Functions==================================================================
    # Cancel Button
    def on_cancel(e):
        page.pop_dialog()

    # Next Button
    def on_next(e):
        if not username_textfield.value:
            username_textfield.helper = "Username cannot be left empty"
            username_textfield.update()
            return
        else:
            username_textfield.helper = None
            username_textfield.update()

        # Check against database
        user = check_username(username_textfield.value)

        if not user:
            error_text.visible = True
            error_text.update()
            return
        else:
            error_text.visible = False
            error_text.update()

        page.session.store.set("user", user)

        # Prepare dialog
        modal.title = "Update Password"
        modal.content = ft.Column(
            tight = True,
            controls = [
                password_textfield,
                cpassword_textfield,
                error_text
            ]
        )
        modal.actions = [
            ft.Button(
            content = "Cancel",
            on_click = on_cancel
            ),
            ft.Button(
                content = "Save",
                on_click = on_save
            ),
        ]
        page.update()

    def on_save(e):
        if not password_textfield.value:
            password_textfield.helper = "password cannot be left empty"
            password_textfield.update()
            return
        else:
            password_textfield.helper = None
            password_textfield.update()

        if not cpassword_textfield.value:
            cpassword_textfield.helper = "cpassword cannot be left empty"
            cpassword_textfield.update()
            return
        else:
            cpassword_textfield.helper = None
            cpassword_textfield.update()

        if password_textfield.value != cpassword_textfield.value:
            error_text.value = "Password do not match"
            error_text.visible = True
            error_text.update()
            return
        else:
            error_text.visible = False
            error_text.update()

        user = page.session.store.get("user")

        user["password"] = password_textfield.value

        # Update global and database
        update_users(user)
        page.session.store.set("user", user)

        page.pop_dialog()

    #========================================================Layout Components=============================================================
    # Username
    username_textfield = ft.TextField(
        hint_text = "Username",
        border_radius = ft.BorderRadius.all(10),
        helper_style = ft.TextStyle(
            color = ft.Colors.RED
        )
    )

    # Passsword
    password_textfield = ft.TextField(
        hint_text = "Password",
        password = True,
        can_reveal_password = True,
        border_radius = ft.BorderRadius.all(10),
        helper_style = ft.TextStyle(
            color = ft.Colors.RED
        )
    )

    cpassword_textfield = ft.TextField(
        hint_text = "Corfirm Password",
        password = True,
        can_reveal_password = True,
        border_radius = ft.BorderRadius.all(10),
        helper_style = ft.TextStyle(
            color = ft.Colors.RED
        )
    )

    # Error Message
    error_text = ft.Text(
        "Username not found",
        size = 15,
        weight = ft.FontWeight.BOLD,
        color = ft.Colors.RED,
        visible = False,
    )

    modal = ft.AlertDialog(
        modal = True,
        title = "Confirm Username",
        content = ft.Column(
            tight = True,
            controls = [
                username_textfield,
                error_text
            ]
        ),
        actions = [
            ft.Button(
                content = "Cancel",
                on_click = on_cancel
            ),
            ft.Button(
                content = "Next",
                on_click = on_next
            ),
        ]
    )

    return modal