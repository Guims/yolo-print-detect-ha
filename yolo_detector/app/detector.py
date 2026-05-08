from flask import Flask, jsonify
import cv2
import numpy as np
import requests
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO("yolov8n.pt")

CAMERA_URL = "http://camera/snapshot.jpg"
THRESHOLD = 0.65

def analyze_image():
    img_data = requests.get(CAMERA_URL).content
    img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)

    results = model(img)

    # logique simple : trop de "anomalies" = fail
    score = 0
    for r in results:
        for box in r.boxes:
            score += float(box.conf)

    return score / max(len(results), 1)

@app.route("/check")
def check():
    score = analyze_image()

    return jsonify({
        "score": score,
        "fail": score < THRESHOLD
    })

app.run(host="0.0.0.0", port=5001)
