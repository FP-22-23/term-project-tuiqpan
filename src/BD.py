import csv
from collections import namedtuple, defaultdict
from datetime import datetime
from parsers import *

#Let BD as an abbreviation of "Bank Data"


Info = namedtuple("BD", "First_name,Last_name,Email,Address,Phone_Number,Date_Of_Birth,Balance,Credit_Card,Country_Code,Card_Type,Mortgage")

def reader(file):
    with open(file, encoding='utf-8')as f:
        reader = csv.reader(f)
        next(reader)
        res=[]

        for First_name,Last_name,Email,Address,Phone_Number,Date_Of_Birth,Balance,Credit_Card,Country_Code,Card_Type,Mortgage in reader:
            tuple = Info(str(First_name), str(Last_name), str(Email), str(Address), str(Phone_Number), datetime_parsing(Date_Of_Birth),
            balance_parsing(Balance), int(Credit_Card),str(Country_Code), str(Card_Type), bool_parsing(Mortgage))

            res.append(tuple)

    return res

#BLOCK I

def filter_by_country_code_and_card_type(register, Country_Code, Mortgage):
    return [(r.First_name, r.Last_name) for r in register if (r.Country_Code==Country_Code and r.Mortgage==Mortgage)]


def different_country_codes(register):
    return sorted(set([r.Country_Code for r in register]))


def compute_average_balance_of_a_country(register, Country_Code="US"):
    res = [r.Balance for r in register if r.Country_Code==Country_Code]
    average = sum(res)/len(res)
    return "{:.2f}".format(average)


#BLOCK II
register = reader("./data/bank_account_sample.csv")
def obtain_accounts_with_max_or_min_balance_of_a_country(register, Country_Code, function):
    res = [r for r in register if r.Country_Code==Country_Code]
    max_min = function(res, key = lambda r:r.Balance)
    res_1 = [r for r in res if r.Balance == max_min.Balance]
    return res_1

print(obtain_accounts_with_max_or_min_balance_of_a_country(register, function=min, Country_Code="US"))

def obtain_descending_sorted_bank_account_balances(register, Country_Code="FR"):

    res = [r for r in register if r.Country_Code==Country_Code]
    res.sort(key=lambda x:x.Balance, reverse=True)
    return res

def credit_cards_of_countries(register):
    d = defaultdict(set)
    for r in register:
        d[r.Country_Code].add(r.Card_Type)
    return d

