import reflex as rx 

def header()-> rx.Component:
    return rx.vstack(
        rx.avatar(name="Albert García",size="xl"),
        rx.text("@spv4ever"),
        rx.text('Hola Mi nombre es Alberto García'),
        rx.text("""Soy técnico informático con más de 30 años de experiencia, 
                fanático de la gestión de datos y bigdata. Entre mis hobbies está seguir
                aprendiendo cada día y python me está fascinando. Actualmente sigo desarrollando
                principalmente rutinas y procesos en python que llevarían horas de trabajo y enormes
                tablas dinámicas en excel. Entre mis últimos aprendizajes ha sido generar una app para
                subir de forma masiva diferentes excels a una base de datos SQL""")
        )
    