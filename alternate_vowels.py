def is_alt(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    extractedVowels = []
    for j in range(1, len(s)):
        if (s[j] in vowels and s[j-1] in vowels) or (s[j] not in vowels and s[j-1] not in vowels):
            return False
    return True

print(is_alt("yay"))