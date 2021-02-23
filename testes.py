import cv2
import os

BLUE_COLOR = (255, 0, 0)
STROKE = 2
frontal = 'train/haarcascade_frontalface_alt2.xml'
clf = cv2.CascadeClassifier(frontal)
comFace = []
for file in os.listdir('data'):
    img = cv2.imread('data/{}'.format(file))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(gray)
    for x, y, w, h in faces:
        comFace.append(file)
        print('arquivo: {} = {}'.format(file,x))

for file in os.listdir('data'):
    if not file in comFace:
        print(file,"sem rosto")
