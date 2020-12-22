import json, os, requests

KEY = "Sua Chave aqui"
BASE_URL = 'https://teste-tcc.cognitiveservices.azure.com/face/v1.0/detect'
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
headers = {'Ocp-Apim-Subscription-Key': KEY}

params = {
    'detectionModel': 'detection_01',
    'returnFaceId': 'false',
    'returnFaceAttributes': 'emotion'
}


def getEmtions():
    response = requests.post(BASE_URL, params=params, headers=headers, json={"url": img_url})
    print(response.json()[0]['faceAttributes']['emotion'])


getEmtions()