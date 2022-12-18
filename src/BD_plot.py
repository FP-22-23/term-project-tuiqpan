from BD_test_functions import *

def mortgages_per_country_plot(register, country):
    res = mortgages_per_country(register)
    a = res.items()
    res  = list(a)
    listt = [(r[0], r[1]) for r in res if r[0] in country]
    countries=[t[0] for t in listt if t[0] in country]
    mortgages=[t[1] for t in listt]
    title='People paying mortgages in the given countries'
    plt.title(title)
    plt.pie(mortgages, labels = countries, autopct= "%2.1f%%")
    plt.show()


def date_of_birth_balance_plot(register, year, Balance=18000, Gender="Male"):
    res = date_of_birth_balance(register, Balance, Gender)
    a = res.items()
    res =list(a)
    listt = [(r[0], r[1]) for r in res if r[0] in year]
    year=[t[0] for t in listt]
    perc=[t[1] for t in listt]
    title=f'Percentage of {Gender} people having more than {Balance}$ in their bank accounts'
    plt.title(title)
    plt.plot(year, perc)
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.show()
    

def three_most_popular_cars_of_a_country_plot(register, Country):
    res = cars_of_a_country(register, Country)
    a = res.items()
    res =(list(a))
    res1 = res.sort(key=lambda i:i[1], reverse=True)
    res1 = res[0], res[1], res[2]
    listt = [(r[0], r[1]) for r in res1]
    car=[t[0] for t in listt]
    number=[t[1] for t in listt]
    title=f'3 most popular cars of {Country}'
    plt.title(title)
    indx = range(len(car))
    plt.bar(indx, number)
    plt.xticks(indx, car)
    plt.show()

date_of_birth_balance_plot(register, [1980,1981,1982,1983,1985])

mortgages_per_country_plot(register, ["Mexico", "Portugal", "France","Morocco", "Spain"])

three_most_popular_cars_of_a_country_plot(register, "China")

