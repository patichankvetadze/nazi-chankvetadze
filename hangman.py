#თამაში Hangman
import random #დავაიმპორტოთ რანდომი გამოსაყეებლად
word_list=["vashli", "smxali", "atami", "kliavi", "nushi", "banani"] #განვსაზღვრე რა ხილი უნდა გამოიცნოს
lives=10
chosen_word=random.choice(word_list)
#print(chosen_word) სიტყვის ადვილად გამოსაცნობად შემიძლია დავბეჭდო სიტყვა თუმცა თამაშისთვის არ გვჭირდება

tire="_" #რამდენი ასოა იმდენი ტირე რომ დაიბეჭდოს
for a in range(1, len(chosen_word)):
    tire+="_"
print(tire)
game_over=False
lst=[] #გამოცნობილი ასოები რომ ჩავწერო ლისტში
print("choes a fruit")

while not game_over: #სანამ სიცოცხლე არ ამოიწურება ან გამოიცნობს თამაში უნდა გაგრძელდეს

    guess=input("Guess a letter: ").lower()
    if guess in lst:
        print("You have already guessed that letter")
    if guess not in lst:
        print(f'you have {lives} lives')
    space=" "
    for i in chosen_word: #თუ გამოიცნობს ლისტსში რომ ჩაიწეროს
        if guess==i:
            space+=i
            lst.append(guess)
        elif i in lst:
            space+=i
        else:
            space+="_"
    print(space)
    if guess not in chosen_word: #თუ ვერ გამოიცნობს სიცოცხლე რომ მოაკლეს
        lives-=1
        if lives==0:
            game_over=True
            print("You lost")
    if "_" not in space:
        game_over=True
        print("You win")
