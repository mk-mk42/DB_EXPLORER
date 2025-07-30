# main.py

import sys
from PyQt6.QtWidgets import QApplication
from db import initialize_database
from main_window import MainWindow

if __name__ == "__main__":
    # ডাটাবেস এবং প্রয়োজনীয় টেবিল তৈরি করে
    initialize_database()

    # মূল অ্যাপলিকেশন শুরু করে
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())