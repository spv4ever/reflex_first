import reflex as rx
import datetime
from reflex_first.styles.styles import Size as Size

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src='avatar.png'),
        rx.link(f'© 1991-{datetime.date.today().year} Blog personal de Albert García.',
                href="https://github.com/spv4ever",
                is_external=True,
                font_size = Size.MEDIUM.value),
                rx.hstack(
                    rx.text(
                        "Aprendiendo desarrollo web desde Catalunya. Gracias",
                        font_size = Size.MEDIUM.value,
                        ),
                    rx.link(
                        "@mouredev",
                        href="https://mouredev.com/",
                        is_external=True,
                        font_size = Size.MEDIUM.value,
                        ),
                    margin_top="0px !important",
                    ),
    margin_bottom=Size.BIG.value,
    )