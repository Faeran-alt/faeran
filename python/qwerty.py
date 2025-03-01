'''
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Если символ — буква
            shift_amount = shift % 26  # Учитываем сдвиг больше 26
            if char.islower():  # Для маленьких букв
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:  # Для больших букв
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char  # Не буквы оставляем как есть
    return result

# Ввод данных
text = input("Введите строку: ")
shift = int(input("Введите сдвиг: "))

# Шифрование и вывод
encrypted = caesar_cipher(text, shift)
print("Зашифрованная строка:", encrypted)

# Дешифрование и вывод
decrypted = caesar_cipher(encrypted, -shift)
print("Расшифрованная строка:", decrypted)
#----------------------------
for code in range(20, 30): 
    try:
        print(f"Код: {code}, Символ: {chr(code)}")
    except ValueError:
        continue
'''


N = 4
A = []
for i in range(N):
    A.append([0]* N)
k = 1  
for q in range((N + 1) // 2):
    for i in range(q, N - q):
        A[q][i] = k
        k += 1

    for i in range(q + 1, N - q):
        A[i][N - q - 1] = k
        k += 1

    for i in range(N - q - 2, q - 1, -1):
        A[N - q - 1][i] = k
        k += 1

    for i in range(N - q - 2, q, -1):
        A[i][q] = k
        k += 1
for row in A:
    print(row)