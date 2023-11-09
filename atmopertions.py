# program for atm operations
# file name is called module name
#program num 3

from atmexceptions import *
bal=500
def deposit():
    dmt=float(input('Enter amount to deposit:'))
    if (dmt<=0):
        raise DepositError
    else:
        global bal
        bal +=dmt
        print("ur account Acxxxxxxxx123 is deposited wth inr :{}".format(dmt))
        print("now ur account balance is :{}".format(bal))

def withdraw():
    global bal
    wmt=float(input("Enter the amount u want to want draw:"))
    if wmt<=0:
        raise WitdrawError
    elif((wmt+500)>bal):
        raise InsuffundError
    else:
        bal =bal-wmt
        print("Ur acc xxxxxxxxxx123 is debited with the amount of :{}".format(wmt))
        print("now ur balance is:{}".format(bal))
def balenquiry():
    print("Ur Acc balance is INR:{}".format(bal))
