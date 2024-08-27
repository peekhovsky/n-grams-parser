# N-Grams Parsing

Use Python to produce a CSV file with top five word 3-grams
(n-grams, use lowercase and remove punctuation)
in the commit messages for each author name in event type “PushEvent”
within the attached file:
[10K.github.jsonl](task%2F10K.github.jsonl).

https://pypi.org/project/ijson/

#### Pattern:

```csv
 'author' 'first 3-gram' 'second 3-gram'
 'third 3-gram' 'fourth 3-gram' 'fifth 3-gram'
```

#### Example:

```csv
 'erfankashani' 'merge pull request' 'pull request #4'
 'request #4 from' 'rack from 207' 'from 207 to'
````

Feel free to add all best practice elements such as Unit Tests.

##### Load jsonl file

```python
import json

with open('your_file.jsonl', 'r') as jsonl_file:
    json_list = list(jsonl_file)  # Read lines into a list

    for json_str in json_list:
        result = json.loads(json_str)  # Parse each line as a JSON object
        print(f"Result: {result}")

import jsonlines

with jsonlines.open('input.jsonl') as reader:
    for obj in reader:

````

##### Load usual json file

```python
import json

with open('your_file.jsonl', 'r') as data_file:
    data = json.load(data_file)

    actor_url = data["actor"]["url"]
    repo_url = data["repo"]["url"]
    z
````

