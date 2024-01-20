import reflex as rx
from reflex_first.styles.styles import Size as Size
from reflex_first.styles.colors import Color as Color
from reflex_first.styles.colors import TextColor as TextColor

def info_text(title: str, body: str)->rx.Component:
    return rx.box(
            rx.span(
                title,
                font_weight = "blod",
                color = Color.PRIMARY.value
                ),
            f" {body}",
            font_size=Size.MEDIUM.value,
            color = TextColor.BODY.value,

            )   