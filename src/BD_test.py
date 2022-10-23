from BD import *


def lector_test(file):
    register = lector(file)
    print("The total number of registers is: ", len(register)) #It will print the total amount of registers
    print("The first 3 register are: ",register[:3]) #It will print the 3 first registers
    print("The last 3 registers are: ",register[-3:]) #It will print the 3 last registers

lector_test("./data/bank_account_sample.csv")