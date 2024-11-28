#თამაში რიცხვის გამოცნობა
import random #იმპორტის ფუნქციის გამოსაყენებლად უნდა დავაიმპორტოთ ფუნქცია
livess=10 #განვსაზღვრე სიცოცხლის რაოდენობა
lives=0 #შემოვიტანე ცვლადი ფუნქციაში გამოსაყენებლად

def game(ask2, number, lives): #განვსაზღვრე ფუნქცია სიცოცხლის რაოდენობა რომ შემცირდეს არასწორი ციფრის შეყვანისას
    if ask2>number:
        print("too high")
        return lives-1
    elif ask2<number:
        print("too low")
        return lives-1
    elif ask2==number:
        print ("you win") #თუ რიცხვი გამოიცნო მოიგებს


def func(): #განვსაზღვრე თამაშის ფუნქცია
    print("welcome")
    print("i am thinking about number")
    number=random.randrange(1,100)
    #print(number) დავმალე რიცხვი რაც რანდომმა აირჩია თუ დამჭირდება გავუშვებ რომ ადვილად გავტესტო ფუნქციის მუშაობა
    lives=livess


    ask2=0
    while ask2!=number:
        print(f' you have {lives} lives')
        ask2=int(input("guess number"))
        lives=game(ask2, number, lives)
        if lives==0:
            print("you lose")
            return
        elif ask2!=number:
            print("AGAIN")
func() #გამოვიძახე ფუნქცია
