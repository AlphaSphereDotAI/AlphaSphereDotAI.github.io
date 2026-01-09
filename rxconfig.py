import reflex as rx

config = rx.Config(
    app_name="alphaspheredotai_github_io",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    show_built_with_reflex=False,api_url="https://alphaspheredotai.is-a.dev"
)
