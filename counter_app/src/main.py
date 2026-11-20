import flet as ft

count = 0

def main(page: ft.Page):
    page.title = "Counter"
    page.window.height = 750
    page.window.width = 450

    def add(e):
        global count
        count += 1
        counter.value = count
        counter.update()

    def reset(e):
        global count
        count = 0
        counter.value = count
        counter.update()

    def minus(e):
        global count
        count -= 1
        counter.value = count
        counter.update()

    head_text = ft.Text(
        value = "Counter App",
        size = 50,
        style = ft.TextStyle(
            color = ft.Colors.WHITE,
        )
    )

    counter = ft.Text(
        value = count,
        size = 250,
        style = ft.TextStyle(
            color = ft.Colors.ORANGE,
        )
    )

    minus_button = ft.Button(
        content = ft.Icon(icon = ft.Icons.REMOVE, size = 30),
        style = ft.ButtonStyle(shape = ft.CircleBorder(), padding = 30),
        bgcolor = ft.Colors.RED,
        on_click = minus,
    )

    reset_button = ft.Button(
        content = ft.Icon(icon = ft.Icons.RESTORE, size = 30),
        style = ft.ButtonStyle(shape = ft.StadiumBorder(), padding = 30),
        on_click = reset,
    )

    add_button = ft.Button(
        content = ft.Icon(icon = ft.Icons.ADD, size = 30),
        style = ft.ButtonStyle(shape = ft.CircleBorder(), padding = 30),
        bgcolor = ft.Colors.BLUE,
        on_click = add,
    )


    body = ft.Container(
        bgcolor = ft.Colors.BLACK,
        expand = True,
        height = page.height,
        width = page.width,

        content = ft.Column(
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,

            controls = [
                head_text,
                counter,
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        minus_button,
                        reset_button,
                        add_button
                    ]
                )
            ]
        )
    )


    page.add(body)              



if __name__ == "__main__":
    ft.run(main)
