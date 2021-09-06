import random
import time
import sys
import json
from Hangman_UI import stages, logo


# print(len(dashed_word))
# print(len(format_guess_word))
time.sleep(0.5)
print(logo)
time.sleep(1)


text = "This is the new world order!\nGary Vaynerchuk, the evil entrepreneur/motivational speaker has taken control of the world\nand now is the supreme power!\nHe has set unrealistic standards of commitment and work.\nThere is no place for lazy people here!!!\nGary has ordered to execute all the lazy people in the world!!!\nI know what you are thinking...'T..T...Tejas!!'\nYes, the inevitable has happened and Tejas is on the\ndeath row, right on the top of the list, for being the laziest human alive!\nBut wait, there is a way to save him!\nTejas challenged Gary for a bet and it was decided that if Tejas wins he gets to live\nand if he loses he is a dead man.\nThe condition is that Gary will pick a random word in his mind,\nand you have to figure out what it is.\nYou will see blank lines which equal to the number of letters in the word.\nWhen you guess a correct letter,\nthe blank at the position of that letter in the particular word that Gary has picked in his mind\nwill be replaced by correct letter.\nRemember Tejas has only 5 lives meaning, he will loose one life for every letter that you guess wrong!' His life is in your hands!\nSave him!!!\n"
main = True
while(main):

    word_dict = json.load(open("dictionary.json"))
    word_list = list(word_dict.keys())
    guess_word = random.choice(word_list)
    input_list = []
    guess_word1 = guess_word.replace(" ", "")
    format_guess_word = " ".join(guess_word1) + " "
    format_guess_word = format_guess_word.replace("-","_")
    format_guess_word = format_guess_word.lower()
    no_of_dashes = len(guess_word)

    dashed_word = "_ " * no_of_dashes
    game = 1
    intro = True
    while(intro):

        time.sleep(1)
        instructions = input("Press 1 for instructions, press 0 to skip \n")
        if instructions.isnumeric() == False:
            time.sleep(0.5)
            print("Wrong Input")

        else:
            if instructions == "1":
                for l in text:
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    time.sleep(0.035)
                    intro = False
            elif instructions == "0":
                intro = False

            else:
                time.sleep(0.5)
                print("Wrong Input")
                pass

    input("Press Enter to start the game")
    time.sleep(1)
    print(stages[0])
    # print(guess_word)
    time.sleep(1)
    print(f"Lives Remaining: {6 - game}/5")
    time.sleep(1)
    print(dashed_word)
    # print(guess_word)
    # print(format_guess_word)

    while(game < 6):
        # print(len(dashed_word))
        # print(len(format_guess_word))
        # print(format_guess_word)
        # print(dashed_word[len(dashed_word) - 1])

        time.sleep(0.5)
        user_guess = input("guess the letter\n").lower()
        if user_guess.isalpha() == False:
            time.sleep(0.5)
            print("Enter an alphabet!")
            time.sleep(0.5)
            print(dashed_word)

        elif user_guess in dashed_word:
            time.sleep(0.5)
            print("You have guessed this letter already")
            time.sleep(0.5)
            print(f"Lives Remaining: {5 - game}/5")
            time.sleep(0.5)
            print(dashed_word)

        elif len(user_guess)>1 or len(user_guess)<1:
            time.sleep(1)
            print("You can guess only one letter at a time!")

        else:

            if user_guess in guess_word:
                count = []
                for position in range(0, len(guess_word)):
                    if guess_word[position] == user_guess:
                        count.append(position*2)

                yeah = dashed_word
                for position_no in count:
                    dashed_word = dashed_word[:position_no] + user_guess + dashed_word[position_no + 1:]
                    yeah = dashed_word
                time.sleep(0.75)
                print(f"Your previous wrong guesses: {input_list}")
                time.sleep(1)
                print(f"Lives Remaining: {6 - game}/5")
                time.sleep(0.5)
                print(yeah)

                if yeah == format_guess_word:
                    time.sleep(1)
                    print("Congratulations! You guessed the word and saved Tejas' life!!!! He says thank you :)!\n(Not sure if he will stop being lazy though! XD)")
                    time.sleep(1)

                    print(f"The meaning of this word is\n{guess_word}: {word_dict[guess_word]}")
                    time.sleep(1)
                    print(logo)
                    game = 8
                    exit = True
                    while (exit):
                        time.sleep(1)
                        retry = input("Enter 1 to play again /  0 to exit the game  \n")
                        if retry == "1":
                            exit = False
                        elif retry == "0":
                            exit = False
                            main = False
                        else:
                            print("Wrong Input\n")
                            time.sleep(0.5)
                            pass

            else:
                game = game + 1
                time.sleep(0.75)
                print("wrong guess")
                user_guess = str(user_guess)
                input_list.append(user_guess)
                time.sleep(0.75)
                print(f"Your previous wrong guesses: {input_list}")

                if game == 6:
                    time.sleep(1)
                    print(stages[game])
                    time.sleep(0.5)
                    print(dashed_word)
                    time.sleep(1)
                    print(f"Lives Remaining: {6 - game}/5")
                    time.sleep(0.75)
                    print("Game Over, you couldn't save Tejas! He tells you to go buy a dictionary!")
                    time.sleep(1)
                    print(f"The word was '{guess_word}'")
                    time.sleep(1)
                    print(f"The meaning of this word is\n{guess_word}: {word_dict[guess_word]}")
                    exit = True
                    while(exit):
                        time.sleep(1)
                        retry = input("Enter 1 to play again /  0 to exit the game  \n")
                        if retry == "1":
                            exit = False
                        elif retry == "0":
                            exit = False
                            main = False
                        else:
                            print("Wrong Input\n")
                            time.sleep(0.5)
                            pass

                else:
                    time.sleep(1)
                    print(stages[game])
                    print(f"Lives Remaining: {6 - game}/5")
                    time.sleep(0.5)
                    print(dashed_word)

            # print("Game Over")
            # print(f"The word was{guess_word}")
        # print("Game Over, you couldn't save Tejas! He tells you to go buy a dictionary!")
        # print(f"The word was {guess_word}")






