from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Выполнил: Александров Роман Олегович")  
        self.setGeometry(100, 100, 400, 300)  
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Создаем и добавляем метки с текстом
        group_label = QLabel("Группа: ИБАС 24-11-2")  
        age_label = QLabel("Возраст: 18")  
        animal_label = QLabel("Моё любимое животное: Котики")  
        characteristic_label = QLabel("Моя характеристика: я человек и фокусник, умный, шикарный") 
        
        layout.addWidget(group_label)
        layout.addWidget(age_label)
        layout.addWidget(animal_label)
        layout.addWidget(characteristic_label)  # Добавляем новую метку в layout
        
        close_button = QPushButton("bb пиявка")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        layout.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())