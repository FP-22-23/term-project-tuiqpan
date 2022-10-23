import csv
from collections import namedtuple
from datetime import datetime
from parsers import *

#Let BD as an abbreviation of "Bank Data"


BD = namedtuple("BD", "First_name,Last_name,Email,Address,Phone_Number,Date_Of_Birth,Balance,Credit_Card,Country_Code,Card_Type,Mortage")

def lector(file):
    with open(file, "r", encoding='utf-8')as f:
        lector = csv.reader(f)
        next(lector)
        register=[]

        for First_name,Last_name,Email,Address,Phone_Number,Date_Of_Birth,Balance,Credit_Card,Country_Code,Card_Type,Mortage in lector:
            res = BD(str(First_name), str(Last_name), str(Email), str(Address), str(Phone_Number),
                     datetime_parsing(Date_Of_Birth), balance_parsing(Balance), int(Credit_Card),str(Country_Code), str(Card_Type), bool(Mortage))

            register.append(res)

    return register


