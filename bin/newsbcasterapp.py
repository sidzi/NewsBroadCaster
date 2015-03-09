from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class CasterGUI(FloatLayout):
    def __init__(self, **kwargs):
        super(CasterGUI, self).__init__(**kwargs)
        self.cols = 3

        self.add_widget(Label(text="NewsBcast v0.1", font_size=20, size_hint=(1, 0.5),
                              pos_hint={"center_x": 0.5, "center_y": 0.95}))

        start_button = Button(text="Start Broadcast", background_color=(0, 0, 1, 1), size_hint=(.25, .10),
                              pos_hint={"center_x": 0.25, "center_y": 0.85})

        stop_button = Button(text="Stop Broadcast", background_color=(1, 0, 1, 1), size_hint=(.25, 0.10),
                             pos_hint={"center_x": 0.75, "center_y": 0.85})

        self.add_widget(start_button)
        self.add_widget(stop_button)
        # self.add_widget(TextInput(text="Enter complete path to video file", multiline=False, size_hint=(1, 0.2),
        # pos_hint={"center_x": 0.5, "center_y": 0}))


class NewsBcastApp(App):
    def build(self):
        return CasterGUI()


if __name__ == "__main__":
    NewsBcastApp().run()