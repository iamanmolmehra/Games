print("WELCOME TO SBI BANK\n")
print('Please Insert Your Card ')
print('''
    1.Hindi
    2.English
    ''')
a=input("Please Choose Your Language : ")
print('''
1.Current Account
2.Saving Account
''')
am=20000
a=int(input("Enter Which Account : "))
print("\nCurrent Account\n") if a==1 else print("\nSaving Account\n")
pin_number=int(input("Enter Your Pin : "))
if pin_number==1234:
    print('\nWhat You Want To Do ?')
    print('''
1.Balance Enquiry
2.Withdraw Cash
3.Deposit
4.Statement
5.Exit''')
    i=1
    while i>0: 
        z=int(input('\nEnter What You Want To Do ? '))
        if z==1: print(f"\n{am}")
        elif z==2:
            amount=int(input("\nEnter an amount: "))
            print("\nTransaction Successfully")
            am-=amount
        elif z==3: 
            print("\nEnter Your deposit amount : ") 
            amount=int(input("\nEnter Your Amount : ")) 
            am+=amount
        elif z==4: print("\nPrint your statement")
        elif z==5: print("\nThanks for coming") 
        break
        x=input('\nWant to do something more?')   
        if x=='y' or x=='Y': i+=1
        else: break      
    else: print("\nWrong Pin, Please check and Insert correctly again ")
