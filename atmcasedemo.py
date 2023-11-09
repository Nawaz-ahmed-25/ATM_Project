#program for atm use case demo
# importing 3 module or file names from same folder where current file is residing
#that is :
from atmmenu import menu
from atmexceptions import *
from atmopertions import *
import sys

while True:
    menu()
    try:
        ch= int(input("enter ur choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("dont enter alnums,strs, symbols for deposit amount")
                except DepositError:
                    print('dont deposit -ve amount and 0s amount')

            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("dont enter alnums,strs, symbols for deposit amount")
                except WitdrawError:
                    print("dont try to withdraw -ve and 0s amount")
                except InsuffundError:
                    print('Ur account dont have enough suffice fund ')
            case 3:
                balenquiry()
            case 4:
                print("Thanx for using this program")
                sys.exit()
            case _:
                print("ur selection of operation is wrong try again")
    except ValueError:
                    print("Dont enter strs alnums and symbols For choice")