import reflex as rx
import reflex_first.styles.styles as styles

def linkicon(url: str)->rx.Component:
    return rx.link(
        rx.icon(
            tag="link"
        ),
        is_external=True,
        href=url,
    )