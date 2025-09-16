import flet as ft
from .service import services_page
from .mine import mine_page


pages = {
    "home": ft.Container(
        content=ft.Text(
            value="home"
        ),
        alignment=ft.alignment.center
    ),
    "service": services_page,
    "mine" : mine_page,
    "not_found" : ft.Container(
        content=ft.Text(
            value="404"
        ),
        alignment=ft.alignment.center
    )
}
