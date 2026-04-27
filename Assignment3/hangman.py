"""
File: hangman.py
Name:呂沅翰
-----------------------------
This program plays a console-based Hangman game.

The user is shown a word represented by dashes and tries to
guess the hidden word by entering one character in each round.
If the guessed character is correct, the program updates and
displays the word on the console.

The player has a limited number of chances, defined by
N_TURNS, to successfully guess the word and win the game.
"""


import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    word = random_word()
    dashed = "-" * len(word)
    turns = N_TURNS
    guessed_letters = ""  # 紀錄猜過的字母

    print("The word looks like:", dashed)
    print("You have", turns, "guesses left.")

    while turns > 0:
        guess = input("Your guess: ").upper()

        # 檢查輸入是否合法
        if len(guess) != 1 or not guess.isalpha():
            print("Illegal format.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters += guess

        # 猜對
        if guess in word:
            new_dashed = ""
            for i in range(len(word)):
                if word[i] == guess:
                    new_dashed += guess
                else:
                    new_dashed += dashed[i]
            dashed = new_dashed

            print("You are correct!")
        else:
            turns -= 1
            print("There is no", guess, "'s in the word.")

        print("The word looks like:", dashed)
        print("You have", turns, "guesses left.")

        # 檢查是否贏
        if dashed == word:
            print("You win!!")
            print("The word was:", word)
            return

    # 輸掉
    print("You are completely hung :(")
    print("The word was:", word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
