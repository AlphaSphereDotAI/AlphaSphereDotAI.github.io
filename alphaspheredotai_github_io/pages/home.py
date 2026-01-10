import reflex as rx

from alphaspheredotai_github_io.component import navbar_icons


def home_page() -> rx.Component:
    """Home page component."""
    return rx.container(
        navbar_icons(),
        rx.center(
            (
                rx.image(
                    src="https://raw.githubusercontent.com/AlphaSphereDotAI/.github/main/Logos/400x400.jpg",
                    alt="AlphaSphere.AI Logo",
                    border_radius="50%",
                    height="auto",
                    width="25%",
                ),
                rx.desktop_only(
                    rx.heading("AlphaSphere.AI", size="9", weight="bold"),
                ),
                rx.mobile_and_tablet(
                    rx.heading("AlphaSphere.AI", size="7", weight="bold"),
                ),
            ),
            spacing="5",
            justify="center",
            align="center",
            direction="column",
            min_height="85vh",
        ),
        min_height="85vh",
        background="linear-gradient(#543af5,#1d173d)",
        radius="full",
        width="100%",
        height="100vh",
    )
