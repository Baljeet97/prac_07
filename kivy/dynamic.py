from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.names = ["Bob", "Brown", "Jane", "Cat", "Mike", "Oren", "Jess", "Anna", "Maddi"]

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_button)


DynamicWidgetsApp().run()
