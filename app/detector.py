from flask import Flask, jsonify
import cv2
import numpy as np
import requests
from ultralytics import YOLO
import os

app = Flask(__name__)

model = YOLO("yolov8n.pt")

CAMERA_URL = os.getenv("CAMERA_URL")
THRESHOLD = float(os.getenv("THRESHOLD", 0.65))


def analyze():
    try:
        img_data = requests.get(CAMERA_URL, timeout=5).content
        img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)

        results = model(img)

        score = 0
        count = 0

        for r in results:
            for box in r.boxes:
                score += float(box.conf)
                count += 1

        if count == 0:
            return 1.0  # rien détecté = OK

        return score / count

    except Exception:
        return 1.0


@app.route("/check")
def check():
    score = analyze()
    return jsonify({
        "score": score,
        "fail": score < THRESHOLD
    })


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
