from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
# gghjg
KV = """
ScreenManager:
    MDScreen:
        id: home

        MDLabel:
            text: "Загрузите изображение для распоснания"
            #theme_text_color: "Custom"
            #text_color: .5, .5, .45, .8
            pos_hint: {"center_x": .5, "center_y": .93}
            halign: "center"
            font_style: "H4"

        MDCard:
            orientation: "vertical"
            elevation: 15
            size_hint: .7, .7
            pos_hint: {"center_x": .5, "center_y": .5}
            radius: [15, 15, 15, 15]

            FitImage:
                id: img
                #size_hint: .7, .7
                #pos_hint: {"center_x": .5, "center_y": .5}
                radius: [15, 15, 15, 15]

        MDRaisedButton:
            text: "Load Image"
            pos_hint: {"center_x": .5, "center_y": .3}
            on_press: app.file_chooser()

        MDRoundFlatButton:
            text: "Начать распознование"
            pos_hint: {"center_x": .5, "center_y": .1}


"""


class ImageClassify(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            self.root.ids.img.source = selection[0]
            print(selection[0])


if __name__ == "__main__":
    ImageClassify().run()