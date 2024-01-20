import reflex as rx 
from reflex_first.componentes.linkicon import linkicon
from reflex_first.componentes.info_text import info_text
from reflex_first.styles.styles import Size as Size

def header()-> rx.Component:
    return rx.vstack(
            rx.hstack(
                rx.avatar(name="Albert García",size="xl", src = "avatar2.png"),
                rx.vstack(
                    rx.heading(
                        'Alberto García', 
                        size= "lg"
                        ),
                    rx.text(
                        "@spv4ever",
                        margin_top="0px !important"
                        ),
                    rx.hstack(
                    linkicon("https://x.com"),
                    linkicon("https://x.com"),
                    linkicon("https://x.com"),
                    ),
                    
                    align_items="start",
                ),
                spacing=Size.BIG.value,
            ),
        rx.flex(
            info_text("+30","años de experiencia"),
            rx.spacer(),
            info_text("5","lenguajes de programación"),
            rx.spacer(),
            info_text("+500","informes de resultados"),
            width = "100%"

        ),
        rx.text("""Soy técnico informático con más de 30 años de experiencia, 
                fanático de la gestión de datos y bigdata. Entre mis hobbies está seguir
                aprendiendo cada día y python me está fascinando. Actualmente sigo desarrollando
                principalmente rutinas y procesos en python que llevarían horas de trabajo y enormes
                tablas dinámicas en excel. Entre mis últimos aprendizajes ha sido generar una app para
                subir de forma masiva diferentes excels a una base de datos SQL."""),
        spacing=Size.BIG.value,
        align_items="start",
        )
    