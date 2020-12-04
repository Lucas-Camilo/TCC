from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder


# from kivy.core.window import Window
# import Cores
# Window.clearcolor = Cores.AZUL


class Gerenciador(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_screen(self, name):
        self.current_screen = name


class Login(Screen):
    pass


class Main(Screen):
    pass


class Inicial(App):
    def build(self):
        Builder.load_string(open("ky/inicial.kv", encoding="utf-8").read(), rulesonly=True)
        m = Gerenciador()
        return m


Inicial().run()
