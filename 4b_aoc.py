valid_passphrases = 0

def count(ch,word):
    "Counts number of occourances of ch in word"
    r = 0
    for char in word:
        if char==ch:
            r += 1
    return r

def is_anagram(w1,w2):
    if len(w1)!=len(w2):
        return False
    else:
        for ch in w1:
            if count(ch,w1) != count(ch,w2):
                return False
        return True

def validate(passphrase):
    appeared_words = []
    for word in passphrase.split():
        for checkword in appeared_words:
            if is_anagram(word,checkword):
                return False
        appeared_words.append(word)
    return True

try:
    while True:
        valid_passphrases += int(validate(raw_input()))
except EOFError:
    print valid_passphrases
