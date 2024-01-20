import reflex as rx
from reflex_first.componentes.linkbutton import linkbutton
from reflex_first.componentes.title import title
from reflex_first.styles.styles import Size as Size

def links()-> rx.Component:
    return rx.vstack(
        title("Primer Grupo"),
        linkbutton("Reflex Dev",
                   "Para crear páginas web con Python",
                   "https://reflex.dev"),
        linkbutton("Google",
                   "Buscador universal",
                   "http://www.google.es"),
        linkbutton("Mouredev", 
                   "El Maestro", 
                   "http://moure.dev"),
        linkbutton('CSS Tutorial', 
                   "Aprende CSS", 
                   'https://www.w3schools.com/css/'),
        linkbutton('GitHub', 
                   "Mi repositorio en Git Hub", 
                   'https://github.com/spv4ever'),
        title("Primer Grupo"),
        linkbutton("Reflex Dev",
                   "Para crear páginas web con Python",
                   "https://reflex.dev"),
        linkbutton("Google",
                   "Buscador universal",
                   "http://www.google.es"),
        linkbutton("Mouredev", 
                   "El Maestro", 
                   "http://moure.dev"),
        linkbutton('CSS Tutorial', 
                   "Aprende CSS", 
                   'https://www.w3schools.com/css/'),
        linkbutton('GitHub', 
                   "Mi repositorio en Git Hub", 
                   'https://github.com/spv4ever'),
        width = "100%",
        spacing=Size.MEDIUM.value,
           
    )