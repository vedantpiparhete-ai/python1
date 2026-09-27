service = int(input("Enter Service code: "))
match service:
    case 1:
        print("Service Type: General Service")
    case 2:
        print("Service Type: Oil Change")
    case 3:
        print("Service Type: Engine Check")
    case 4:
        print("Service Type: Full Service")
    case _:
        print("Invalid Service Code")