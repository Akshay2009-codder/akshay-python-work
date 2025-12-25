text = "this is a test this is python test"

words = text.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

for word, count in freq.items():
    print(word, ":", count)
