def get_count(sentence):
    vowels = ['a','e','i','o','u']
    counts = 0
    for letter in sentence:
        if letter in vowels:
            counts+=1
    return counts

    #using one line 
    # return sum(letter in 'aeiou' for letter in sentence)

print(get_count("abracadabra"))