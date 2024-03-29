import reflex as rx
from reflex_first.styles.styles import Size as Size
from reflex_first.styles.colors import Color as Color
from reflex_first.styles.colors import TextColor as TextColor
import reflex_first.styles.styles as styles


def navbar():
    return rx.hstack(
            rx.image(src="avatar.png",
                        width="50px",
                        height="auto",
                        border_radius="15px 50px",
                        border="5px solid #555",
                        box_shadow="lg"),
            rx.box(
                rx.span("Keiko",
                        color=Color.PRIMARY.value,
                        
                        ),
                rx.span("Dev",
                         color=Color.SECONDARY.value
                        ),
                style=styles.navbar_title_style
                ),        
        position="sticky",

        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        width="100%",
        z_index = "999",
        top="0"
        )
    