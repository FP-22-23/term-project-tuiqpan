from BD_functions import *
register = reader("./data/bank_account_sample.csv")

#First Delivery

def information(register):
    print('The total number of registers is: {}'.format(len(register)))
    print('The first 3 registers are:\n {}'.format(register[:3]))
    print('The last 3 register are:\n {}'.format(register[-3:]))
    
#Second Delivery

    #^*··1st Block··*^

def filter_by_country_and_mortgage_test(register, Country, Mortgage):
    res = filter_by_country_and_mortgage(register, Country, Mortgage)
    print("The total ammount of people paying/not paying a mortage in the given country is {}, and they are:\n {}".format(len(res), res))


def different_countries_test(register):
    res = different_countries(register)
    print("The different countries that we can find in our database are:\n", res)


def compute_average_balance_of_a_country_test(register, Country):
    res = compute_average_balance_of_a_country(register, Country)
    print("The average balance of the country is {}".format(res))
    
    #^*··2nd Block··*^

def obtain_accounts_with_max_or_min_balance_of_a_country_test(register, Country, function):
    res = obtain_accounts_with_max_or_min_balance_of_a_country(register, Country, function)   

    if function==min:
        print("The account with the least balance in the given country is:\n", res)
    
    elif function==max:
        print("The bank account with the most balance in the given country is:\n", res)
    

def obtain_descending_sorted_bank_account_balances_test(register, Country):
    res = obtain_descending_sorted_bank_account_balances(register, Country)
    print("The descending bank account order with depending on the balance of the accounts of the given country is:\n", res)


def credit_cards_of_countries_test(register, C_Code):
    index = credit_cards_of_countries(register)
    for Country in [C_Code]:
        print(f"The given country is {Country}, where we can find {len(index[Country])} different card types: \n{', '.join(sorted(index[Country]))}")

    #^*··3rd Block··*^

def mortgages_per_country_test(register):
    res = mortgages_per_country(register)
    print("Number of mortgages that are being payed in each country:\n")
    for country, number in sorted(res.items(), key=lambda kv:kv[1], reverse=True):
        print("{}: {}".format(country, number))


def most_popular_car_of_a_country_test(register, Country="Spain"):
    res = most_popular_car_of_a_country(register, Country)
    print("The most popular car in the specified country is:",res)


def date_of_birth_balance_test(register, Balance, Gender="Male"):
    res = date_of_birth_balance(register, Balance, Gender="Male")
    print(f"Percentaje of {Gender}s persons in each date of birth having more than ${Balance}in their bank account:\n")
    for n in res:
        print("{}: {:.2f}%".format(n, res[n]))


def account_with_the_most_balance_of_each_country_test(register):
    res=account_with_the_most_balance_of_each_country(register)
    print("The accounts with the most balance in their banks (with their respective balance) of each country are:\n")

    for k in res:
        print(f"{k}: {res[k]}")


#DELETE THE COMMENTS TO INVOKE ALL THE TEST FUNCTIONS AT THE SAME TIME


"""
#1
information(register)
print("\n")

#2
filter_by_country_and_mortgage_test(register, "China", False)
print("\n")

#3
different_countries_test(register)
print("\n")

#4
compute_average_balance_of_a_country_test(register, "Spain")
print("\n")

#5
obtain_accounts_with_max_or_min_balance_of_a_country_test(register, "Indonesia", max)
print("\n")

#6
obtain_descending_sorted_bank_account_balances_test(register, "Peru")
print("\n")

#7
credit_cards_of_countries_test(register, "France")
print("\n")

#8
mortgages_per_country_test(register)
print("\n")

#9
most_popular_car_of_a_country_test(register, Country="Spain")
print("\n")

#10
date_of_birth_balance_test(register, 180000)
print("\n")

#11
account_with_the_most_balance_of_each_country_test(register)
print("\n")

"""