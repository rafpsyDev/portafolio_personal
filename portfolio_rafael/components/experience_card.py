import reflex as rx

def card_xp():
    return rx.box(
      rx.flex(
        rx.text("Ingeniero de Software Full-Stack", size="6"),
        rx.badge("2021 - Presente", color_scheme="yellow", ml="4", align_self="center"),
        justify="between",size="2",
      ),
      rx.heading("Desarrollador Independiente",size="3"),
      rx.text("Liderazgo técnico en proyectos empresariales complejos, desde levantamiento de requerimientos hasta implementación y despliegue.",class_name="mt-4"),
      rx.vstack(
        rx.text("LOGROS PRINCIPALES",size="4", class_name="mt-6 mb-2"),
        rx.unordered_list(
          rx.list.item("Desarrollo de 2 proyectos completos desde cero con gestión directa del cliente"),
          rx.list.item("Arquitectura de sistemas escalables para hospitales medianos"),
          rx.list.item("Implementación de sistemas de almacén con autenticación biométrica"),
          rx.list.item("Integración con normativas SAT y control de trazabilidad de productos"),
          class_name="list-disc pl-5 space-y-2",
        ),
      ),
      rx.vstack(
        rx.flex(
          rx.badge("Laravel", color_scheme="amber", size="2"),
          rx.badge("Python", color_scheme="amber", size="2"),
          rx.badge("React", color_scheme="amber", size="2"),
          rx.badge("Astro", color_scheme="amber", size="2"),
          rx.badge("PostgreSQL", color_scheme="amber", size="2"),
          rx.badge("MySQL", color_scheme="amber", size="2"),
          class_name="gap-2 mt-6",
        ),
      ),
      class_name="border border-solid border-yellow-300 rounded-2xl p-6 shadow-lg my-2",
    )

