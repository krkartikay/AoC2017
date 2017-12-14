def main():
    valid_passphrases = 0
    try:
        while True:
            inp = raw_input()
            if validate(inp):
                valid_passphrases += 1
    except EOFError:
        print valid_passphrases


def validate(passphrase):
    appeared_words = []
    for word in passphrase.split():
        l = list(word)
        l.sort()
        word = "".join(l)
        if word in appeared_words:
            return False
        appeared_words.append(word)
    return True

main()