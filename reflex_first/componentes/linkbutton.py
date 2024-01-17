import reflex as rx

def linkbutton(text: str, url: str)->rx.Component:
    return rx.link(
        rx.button(text),
        href=url,
        color="rgb(107,99,246)",
        button=True,
    )