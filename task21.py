code = int(input("Enter ticket type code: "))
match code:
    case 1:
        print('Issue Category: Billing Issue')
    case 2:
        print('Issue Category: Technical Issue')
    case 3:
        print('Issue Category: Account Issue')
    case 4:
        print('Issue Category: General Issue')
    case _:
        print('Invalid Code')