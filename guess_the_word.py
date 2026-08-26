import random
word_list = ("program","python","java","word")

chossen_word = random.choice(word_list) #randomly kuch bhe chunaga wordlist se

word_length = len(chossen_word) #apne pc ko bataya ga word list ka word kitna bada hea so that it could give that much specific space

placeholder = ""

for position in range(word_length):
    placeholder += "_"
print(placeholder)

while "_" in placeholder:
    guess = input("guess the letter : ").lower()
    new_placeholder = ""

    for i, letter in enumerate(chossen_word):
        if letter == guess:
            new_placeholder += letter
        else:
            new_placeholder += placeholder[i]
    placeholder = new_placeholder
    print(placeholder)

print("you win !!!")