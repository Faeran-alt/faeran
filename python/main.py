from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Маркевич Даниил Германович")  
        self.setGeometry(100, 100, 400, 300)  # Размеры окна: x=100, y=100, ширина=400, высота=300
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Создаем и добавляем метки с текстом
        group_label = QLabel("Группа: ИБАС 24-11-2")  
        age_label = QLabel("Возраст: 19")  
        animal_label = QLabel("Моё любимое животное: Собака") 
        characteristic_label = QLabel("Моя характеристика: миллионер, актёр, тиктокер, ютубер  ")  
        
        # Добавляем метки в layout
        layout.addWidget(group_label)
        layout.addWidget(age_label)
        layout.addWidget(animal_label)
        layout.addWidget(characteristic_label)  # Добавляем новую метку в layout
        
        # Создаем кнопку закрытия
        close_button = QPushButton("Пока")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        # Устанавливаем выравнивание по центру
        layout.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())