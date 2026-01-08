import reflex as rx


def _navbar_item_desktop_only(text: str, icon: str, url: str) -> rx.Component:
    """Create a navbar item for desktop view."""
    return rx.link(rx.hstack(rx.icon(icon), rx.text(text, size="4", weight="medium")), href=url)


def _navbar_item_mobile_and_tablet(text: str, icon: str, url: str) -> rx.Component:
    """Create a navbar item for mobile and tablet view."""
    return rx.link(rx.hstack(rx.icon(icon, size=16), rx.text(text, size="3", weight="medium")), href=url)


def navbar_icons() -> rx.Component:
    """Create the navbar with icons for desktop and mobile/tablet."""
    return rx.box(
        (
            rx.desktop_only(
                rx.hstack(
                    (
                        _navbar_item_desktop_only("Home", "home", "/"),
                        _navbar_item_desktop_only("Projects", "code-xml", "/projects"),
                        _navbar_item_desktop_only("Contact", "mail", "/contact"),
                        rx.color_mode.button(),
                    ),
                    spacing="6",
                    justify="between",
                    align_items="center",
                ),
            ),
            rx.mobile_and_tablet(
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        _navbar_item_mobile_and_tablet("Home", "home", "/"),
                        _navbar_item_mobile_and_tablet("Projects", "code-xml", "/projects"),
                        _navbar_item_mobile_and_tablet("Contact", "mail", "/contact"),
                        rx.color_mode.button(),
                    ),
                    justify="end",
                ),
            ),
        ),
        # background="#543af5",
        padding="0.5em",
        width="100%",
        border_radius="5px",
    )


def contact_item(
    name: str,
    url: str,
    avatar: str,
    username: str = "@AlphaSphereDotAI",
) -> rx.Component:
    """Create a contact item card."""
    return rx.card(
        rx.flex(
            (
                rx.avatar(src=avatar),
                rx.heading(name, size="4", weight="bold"),
                rx.text(username, color_scheme="gray"),
                rx.button(
                    (rx.text("link"), rx.icon("link", size=16, color="gray")),
                    variant="soft",
                    on_click=rx.redirect(url, is_external=True),
                ),
            ),
            direction="column",
            spacing="1",
            align="center",
        ),
    )
