import qrcode
import os

def generate_qr(id_tiket):
    if not os.path.exists("qr"):
        os.makedirs("qr")

    filename = f"qr/{id_tiket}.png"

    qr = qrcode.make(id_tiket)
    qr.save(filename)

    return filename