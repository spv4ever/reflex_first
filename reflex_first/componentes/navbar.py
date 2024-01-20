import reflex as rx
from reflex_first.styles.styles import Size as Size

def navbar():
    return rx.hstack(
            rx.image(src="avatar.png",
                        width="50px",
                        height="auto",
                        border_radius="15px 50px",
                        border="5px solid #555",
                        box_shadow="lg"),
            rx.heading("Alberto García", font_size="1em"),        
        position="sticky",
        bg="lightgray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        width="100%",
        z_index = "999",
        top="0px"
        )
    