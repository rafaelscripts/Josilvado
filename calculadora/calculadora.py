from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.window import Window


class CalculadoraLayout(BoxLayout):
    display_text = StringProperty("0")
    open_parentheses = False  # Adicionando a propriedade open_parentheses

    def clear_display(self):
        self.display_text = "0"

    def update_display(self, text):
        if self.display_text == "0":
            self.display_text = text
        else:
            self.display_text += text

    def calculate_result(self):
        try:
            self.display_text = str(eval(self.display_text))
        except Exception as e:
            self.display_text = "Error"

    def toggle_parentheses(self):
        if self.open_parentheses:
            self.update_display(")")
            self.open_parentheses = False
        else:
            self.update_display("(")
            self.open_parentheses = True


class CalculadoraApp(App):
    def build(self):
        Window.size = (360, 600)
        return CalculadoraLayout()


if __name__ == "__main__":
    CalculadoraApp().run()
