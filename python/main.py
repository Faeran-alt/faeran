def create_multiplication_tables():
    # Открываем файл для записи
    with open('multiplication_tables.csv', 'w', encoding='utf-8') as file:
        # Создаем таблицы умножения от 2 до 9
        for number in range(2, 10):
            # Записываем заголовок таблицы
            file.write(f'таблица умножения на {number}\n')
            
            # Создаем заголовки столбцов
            file.write('Пример,Результат\n')
            
            # Записываем примеры и результаты
            for i in range(1, 11):
                file.write(f'{number}*{i},{number * i}\n')
            
            # Добавляем пустые строки между таблицами
            file.write('\n')

if __name__ == '__main__':
    create_multiplication_tables()
    print("Таблицы умножения созданы в файле 'multiplication_tables.csv'")
    print("Откройте файл в Excel для просмотра результатафцыувапр")