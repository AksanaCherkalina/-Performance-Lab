# Это main.py
import sys
from task1 import circular_array_path

def main(n, m):
    path = circular_array_path(n, m)
    print(''.join(map(str, path)))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        main(n, m)
    else:
        print("Пожалуйста, введите два аргумента: n и m.")
