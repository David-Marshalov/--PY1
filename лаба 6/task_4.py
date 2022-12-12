import json

INPUT_FILE = "input.csv"

     # TODO реализовать конвертер из csv в json
def csv_to_list_dict(filename, delimiter=",") -> list[dict]:
    with open(filename) as file:
        lst = []
        headers = file.readline()
        headers = headers.split(delimiter)
        headers[len(headers) - 1] = headers[len(headers) - 1][:-1]
        values = [file.read()]
        values = values[0].split()

        for i in range(len(values)):
            line_of_values = values[i].split(delimiter)
            ready_dict = {headers[i]: line_of_values[i] for i in range(len(line_of_values))}
            lst.append(ready_dict)
        return lst

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))




