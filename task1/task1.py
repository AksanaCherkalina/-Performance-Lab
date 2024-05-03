import sys

def circular_array_path(n, m):
    path = []
    current_position = 0
    while True:
        current_position = (current_position + m) % n
        path.append(current_position + 1)
        if current_position == 0:
            break
    return path

if __name__ == "__main__":
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        result = circular_array_path(n, m)
        print(''.join(map(str, result)))
    else:
        print("Пожалуйста, введите два аргумента: n и m.")

