#შევქმნათ კალკულატორი
#გავაკეთოთ ფუნქციები კალკულატორის ყველა ფუნქციისთვის
def add (n1, n2):
    return n1 + n2
def subtract (n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

#შევქმნათ ლექსიკონი სიმბოლოების და ფუნქციების გამოყენებით
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }
#დავწეროთ კალკულატორის ფუნქცია
def calculator():
    cont=True
    try: #შეცდომით  ციფრის მაგივრად ასო რომ შეიყვანოს გამოუტანს შეტყობინებას შეიყვანოს რიცხვი
        n1=float(input("n1")) #შეიყვანოს ციფრი
    except ValueError:
        print("Please enter a number")
        n1 = float(input("n1"))

    while cont:
        for i in operations:
            print(i) #რომ დაბეჭდოს რა სიმბოლო აირჩია
        oper=input("schooes operation")
        try:
            n2=float(input("n2")) #შეიყვანოს ციფრი
        except ValueError:
            print("Please enter a number")
            n2 = float(input("n2"))
        answer = operations[oper](n1,n2)
        print(F"{n1}{oper}{n2}={answer}")

        ask=input("Continue? [Y/N]").lower()

        if ask=="y": #თუ გააგრძელებს კალკულატორის გამოყენებას მიღებული პასუხი რომ გამოიყენოს შემდეგი ოპერაციისთვის
            n1=answer

        else:
            cont=False
            calculator()
calculator() #გამოვიძახოთ ფუნქცია


