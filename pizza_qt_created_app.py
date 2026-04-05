# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pizza_qt_created_guiAvYKrh.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from pathlib import Path
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QFrame,
    QGraphicsView,
    QGraphicsScene,
    QGroupBox,
    QLabel,
    QMainWindow,
    QMenuBar,
    QPlainTextEdit,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QStatusBar,
    QWidget,
    QMessageBox,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 525)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.labelTopCaption = QLabel(self.centralwidget)
        self.labelTopCaption.setObjectName("labelTopCaption")
        self.labelTopCaption.setGeometry(QRect(120, 10, 241, 41))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.labelTopCaption.setFont(font)
        self.labelTopCaption.setAutoFillBackground(False)
        self.labelTopCaption.setScaledContents(False)
        self.labelTopCaption.setIndent(-10)
        
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setGeometry(QRect(10, 10, 111, 101))
        
        self.frameLeft = QFrame(self.centralwidget)
        self.frameLeft.setObjectName("frameLeft")
        self.frameLeft.setGeometry(QRect(10, 120, 361, 331))
        self.frameLeft.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLeft.setFrameShadow(QFrame.Shadow.Raised)
        
        self.groupToppings = QGroupBox(self.frameLeft)
        self.groupToppings.setObjectName("groupToppings")
        self.groupToppings.setGeometry(QRect(20, 20, 141, 281))
        self.groupToppings.setCheckable(False)
        
        self.chkPepperoni = QCheckBox(self.groupToppings)
        self.chkPepperoni.setObjectName("chkPepperoni")
        self.chkPepperoni.setGeometry(QRect(10, 30, 78, 20))
        
        self.chkMushroom = QCheckBox(self.groupToppings)
        self.chkMushroom.setObjectName("chkMushroom")
        self.chkMushroom.setGeometry(QRect(10, 60, 91, 20))
        
        self.chkSausage = QCheckBox(self.groupToppings)
        self.chkSausage.setObjectName("chkSausage")
        self.chkSausage.setGeometry(QRect(10, 90, 78, 20))
        
        self.chkOnions = QCheckBox(self.groupToppings)
        self.chkOnions.setObjectName("chkOnions")
        self.chkOnions.setGeometry(QRect(10, 120, 91, 20))
        
        self.chkOlives = QCheckBox(self.groupToppings)
        self.chkOlives.setObjectName("chkOlives")
        self.chkOlives.setGeometry(QRect(10, 150, 91, 20))
        
        self.chkGreenPeppers = QCheckBox(self.groupToppings)
        self.chkGreenPeppers.setObjectName("chkGreenPeppers")
        self.chkGreenPeppers.setGeometry(QRect(10, 180, 111, 20))
        
        self.chkPineapple = QCheckBox(self.groupToppings)
        self.chkPineapple.setObjectName("chkPineapple")
        self.chkPineapple.setGeometry(QRect(10, 210, 111, 20))
        
        self.chkSpinach = QCheckBox(self.groupToppings)
        self.chkSpinach.setObjectName("chkSpinach")
        self.chkSpinach.setGeometry(QRect(10, 240, 111, 20))
        
        self.groupShape = QGroupBox(self.frameLeft)
        self.groupShape.setObjectName("groupShape")
        self.groupShape.setGeometry(QRect(170, 100, 171, 80))
        self.groupShape.setCheckable(False)
                
        self.radioShapeRounded = QRadioButton(self.groupShape)
        self.radioShapeRounded.setObjectName("radioShapeRounded")
        self.radioShapeRounded.setGeometry(QRect(10, 20, 92, 20))
        self.radioShapeSquare = QRadioButton(self.groupShape)
        self.radioShapeSquare.setObjectName("radioShapeSquare")
        self.radioShapeSquare.setGeometry(QRect(10, 50, 92, 20))
        self.groupCheeseSelector = QGroupBox(self.frameLeft)
        self.groupCheeseSelector.setObjectName("groupCheeseSelector")
        self.groupCheeseSelector.setGeometry(QRect(170, 190, 171, 111))
        self.radioCheeseStandard = QRadioButton(self.groupCheeseSelector)
        self.radioCheeseStandard.setObjectName("radioCheeseStandard")
        self.radioCheeseStandard.setGeometry(QRect(10, 20, 92, 20))
        self.radioCheeseDouble = QRadioButton(self.groupCheeseSelector)
        self.radioCheeseDouble.setObjectName("radioCheeseDouble")
        self.radioCheeseDouble.setGeometry(QRect(10, 50, 121, 20))
        self.radioCheeseNone = QRadioButton(self.groupCheeseSelector)
        self.radioCheeseNone.setObjectName("radioCheeseNone")
        self.radioCheeseNone.setGeometry(QRect(10, 80, 92, 20))
        self.comboSize = QComboBox(self.frameLeft)
        self.comboSize.setObjectName("comboSize")
        self.comboSize.setGeometry(QRect(170, 50, 171, 21))
        self.labelSize = QLabel(self.frameLeft)
        self.labelSize.setObjectName("labelSize")
        self.labelSize.setGeometry(QRect(170, 10, 171, 31))
        self.frameRight = QFrame(self.centralwidget)
        self.frameRight.setObjectName("frameRight")
        self.frameRight.setGeometry(QRect(380, 120, 291, 301))
        self.frameRight.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameRight.setFrameShadow(QFrame.Shadow.Raised)
        self.labelCustomer = QLabel(self.frameRight)
        self.labelCustomer.setObjectName("labelCustomer")
        self.labelCustomer.setGeometry(QRect(10, 10, 171, 31))
        self.plainTextCustomerName = QPlainTextEdit(self.frameRight)
        self.plainTextCustomerName.setObjectName("plainTextCustomerName")
        self.plainTextCustomerName.setGeometry(QRect(10, 50, 241, 31))
        self.labelSummaryNotes = QLabel(self.frameRight)
        self.labelSummaryNotes.setObjectName("labelSummaryNotes")
        self.labelSummaryNotes.setGeometry(QRect(10, 90, 171, 31))
        self.plainTextSummaryNotes = QPlainTextEdit(self.frameRight)
        self.plainTextSummaryNotes.setObjectName("plainTextSummaryNotes")
        self.plainTextSummaryNotes.setGeometry(QRect(10, 120, 261, 81))
        self.btnClearToppings = QPushButton(self.frameRight)
        self.btnClearToppings.setObjectName("btnClearToppings")
        self.btnClearToppings.setGeometry(QRect(10, 240, 121, 51))
        self.btnSummarize = QPushButton(self.frameRight)
        self.btnSummarize.setObjectName("btnSummarize")
        self.btnSummarize.setGeometry(QRect(10, 210, 121, 24))
        self.btnPlaceOrder = QPushButton(self.frameRight)
        self.btnPlaceOrder.setObjectName("btnPlaceOrder")
        self.btnPlaceOrder.setGeometry(QRect(150, 210, 111, 81))
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(380, 430, 291, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 697, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.labelTopCaption.setText(
            QCoreApplication.translate("MainWindow", "Eden's Pizza", None)
        )
        self.groupToppings.setTitle(
            QCoreApplication.translate("MainWindow", " Toppings ", None)
        )
        self.chkPepperoni.setText(
            QCoreApplication.translate("MainWindow", "Pepperoni", None)
        )
        self.chkMushroom.setText(
            QCoreApplication.translate("MainWindow", "Mushroom", None)
        )
        self.chkSausage.setText(
            QCoreApplication.translate("MainWindow", "Sausage", None)
        )
        self.chkOnions.setText(QCoreApplication.translate("MainWindow", "Onions", None))
        self.chkOlives.setText(QCoreApplication.translate("MainWindow", "Olives", None))
        self.chkGreenPeppers.setText(
            QCoreApplication.translate("MainWindow", "Green Peppers", None)
        )
        self.chkPineapple.setText(
            QCoreApplication.translate("MainWindow", "Pineapple", None)
        )
        self.chkSpinach.setText(
            QCoreApplication.translate("MainWindow", "Spinach", None)
        )
        self.groupShape.setTitle(
            QCoreApplication.translate("MainWindow", " Shape ", None)
        )
        self.radioShapeRounded.setText(
            QCoreApplication.translate("MainWindow", "Rounded", None)
        )
        self.radioShapeSquare.setText(
            QCoreApplication.translate("MainWindow", "Square", None)
        )
        self.groupCheeseSelector.setTitle(
            QCoreApplication.translate("MainWindow", " Cheese Selector ", None)
        )
        self.radioCheeseStandard.setText(
            QCoreApplication.translate("MainWindow", "Standard", None)
        )
        self.radioCheeseDouble.setText(
            QCoreApplication.translate("MainWindow", "Double-cheese", None)
        )
        self.radioCheeseNone.setText(
            QCoreApplication.translate("MainWindow", "None", None)
        )
        self.labelSize.setText(QCoreApplication.translate("MainWindow", "Size", None))
        self.labelCustomer.setText(
            QCoreApplication.translate("MainWindow", "Customer Name", None)
        )
        self.labelSummaryNotes.setText(
            QCoreApplication.translate("MainWindow", "Summary - Notes", None)
        )
        self.btnClearToppings.setText(
            QCoreApplication.translate("MainWindow", "Clear Toppings", None)
        )
        self.btnSummarize.setText(
            QCoreApplication.translate("MainWindow", "Summarize", None)
        )
        self.btnPlaceOrder.setText(
            QCoreApplication.translate("MainWindow", "Place Order", None)
        )

    # retranslateUi

    def on_load(self):
        #self.selected_toppings = set()  # Initialize the set to store uniquely selected toppings
        
        # Set default values and states for UI components
        self.plainTextCustomerName.setPlaceholderText("Enter customer name here...")
        self.comboSize.addItems(["Small", "Medium", "Large", "Extra Large"])
        self.comboSize.setCurrentIndex(1)  # Set default selection to "Medium"
        self.radioShapeRounded.setChecked(True)  # Set default shape to Rounded
        self.radioCheeseStandard.setChecked(True)  # Set default cheese to Standard 
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())  # Set current date and time
        self.dateTimeEdit.setButtonSymbols(QDateTimeEdit.ButtonSymbols.NoButtons)  # Hide the up/down buttons
        self.plainTextSummaryNotes.setPlaceholderText("Enter any special instructions or notes for your order here...") 
        
        # Create one scene, load local image, and fit it into the view.
        scene = QGraphicsScene(self.graphicsView)
        # Get the directory of the current script and construct the path to the image.   
        base_dir = Path(__file__).resolve().parent 
        pizza_pixmap = QPixmap(str(base_dir / "pizza_logo.png"))

        # Check if the image was loaded successfully before adding it to the scene.
        if not pizza_pixmap.isNull():
            scene.addPixmap(pizza_pixmap)
            # Set the scene rectangle to the size of the pixmap for proper fitting.
            scene.setSceneRect(pizza_pixmap.rect()) 
            self.graphicsView.setScene(scene)
            # Fit the view to the scene while maintaining the aspect ratio.
            self.graphicsView.fitInView(
                scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
        else:
            # Keep a visible fallback (red box) if the image cannot be loaded.
            self.graphicsView.setBackgroundBrush(QBrush(QColor(255, 0, 0)))
            self.graphicsView.setScene(scene)

        # Connect combo box selection to plainTextEdit
        self.comboSize.currentTextChanged.connect(self.on_comboSize_selection_changed)

        # Connect the Clear Toppings button to clear the toppings selection and update the text edit.
        self.btnClearToppings.clicked.connect(self.on_clear_toppings_clicked)
        
        # Connect the Summarize button to update the summary notes with the current selections.
        self.btnSummarize.clicked.connect(self.on_summarize_clicked)
        
        # Connect the Place Order button to a placeholder method for future implementation.
        self.btnPlaceOrder.clicked.connect(self.on_place_order_clicked)
        
    def on_place_order_clicked(self):
        # display a message box confirming the order placement with the current summary notes
        from PySide6.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setWindowTitle("Place Order")
        msg.setText("Are you sure you want to place this order?")
        msg.setInformativeText(self.plainTextSummaryNotes.toPlainText())
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec() == QMessageBox.Yes:
            pass
        else:
            pass
        # on_place_order_clicked

    def on_clear_toppings_clicked(self):
        #for each checkbox, uncheck it and clear the selected toppings set
        for checkbox in self.groupToppings.findChildren(QCheckBox):
            checkbox.setChecked(False)
        #on_clear_toppings_clicked
        
    def on_summarize_clicked(self):
        # Update the summary notes with the current selections  
        current_notes = self.plainTextSummaryNotes.toPlainText()

        # show the name, notes, toppings, shape, and cheese selections in the summary notes
        summary_text = f"Customer Name: {self.plainTextCustomerName.toPlainText()}\n"
        summary_text += f"Selected Size: {self.comboSize.currentText()}\n"  
        summary_text += "Selected Toppings: " + ", ".join(
            checkbox.text() for checkbox in self.groupToppings.findChildren(QCheckBox) if checkbox.isChecked()
        ) + "\n"
        summary_text += "Selected Shape: " + ("Rounded" if self.radioShapeRounded.isChecked() else "Square") + "\n"
        summary_text += "Selected Cheese: " + ("Standard" if self.radioCheeseStandard.isChecked() else "Double-cheese" if self.radioCheeseDouble.isChecked() else "None") + "\n"
        self.plainTextSummaryNotes.setPlainText(summary_text)   
        # on_summarize_clicked
    
    def on_comboSize_selection_changed(self, new_size):
        # Update the summary notes with the new size selection
        current_notes = self.plainTextSummaryNotes.toPlainText()
        new_notes = f"Selected Size: {new_size}"
        self.plainTextSummaryNotes.setPlainText(new_notes)

    # on_load


# Ui_MainWindow

# main -----------------------------------------------------------------
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()    
    ui.setupUi(MainWindow)
    ui.on_load()  # Call the on_load method to initialize the UI
    MainWindow.show()
    sys.exit(app.exec())
