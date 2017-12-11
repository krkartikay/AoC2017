valid_passphrases = 0

def validate(passphrase):
    appeared_words = []
    for word in passphrase.split():
        if word in appeared_words:
            return False
        appeared_words.append(word)
    return True

try:
    while True:
        valid_passphrases += int(validate(raw_input()))
except EOFError:
    print valid_passphrases
