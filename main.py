import flet as ft
from layout import pages

navigation_bar_index = [
    "home", "service", "home", "mine"
]

page_content = ft.SafeArea(
    adaptive=True,
    expand=1,
    content=pages[navigation_bar_index[0]]
)
flet_theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN_900)

def main(page: ft.Page):
    global page_content

    def on_change_page(e):
        selected_index = e.control.selected_index
        if 0 <= selected_index < len(navigation_bar_index):
            page_content.content = pages[navigation_bar_index[selected_index]]
            page.update()
        else:
            print(f"Index {selected_index} is out of bounds")
            page_content.content = pages["not_found"]
            page.update()

    page.theme = flet_theme
    page.title = "农大生活"
    page.navigation_bar = ft.NavigationBar(
        adaptive=True,
        height=90,
        on_change=on_change_page,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="首页"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.APPS,
                label="服务"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SMART_TOY,
                label="农大智能",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.ACCOUNT_CIRCLE_OUTLINED,
                label="我的",
            ),
        ]
    )
    page.add(
        page_content
    )


ft.app(main)
