from module1 import *

if __name__ == "__main__":
    register = lector("./data/bank_account_sample.csv")
    print(len(register)) #It will print the total amount of registers
    print(register[0:3]) #It will print the 3 first registers
    print(register[-3:-1]) #It will print the 3 last registers
   