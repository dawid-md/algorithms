# import re
# def order(sentence):
#     finalSentence = ['','','','','','','','','']
#     for word in sentence.split(" "):
#         num = re.search(r'\d', word).group()
#         finalSentence[int(num)-1] = word
#     return " ".join(finalSentence)

# print(order("is2 sentence4 This1 a3"))

import re
def order(sentence):
    return ' '.join(sorted(sentence.split(' '), key=lambda x: int(re.search(r'\d', x).group())))

def order2(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

print(order2("is2 sentence4 This1 a3"))