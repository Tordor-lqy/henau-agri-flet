import flet as ft
import flet_webview as ftwv

def time_picker_con(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # def handle_change(e):
    #     page.add(ft.Text(f"TimePicker change: {time_picker.value}"))
    #
    # def handle_dismissal(e):
    #     page.add(ft.Text(f"TimePicker dismissed: {time_picker.value}"))
    #
    # def handle_entry_mode_change(e):
    #     page.add(ft.Text(f"TimePicker Entry mode changed to {e.entry_mode}"))

    time_picker = ft.TimePicker(
        confirm_text="确认",
        cancel_text="取消",
        error_invalid_text="Time out of range",
        help_text="Pick your time slot",
        # on_change=handle_change,
        # on_dismiss=handle_dismissal,
        # on_entry_mode_change=handle_entry_mode_change,
    )
    return ft.ElevatedButton(
            "Pick time",
            badge="111",
            icon=ft.Icons.TIME_TO_LEAVE,
            on_click=lambda _: page.open(time_picker),
        )



def main(page: ft.Page):

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="教室预约",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="预约历史",
                # icon=ft.Icons.SETTINGS,
                content=ft.Container(
                    content=time_picker_con(page), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.CircleAvatar(
                    foreground_image_src="https://avatars.githubusercontent.com/u/7119543?s=88&v=4"
                ),
                content=ftwv.WebView(
                    url="https://dormitory.soarli.top/",
                    on_page_started=lambda _: print("Page started"),
                    on_page_ended=lambda _: print("Page ended"),
                    on_web_resource_error=lambda e: print("Page error:", e.data),
                    expand=True,
                ),
            ),
        ],
        expand=1,
    )
    page.add(
        ft.Container(height=30)
    )
    page.add(t)


ft.app(main)