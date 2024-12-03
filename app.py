from shiny.express import input, render, ui
from shinyswatch import theme

ui.page_opts(theme=theme.minty)

ui.tags.link(href="css/style.css", rel="stylesheet")

ui.h1("My app")

ui.input_slider("val", "Slider label", min=0, max=100, value=50)

@render.text
def slider_val():
    return f"Slider value: {input.val()}"

ui.div(
    ui.h2("こんにちは"),
    ui.p("Ciao"),
    class_="hello"
)
