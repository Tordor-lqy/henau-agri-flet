import flet as ft
from layout.pages import pages

class NavTab(ft.Tabs):
    def __init__(self, nav_tab_config: dict, *args, **kwargs):
        super().__init__(
            selected_index=1,
            animation_duration=300,
            # scrollable=False,
            tabs=[
                ft.Tab(
                    text=tab.get('text', "未知"),
                    content=pages.get(
                        tab.get('page'),
                        ft.Container(
                            content=ft.Text(
                                value=tab.get('text' , "未知") + "页面不可用"
                            ),
                            alignment=ft.alignment.center
                        )
                    )
                )
                for tab in nav_tab_config.get('tabs', [])
            ],
            expand=1,
            *args, **kwargs)