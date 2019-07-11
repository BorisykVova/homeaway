import csv
import json
import typing as typ


def load_data(path: str) -> typ.List[str]:
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        return [item[0] for item in csv_reader]


def save_data(data: dict, result_path: str) -> None:
    with open(result_path, 'a+') as json_file:
        json_file.write(json.dumps(data, indent=4) + ',\n')
