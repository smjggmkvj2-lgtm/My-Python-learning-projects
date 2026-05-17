import random 
while True:
    start = input("Enter 1 for play or 2 for exit: ")
    if start == "1":
        num = random.randint(1, 50)
        difficulty = input("Choose your difficulty easy or hard: ")
        if difficulty == "easy":
            max_attempts = 10
        else: 
            max_attempts = 5
        attempts = 0
        while True:
            try:
                guess = int(input("Enter your number "))
            except ValueError:
                print("You should guess only with numbers")
                continue
            attempts = attempts + 1
            print("Attempts" , attempts)
            if guess == num:
                print("You won on " , attempts , "Attempts")
                break
            elif guess < num:
                    print("Bigger")
            elif guess > num:
                    print("Smaller")
            if attempts == max_attempts:
                print("Game over")    
                break
        print("The number was", num)
        again = input("Play again? yes / no: ")
        if again == "no":
            break
    elif start == "2":
        print("Goodbye")
        break
    else:
        print ("Wrong choice")