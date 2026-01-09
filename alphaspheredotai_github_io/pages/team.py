import reflex as rx

from alphaspheredotai_github_io.component import navbar_icons, team_member_card
from alphaspheredotai_github_io.team.member import (
    AbdelrahmanAminInfo,
    AbdelrahmanMostafaInfo,
    MohamedHishamInfo,
    YousefMohamedInfo,
)


def team_page() -> rx.Component:
    """Team page component."""
    return rx.container(
        (
            navbar_icons(),
            rx.center(
                rx.flex(
                    (
                        team_member_card(AbdelrahmanAminInfo),
                        team_member_card(AbdelrahmanMostafaInfo),
                        team_member_card(MohamedHishamInfo),
                        team_member_card(YousefMohamedInfo),
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
