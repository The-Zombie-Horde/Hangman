import random
import os
import pygame
from turtle import *
import time


def choose_word():
    return random.sample(WORDS, 1)  # chooses a word to play with


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # clears screen


def hangman_(attempt=0):
    if attempt == 0:
        color('black')
        pensize(5)
        speed(5)
        fd(150)
        lt(180)
        fd(100)
        rt(90)
        fd(300)
        rt(90)
        fd(75)
        rt(90)
        fd(50)
    elif attempt == 1:
        rt(90)
        circle(25)
        return None
    elif attempt == 2:
        circle(25, 180)
        rt(90)
        fd(25)
        rt(90)
        fd(50)
        rt(180)
        fd(100)
        rt(180)
        fd(50)
        lt(90)
        fd(25)
    elif attempt == 3:
        rt(180)
        fd(25)
        lt(90)
        fd(50)
        lt(65)
        fd(25)
        lt(180)
        fd(50)
    elif attempt == 4:
        lt(180)
        fd(25)
        lt(115)
        fd(100)
        lt(120)
        fd(25)
        rt(180)
        fd(50)
    elif attempt == 5:
        rt(180)
        fd(25)
        lt(60)
        fd(50)
        lt(90)
        fd(55)
    elif attempt == 6:
        fd(20)
    elif attempt == 7:
        rt(45)
        fd(50)
    elif attempt == 8:
        fd(25)
    elif attempt == 9:
        rt(180)
        fd(75)
        rt(90)
        fd(50)
    elif attempt == 10:
        fd(25)
        print('You may now close turtle')
        done()


def game_loop():
    penup()  # Set turtle to the correct position, make adjustment as you wish to setx and sety
    setx(-200)
    sety(-200)
    pendown()
    fd(1)   # You must initialize turtle before pygame or else you will get an error
    pygame.init()
    hangman = pygame.mixer.Sound("./media/HangmanWav1.wav")
    hangman.play()
    input("Press 'Enter' to play Hangman!  ")  # starts game
    pygame.init()
    hangman = pygame.mixer.Sound("./media/RUN.wav")
    hangman.play()
    clear_screen()  # clears screen
    word = choose_word()[0]  # chooses a word
    word_guessed = []  # word in '-' and letter form
    for _ in word:
        word_guessed.append("-")  # create an unguessed, blank version of the word
    joined_word = None  # joins the words in the list word_guessed
    tries = 10  # how many times you are aloud to fail
    guessed_letters = []  # list of all letters guessed
    hangman_()  # Draws hangman
    while tries != 0 and "-" in word_guessed:
        print("\nYou have {} attempts remaining".format(tries))
        pygame.init()
        hangman = pygame.mixer.Sound("./media/Tries.wav")
        hangman.play()
        time.sleep(3)
        strs = ''.join(word_guessed)
        print(strs)
        try:
            pygame.init()
            hangman = pygame.mixer.Sound("./media/Select.wav")
            hangman.play()
            time.sleep(4)
            player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()

        except ValueError:  # check valid input
            pygame.init()
            hangman = pygame.mixer.Sound("./media/ValidInput.wav")
            hangman.play()
            print("That is not valid input. Please try again.")
            time.sleep(3)
            continue

        else:
            if not player_guess.isalpha():  # check the input is a letter. Also checks an input has been made.
                pygame.init()
                hangman = pygame.mixer.Sound("./media/NotLetter.wav")
                hangman.play()
                print("That is not a letter. Please try again.")
                time.sleep(4.5)
                continue
            elif len(player_guess) > 1:  # check the input is only one letter
                pygame.init()
                hangman = pygame.mixer.Sound("./media/MoreLetter.wav")
                hangman.play()
                print("That is more than one letter. Please try again.")
                time.sleep(3)
                continue
            elif player_guess in guessed_letters:  # check it letter hasn't been guessed already
                pygame.init()
                hangman = pygame.mixer.Sound("./media/Guessed.wav")
                hangman.play()
                print("You have already guessed that letter. Please try again.")
                time.sleep(5)
                continue
            else:
                pass

        guessed_letters.append(player_guess)

        for letter in range(len(word)):
            if player_guess.lower() == (word[letter].lower()):
                word_guessed[letter] = player_guess  # replace all letters in the chosen word that match the players guess
                pygame.init()
                drums = pygame.mixer.Sound("./media/drum_roll_y.wav")
                drums.play()

        if player_guess.lower() not in word.lower():
            tries -= 1
            pygame.init()
            gasp = pygame.mixer.Sound("./media/gasp_x.wav")
            gasp.play()
            hangman_(10-tries)

    if "-" not in word_guessed:  # no blanks remaining
        pygame.init()
        hangman = pygame.mixer.Sound("./media/Congrats.wav")
        hangman.play()
        print("\nCongratulations! {} was the word!".format(word))
        pygame.init()
        cymbal = pygame.mixer.Sound("./media/applause3.wav")
        cymbal.play()
        ball = pygame.mixer.Sound("./media/woow_x.wav")
        ball.play()
        sphere = pygame.mixer.Sound("./media/Victory.wav")
        sphere.play()
        reset()
    else:  # loop must have ended because attempts reached 0
        pygame.init()
        hangman = pygame.mixer.Sound("./media/Unlucky.wav")
        hangman.play()
        print("\nUnlucky! The word was {}.".format(word))
        pygame.init()
        hangman = pygame.mixer.Sound("./media/fail-trombone-02.wav")
        hangman.play()

text_file = open('test.txt','rb')
text_content = str(text_file.read())[2:-1]
WORDS = text_content.split(r'\r\n')[:-1]

game_loop()