from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.popup import Popup
from ClsVideo import Video
from ClsRelatorio import Relatorio
from threading import Thread

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
        n_video.filtro()
        thread = Thread(target=n_video.analizar_usuario)
        thread.start()
        thread.join()
        n_video.resultado_final()
        self.manager.current = 'resultado'


class Resultado(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mostrar_resultados(self):
        global n_video
        self.ids.raiva.text = "Raiva: "+str(n_video.final_resultados['anger'])+" %"
        self.ids.medo.text = "Medo: " + str(n_video.final_resultados['fear']) + " %"
        self.ids.nojo.text = "Nojo: " + str(n_video.final_resultados['disgust']) + " %"
        self.ids.felicidade.text = "Felicidade: " + str(n_video.final_resultados['happiness']) + " %"
        self.ids.tristeza.text = "Tristeza: " + str(n_video.final_resultados['sadness']) + " %"
        self.ids.surpresa.text = "Surpresa: " + str(n_video.final_resultados['surprise']) + " %"
        self.ids.desprezo.text = "Desprezo: " + str(n_video.final_resultados['contempt']) + " %"
        self.ids.neutro.text = "Neutro: " + str(n_video.final_resultados['neutral']) + " %"

    def exportar_pdf(self):
        global n_video
        n_relatorio = Relatorio(n_video.resultados, n_video.final_resultados)
        n_relatorio.criaPDF()
        n_relatorio.criaTxt()


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
