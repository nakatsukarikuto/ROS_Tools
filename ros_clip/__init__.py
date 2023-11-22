import torch
import clip
import cv2
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

#cudaの設定
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# CLIPモジュール
class CLIP():
    def __init__(self,txt: list) -> None:
        #USB接続したカメラから画像取得
        self.camera = cv2.VideoCapture(4)
        self.text = txt
        self.show = []

    def get_image(self):
        ret, frame = self.camera.read()
        if ret:
            return frame
        else:
            return None

    def judge_core(self):
        got_img = self.get_image()
        pil_img = Image.fromarray(cv2.cvtColor(got_img, cv2.COLOR_BGR2RGB))
        #CLIP
        image = preprocess(pil_img).unsqueeze(0).to(device)
        text = clip.tokenize(self.text).to(device)

        with torch.no_grad():
            image_features = model.encode_image(image)
            text_features = model.encode_text(text) 
            logits_per_image, logits_per_text = model(image, text)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy()
            return probs
        
    def plotting(self):
        data = pd.DataFrame(self.show)
        max_value = data[0].max()
        print(max_value)
        plt.plot(data[0], data[1], label = "probability")
        plt.legend(prop={"size": 10}, loc="best")
        plt.xlabel("time [s]")
        plt.ylabel("probs")
        plt.hlines(y=0.65, xmin=0, xmax=max_value, linestyles=":",colors="red", linewidth = 1)
        plt.savefig("analyze__.pdf")
        plt.show()

    def judgement(self):
        switch = True
        start_time = time.time()
        while switch:
            get_time = time.time()
            difference_time = get_time-start_time
            probs = self.judge_core()
            self.show.append([difference_time, probs[0][0]])
            if probs[0][0]>0.65:
                print("STOP")
                switch = False
            else:
                print(difference_time)
        self.plotting()