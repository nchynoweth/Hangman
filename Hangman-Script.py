import requests
import random
import string

word_file = open("words.txt", "r")
words = word_file.readlines()

def select_num():
    num_length_r = input("Please select a number between 4 and 8 to indicate the length of the word you will be guessing:")
    return num_length_r

def select_num_2():
    num_length_r2 = input("Please again, select a number between 4 and 8 to indicate the length of the word you will be guessing and as a note, you selected %s last time:" % (num_length))
    return num_length_r2

print("Welcome to Hangman!")
num_length = select_num()

while (int(num_length) > 8) or (int(num_length) < 4):
    num_length = select_num_2()

def select_num_guess():
    num_guesses = input("Please select how many guesses you will have (between 5 and 20):")
    return num_guesses

def select_num_guess_2():
    num_guesses_r2 = input("Please use only a number between 5 and 20:")
    return num_guesses_r2

num_guess_length = select_num_guess()
while((int(num_guess_length) > 20) or (int(num_guess_length) < 5)):
    num_guess_length = select_num_guess_2()

sorted_words = []
for word in words:
    if len(word) == int(num_length):
        sorted_words.append(word)

def pick_int(list):
    length = len(sorted_words)
    return random.randint(1, length)

def pick_word(int):
    return sorted_words[int]

value_int = pick_int(sorted_words)
value_word = pick_word(value_int).lower()

def print_status(guesses):
    output = []
    build_word = ''
    guess = guesses[-1]
    correct = 0
    for letter in value_word:
        build_word = build_word + '*'
    for guess in guesses:
        l_build = list(build_word)
        l_position = 0
        for letter in value_word:
            l_position += 1
            ll_position = 0
            for star in l_build:
                ll_position += 1
                if (letter == guess) and (ll_position == l_position):
                    l_build[ll_position - 1] = str(letter)
                    build_word = ''.join(l_build)
    for letter in value_word:
        if str(letter) == str(guess):
            correct = 1
    output.append(build_word)
    output.append(correct)
    return output

def take_letter():
    condition = True
    while condition:
        userInput = input("Enter in a single letter:")
        if (userInput.isdigit()) or (int(len(userInput)) != 1):
            condition = True
        else:
            return userInput.lower()


def append_guess(guess):
    guesses.append(guess)

guesses = []
guesses_missed = []
round = 1
end_round = 0

def start_round():
    global round
    global end_round
    print("Starting round %s!" % (str(round)))
    guesses_left = int(num_guess_length) - int(len(guesses_missed))
    print("You have %s guesses left:" % (guesses_left))
    letter = take_letter()
    while letter in guesses:
        print("You have already guessed that!")
        letter = take_letter()
    append_guess(letter)
    output = print_status(guesses)
    if output[1] == 1:
        print("Gottem! %s" % (str(output[0])))
        print(" ")
        round += 1
    else:
        print("Missed... 1 body part added.. %s" % (str(output[0])))
        print(" ")
        guesses_missed.append(letter)
        end_round += 1
        round += 1

print("We have selected a word for you to guess, its a %s letter word!" % (num_length))

while (int(end_round) != (int(num_guess_length))):
    start_round()

print("All out of guesses, the correct word is %s!" % (value_word))
print("Thanks for playing!")
