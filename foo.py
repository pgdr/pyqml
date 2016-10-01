import sys

from PyQt4.QtCore import QObject, QUrl, pyqtSignal
from PyQt4.QtGui import QApplication
from PyQt4.QtDeclarative import QDeclarativeView


class Counter(QObject):
    
    counter = pyqtSignal(str)

    def __init__(self):
        super(Counter, self).__init__()
        self.c = 1

    def emit(self):
        self.c += self.c
        self.counter.emit(str(self.c))


app = QApplication(sys.argv)
cnt = Counter()

view = QDeclarativeView()
view.setSource(QUrl('foo.qml'))
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

rect = view.rootObject()
rect.clicked.connect(cnt.emit)
rect.shutdownRequested.connect(app.quit)

cnt.counter.connect(rect.updateMessage)
rect.updateMessage("Click here")

view.setGeometry(100, 100, 400, 240)
view.show()

app.exec_()
