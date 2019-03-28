import requests
import random
import string
from os import system, name
from time import sleep

word_file = open("words.txt", "r")
words = word_file.readlines()

def clear():
    if name == 'nt':
        _ = system('clear')

def select_num():
    num_length_r = input("Please select a number between 4 and 8 to indicate the length of the word you will be guessing:")
    clear()
    return num_length_r

def select_num_2():
    num_length_r2 = input("Please again, select a number between 4 and 8 to indicate the length of the word you will be guessing and as a note, you selected %s last time:" % (num_length))
    clear()
    return num_length_r2

clear()
print("Welcome to Hangman!")
sleep(2)
clear()
num_length = select_num()

while (int(num_length) > 8) or (int(num_length) < 4):
    num_length = select_num_2()

def select_num_guess():
    num_guesses = input("Please select how many guesses you will have (between 5 and 20):")
    clear()
    return num_guesses

def select_num_guess_2():
    num_guesses_r2 = input("Please use only a number between 5 and 20:")
    return num_guesses_r2

num_guess_length = select_num_guess()
while((int(num_guess_length) > 20) or (int(num_guess_length) < 5)):
    num_guess_length = select_num_guess_2()

sorted_words = []
for word in words:
    if len(word) == (int(num_length) + 1):
        sorted_words.append(word.replace("\n", "").replace("\t", ""))

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
    if len(guesses) == 0:
        guess = ""
    else:
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
        userInput = input(" - Enter in a single letter:")
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
letter = ""

def start_round():
    clear()
    global round
    global end_round
    global letter
    output = print_status(guesses)
    if round == 1:
        print("Starting round 1!")
        guesses_left = int(num_guess_length) - int(len(guesses_missed))
        print(" - You have %s guesses!" % (guesses_left))
        print(" - %s" % (str(output[0])))
        letter = take_letter()
        while letter in guesses:
            print(" - You have already guessed %s" % (letter))
            letter = take_letter()
        append_guess(letter)
        output = print_status(guesses)
        round += 1
        if int(output[1]) == 0:
            guesses_missed.append(letter)
            end_round += 1
        sleep(1)
        return letter
    else:
        print("Starting round %s!" % (round))
        guesses_left = int(num_guess_length) - int(len(guesses_missed))
        if output[1] == 1:
            print(" - You got one!")
            round += 1
        else:
            print(" - Missed! There is no '%s'" % (letter))
            guesses_missed.append(letter)
            guesses_left = int(num_guess_length) - int(len(guesses_missed))
            end_round += 1
            round += 1
        if guesses_left != 1:
            print(" - You have %s guesses left!" % (guesses_left))
        else:
            print(" - You have 1 more guess!")
        print(" - You have guessed:", guesses)
        print(" - %s" % (str(output[0])))
        letter = take_letter()
        while letter in guesses:
            print(" - You have already guessed %s" % (letter))
            letter = take_letter()
        append_guess(letter)
        output = print_status(guesses)
        sleep(1)
        return letter

print("We have selected a word for you to guess, its a %s letter word!" % (num_length))
sleep(2.5)
clear()

def check_done(guesss, word):
    return_num = 0
    check_num = 0
    length_word = len(word)
    for letter in word:
        if letter in guesss:
            check_num +=1
    if length_word == check_num:
        return_num = 1
    return return_num

while ((int(end_round) + 1) != (int(num_guess_length)) and (check_done(guesses, value_word) != 1)):
    letter = start_round()

if (check_done(guesses, value_word) == 0):
    clear()
    print("All out of guesses, the correct word is %s!" % (value_word))
    print("Thanks for playing!")
else:
    clear()
    print("You got it correct!")
    print("The correct word is %s!" % (value_word))
