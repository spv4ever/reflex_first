import reflex as rx
import datetime
from reflex_first.styles.styles import Size as Size
from reflex_first.styles.colors import Color as Color
from reflex_first.styles.colors import TextColor as TextColor
from reflex_first.styles.fonts import Fuentes as Fuentes

def footer()-> rx.Component:
    return rx.vstack(

        rx.avatar(name="Albert García",
                          size="xl", 
                          src = "keiko_manga.png",
                          padding="2px",
                          border="4px",
                          border_color = Color.PRIMARY.value,
                          ),
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
                    margin_top=Size.ZERO.value,
                    ),
                margin_bottom=Size.BIG.value,
                padding_bottom = Size.BIG.value,
                color = TextColor.FOOTER.value,
                font_family = Fuentes.DEFAULT.value,

    )