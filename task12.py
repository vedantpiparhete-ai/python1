balance = float(input("Enter Balance: "))
withdraw = float(input("Enter Withdraw amount: "))
if withdraw <= balance:
    print('Transaction successful')
else:
    print('Insufficient funds')