import re

words = {}

f = open("story.txt", 'rt')
story = f.read()
f.close()


tokens = re.split(r"\W+", story)
for t in tokens:
    if len(t.strip()) == 0:
        continue

    if t in words:
        words[t] += 1  # increment count
    else:
        words[t] = 1  # new entry
#
for word, count in sorted(words.items()):
    print(f"{word:15} {count:3}")
