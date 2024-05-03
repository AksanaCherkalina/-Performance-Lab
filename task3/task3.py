import json

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def fill_values(tests, values):
    if isinstance(tests, list):
        for item in tests:
            fill_values(item, values)
    elif isinstance(tests, dict):
        if "id" in tests and "value" in tests:
            test_value = values.get(str(tests["id"]), None)
            if test_value is not None:
                tests["value"] = test_value
        for key in tests:
            if isinstance(tests[key], (dict, list)):
                fill_values(tests[key], values)

def save_json_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main(values_path, tests_path, report_path):
    values_data = load_json_file(values_path)
    tests_data = load_json_file(tests_path)

    values_dict = {str(item["id"]): item["value"] for item in values_data["values"]}
    fill_values(tests_data["tests"], values_dict)

    save_json_file(tests_data, report_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Использование: python script.py values.json tests.json report.json")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
