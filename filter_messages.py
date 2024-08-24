def filter_messages(messages):
    finalSentences = []
    delIndexes = []
    for sentence in messages:
        sentenceSplit = sentence.split()
        counter = 0
        for j in range(len(sentenceSplit) -1, -1, -1):
            if sentenceSplit[j] == 'dang':
                del(sentenceSplit[j])
                counter += 1
        finalSentences.append(' '.join(sentenceSplit))
        delIndexes.append(counter)
    return finalSentences, delIndexes

print(filter_messages(['darn it', "this dang thing won't work", 'lets fight one on one']))