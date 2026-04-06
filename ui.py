import cv2
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap

from core.camera import proses_masuk


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistem Parkir")

        self.url = "http://192.168.0.104:8080/video"
        self.cap = cv2.VideoCapture(self.url, cv2.CAP_FFMPEG)

        # UI
        self.title = QLabel("SISTEM PARKIR")

        self.video_label = QLabel()
        self.video_label.setFixedSize(400, 300)
        self.video_label.setScaledContents(True)
        self.video_label.setStyleSheet("border: 2px solid black;")

        self.info_label = QLabel("Tekan tombol untuk masuk")

        self.btn_masuk = QPushButton("Kendaraan Masuk")
        self.btn_masuk.clicked.connect(self.handle_masuk)

        self.qr_label = QLabel()
        self.qr_label.setFixedSize(200, 200)
        self.qr_label.setScaledContents(True)
        self.qr_label.setStyleSheet("border: 1px solid gray;")

        # Layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.title)
        left_layout.addWidget(self.video_label)
        left_layout.addWidget(self.info_label)
        left_layout.addWidget(self.btn_masuk)

        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("QR TIKET"))
        right_layout.addWidget(self.qr_label)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

        # Timer kamera
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()

        if ret:
            frame = cv2.resize(frame, (400, 300))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, ch = frame.shape
            bytes_per_line = ch * w

            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.video_label.setPixmap(QPixmap.fromImage(qt_image))

    def handle_masuk(self):
        # sementara plat dummy
        plat = "BELUM_DETECT"

        id_tiket, qr_path = proses_masuk(plat)

        if id_tiket:
            self.info_label.setText(f"ID Tiket: {id_tiket}")
            self.qr_label.setPixmap(QPixmap(qr_path))
        else:
            self.info_label.setText("Gagal mengambil data")

    def closeEvent(self, event):
        self.cap.release()
        event.accept()