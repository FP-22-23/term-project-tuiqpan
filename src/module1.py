import csv
from collections import namedtuple
from datetime import datetime
from parsers import *

#Let BD as an abbreviation of "Bank Data"


BD = namedtuple("BD", "First_name,Last_name,Email,Address,Phone_Number,Date_Of_Birth,Balance,Credit_Card,Has_More_Cards,Card_Type")

def lector(file):
    with open(file, "r", encoding='utf-8')as f:
        lector = csv.reader(f)
        next(lector)
        register=[]

        for First_name,Last_name,Email,Address,Phone_Number,Date_Of_Birth,Balance,Credit_Card,Has_More_Cards,Card_Type in lector:
            res = BD(str(First_name), str(Last_name), str(Email), str(Address), str(Phone_Number), datetime_parsing(Date_Of_Birth), balance_parsing(Balance), int(Credit_Card), bool(Has_More_Cards), str(Card_Type))

            register.append(res)

    return register

register = lector("./data/bank_account_sample.csv")

