from venv import create  # Этот импорт не нужен




import string  # Импортируем модуль string для доступа к знакам пунктуации


def file_sort():
    word_counts = {}

    try:
        with open("input.txt", "r") as input_file:
            text = input_file.read()


            translator = str.maketrans('', '', string.punctuation)
            text_without_punctuation = text.translate(translator)


            words = text_without_punctuation.lower().split()

    except FileNotFoundError:
        print("Файл input.txt не найден")
        return


    for word in words:
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1

    try:
        with open("output.txt", "w") as output_file:

            for word, count in sorted(word_counts.items()):
                output_file.write(f"{word}: {count}\n")
    except Exception as e:
        print(f"Ошибка записи в файл: {e}")



with open("input.txt", "w") as f:
    f.write(input("введите текст для обработки"))

file_sort()
print("Программа выполнена. Результат в output.txt")


with open("output.txt", "r") as f:
    print("\nСодержимое output.txt:")
    print(f.read())

