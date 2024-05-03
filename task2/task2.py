import sys

def read_circle_data(filepath):
    with open(filepath, 'r') as file:
        x, y, r = map(float, file.readline().split())
        return (x, y, r)

def read_points(filepath):
    with open(filepath, 'r') as file:
        points = [tuple(map(float, line.split())) for line in file]
        return points

def calculate_position(circle, points):
    cx, cy, r = circle
    results = []
    for px, py in points:
        distance = ((px - cx)**2 + (py - cy)**2)**0.5
        if distance < r:
            results.append(1)  # Точка внутри
        elif distance == r:
            results.append(0)  # Точка лежит на окружности
        else:
            results.append(2)  # Точка снаружи
    return results

def main(circle_file, points_file):
    circle = read_circle_data(circle_file)
    points = read_points(points_file)
    positions = calculate_position(circle, points)
    for position in positions:
        print(position)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py <путь к файлу окружности> <путь к файлу точек>")
    else:
        main(sys.argv[1], sys.argv[2])
