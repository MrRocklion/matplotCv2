import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QFileDialog
from PySide6.QtCore import QFile, QIODevice, QThread
from PySide6.QtGui import QIcon
import matplotlib.pyplot as plt
import numpy as np
import time
import random

datos1 = []
datos2 = []


def plotting_ear(pts_ear, line1):
     global figure
     pts = np.linspace(0, 1, 5)
     if line1 == []:
          plt.style.use("ggplot")
          plt.ion()

          figure, ax = plt.subplots()
          line1, = ax.plot(pts, pts_ear)
          plt.ylim(0.1, 0.4)
          plt.xlim(0, 1)
          plt.ylabel("EAR", fontsize=18)
     else:
          line1.set_ydata(pts_ear)
          figure.canvas.draw()
          figure.canvas.flush_events()

     return line1



if __name__ == "__main__":
     app = QApplication(sys.argv)

     ui_file_name = "mainWindow.ui"
     ui_file = QFile(ui_file_name)
     if not ui_file.open(QIODevice.ReadOnly):
          sys.exit(-1)
     loader = QUiLoader()
     window = loader.load(ui_file)

     datos1.append(random.randint(1,10))
     if len(datos1) >= 5:
          datos2 = plotting_ear(datos1,datos2)
          datos1.pop(0)
     print(datos1)
     ui_file.close()
     if not window:
          sys.exit(-1)
     window.show()
     sys.exit(app.exec())
