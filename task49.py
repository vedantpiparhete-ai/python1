import random

totalcredits = 10000
while True:
    print(f"Total Credits:{totalcredits}")

    # Get user inputs
    try:
        usernumber = int(input("Select any number(1-10): "))
        betcredit = int(input("Enter credit you want to bet: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    # Validate inputs
    if usernumber < 1 or usernumber > 10:
        print("Number must be between 1 and 10.")
        continue
    if betcredit > totalcredits or betcredit <= 0:
        print("Invalid bet amount.")
        continue

    # Generate random system number
    systemnumber = random.randint(1, 10)
    print(f"System Generated: {systemnumber}")

    # Check win/loss logic
    if usernumber == systemnumber:
        # Winning doubles the bet amount and adds it to total credits
        woncredits = betcredit * 2
        totalcredits += woncredits
        print(f"You won {woncredits} credits")
    else:
        # Losing subtracts the bet amount from total credits
        totalcredits -= betcredit
        print(f"You loose {betcredit} credits")

    print(f"Avl.Credits:{totalcredits}")

    # Check if player ran out of credits
    if totalcredits <= 0:
        print("You have run out of credits!")
        break

    # Ask to repeat
    playagain = input("Do you want to bet again(y/n): ")
    if playagain != 'y':
        print("Thank you for playing with us!!")
        break
