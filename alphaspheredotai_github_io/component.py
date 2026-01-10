import reflex as rx

from alphaspheredotai_github_io.team.team_member import TeamMember


def _navbar_item_desktop_only(text: str, icon: str, url: str) -> rx.Component:
    """Create a navbar item for desktop view."""
    return rx.link(
        rx.hstack(rx.icon(icon), rx.text(text, size="4", weight="medium")),
        href=url,
    )


def _navbar_item_mobile_and_tablet(text: str, icon: str, url: str) -> rx.Component:
    """Create a navbar item for mobile and tablet view."""
    return rx.link(
        rx.hstack(rx.icon(icon, size=16), rx.text(text, size="3", weight="medium")),
        href=url,
    )


def navbar_icons() -> rx.Component:
    """Create the navbar with icons for desktop and mobile/tablet."""
    return rx.box(
        (
            rx.desktop_only(
                rx.hstack(
                    (
                        _navbar_item_desktop_only("Home", "home", "/"),
                        _navbar_item_desktop_only("Team", "users", "/team"),
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
                        _navbar_item_mobile_and_tablet("Team", "users", "/team"),
                        _navbar_item_mobile_and_tablet(
                            "Projects",
                            "code-xml",
                            "/projects",
                        ),
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
                rx.image(
                    src=avatar,
                    alt=name,
                    border_radius="25%",
                    height="25%",
                    width="25%",
                ),
                rx.heading(name, size="4", weight="bold"),
                rx.text(username, color_scheme="gray"),
                rx.link(
                    rx.button(
                        (
                            rx.text("link"),
                            rx.icon("link", size=16, color="gray"),
                        ),
                        variant="soft",
                    ),
                    href=url,
                    is_external=True,
                ),
            ),
            direction="column",
            spacing="1",
            align="center",
        ),
    )


def socialmedia_links(link: str, socialmedia_type: str) -> rx.Component:
    """Create social media links component."""
    return rx.link(
        rx.icon(socialmedia_type, size=24),
        href=link,
        is_external=True,
    )


def team_member_card(team_member: TeamMember) -> rx.Component:
    """Create a team member card."""
    return rx.card(
        rx.flex(
            (
                rx.image(
                    src=team_member.avatar,
                    alt=team_member.name,
                    border_radius="25%",
                    height="auto",
                    width="100px",
                ),
                rx.heading(team_member.name, size="4", weight="bold"),
                rx.text(team_member.role, color_scheme="gray", italic=True),
                rx.text(team_member.bio, text_align="center"),
                rx.flex(
                    (
                        socialmedia_links(
                            team_member.social_links.github,
                            "github",
                        ),
                        socialmedia_links(
                            team_member.social_links.linkedin,
                            "linkedin",
                        ),
                        socialmedia_links(
                            team_member.social_links.twitter,
                            "twitter",
                        )
                        if team_member.social_links.twitter
                        else None,
                    ),
                    direction="row",
                    align="center",
                    justify="center",
                    spacing="5",
                    flex_wrap="wrap",
                ),
            ),
            direction="column",
            align="center",
            justify="center",
            spacing="2",
        ),
        align="center",
        justify="center",
    )


def project_card(title: str, description: str, project_url: str) -> rx.Component:
    """Create a project card component."""
    return rx.card(
        rx.flex(
            (
                rx.heading(title, size="4", weight="bold"),
                rx.text(description),
                rx.link(
                    rx.button(
                        (
                            rx.text("View Project"),
                            rx.icon("external-link", size=16, color="gray"),
                        ),
                        variant="soft",
                    ),
                    href=project_url,
                    is_external=True,
                ),
            ),
            direction="column",
            align="center",
            spacing="3",
        ),
        size="5",
        direction="column",
    )
