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
    indx = range(len(countries))
    plt.bar(indx, mortgages)
    plt.xticks(indx, countries, fontsize=8)
    plt.show()

mortgages_per_country_plot(register, ["Spain", "Portugal", "France"])


def date_of_birth_balance_plot(register, year, Balance=18000, Gender="Male"):
    res = date_of_birth_balance(register, Balance, Gender)
    a = res.items()
    res =list(a)
    listt = [(r[0], r[1]) for r in res if r[0] in year]
    year=[t[0] for t in listt]
    perc=[t[1] for t in listt]
    title=f'Percentage of {Gender} people having more than {Balance}$ in their bank accounts'
    plt.title(title)
    indx = range(len(year))
    plt.bar(indx, perc)
    plt.xticks(indx, year, fontsize=8)
    plt.show()

date_of_birth_balance_plot(register, [1980, 1981,1982,1983, 1985])