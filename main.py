from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex('5ca0c2')


class Gerenciador(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def coletaDados(self):
        user = self.ids.user.text
        senha = self.ids.password.text
        return [user, senha]

    def login(self):
        usersenha: list = self.coletaDados()
        is_valido = self.valida(usersenha)
        if is_valido:
            self.manager.current = "main"
        else:
            print("Dados incorretos")

    def valida(self, dados:list):
        isvalido: bool = False
        if dados[0] != "" and dados[1] != "":
            isvalido = True
        return isvalido


class Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass


class GetVideo(Screen):
    def __init__(self, **kwargs):
        super(GetVideo, self).__init__(**kwargs)

    def on_enter(self, *args):
        pass

    def get_video(self):
        print("pegando Video... ")


class Inicial(App):
    def build(self):
        Builder.load_string(open("ky/inicial.kv", encoding="utf-8").read(), rulesonly=True)
        m = Gerenciador()
        return m


Inicial().run()
