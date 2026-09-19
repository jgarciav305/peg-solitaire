"""Sprint 0 GUI exercise: a standalone PyQt6 program demonstrating basic
widgets (text, lines, a checkbox, and radio buttons) ahead of the real
Peg Solitaire GUI. Not part of the Solitaire project itself."""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

TOP_MARGIN = 30

"""Simplified outlines (not the real peg grid)
just to show the different board shapes differ, using straight lines."""
SHAPE_OUTLINES: dict[str, list[tuple[int, int]]] = {
    "English": [
        (105, 0), (155, 0), (155, 50), (205, 50), (205, 100),
        (155, 100), (155, 150), (105, 150), (105, 100), (55, 100),
        (55, 50), (105, 50),
    ],
    "Hexagon": [
        (60, 65), (95, 10), (165, 10), (200, 65), (165, 120), (95, 120),
    ],
    "Diamond": [
        (130, 0), (230, 65), (130, 130), (30, 65),
    ],
    "Triangle": [
        (130, 0), (230, 130), (30, 130),
    ],
}


class LineCanvas(QWidget):

    # Draws a label plus the current board shape as a line outline
    def __init__(self) -> None:
        super().__init__()
        self.setMinimumHeight(190)
        self._shape = "English"

    def set_shape(self, shape: str) -> None:
        if shape in SHAPE_OUTLINES:
            self._shape = shape
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(QPen(Qt.GlobalColor.darkGray, 2))
        painter.drawText(10, 20, f"Board shape preview: {self._shape}")

        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        points = SHAPE_OUTLINES[self._shape]
        closed_points = points + [points[0]]
        for (x1, y1), (x2, y2) in zip(closed_points, closed_points[1:]):
            painter.drawLine(x1, y1 + TOP_MARGIN, x2, y2 + TOP_MARGIN)


class DemoWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Sprint 0 GUI Demo")

        self.canvas = LineCanvas()

        self.record_checkbox = QCheckBox("Record game")

        board_type_box = QGroupBox("Board Type")
        board_type_layout = QVBoxLayout()
        self.board_type_group = QButtonGroup(self)
        for i, name in enumerate(["English", "Hexagon", "Diamond","Triangle"]):
            button = QRadioButton(name)
            if i == 0:
                button.setChecked(True)
            self.board_type_group.addButton(button)
            board_type_layout.addWidget(button)
        board_type_box.setLayout(board_type_layout)

        self.status_label = QLabel("Board type: English | Record game: off")
        self.board_type_group.buttonClicked.connect(self._on_board_type_changed)
        self.record_checkbox.stateChanged.connect(self._update_status)

        options_row = QHBoxLayout()
        options_row.addWidget(board_type_box)
        options_row.addWidget(self.record_checkbox)

        root = QVBoxLayout()
        root.addWidget(self.canvas)
        root.addLayout(options_row)
        root.addWidget(self.status_label)

        central = QWidget()
        central.setLayout(root)
        self.setCentralWidget(central)

    def _on_board_type_changed(self, button: QRadioButton) -> None:
        self.canvas.set_shape(button.text())
        self._update_status()

    def _update_status(self) -> None:
        checked_button = self.board_type_group.checkedButton()
        board_type = checked_button.text() if checked_button else "none"
        record_state = "on" if self.record_checkbox.isChecked() else "off"
        self.status_label.setText(
            f"Board type: {board_type} | Record game: {record_state}"
        )


def main() -> None:
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()