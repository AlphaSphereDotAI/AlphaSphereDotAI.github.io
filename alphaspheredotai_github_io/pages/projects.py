import reflex as rx

from alphaspheredotai_github_io.component import navbar_icons, project_card


def projects_page() -> rx.Component:
    """Projects page component."""
    return rx.container(
        (
            navbar_icons(),
            rx.center(
                rx.flex(
                    (
                        project_card(
                            title="Chatacter",
                            description="Live Chat with Virtual Character.",
                            project_url="https://github.com/AlphaSphereDotAI/chatacter",
                        ),
                        project_card(
                            title="Vocalizr",
                            description="Voice Generator part of the Chatacter Backend.",
                            project_url="https://github.com/AlphaSphereDotAI/vocalizr",
                        ),
                        project_card(
                            title="Visualizr",
                            description="Video Generator part of the Chatacter Backend.",
                            project_url="https://github.com/AlphaSphereDotAI/visualizr",
                        ),
                        project_card(
                            title="Chattr",
                            description="App part of the Chatacter Backend.",
                            project_url="https://github.com/AlphaSphereDotAI/chattr",
                        ),
                    ),
                    align="center",
                    justify="center",
                    spacing="5",
                    flex_wrap="wrap",
                    width="100%",
                ),
                justify="center",
                align="center",
                direction="column",
                min_height="85vh",
            ),
        ),
    )
