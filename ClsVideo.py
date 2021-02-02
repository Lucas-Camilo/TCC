from pathlib import Path
from time import sleep
import cv2
import glob
import os
import API_Conection as api

class Video:
    def __init__(self, caminho : str):
        self.caminho = caminho
        self.resultados = []
        self.final_resultados = {}

    def extrat_frames(self):
        video = cv2.VideoCapture(r"{}".format(self.caminho))
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print('Error: Creating directory of data')
        currentframe = 0
        salvando = True
        while salvando:
            ret, frame = video.read()
            if ret:
                name = './data/frame' + str(currentframe) + '.jpg'
                cv2.imwrite(name, frame)
                currentframe += 1
            else:
                salvando = False
        video.release()
        cv2.destroyAllWindows()

    def clear_folder(self):
        for f in Path('data').glob('*.jpg'):
            try:
                f.unlink()
            except OSError as e:
                print("Erro", e)

    def analizar_usuario(self):
        # Primeira tentativa de analise
        removido = []
        for filename in glob.glob('data/*.jpg'):
            resultado = api.getEmotionsSDK(filename)
            if resultado == 'erro':
                break
            else:
                self.resultados.append(resultado)
                removido.append(filename)
                os.remove(filename)
        if os.listdir('data'):
            sleep(3)
            self.analizar_usuario()

    def resultado_final(self):
        angry, contempt, disgust, fear, happiness, neutral, sadness, surprise = 0, 0, 0, 0, 0, 0, 0, 0
        for itens in self.resultados:
            angry += itens['anger']
            contempt += itens['contempt']
            disgust += itens['disgust']
            fear += itens['fear']
            happiness += itens['happiness']
            neutral += itens['neutral']
            sadness += itens['sadness']
            surprise += itens['surprise']
        if len(self.resultados) > 0:
            angry = angry / len(self.resultados)
            contempt = contempt / len(self.resultados)
            disgust = disgust / len(self.resultados)
            fear = fear / len(self.resultados)
            happiness = happiness / len(self.resultados)
            neutral = neutral / len(self.resultados)
            sadness = sadness / len(self.resultados)
            surprise = surprise / len(self.resultados)

        self.final_resultados = {
            "anger": round(angry, 2) / 100, "contempt": round(contempt, 2), "disgust": round(disgust, 2) / 100,
            "fear": round(fear, 2) / 100, "happiness": round(happiness, 2) / 100,
            "neutral": round(neutral, 2) / 100, "sadness": round(sadness, 2) / 100, "surprise": round(surprise, 2) / 100
        }
