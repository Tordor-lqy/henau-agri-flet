import flet as ft
from flet.core.buttons import ButtonStyle


class Button(ft.ElevatedButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            style=ButtonStyle(
                shape=ft.ContinuousRectangleBorder(
                    radius=10,
                ),
                shadow_color=ft.CupertinoColors.with_opacity(
                    opacity=0, color="primary"
                )
            ),
            animate_opacity=0,
            *args, **kwargs)
