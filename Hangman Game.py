import random

# Import text file to read
with open("Hangman.txt", "r") as f:
    data = f.read()
    words = data.split()

# Choose random words
word = random.choice(words)

chances = 5
guess_word = "_" * len(word)
print(guess_word)

while chances > 0 and guess_word != word:
    letter = input("Guess a letter:")
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guess_word = guess_word[:index] + letter + guess_word[index + 1:]
        print(guess_word)
    else:
        chances -= 1
        print("Incorrect guess")
        print("The remaining chances:", chances)

if guess_word == word:
    print("Congratulations! You won")
else:
    print("Game over")
    print("You lose")
    print("All chances are exhausted")
    print("Correct word is:", word)
