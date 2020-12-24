from pathlib import Path
import cv2
import glob
import os
import API_Conection as api

class Video:
    def __init__(self, caminho : str):
        self.caminho = caminho
        self.resultados = []

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
        fotos = 0
        for filename in glob.glob('data/*.jpg'):
            resultado = api.getEmotionsSDK(filename)
            if resultado == 'erro':
                break
            self.resultados.append(resultado)
            fotos += 1