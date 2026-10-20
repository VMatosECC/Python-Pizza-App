# -*- coding: utf-8 -*-
# pizza_app.py  –  Eden's Pizza  –  Application logic
#
# Architecture: MainWindow inherits from both QMainWindow (Qt window machinery)
# and Ui_MainWindow (the generated layout class).  The two parents are kept in
# separate files so pyside6-uic can regenerate pizza_qt_created_gui.py freely
# without touching any of the code written here.
#
# File layout:
#   pizza_qt_created_gui.py   ← AUTO-GENERATED  (never edit by hand)
#   pizza_app.py              ← THIS FILE  (all your code lives here)
#   pizza_logo.png            ← asset bundled next to the scripts

import sys
from pathlib import Path

from PySide6.QtCore    import QDateTime, Qt
from PySide6.QtGui     import QBrush, QColor, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QGraphicsScene,
    QMainWindow,
    QMessageBox,
)

# Import the generated UI class — do NOT edit that file!
from pizza_qt_created_gui import Ui_MainWindow


# -- Utility --------------------------------------------------------------------

def resource_path(relative: str) -> Path:
    """Return the absolute path to a bundled asset.

    Works in two contexts:
    • During development: returns the folder that contains this .py file.
    • Inside a PyInstaller --onefile .exe: returns sys._MEIPASS, the temporary
      folder where PyInstaller extracts bundled data files at runtime.
    """
    base = getattr(sys, "_MEIPASS", Path(__file__).resolve().parent)
    return Path(base) / relative


# -- Main window class ----------------------------------------------------------

class MainWindow(QMainWindow, Ui_MainWindow):
    """The application's main window.

    Inherits from:
      QMainWindow    provides the actual OS window, menu bar, status bar, etc.
      Ui_MainWindow  provides setupUi() which populates the window with widgets.

    All slot methods (event handlers) are defined in this class.
    No logic whatsoever lives in pizza_qt_created_gui.py.
    """

    def __init__(self, parent=None):
        # 1. Initialise both parent classes.
        super().__init__(parent)

        # 2. Build all widgets inside this window (calls Ui_MainWindow.setupUi).
        #    After this call every widget is available as self.<objectName>.
        self.setupUi(self)

        # 3. Set default widget states and connect signals -> slots.
        self._initialise_ui()

    # -- Initialisation ---------------------------------------------------------

    def _initialise_ui(self):
        """Set default values and wire up every signal -> slot connection.

        Called once from __init__.  Separating this from __init__ makes it
        easier to see at a glance what the app's startup state is.
        """
        # Customer name placeholder
        self.plainTextCustomerName.setPlaceholderText(
            "Enter customer name here..."
        )

        # Populate size combo and default to Medium (index 1)
        self.comboSize.addItems(["Small", "Medium", "Large", "Extra Large"])
        self.comboSize.setCurrentIndex(1)

        # Default radio button states
        self.radioShapeRounded.setChecked(True)
        self.radioCheeseStandard.setChecked(True)

        # Date / time widget — show now, hide spin arrows (read-only feel)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit.setButtonSymbols(
            self.dateTimeEdit.ButtonSymbols.NoButtons
        )

        # Summary notes placeholder
        self.plainTextSummaryNotes.setPlaceholderText(
            "A summary of your order will be shown here..."
        )

        # Load the pizza logo into the QGraphicsView
        self._load_logo()

        # -- Signal -> slot connections ------------------------------------------
        # Each line says: "when THIS widget emits THAT signal, call THIS method"
        self.comboSize.currentTextChanged.connect(self._on_size_changed)
        self.btnClearToppings.clicked.connect(self._on_clear_toppings)
        self.btnSummarize.clicked.connect(self._on_summarize)
        self.btnPlaceOrder.clicked.connect(self._on_place_order)

    def _load_logo(self):
        """Load pizza_logo.png into the QGraphicsView widget."""
        pizza_pixmap = QPixmap(str(resource_path("pizza_logo.png")))
        scene = QGraphicsScene(self.graphicsView)

        if not pizza_pixmap.isNull():
            scene.addPixmap(pizza_pixmap)
            scene.setSceneRect(pizza_pixmap.rect())
            self.graphicsView.setScene(scene)
            self.graphicsView.fitInView(
                scene.sceneRect(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            )
        else:
            # Visible fallback so a missing image is obvious during testing.
            self.graphicsView.setBackgroundBrush(QBrush(QColor(255, 0, 0)))
            self.graphicsView.setScene(scene)

    # -- Slot methods -----------------------------------------------------------
    # Naming convention: _on_<what_happened>.
    # The leading underscore marks these as internal (not part of the public API).

    def _on_size_changed(self, new_size: str):
        """Slot: called by comboSize.currentTextChanged.

        Qt passes the newly selected text as new_size automatically because
        currentTextChanged carries a str payload.
        """
        #self.plainTextSummaryNotes.setPlainText(f"Selected Size: {new_size}")

    def _on_clear_toppings(self):
        """Slot: called by btnClearToppings.clicked.

        Unchecks every QCheckBox inside groupToppings and clears the summary.
        findChildren() returns all descendant widgets of the given type, so the
        loop works regardless of how many toppings exist.
        """
        self.plainTextSummaryNotes.clear()
        for checkbox in self.groupToppings.findChildren(QCheckBox):
            checkbox.setChecked(False)

    def _on_summarize(self):
        """Slot: called by btnSummarize.clicked.

        Reads the current state of every input widget and writes a formatted
        summary string to the plainTextSummaryNotes area.
        """
        # Collect the text of every CHECKED topping checkbox.
        checked_toppings = ", ".join(
            cb.text()
            for cb in self.groupToppings.findChildren(QCheckBox)
            if cb.isChecked()
        ) or "None"

        # Shape — exactly one radio button is checked at all times.
        shape = "Rounded" if self.radioShapeRounded.isChecked() else "Square"

        # Cheese — three mutually exclusive options.
        if self.radioCheeseStandard.isChecked():
            cheese = "Standard"
        elif self.radioCheeseDouble.isChecked():
            cheese = "Double-cheese"
        else:
            cheese = "None"

        summary = (
            f"Customer Name:     {self.plainTextCustomerName.toPlainText()}\n"
            f"Selected Size:     {self.comboSize.currentText()}\n"
            f"Selected Toppings: {checked_toppings}\n"
            f"Selected Shape:    {shape}\n"
            f"Selected Cheese:   {cheese}\n"
        )
        self.plainTextSummaryNotes.setPlainText(summary)

    def _on_place_order(self):
        """Slot: called by btnPlaceOrder.clicked.

        Shows a modal QMessageBox asking the customer to confirm the order.
        msg.exec() blocks until the user clicks a button, then returns its value.
        """
        msg = QMessageBox(self)          # passing 'self' centres the dialog
        msg.setWindowTitle("Place Order")
        msg.setText("Are you sure you want to place this order?")
        msg.setInformativeText(self.plainTextSummaryNotes.toPlainText())
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        if msg.exec() == QMessageBox.Yes:
            print("Order placed!\n", self.plainTextSummaryNotes.toPlainText())
        else:
            print("Order cancelled.")


# -- Entry point ----------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)   # Must be created before any widget
    window = MainWindow()          # __init__ calls setupUi + _initialise_ui
    window.show()
    sys.exit(app.exec())
