import random
import json
from pathlib import Path

path = Path("/Users/prithvi_vasistha/Documents/ppv-skill-dev/python/Codes-Notebooks/github/chapter-11-testing-with-pytest/Testing-a-class/testcases.json")

test_list = []
language_list = ['English', 'Spanish', 'Kannada', 'Hindi', 'Tamil']

for number in range(0, 1001):

    test_list.append(random.choice(language_list))

formatted = json.dumps(test_list)
path.write_text(formatted)
