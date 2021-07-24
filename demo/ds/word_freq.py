# Word Frequency
text = "Programming is fun. Programs can name a lot of difference. Programming is a pain for some"

words = {}

for w in text.split(" "):
    w = w.strip(".")  # Remove . at the end
    if w in words:  # Existing word so increment it
        words[w] = words[w] + 1
    else:  # New word so place it without count 1
        words[w] = 1

for w, c in sorted(words.items()):
    print(f"{w:20} {c:3}")
