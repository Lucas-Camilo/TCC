import cv2
import os
from pathlib import Path


class Video:
    def __init__(self, caminho : str):
        self.caminho = caminho

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
                print('Creating...' + name)
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
        print("analizando")
