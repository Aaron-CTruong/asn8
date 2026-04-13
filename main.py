import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox 
from asn8_ui import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnS.clicked.connect(self.submit_data)
        self.ui.btnR.clicked.connect(self.reset_fields)
        self.ui.btnQ.clicked.connect(self.close)
        

    def submit_data(self):
        first_name = self.ui.entFirst.text()
        last_name = self.ui.entLast.text()
        email = self.ui.entEmail.text()
        phone = self.ui.entPhone.text()

        if not first_name or not last_name or not email or not phone:
            QMessageBox.warning(self, "Error", "First and Last name are required!")
            return
        
        full_name = first_name + " " + last_name

        QMessageBox.information(self, "Submitted Data", f"Name: {full_name}\nEmail: {email}\nPhone: {phone}")


    def reset_fields(self):
        self.ui.entFirst.clear()
        self.ui.entLast.clear()
        self.ui.entEmail.clear()
        self.ui.entPhone.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())