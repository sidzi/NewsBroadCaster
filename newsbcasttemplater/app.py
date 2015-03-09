from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class CasterGUI(FloatLayout):
    def __init__(self, **kwargs):
        super(CasterGUI, self).__init__(**kwargs)
        self.cols = 3

        version_info = Label(text="NewsBcaster v0.1", font_size=20, size_hint=(1, 0.5),
                             pos_hint={"center_x": 0.5, "center_y": 0.95})

        start_button = Button(text="Start Broadcast", background_color=(0, 0, 1, 1), size_hint=(.25, .10),
                              pos_hint={"center_x": 0.25, "center_y": 0.85})

        stop_button = Button(text="Stop Broadcast", background_color=(1, 0, 1, 1), size_hint=(.25, 0.10),
                             pos_hint={"center_x": 0.75, "center_y": 0.85})

        add_overlay = Button(text="Add Overlay", background_color=(1, 1, 1, 1), size_hint=(.25, 0.10),
                             pos_hint={"center_x": 0.50, "center_y": 0.50})

        overlay_text = TextInput(text="Enter the text to overlay", multiline=True, size_hint=(.75, 0.10),
                                 pos_hint={"center_x": .50, "center_y": .40})

        self.add_widget(version_info)
        self.add_widget(start_button)
        self.add_widget(stop_button)
        self.add_widget(add_overlay)
        self.add_widget(overlay_text)


class NewsBcastApp(App):
    def build(self):
        return CasterGUI()


if __name__ == "__main__":
    NewsBcastApp().run()
