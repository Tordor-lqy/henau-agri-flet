import flet as ft
import layout as ly


def main(page: ft.Page):
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.add(
        ft.SafeArea(
            ly.nav_tab,
            expand=True
        )
    )


ft.app(main)
