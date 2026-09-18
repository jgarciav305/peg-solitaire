"""Sprint 0: Confirm the tools chosen actually work
end to end before any game code is written."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt6.QtWidgets import QApplication, QPushButton


def test_pyqt6_widget_can_be_created():
    app = QApplication.instance() or QApplication([])
    button = QPushButton("New Game")
    assert button.text() == "New Game"
    assert app is not None