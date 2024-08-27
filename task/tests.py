import json
import csv

json_path = 'task/10K.github.jsonl'
json_path_test = 'task/test_file.jsonl'
json_path_test2 = 'task/test_file2.json'

csv_path = 'task/output.csv'


def parse_json(line):
    pass


# fieldnames = ["Type", "Actor", "URL"]

fieldnames2 = ["Author", ""]


def trim_data_file():
    with (open(json_path, 'r') as json_file,
          open('task/small_test_data.jsonl', 'w') as json_output):
        res = []

        for row in json_file:
            data = json.loads(row)
        if 'message' in row:
            res.append(data)
            json.dump(data, json_output)
            json_output.write('\n')

        # url_data = [
        #     {"Type": "Author", "URL": data["actor"]["url"]},
        #     {"Type": "Repo", "URL": data["repo"]["url"]},
        #     {"Type": "Org", "URL": data["org"]["url"]}
        # ]
        #
        # csv_writer.writerow(data["actor"]["url"])
        # print("json")
        # print(data)


def parse_json_lines():
    with (open(json_path, 'r') as json_file,
          open('task/small_test_data.jsonl', 'w') as json_output,
          open(csv_path, 'w') as csv_file):
        # csv_writer = csv.writer(csv_file)
        # csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # csv_writer.writeheader()

        res = []

        for row in json_file:
            data = json.loads(row)
            if 'message' in row:
                res.append(data)
                json.dump(data, json_output)

            # url_data = [
            #     {"Type": "Author", "URL": data["actor"]["url"]},
            #     {"Type": "Repo", "URL": data["repo"]["url"]},
            #     {"Type": "Org", "URL": data["org"]["url"]}
            # ]
            #
            # csv_writer.writerow(data["actor"]["url"])
            # print("json")
            # print(data)


def parse_json_lines_():
    with open(json_path_test, 'r') as f:
        for line in f:
            data = json.loads(line)

            print("json")
            print(data)

            actor_url = data["actor"]["url"]
            repo_url = data["repo"]["url"]
            org_url = data["org"]["url"]

            # Create a list of dictionaries (one for each URL)
            url_data = [
                {"Type": "Actor", "URL": actor_url},
                {"Type": "Repo", "URL": repo_url},
                {"Type": "Org", "URL": org_url}
            ]
            print('url_data')
            print(url_data)


if __name__ == '__main__':
    parse_json_lines()
