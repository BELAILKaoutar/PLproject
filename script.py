from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Méthode Simplexe")
        self.setGeometry(100, 100, 600, 400)

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        # Add the first label
        label1 = QLabel("Bonjour, Vous pouvez appliquer la méthode simplexe !", parent=self)
        label1.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label1)

        # Calculate label2_y position
        label2_y = label1.y() + label1.height() + 20

        # Add label and input for number of variables
        label2 = QLabel("Entrer le nombre de variables que vous avez!", parent=self)
        self.layout.addWidget(label2)
        self.input_box1 = QLineEdit(self)
        self.layout.addWidget(self.input_box1)
        label2.setGeometry(50, label2_y, 300, 30)
        self.input_box1.setGeometry(50, label2_y + 40, 200, 30)

        # Button to add variable inputs
        add_variable_button = QPushButton("Add Variables", self)
        add_variable_button.clicked.connect(self.add_variable_inputs)
        self.layout.addWidget(add_variable_button)
        
        # Add label and input for number of constraints
        label3 = QLabel("Entrer le nombre de contraintes que vous avez!", parent=self)
        self.layout.addWidget(label3)
        self.input_box2 = QLineEdit(self)
        self.layout.addWidget(self.input_box2)
        label3.setGeometry(850, label2_y, 300, 30)
        self.input_box2.setGeometry(850, label2_y + 40, 200, 30)

        # Button to add constraint inputs
        add_constraint_button = QPushButton("Add Constraints", self)
        add_constraint_button.clicked.connect(self.add_constraint_inputs)
        self.layout.addWidget(add_constraint_button)

        # Lists to store dynamically added labels and input boxes
        self.variable_labels = []
        self.variable_inputs = []
        self.constraint_labels = []
        self.constraint_inputs = []

    def add_variable_inputs(self):
        num_variables = int(self.input_box1.text())
        self.clear_layout(self.variable_labels, self.variable_inputs)
        for i in range(num_variables):
            label = QLabel(f"Variable {i+1}:", parent=self)
            self.layout.addWidget(label)
            input_box = QLineEdit(self)
            self.layout.addWidget(input_box)
            self.variable_labels.append(label)
            self.variable_inputs.append(input_box)

    def add_constraint_inputs(self):
        num_constraints = int(self.input_box2.text())
        self.clear_layout(self.constraint_labels, self.constraint_inputs)
        for i in range(num_constraints):
            label = QLabel(f"Contrainte {i+1}:", parent=self)
            self.layout.addWidget(label)
            input_box = QLineEdit(self)
            self.layout.addWidget(input_box)
            self.constraint_labels.append(label)
            self.constraint_inputs.append(input_box)

    def clear_layout(self, labels, inputs):
        for label in labels:
            label.deleteLater()
        for input_box in inputs:
            input_box.deleteLater()
        labels.clear()
        inputs.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
