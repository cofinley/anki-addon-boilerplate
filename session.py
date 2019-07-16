# import the main window object (mw) from aqt
from aqt import mw

# import all of the Qt GUI library
from aqt.qt import *


class Session(QWidget):
    def __init__(self):
        super().__init__()

        self.parent = mw
        self.setupMenu()

    def setupMenu(self):
        action = QAction("Fluent Forever", mw)
        action.triggered.connect(self.showUI)
        mw.form.menuTools.addAction(action)

        # Setup config button
        # mw.addonManager.setConfigAction(addon_id, self.show_config)

    def showUI(self):
        mainLayout = QVBoxLayout()
        self.layout = mainLayout
        self.setLayout(mainLayout)

        # Add an horizontal line
        mainLayout.addWidget(self.hLine())

        # Add, reset and cancel buttons
        okButton = QPushButton("Add")
        okButton.clicked.connect(self.add)
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)
        resetButton = QPushButton("Reset")
        resetButton.clicked.connect(self.reset)
        btnLayout = QHBoxLayout()
        btnLayout.addStretch(1)
        btnLayout.addWidget(okButton)
        btnLayout.addWidget(cancelButton)
        btnLayout.addWidget(resetButton)
        self.layout.addLayout(btnLayout)

        # Center the window
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle("Fluent Forever")
        self.show()
        self.raise_()
        self.activateWindow()

    def hLine(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line

    def add(self):
        pass

    def reset(self):
        pass

