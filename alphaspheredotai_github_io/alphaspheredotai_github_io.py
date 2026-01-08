"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from alphaspheredotai_github_io.component import contact_item, navbar_icons

app = rx.App(theme=rx.theme(has_background=True, radius="large", accent_color="gray"))


@rx.page(route="/", title="Home Page")
def index() -> rx.Component:
    return rx.container(
        navbar_icons(),
        rx.vstack(
            (rx.heading("AlphaSphere.AI", size="9", weight="bold"),),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


@rx.page(route="/projects", title="Projects")
def projects() -> rx.Component:
    return rx.container((
        navbar_icons(),
        rx.center(
            rx.heading("This page is under construction", size="5", weight="bold"),
            justify="center",
            align="center",
            direction="column",
            min_height="85vh",
        ),
    ))


@rx.page(route="/contact", title="Contact")
def contact() -> rx.Component:
    return rx.container((
        navbar_icons(),
        rx.center(
            (
                rx.button(
                    "alphasphere.ai@gmail.com",
                    size="4",
                    variant="soft",
                    on_click=rx.redirect(
                        "mailto:alphasphere.ai@gmail.com",
                        is_external=True,
                    ),
                ),
                rx.divider(),
                rx.hstack(
                    (
                        contact_item("GitHub", "https://github.com/AlphaSphereDotAI"),
                        contact_item("Kaggle", "https://kaggle.com/organizations/AlphaSphereDotAI"),
                        contact_item("Hugging Face", "https://huggingface.co/AlphaSphereDotAI"),
                        contact_item("LinkedIn", "https://linkedin.com/company/AlphaSphereDotAI"),
                        contact_item("Twitter", "https://twitter.com/AlphaSphereAI"),
                    ),
                    align="center",
                    justify="center",
                    spacing="5",
                ),
            ),
            justify="center",
            align="center",
            direction="column",
            min_height="85vh",
            spacing="5",
        ),
    ))
