from random_words import RandomWords


def fetch_word():
    rw = RandomWords()
    word = rw.random_word()
    return word


def replaceall(positions, guesschar, guess):
    guess = list(guess)
    for i in positions:
        guess[i] = guesschar
    guess = ''.join(guess)
    return guess


def main():
    word = fetch_word()
    guess = "-" * len(word)
    remaining = 7
    print(word)
    alreadyguessed = []
    while "-" in guess:
        positions = []
        print(guess)
        guesschar = input("Enter a Character")
        positions = [i for i, x in enumerate(word) if x == guesschar]
        if guesschar in alreadyguessed:
            print("You have already guessed %s" % guesschar)
        else:
            if not positions:
                remaining = remaining - 1
                print("Wrong! %s guesses remain" % remaining)
            else:
                guess = replaceall(positions, guesschar, guess)

            if remaining == 0:
                print("You lose! The word is %s" % word)
                exit(0)
        alreadyguessed.append(guesschar)
    print("You guessed it! The word is %s" % word)


if __name__ == '__main__':
    main()