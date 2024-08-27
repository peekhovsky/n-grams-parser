import json
from typing import Tuple, Dict, List, Any
import itertools

json_path = 'data/10K.github.jsonl'


def by_author(commits, end=None):
    commits = sorted(commits, key=lambda c: c[0])
    grouped = itertools.groupby(commits, key=lambda c: c[0])

    return [(author, [message for _, message in commits])
            for author, commits in grouped]


def get_by_authors(commits, start=0, end=None):
    commits = sorted(commits, key=lambda c: c[0])
    grouped = itertools.groupby(commits, key=lambda c: c[0])

    res = ([(author, [message for _, message in commits])
            for author, commits in grouped])
    return res[start:(end or len(res))]


def get_entry(commit):
    author = commit.get('author', {}).get('name')
    message = commit.get('message')
    return author, message


def get_commits(data: dict) -> list[tuple[str, str]]:
    if data.get('type') == 'PushEvent':
        commits = data.get('payload', {}).get('commits', [])
        return list([(get_entry(commit)) for commit in commits])
    return []
