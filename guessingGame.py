import random

def numberGuessingGame():
    maxChoice = 3
    
    while True:  # Loop for replaying the game
        randomNum = random.randint(1, 10)
        remainingChoice = maxChoice
        
        while remainingChoice > 0:
            try:
                print(f"You have {remainingChoice} chances to guess the correct number.")
                userInput = int(input("Enter your guessed number (1-10): "))
                
                if userInput == randomNum:
                    print("Congratulations! You guessed the correct number.")
                    break
                elif userInput < randomNum:
                    print("Your guessed number is too low. Try again!")
                elif userInput > randomNum:
                    print("Your guessed number was too high. Try again!")

                remainingChoice -= 1
                if remainingChoice == 0:
                    print(f"You have no remaining chances, the correct number was {randomNum}.")
            
            except ValueError:
                print("Invalid input! Please enter a valid integer number.")
        
        # Ask the user if they want to play again
        answer = input("Would you like to play again? (Yes/No): ").strip().lower()
        if answer != "yes":
            print("Thank you for playing!")
            break  # Exit the game loop if the user doesn't want to play again

numberGuessingGame()

        

        

