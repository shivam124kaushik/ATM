def creditamount(balance):
    amt_cre = int(input("Enter the amount to be credited: "))
    balance += amt_cre 
    print(f"Amount credited. Updated balance is {balance}")
    return balance

def debitamount(balance):
    amt_deb = int(input("Enter the amount to be debited: "))
    if (amt_deb < balance):
        balance -= amt_deb
        print("insufficient funds")
    else:
        print(f"Amount debited. Updated balance is {balance}")
    return balance

while True:   
    with open("shivampin.txt") as f:
        shivampin = f.read()
        a=int(shivampin)
    
    with open("amitpin.txt") as f:
        amitpin = f.read()
        b=int(amitpin)

    with open("shivam_balance.txt") as f:
        shivam_balance = f.read()
        c=int(shivam_balance)


    with open("amit_balance.txt") as f:
        amit_balance = f.read()
        d=int(amit_balance)

    with open("shivam_bankname.txt") as f:
        shivam_bankname = f.read()
        e=str(shivam_bankname)
    
    with open("amit_bankname.txt") as f:
        amit_bankname = f.read()
        f=str(amit_bankname)
        
    pin = int(input("enter your pin"))
    if pin == a:
        while True:
            print(f"welcome shivam")
            print('''Choose an option -
                                  1 - BALANCE
                                  2 - BANK NAME
                                  3 - CREDIT
                                  4 - DEBIT
                                  5 - change pin
                                  6 - EXIT''')
            choice = int(input("Choose option : 1,2,3,4,5,6 :"))
            
            if choice == 1:
                print(f"your bank balance is:{c}")
                    
            elif choice == 2:
                print(f"your bank name is: {shivam_bankname}")
                    
            elif choice == 3:
                shivam_balance = creditamount(c)
                print(shivam_balance)
                sb=str(shivam_balance)
                with open("shivam_balance.txt","w") as f:
                    f.write(sb)
                    # print(f"your credit amount is:{sb}")
                    
            elif choice == 4:
                shivam_balance = debitamount(c)
                print(shivam_balance)
                sb=str(shivam_balance)
                with open("shivam_balance.txt","w") as f:
                    f.write(sb)
                    # print(f"your debited amount is :{shivam_balance}")
    
            elif choice == 5:
                shivam_pin=int(input("enter a new pin : "))
                print("pin change sucessfully")
                shivampin=str(shivam_pin)
                with open("shivampin.txt","w") as f:
                    f.write(shivampin)
                    break
                     
            elif choice == 6:
                print(f"exiting....")
                break
            else:
                print("invalid choice")
                
    elif pin == b:
        while True:
            print(f"welcome amit")
        
            print('''Choose an option -
                          1 - BALANCE
                          2 - BANK NAME
                          3 - CREDIT
                          4 - DEBIT
                          5 - change pin
                          6 - EXIT''')
            choice = int(input("Choose option : 1,2,3,4,5,6 :"))
            
            if choice == 1:
                print(f"your bank balance is:{amit_balance}")
                    
            elif choice == 2:
                print(f"your bank name is: {amit_bankname}")
                 # ab= amit balance 
                
            elif choice == 3:
                amit_balance = creditamount(d)
                print(amit_balance)
                ab=str(amit_balance)
                with open("amit_balance.txt","w") as f:
                    f.write(ab)
                    
            elif choice == 4:
                amit_balance = debitamount(d)
                print(amit_balance)
                ab=str(amit_balance)
                with open("amit_balance.txt","w") as f:
                    f.write(ab)
    
            elif choice == 5:
                amit_pin=int(input("enter a new pin : "))
                print("pin change sucessfully")
                amitpin=str(amit_pin)
                with open("amitpin.txt","w") as f:
                    f.write(amitpin)
                    break
                    
            elif choice == 6:
                print(f"exiting....")
                break
                
            else:
                print("invalid choice")
                
    else:
        print("invalid pin")