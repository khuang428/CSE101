def add_s(words, starts):
    for word in words:
        if word[0] in starts:
            words[words.index(word)] = word + 's'
    return words

print(add_s(['cave','head','beer','Note'], 'ahdDuNec'))


