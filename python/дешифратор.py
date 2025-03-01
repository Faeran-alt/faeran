
keyboard_mapping = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г',
    'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы',
    'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
    ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
    'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.'
}
def translate_to_russian(text):
    result = []
    for char in text:
        if char.lower() in keyboard_mapping:
            if char.isupper():
                result.append(keyboard_mapping[char.lower()].upper())
            else:
                result.append(keyboard_mapping[char])
        else:
            result.append(char)
    return ''.join(result)
english_text = input("текст: ")
russian_text = translate_to_russian(english_text)
print(russian_text)