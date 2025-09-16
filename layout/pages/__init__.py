import flet as ft
from .service import services_page


pages = {
    "home": ft.Container(
        content=ft.Text(
            value="home"
        ),
        alignment=ft.alignment.center
    ),
    "service": ft.Container(
        content=services_page
    ),
    "not_found" : ft.Container(
        content=ft.Text(
            value="404"
        ),
        alignment=ft.alignment.center
    )
}
