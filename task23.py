choic = int(input("Enter your Choice: "))
match choic:
    case 1:
        print("Selected Transaction: Balance Enquiry")
    case 2:
        print("Selected Transaction: Cash Withdraw")
    case 3:
        print("Selected Transaction: Mini Statement")
    case 4:
        print("Selected Transaction: PIN Change")
    case _:
        print("Invalid Choice")