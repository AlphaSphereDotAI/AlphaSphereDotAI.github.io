import reflex as rx

from alphaspheredotai_github_io.component import navbar_icons


def projects_page() -> rx.Component:
    return rx.container(
        (
            navbar_icons(),
            rx.center(
                rx.heading("This page is under construction", size="5", weight="bold"),
                justify="center",
                align="center",
                direction="column",
                min_height="85vh",
            ),
        ),
    )
