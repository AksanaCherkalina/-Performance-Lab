import sys
from task3 import main  # Импорт функции main из файла task3.py

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python main.py values.json tests.json report.json")
        sys.exit(1)
    # Получение путей к файлам из аргументов командной строки
    values_path, tests_path, report_path = sys.argv[1], sys.argv[2], sys.argv[3]
    # Вызов функции main с этими путями
    main(values_path, tests_path, report_path)

