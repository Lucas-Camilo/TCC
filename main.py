from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.popup import Popup
from ClsVideo import Video
Window.clearcolor = get_color_from_hex('4682B4')

n_video = Video("")


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

    def valida(self, dados: list):
        isvalido: bool = False
        if dados[0] != "" and dados[1] != "":
            isvalido = True
        return isvalido


class Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GetVideo(Screen):
    def __init__(self, **kwargs):
        super(GetVideo, self).__init__(**kwargs)
        self.arquivo_caminho = ""
        self.pop = MyPopUp()
        self.carregando = PopCarregando()

    def get_video(self):
        self.pop = MyPopUp()
        self.pop.open()
        self.pop.on_dismiss = lambda *args: self.salvaCaminho()

    def salvaCaminho(self):
        self.ids.caminho.text = self.pop.caminho
        self.arquivo_caminho = self.pop.caminho

    def analizar(self):
        global n_video
        n_video = Video(self.arquivo_caminho)
        n_video.extrat_frames()
        n_video.analizar_usuario()
        self.manager.current = 'resultado'


class Resultado(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PopCarregando(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyPopUp(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.caminho = ""

    def salvar(self, *args):
        self.caminho = args[1][0]
        self.dismiss()


class Inicial(App):
    def build(self):
        Builder.load_string(open("ky/inicial.kv", encoding="utf-8").read(), rulesonly=True)
        m = Gerenciador()
        self.icon = "images/Logo.png"
        return m


Inicial().run()
