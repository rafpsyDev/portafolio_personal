import reflex as rx

def card_xp(title: str, subtitle: str, description: str, date: str, logros: list[str], technologies: list[str]):
  return rx.box(
    rx.flex(
      rx.text(title, size="6"),
      rx.badge(date, color_scheme="yellow", ml="4", font_family="GeistMono", align_self="center"),
      justify="between", size="2",
    ),
    rx.heading(subtitle, size="3",font_family="GeistMono"),
    rx.text(description,font_family="Montserrat",weight="light", class_name="mt-4 text-base"),
    rx.vstack(
      rx.text("LOGROS PRINCIPALES", size="4", class_name="mt-6 mb-2",font_family="Montserrat"),
      rx.unordered_list(
        *[rx.list_item(logro) for logro in logros],
        font_family="Montserrat",
        class_name="list-disc pl-5 space-y-2 text-base",
      ),
    ),
    rx.vstack(
      rx.flex(
        *[
          rx.badge(tec, color_scheme="amber", size="2")
          for tec in technologies
        ],
        font_family="GeistMono",
        class_name="gap-2 mt-6 flex-wrap text-base",
      ),
    ),
    class_name="border border-solid border-yellow-300 rounded-2xl p-6 shadow-lg my-2 w-full",
  )
