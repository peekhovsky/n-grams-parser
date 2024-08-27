import json
import csv

import logging

logging.basicConfig(level=logging.DEBUG)

from typing import List, Tuple
import tempfile

import jsonlines

import task.data_parser as parser
from task.ngrams_ananlyzer import find_common_ngrams

csv_path = 'task/10K.github.jsonl'

columns = ('author', 'first 3-gram', 'second 3-gram',
           'third 3-gram', 'fourth 3-gram', 'fifth 3-gram')

type NgramMap = Tuple[str, List[str]]

test_file_path = 'task/data/10K.github.jsonl'


class DataLoader:
    temp_file_path = '.temp_data'

    def __init__(self, file_path: str, chunk_size=100):
        self.file_path = file_path
        self.chunk_size = chunk_size

    def load_chunk(self):
        logging.info('Initializing data...')
        lines = []

        for line in open(self.file_path, 'r'):
            logging.debug('line: %s', line)

            if not line or len(lines) >= self.chunk_size:
                logging.debug('yield lines')
                yield lines
                lines = []
            else:
                lines.append(line)

        logging.debug('end lines')
        logging.debug(lines)
        return lines

    def process_data(self, lines: List[str]):
        yield lines


def test_load_data():
    # data_loader = DataLoader('data/test_file.jsonl', 5)
    loader = DataLoader('data/10K.github.jsonl', 5)
    for lines in loader.load_chunk():
        logging.debug(f'lines size: {len(lines)}')
        break


def analyze_data(n=3, limit=5, crop=None):
    commits = []

    with open('data/10K.github.jsonl', 'r') as jsonl_file:
        for json_line in jsonl_file:
            line_commits = parser.get_commits(json.loads(json_line))
            commits.extend(line_commits)

    by_author = parser.get_by_authors(commits, end=crop)


def save_result_csv(ngrams: List[NgramMap]):
    with open('data/most_common_ngrams.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(columns)

        for author, values in ngrams:
            writer.writerow([author, *values])


if __name__ == '__main__':
    test_load_data()

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
