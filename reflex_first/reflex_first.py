# chatapp.py
import reflex as rx

from reflex_first import style
from reflex_first.state import State
from reflex_first.componentes.navbar import navbar
from reflex_first.views.header import header
from reflex_first.views.links import links
from reflex_first.views.footer import footer

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
    )

app = rx.App()
app.add_page(index)