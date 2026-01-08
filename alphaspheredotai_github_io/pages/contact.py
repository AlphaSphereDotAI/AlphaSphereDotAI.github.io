import reflex as rx

from alphaspheredotai_github_io.component import contact_item, navbar_icons


def contact_page() -> rx.Component:
    return rx.container(
        (
            navbar_icons(),
            rx.center(
                rx.flex(
                    (
                        contact_item(
                            "Gmail",
                            "mailto:alphasphere.ai@gmail.com",
                            "https://pbs.twimg.com/profile_images/1313394640393957378/L0W5hykJ_400x400.jpg",
                            "alphasphere.ai@gmail.com",
                        ),
                        contact_item(
                            "GitHub",
                            "https://github.com/AlphaSphereDotAI",
                            "https://pbs.twimg.com/profile_images/1633247750010830848/8zfRrYjA_400x400.png",
                        ),
                        contact_item(
                            "Kaggle",
                            "https://kaggle.com/organizations/AlphaSphereDotAI",
                            "https://pbs.twimg.com/profile_images/1573129499343978498/03a7wgfE_400x400.jpg",
                        ),
                        contact_item(
                            "Hugging Face",
                            "https://huggingface.co/AlphaSphereDotAI",
                            "https://pbs.twimg.com/profile_images/1991559933473497089/mbrRS49P_400x400.jpg",
                        ),
                        contact_item(
                            "LinkedIn",
                            "https://linkedin.com/company/AlphaSphereDotAI",
                            "https://pbs.twimg.com/profile_images/1661161645857710081/6WtDIesg_400x400.png",
                        ),
                        contact_item(
                            "X",
                            "https://x.com/AlphaSphereAI",
                            "https://pbs.twimg.com/profile_images/1955359038532653056/OSHY3ewP_400x400.jpg",
                            "@AlphaSphereAI",
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
                spacing="5",
            ),
        ),
    )
