Dict = {'kavi': {'password': [8123],
                 'balance': [5000]
                },
        'Divi' :{'password': [8123],
                 'balance': [5000]
                 }
        }
name = input('Enter the name: ')
for i in Dict:
    if i == name:

        chance = 3
        while chance>0:
            code = int(input("Enter the password "))
            pas = Dict[name]['password'][-1]
            if code == pas:
                print("press 1 for checking balance")
                print("press 2 for withdrawal")
                print("press 3 to change Password")

                option = int(input("enter the option:"))
                bal = Dict[name]['balance'][-1]
                if option == 1:
                    print('your current bal is: ',bal)
                    break
                if option == 2:
                    Withdraw = int(input('enter amount to withdraw'))
                    if (Withdraw > bal):
                        print('Insufficient balance')
                        break
                    balance = bal - Withdraw
                    Dict[name] = ['balance'].append(bal)
                    print("Available balance : ",balance)
                    break
                if option == 3:
                    NewPass = input("Enter new password: ")
                    if (len(NewPass) < 4 ):
                        print("password must be 4 digit")
                        break
                    if (pas == NewPass):
                        print("entered password is same as old password")
                        break
                    ConfirmPass = input("Re-enter password: ")
                    if (ConfirmPass == NewPass):
                        pas = NewPass
                        print("Password changed Succesfully")
                    else:
                        print("Mismatch in password")
                        break
            else:
                chance -= 1
                if (chance == 0):
                    raise AssertionError("Account blocked")


for i in Dict:
    print(Dict[name]['balance'])









