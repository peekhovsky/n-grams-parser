import json
import csv

from typing import List, Tuple

import task.data_parser as parser
from task.ngrams_ananlyzer import find_common_ngrams

json_path = 'task/10K.github.jsonl'
csv_path = 'task/10K.github.jsonl'

columns = ('author', 'first 3-gram', 'second 3-gram',
           'third 3-gram', 'fourth 3-gram', 'fifth 3-gram')

type NgramMap = Tuple[str, List[str]]


def save_result_csv(ngrams: List[NgramMap]):
    with open('task/data/most_common_ngrams.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(columns)

        for author, values in ngrams:
            writer.writerow([author, *values])


def analyze_author(n, limit, commits: list[tuple[str, ...]]):
    common_ngrams = find_common_ngrams(*commits, n=n, limit=limit)
    return [' '.join(ngram) for ngram in common_ngrams]


def analyze_authors(n, limit, authors_commits: list[tuple[str,]]):
    return [(author, analyze_author(n, limit, commits))
            for author, commits in authors_commits if len(commits) > 0]


def analyze_data(n=3, limit=5, crop=None):
    commits = []

    with open('task/data/10K.github.jsonl', 'r') as jsonl_file:
        for json_line in jsonl_file:
            line_commits = parser.get_commits(json.loads(json_line))
            commits.extend(line_commits)

    by_author = parser.get_by_authors(commits, end=crop)

    common_ngrams = analyze_authors(n, limit, by_author)
    common_ngrams = list(filter(
        lambda ngrams: len(ngrams[0]) > 0 and len(ngrams[1]) > 0,
        common_ngrams))

    with open('task/data/common_ngrams.json', 'w') as ngrams_file:
        json.dump({"data": common_ngrams}, ngrams_file)

    print(f'\nMost common ngrams: {common_ngrams}')
    print(f'\nCommits saved, count: {len(common_ngrams)}')

    save_result_csv(common_ngrams)


if __name__ == '__main__':
    analyze_data(crop=200)

    # for author, messages in parser.by_author(commits):
    # print('Author: ' + author)
    # common_ngrams = find_common_ngrams(*messages)
    # print(common_ngrams)

#

# most_common_ngrams = map(
#     lambda item:
#     find_common_ngrams(item[1], n=n, limit=limit),
#     ngrams_by_author.items())
#
# most_common_ngrams = [
#     [author, *find_common_ngrams(*ngrams, n=n, limit=limit)]
#     for author, ngrams in ngrams_by_author]
