import random
word_list = ["apple", "ball", "cat", "brother"]
choosen_word = random.choice(word_list)
print(choosen_word)
display = []
word_length = len(choosen_word)
for _ in range(len(choosen_word)):
    display += "_"
end_of_game = False    
while not end_of_game:
    guess_word = input("enter a word:").lower()

    for position in range(word_length):
        if guess_word == choosen_word[position]:
            display[position] = guess_word
    print(display)  
    if "_" not in display:
        end_of_game = True
    print("you won")          

