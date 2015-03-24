from threading import Thread

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from bcastClient import BcastClient


class CasterGUI(FloatLayout):
    def __init__(self, **kwargs):
        super(CasterGUI, self).__init__(**kwargs)
        self.cols = 3

        version_info = Label(text="NewsBcaster v0.1", font_size=20, size_hint=(1, 0.5),
                             pos_hint={"center_x": 0.5, "center_y": 0.95})

        start_button = Button(text="Start Broadcast", background_color=(0, 0, 1, 1), size_hint=(.25, .10),
                              pos_hint={"center_x": 0.25, "center_y": 0.85})

        path_to_video = TextInput(focus=True, text="Enter Filepath", multiline=False, size_hint=(.75, 0.05),
                                  pos_hint={"center_x": .50, "center_y": .70})

        start_button.bind(on_press=lambda x: self.callback_start(path_to_video.text))

        stop_button = Button(text="Stop Broadcast", background_color=(1, 0, 1, 1), size_hint=(.25, 0.10),
                             pos_hint={"center_x": 0.75, "center_y": 0.85})

        add_overlay = Button(text="Add Overlay", background_color=(1, 1, 1, 1), size_hint=(.25, 0.10),
                             pos_hint={"center_x": 0.50, "center_y": 0.50})

        overlay_text = TextInput(text="Enter Overlay Text", multiline=True, size_hint=(.75, 0.10),
                                 pos_hint={"center_x": .50, "center_y": .40})

        for widgets in [version_info, start_button, stop_button, add_overlay, path_to_video, overlay_text]:
            self.add_widget(widgets)

    def callback_start(self, filepath):
        bCC = BcastClient(filepath)
        t = Thread(bCC.run())
        t.start()
        t.join()


class NewsBcastApp(App):
    def build(self):
        return CasterGUI()


if __name__ == "__main__":
    NewsBcastApp().run()
