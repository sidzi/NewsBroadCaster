from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from bcastClient import BcastClient


class CasterGUI(FloatLayout):
    def __init__(self, **kwargs):
        super(CasterGUI, self).__init__(**kwargs)

        version_info = Label(text="NewsBcaster v0.1", font_size=20, size_hint=(1, 0.5),
                             pos_hint={"center_x": 0.5, "center_y": 0.95})

        start_button = Button(text="Start Broadcast", background_color=(0, 1, .5, 1), size_hint=(.25, .10),
                              pos_hint={"center_x": 0.25, "center_y": 0.85})

        stop_button = Button(text="Stop Broadcast", background_color=(1, 0.1, 0.1, 1), size_hint=(.25, 0.10),
                             pos_hint={"center_x": 0.75, "center_y": 0.85})

        path_to_video = TextInput(focus=True, text="lmao.mp4", multiline=False, size_hint=(.60, 0.10),
                                  pos_hint={"center_x": .40, "center_y": .70})

        upload_video = Button(text="Upload Video", background_color=(0, 1, 1, 1), size_hint=(.20, .10),
                              pos_hint={"center_x": 0.80, "center_y": 0.70})

        upload_video.bind(on_press=lambda x: self.callback_start(path_to_video.text))

        overlay_text = TextInput(text="Enter Overlay Text", multiline=True, size_hint=(.60, 0.10),
                                 pos_hint={"center_x": .40, "center_y": .40})

        add_overlay = Button(text="Add Overlay", background_color=(1, 1, 1, 1), size_hint=(.20, 0.10),
                             pos_hint={"center_x": 0.80, "center_y": 0.40})

        for widgets in [version_info, start_button, stop_button, add_overlay, path_to_video, overlay_text,
                        upload_video]:
            self.add_widget(widgets)

    @staticmethod
    def callback_start(filepath):
        BcastClient(filepath).run()


class NewsBcastApp(App):
    @staticmethod
    def build():
        return CasterGUI()


if __name__ == "__main__":
    NewsBcastApp().run()
