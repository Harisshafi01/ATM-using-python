while True:
    balance = 100000
    print("----------ATM----------")
    print("""
    1)  Balance
    2)  Withdraw
    3)  Deposit
    4)  Quit
    """)
    print("-----------------------")
    try:
        print("Enter 1, 2, 3, & 4 Only")
        option = int(input("Enter the OPtion: "))
    except Exception as e:
        print("Error:", e)
        continue
    if option ==1:
        print("Balance $",balance)
    if option == 2:
        print("Balance $",balance)
        Widthdraw=float (input("Enter Widthdraw amount $: "))
        if Widthdraw>balance:
            print("No funds in account")
        elif Widthdraw>0:
            NewBalance = (balance-Widthdraw)
            print("|---------------------|")
            print("New Balance $",NewBalance)
            print("|---------------------|")
        else:
            print("None widthdraw made")
    if option == 3:
        print("Balance $", balance)
        Deposit = float(input("Enter the deposit amount $:"))
        if Deposit>0:
            NewBalance = (balance + Deposit)
            print("|---------------------|")
            print("New Balance $",NewBalance)
            print("|---------------------|")

        else:
            print("None widhdraw")
    if option ==4:
        exit()
