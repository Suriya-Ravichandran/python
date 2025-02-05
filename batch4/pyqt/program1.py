import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,QLineEdit,QPushButton

def hello(self):
    return "Hello"

def main():
   
    

   # Create the application instance
   app = QApplication(sys.argv)

   # Create the main window
   window = QMainWindow()
   window.setWindowTitle("Simple PyQt Example")
   window.setGeometry(100, 100, 400, 200)

   # Create a label widget
   label = QLabel("Hello, PyQt!", window)
   label.move(158, 40)

   textfield=QLineEdit(window)
   textfield.move(158, 80)


   btn=QPushButton("Sumit",window)
   btn.move(158,90)

   # Show the window
   window.show()

   # Execute the application
   sys.exit(app.exec())

if __name__ == "__main__":
   main()