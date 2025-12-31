def deposit():
    while True:
        amount = input("Enter the amoun to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be bigger than 0")
        else:
            print("Amount must be a number")
        
    return amount


        
