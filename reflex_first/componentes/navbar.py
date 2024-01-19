import reflex as rx

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
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        width="100%",
        z_index = "999",
        top="0px"
        )
    