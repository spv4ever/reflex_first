# chatapp.py
import reflex as rx

from reflex_first.componentes.navbar import navbar
from reflex_first.views.header import header
from reflex_first.views.links import links
from reflex_first.views.footer import footer
import reflex_first.styles.styles as styles
from reflex_first.styles.styles import Size as Size


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value

                )
            ),
        footer(),
    )

app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets=["fonts/Fonts.css"],
)
app.add_page(index)