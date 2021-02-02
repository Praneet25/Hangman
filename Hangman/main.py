import random
from words import word_list

def word():
    random_word = random.choice(word_list)
    return random_word.upper()

def play(random_word):
    word_completion = "_" * len(random_word)
    tries=6
    guessed = False
    guessed_letter =[]

    guessed_word =[]
    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print(word_completion,"\n")


    while not guessed and tries > 0:
        inp = input("Enter a letter or word to guess!\n").upper()
        if len(inp) == 1 and inp.isalpha():
            if inp in guessed_letter:
                print("You have already guessed that letter")
                print("you have", tries, "remaining!")
            elif inp not in random_word:
                print("Your guess is wrong!")
                tries -=1
                guessed_letter.append(inp)
                print("you have",tries,"remaining!")
            else:
                print("congrats you have guessed the letter!")
                guessed_letter.append(inp)
                word_complist = list(word_completion)
                indices = [i for i,letter in enumerate(random_word) if letter ==inp]
                for index in indices:
                    word_complist[index]=inp
                word_completion="".join(word_complist)
                if "_" not in word_completion:
                    guessed=True
        elif len(inp) == len(random_word) and inp.isalpha():
            if inp == random_word:
                print("You have guessed the word")
                guessed_word.append(inp)
                word_completion = random_word
                guessed = True
            elif inp != random_word:
                print("Your guess is wrong!")
                tries -=1
                print(f"You have {tries} guesses remaining")
            elif inp in guessed_word:
                print("You already guessed the word")
            else:
                print("Enter a valid word")
        else:
            print("Enter a valid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        if guessed:
            print(f"You have won the game")
        elif tries ==0:
            print("You have lost the game")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


if __name__ == '__main__':
    words = word()
    play(words)
    replay = input("Do you want play again? Y/N").upper()
    if replay == "Y" :
        words=word()
        play(words)