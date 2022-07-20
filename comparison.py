from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (14/255, 61/255, 76/255, 1)
# Window.size = (400, 600) only


class Compare(BoxLayout):
    def calc(self):
        price_p1 = float(self.ids.price_p1.text)
        weight_p1 = float(self.ids.weight_p1.text)
        price_p2 = float(self.ids.price_p2.text)
        weight_p2 = float(self.ids.weight_p2.text)

        self.ids.label_p1.text = str(price_p1 / weight_p1 * 1000)
        self.ids.label_p2.text = str(price_p2 / weight_p2 * 1000)

        self.ids.difference.text = str((price_p1 / weight_p1) / (price_p2 / weight_p2) * 100) + ' %'


class Comparison(App):
    def build(self):
        return Compare()


Comparison().run()
