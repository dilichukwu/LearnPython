# check if palindrome

def ispalindrome(word):
    print(word)
    word = list(word)
    while len(word) > 1:
        if word.pop(0) != word.pop():
            return False
    return True

print(ispalindrome('ezratarze'))

def ispalindrome2(word):
    print(word)
    i = len(word)//2
    while i > 0:
        if word[i-1] != word[-i]:
            return False
        i += -1
    return True

print(ispalindrome2('ere'))

def ispalindrome3(word):
    print(word)
    return word == word[::-1]

print(ispalindrome3('apapa'))