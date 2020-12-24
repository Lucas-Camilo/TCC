import json, os, requests, glob

KEY = "1770984949b94697a9f56910f8078f8a"
BASE_URL = 'https://teste-tcc.cognitiveservices.azure.com/face/v1.0/detect'
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'

headers = {
    'Ocp-Apim-Subscription-Key': KEY,
    'Content-Type': 'application/octet-stream'
           }

params = {
    'detectionModel': 'detection_01',
    'returnFaceId': 'false',
    'returnFaceAttributes': 'emotion'
}


def getEmtionsLink():
    response = requests.post(BASE_URL, params=params, headers=headers, json={"url": img_url})
    print(response.json()[0]['faceAttributes']['emotion'])


def getEmotionsSDK(local_image: str):
    image_data = open(local_image, "rb").read()
    response = requests.post(BASE_URL, params=params, headers=headers, data=image_data)
    resultado = {}
    try:
        resultado = response.json()[0]['faceAttributes']['emotion']
    except:
        resultado = 'erro'
    finally:
        return resultado

