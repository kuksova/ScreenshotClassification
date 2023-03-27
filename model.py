import easyocr
import os
from PIL import Image
import numpy as np
import json


def model_inference(path):
    if os.path.exists("input_images.json"):
        print("Json file for /images is exist already" )
        return

    langs = ['en', 'ru']
    reader = easyocr.Reader(langs, gpu=True)
    print('5')

    path_images = os.path.join(path, 'images/')
    # Try / Exept
    if not os.listdir(path_images):
        print("Error: Empty folder")
        return

    # process all images to json file
    img_dict = {}
    for name in os.listdir(path_images):
        img_pil = Image.open(os.path.join(path_images, name)).convert("RGB")

        results = reader.readtext(np.asarray(img_pil))
        text_img = []

        for (bbox, text, prob) in results:
            if prob > 0.5:
                # print("text: ",text, prob)
                # t = str(round(prob, 2)) + " " + text
                text_img.append(str(text))

        img_dict[name] = text_img

    #head, tail = os.path.split(path_images)

    with open("input_images.json", "w", encoding='utf-8') as outfile:
        json.dump(img_dict, outfile, ensure_ascii=False)
    print("Json was created.")
    #return img_dict



