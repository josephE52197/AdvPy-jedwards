#! /usr/bin/env python3
import random
def print_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
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
def readData(hman_words):
    with open('words.txt', 'r') as fr:
        data = fr.readlines()
    for i in data:
        hman_words.append(i.strip())

def game(hman_words):
    secretword = random.choice(hman_words).upper()
    guessed_letters = []
    num_games = 0
    num_wins = 0
    num_losses = 0
    done = False
    playagain = True
    finished_word = "_" * len(secretword)
    tries = 6
    while playagain:
        print("You ready for some hangman?")
        print(print_hangman(tries))
        print(finished_word , "\n")
        while not done and tries > 0:
            guess = input("Guess a letter: ").upper()
            if guess in guessed_letters:
                print("You already guessed that")
            elif guess not in secretword and (guess.isalpha() and len(guess) == 1):
                print("Sorry, your guess was wrong. You have ",tries, ' tries remaining')
                tries -= 1
                guessed_letters.append(guess)
            elif guess in secretword:
                    print("Way to be,", guess, "was a good guess!")
                    guessed_letters.append(guess)
                    word_as_list = list(finished_word) 
                    indices = [i for i, letter in enumerate(secretword) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    finished_word = "".join(word_as_list)
                    if "_" not in finished_word:
                        done = True
            else:
                print("Not a correct input")
            print(print_hangman(tries))
            print(finished_word, "\n")
        if done:
            ans = input("Congratulations! Would you like to play again? Y/N: ")
            num_games += 1
            num_wins += 1
            if ans.upper() == 'Y':
                secretword = random.choice(hman_words).upper()
                finished_word = "_" * len(secretword)
                guessed_letters = []
                tries = 6
                done = False
                continue
            else:
                playagain = False
                print("Thanks for playing!", "\n")
                print("Total games: ", num_games , "Total Wins: ", num_wins, "Total Losses: ", num_losses)                
        else:
            print("Sorry, the word was ", secretword , "\n")
            num_games += 1
            num_losses += 1
            ans = input("Would you like to play again? Y/N: ")
            if ans.upper() == 'Y':
                secretword = random.choice(hman_words).upper()
                finished_word = "_" * len(secretword)
                guessed_letters = []
                tries = 6
                done = False
                continue
            else:
                playagain = False
                print("Thanks for playing!", "\n")
                print("Total games: ", num_games , "Total Wins: ", num_wins, "Total Losses: ", num_losses)  

def main():
    hman_words = []
    readData(hman_words)
    game(hman_words)
            
if __name__ == "__main__":
    main()
