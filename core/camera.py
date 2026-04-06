import cv2
import datetime
import os

from core.database import simpan_data
from core.qr_service import generate_qr

URL_KAMERA = "http://192.168.0.104:8080/video"


def proses_masuk(plat):
    cap = cv2.VideoCapture(URL_KAMERA, cv2.CAP_FFMPEG)
    ret, frame = cap.read()

    if not os.path.exists("foto"):
        os.makedirs("foto")

    if ret:
        filename = f"foto/{datetime.datetime.now().timestamp()}.jpg"
        cv2.imwrite(filename, frame)

        id_tiket = "PKR" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        qr_path = generate_qr(id_tiket)

        simpan_data(id_tiket, plat, filename)

        cap.release()
        return id_tiket, qr_path

    cap.release()
    return None, None