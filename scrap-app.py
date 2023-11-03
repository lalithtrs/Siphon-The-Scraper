import sys
from PyQt5 import QtWidgets, QtCore
import requests

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # Create UI elements
        self.query_le = QtWidgets.QLineEdit()
        self.submit_btn = QtWidgets.QPushButton("Add")
        self.status_label = QtWidgets.QLabel()

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.query_le)
        layout.addWidget(self.submit_btn)
        layout.addWidget(self.status_label)

        container = QtWidgets.QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Connect signals
        self.submit_btn.clicked.connect(self.submit_query)

    def submit_query(self):
        query = self.query_le.text()

        try:
            response = requests.post("http://localhost:5000/add_query", json={"query": query})
            if response.ok:
                self.status_label.setText("Query submitted!")
            else:
                self.status_label.setText("Error submitting query")
        except Exception as e:
            self.status_label.setText("Error: "+str(e))

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
