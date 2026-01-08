"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from alphaspheredotai_github_io.pages import contact_page, home_page, projects_page

app = rx.App(theme=rx.theme(radius="large", accent_color="gray"))


@rx.page(route="/", title="Home Page")
def index() -> rx.Component:
    return home_page


@rx.page(route="/projects", title="Projects")
def projects() -> rx.Component:
    return projects_page


@rx.page(route="/contact", title="Contact")
def contact() -> rx.Component:
    return contact_page
