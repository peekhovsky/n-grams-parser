import json

import nltk

import task.data_parser as parser
import itertools

from task.ngrams_ananlyzer import find_common_ngrams, find_ngrams, \
    format_sentence

json_path = 'data/10K.github.jsonl'


def extract_commits(limit: int = 100):
    commits = []

    with open('data/10K.github.jsonl', 'r') as jsonl_file:
        for json_line in itertools.islice(jsonl_file, limit):
            line_commits = parser.get_commits(json.loads(json_line))
            commits.extend(line_commits)

    return commits


def generate_commits_data(limit: int = 100):
    commits = extract_commits(limit)
    groups = parser.by_author(commits)
    print('\nCommits extracted.')

    with open('data/commits.json', 'w') as commits_file:
        json.dump({'commits': commits}, commits_file)

    with open('data/commits_grouped.json', 'w') as grouped_file:
        json.dump(groups, grouped_file)

    print('\nCommits saved.')


if __name__ == '__main__':
    generate_commits_data()

# def trim_data_file(limit: int):
#     with (open('data/10K.github.jsonl', 'r') as jsonl_file,
#           open('small_test_data.jsonl', 'w') as json_output):
#
#         res = []
#         for json_line in jsonl_file:
#             write_json_line(json_line, len(res))
#
#             if len(res) >= limit:
#                 break
#
#         print('\nConverted.')
#
# def split_jsonline(limit: int):
#     with open('data/10K.github.jsonl', 'r') as jsonl_file:
#         commits = []
#
#         for json_line in jsonl_file:
#             commits = write_json_line(json_line, counter)
#
#             if len(commits):
#                 counter += 1
#
#             if counter >= limit:
#                 break
#
#         print('\nConverted.')
# def write_json_line(line, line_num):
#     with open(f'data/line_commits_{line_num}.json', 'w') as json_file:
#         data = json.loads(line)
#         commits = get_commits(data)
#
#         if len(commits):
#             json.dump(commits, json_file)
#
#         return commits


test_messages = [
    "Merge branch 'master' into Merge branch patch-41",
    "Merge pull request #64 from WayneMRP/patch-41\n\nJacob_Gucci [MrozikK] "
    "- lista ostatniej",
    "Merge branch 'master' into patch-46",
    "Merge pull request #69 from "
    "WayneMRP/patch-46\n\nStanis\u0142aw_Szkodnik [Stanek] - wpis na "
    "list\u0119 ostatniej",
    "Merge pull request #70 from WayneMRP/patch-47\n\nKhali_Touta [Khali] - "
    "edycja wpisu",
    "Merge branch 'master' into patch-48"
]


def test_analyzer():
    n = 2
    ngrams = find_ngrams(*test_messages, n=n)
    print('Custom: ')
    print(ngrams)

    print('Common: ')
    print(find_common_ngrams(*test_messages, n=n, limit=5))

    # Expected
    expected = []
    for sentence in test_messages:
        tokens = nltk.word_tokenize(format_sentence(sentence))
        expected.extend(list(nltk.ngrams(tokens, n)))

    print('Expected:')
    print(expected)


if __name__ == '__main__':
    test_analyzer()
