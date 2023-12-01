## Advent of Code 2023

Here are my solutions.

get_puzzle.py uses a module not pushed here to set the session for AoC so the personal puzzle can be retrieved.

To use it, you can write your own

```python
import os
os.environ['AOC_SESSION'] = 'your_session_id'
```

You can get the session id from the AoC website. Inspect the cookies when you are logged in and grab the value of `session`.