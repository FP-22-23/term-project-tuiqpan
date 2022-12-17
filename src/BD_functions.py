import csv
from collections import namedtuple, defaultdict, Counter
from matplotlib import pyplot as plt
from parsers import *


#Let BD as an abbreviation of "Bank Data"

Info = namedtuple("BD", "Position,Full_name,Gender,Date_Of_Birth,Email,Phone_Number,Country,Card_Type,Balance,Mortgage,Car_maker")

def reader(file):

    with open(file, encoding='utf-8')as f:
        reader = csv.reader(f)
        next(reader)
        res=[]

        for Position,Full_name,Gender,Date_Of_Birth,Email,Phone_Number,Country,Card_Type,Balance,Mortgage,Car_maker in reader:
            tuple = Info(int(Position),str(Full_name), str(Gender), datetime_parsing(Date_Of_Birth), str(Email), str(Phone_Number), str(Country),
            str(Card_Type), balance_parsing(Balance), bool_parsing(Mortgage), str(Car_maker))

            res.append(tuple)

    return res


    #^*··1st Block··*^

#1ST FUNCTION
def filter_by_country_and_mortgage(register, Country, Mortgage=True): 
    return [(r.Full_name) for r in register if r.Country==Country and r.Mortgage==Mortgage]

#2ND FUNCTION    
def different_countries(register):
    return sorted(set([r.Country for r in register]))

#3RD FUNCTION
def compute_average_balance_of_a_country(register, Country):
    res = [r.Balance for r in register if r.Country==Country]
    average = sum(res)/len(res)
    return "{:.2f}".format(average)


    #^*··2nd Block··*^

#4TH FUNCTION
def obtain_accounts_with_max_or_min_balance_of_a_country(register, Country, function):
    res = [r for r in register if r.Country==Country]
    max_min = function(res, key = lambda r:r.Balance)
    res_1 = [r for r in res if r.Balance == max_min.Balance]
    return res_1

#6TH FUNCTION
def obtain_descending_sorted_bank_account_balances(register, Country):
    res = [r for r in register if r.Country==Country]
    res.sort(key=lambda x:x.Balance, reverse=True)
    return res

#7TH FUNCTION
def credit_cards_of_countries(register):
    d = defaultdict(set)
    for r in register:
        d[r.Country].add(r.Card_Type)
    return d


    #^*··3rd Block··*^

#9TH FUNCTION
def mortgages_per_country(register):
    countries = [r.Country for r in register if r.Mortgage==True] 
    return Counter(countries)

#10TH FUNCTION
def most_popular_car_of_a_country(register, Country):
    car = [s.Car_maker for s in register if s.Country==Country]
    count = (Counter(car))

    a = [c for c in count.keys()]
    b = [d for d in count.values()]

    return (max((dict(zip(a, b))), key=(dict(zip(a, b))).get))

#13TH FUNCTION
def date_of_birth_balance(register, Balance, Gender):
    years = [r.Date_Of_Birth.year for r in register if r.Balance >= Balance and r.Gender == Gender]
    count =  Counter(years)

    a = [c for c in count]
    b = [ 100*d/len(register) for d in count.values()]

    dicc = dict(zip(a, b))

    sortedbykey= {k: v for k, v in sorted(dicc.items())}
    return sortedbykey

#14TH FUNCTION
def account_with_the_most_balance_of_each_country(register):
    Countries={r.Country for r in register}
    dicc={}
    for b in Countries:
        list=sorted(("Position:", n.Position, "Full name:", n.Full_name, "Balance:", n.Balance) for n in register if n.Country==b)
        dicc[b]=list[:1]
    
    sortedbykey= {k: v for k, v in sorted(dicc.items())}
    return sortedbykey
