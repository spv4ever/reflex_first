import reflex as rx
from reflex_first.componentes.linkbutton import linkbutton

def links()-> rx.Component:
    return rx.vstack(
        linkbutton("Primer botón","https://reflex.dev"),
        linkbutton("Segundo botón", "http://www.google.es"),
        linkbutton("Tercer  botón", "http://moure.dev"),
    )