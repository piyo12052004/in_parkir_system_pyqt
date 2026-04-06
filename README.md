# 🚗 Sistem In Parkir (Kendaraan Masuk)

Aplikasi **In Parkir** adalah sistem untuk mencatat kendaraan yang masuk ke area parkir menggunakan kamera (QR Code / Barcode) dan input manual nomor plat.

---

## 📌 Fitur Utama

- 📷 klik tombil muncul barcode 
- 🕒 Mencatat waktu masuk otomatis
- 💾 Simpan data ke database
- 🖥️ Tampilan desktop (PyQt5)

---

## 🛠️ Teknologi

- Python 3.x
- PyQt5
- OpenCV
- SQLite / MySQL

---

## 📂 Struktur Project

core
core/
     /camera.py
     /database.py
     /qr_service.py
    /qz_printer.py
db
    /conection.py
foto/
qr/
main.py
README.md
ui.py


---

## ⚙️ Cara Menjalankan

### 1. Clone project
```bash
git clone https://github.com/username/parking-system.git
cd parking-system
python -m venv env
source env/bin/activate  # macOS / Linux
env\Scripts\activate     # Windows
pip install pyqt5 opencv-python
python main.py