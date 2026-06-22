dict={1:"Stone", 2:"Paper", 3:"Scissors"}
import random
def computer():
    Computer=random.randint(1, 3)
    return Computer

def game():
    print("Welcome to the Stone-Paper-Scissors Game!")
    print("Enter your choice: ")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    you=int(input("Your choice: "))
    Computer=computer()
    print(f"Computer's choice: {dict[Computer]}  and   Your choice: {dict[you]}")
    if Computer==you:
            print("It's a tie!")
    elif (you==1 and Computer==2):
        print("Computer wins.")
    elif (you==1 and Computer==3):
        print("You win!")
    elif (you==2 and Computer==1):
        print("You win!")  
    elif (you==2 and Computer==3):
        print("Computer wins.")
    elif (you==3 and Computer==1):
        print("Computer wins.")
    elif (you==3 and Computer==2):
        print("You win!")
game()  
