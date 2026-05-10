name = input('Enter file: ')
handle = open(name, encoding='utf-8')  # <-- fixed encoding issue

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print(f'Most repeated word was: {bigWord}')
print(f'Times the word repeated: {bigCount}')
