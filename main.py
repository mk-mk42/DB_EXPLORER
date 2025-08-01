import sys
from PyQt6.QtWidgets import QApplication
# db.py now  inside of database
# from database.db import initialize_database
# db.py is now inside of the dialogs folder
from dialogs.db import initialize_database
from main_window import MainWindow

if __name__ == "__main__":
    # database and necessary table  create
    initialize_database()

    # main application start
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
