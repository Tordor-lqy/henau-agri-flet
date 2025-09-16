import flet as ft

services_page = ft.Container(
    content=ft.Column(
        controls=[
            ft.Tabs(
                scrollable=False,
                height=40,
                tabs=[
                    ft.Tab(tab_content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.BOOK, size=14),
                            ft.Text(value="二手书交易", size=10)
                        ]
                    )),
                    ft.Tab(tab_content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.FASTFOOD, size=14),
                            ft.Text(value="校外订餐", size=10)
                        ]
                    )),
                    ft.Tab(tab_content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.DESCRIPTION, size=14),
                            ft.Text(value="打印资料", size=10)
                        ]
                    ))
                ]
            ),
        ]
    ),
)
