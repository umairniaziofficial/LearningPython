from collections import defaultdict


d = {"a": 10}

print(d)

d = defaultdict(lambda: 0)

d["Correct"] = 100

print(d["Correct"])

print(d["fuck"])
