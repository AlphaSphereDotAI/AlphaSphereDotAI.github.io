import reflex as rx

from alphaspheredotai_github_io.component import contact_item, navbar_icons


def contact_page() -> rx.Component:
    return rx.container(
        (
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
                            contact_item(
                                "GitHub", "https://github.com/AlphaSphereDotAI"
                            ),
                            contact_item(
                                "Kaggle",
                                "https://kaggle.com/organizations/AlphaSphereDotAI",
                            ),
                            contact_item(
                                "Hugging Face",
                                "https://huggingface.co/AlphaSphereDotAI",
                            ),
                            contact_item(
                                "LinkedIn",
                                "https://linkedin.com/company/AlphaSphereDotAI",
                            ),
                            contact_item(
                                "X", "https://x.com/AlphaSphereAI", "@AlphaSphereAI"
                            ),
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
        ),
    )
