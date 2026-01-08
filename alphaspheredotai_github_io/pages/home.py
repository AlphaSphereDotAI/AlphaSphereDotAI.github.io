import reflex as rx

from alphaspheredotai_github_io.component import navbar_icons


def home_page() -> rx.Component:
    """Home page component."""
    return rx.box(
        rx.container(
            navbar_icons(),
            rx.center(
                rx.hstack(
                    rx.center(
                        (
                            rx.image(
                                src="https://raw.githubusercontent.com/AlphaSphereDotAI/.github/main/Logos/400x400.jpg",
                                alt="AlphaSphere.AI Logo",
                                border_radius="50px",
                                height="100px",
                                width="100px",
                            ),
                            rx.heading(
                                "AlphaSphere.AI",
                                size="9",
                                weight="bold",
                            ),
                        ),
                        spacing="5",
                        justify="center",
                    ),
                    spacing="5",
                    justify="center",
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        ),
        background="linear-gradient(#543af5,#1d173d)",
        radius="full",
        width="100%",
        height="100vh",
    )
