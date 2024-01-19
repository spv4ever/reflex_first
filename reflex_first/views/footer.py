import reflex as rx
import datetime

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src='avatar.png'),
        rx.link(f'© 1991-{datetime.date.today().year} Blog personal de Albert García.',
                href="https://github.com/spv4ever",
                is_external=True),
                rx.hstack(
        rx.text("Aprendiendo desarrollo web desde Catalunya. Gracias"),
        rx.link("@mouredev",href="https://mouredev.com/",is_external=True)
    )
    )