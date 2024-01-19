import reflex as rx
from reflex_first.componentes.linkbutton import linkbutton

def links()-> rx.Component:
    return rx.vstack(
        linkbutton("Reflex Dev","https://reflex.dev"),
        linkbutton("Google", "http://www.google.es"),
        linkbutton("Mouredev", "http://moure.dev"),
        linkbutton('CSS Tutorial', 'https://www.w3schools.com/css/'),
        linkbutton('GitHub', 'https://github.com/spv4ever'),
        
               
    )