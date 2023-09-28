import flet as ft

def main(page: ft.Page):
    page.title = "PyFlet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=150)

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.remove(txt_name, bt1)
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")
    bt1 = ft.ElevatedButton("Say hello!", on_click=btn_click)
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        txt_name,
        bt1,
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click, on_focus=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

#ft.app(target=main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)