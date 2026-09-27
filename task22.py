status = int(input("Enter order status codde: "))
match status:
    case 1:
        print("Order status: Order Placed")
    case 2:
        print("Order status: Preparing")
    case 3:
        print("Order status: Out for Delivery")
    case 4:
        print("Order status: Delivered")
    case _:
        print("Invalid Status")