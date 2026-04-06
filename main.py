import sys
from PyQt5.QtWidgets import QApplication
from ui import App

app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())