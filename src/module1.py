import csv
from collections import namedtuple
from datetime import date

#Let BD as an abbreviation of "Bank Data", and DOB as an abbreviation of "Date Of Birth"

BD = namedtuple("BD", "First_name,Last_name,Email,Address,Phone_Number,DOB,Balance,Credit_Card,Country_is_urban,Card_Type")

def lector(file):
    with open(file, "r", encoding='utf-8')as f:
        lector = csv.reader(f)
        next(lector)
        register=[]

        for First_name,Last_name,Email,Address,Phone_Number,DOB,Balance,Credit_Card,Country_is_urban,Card_Type in lector:
            res = BD(str(First_name), str(Last_name), str(Email), str(Address), str(Phone_Number), date(DOB), float(Balance), str(Credit_Card), bool(Country_is_urban), str(Card_Type))

            register.append(res)

    return register