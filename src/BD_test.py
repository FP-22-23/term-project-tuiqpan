from BD_test_functions import *
import colorama
from colorama import Fore, Back, Style

def menu():
    print(Fore.WHITE + "Please choose an option:\n\n" + Fore.MAGENTA +
    "[0] Exit\n[1] Information of this database\n[2] Filter by country and, whether the people of that country are paying "
    "a mortgage or not\n[3] Show different countries"
    "\n[4] Compute the average balance of a given country\n[5] Obtain the account with the most/least balance in a "
    "given country\n[6] Obtain the descending bank account order depending on the balance of the accounts of a given country\n"
    "[7] Obtain the different types of card types in a given country\n[8] Compute the number of people paying a mortgage\n"
    "[9] Obtain the most popular car of a country\n[10] Obtain the percentage of people of a selected gender of each date of birth"
    "(over the total amount of registers) having a bigger amount of balance in their accounts than a given one\n[11] Obtain the account of each country with the"
    " most balance with their respective balance")

def main():

    register = reader("./data/bank_account_sample.csv")

    menu ()

    option = int(input(Fore.WHITE + "\nEnter your option: "))
    
    while option != 0:

        print()

        if option == 0:
            break

        elif option==1:
            information(register)

        elif option==2:
            Country_Code = str(input("Please, enter a country:\n"))
            Mortgage = bool(input("Please, enter 'False' or 'True':\n"))
            filter_by_country_and_mortgage_test(register, Country_Code, Mortgage)

        elif option==3:
            different_countries_test(register)

        elif option==4:
            Country_Code = str(input("Please, enter a country:\n"))
            compute_average_balance_of_a_country_test(register, Country_Code)

        elif option==5:
            Country_Code = str(input("Please, enter a country:\n"))
            function = str(input("Would you like to obtain the account with the 'Most' or with the 'Least' balance of the given country:\n"))
            if function == "Most":
                function=max
            elif function == "Least":
                function=min

            obtain_accounts_with_max_or_min_balance_of_a_country_test(register, Country_Code, function)

        elif option==6:
            C_Code = str(input("Please, enter a country:\n"))
            obtain_descending_sorted_bank_account_balances_test(register, Country_Code)

        elif option==7:
            C_Code = str(input("Please, enter a country:\n"))
            credit_cards_of_countries_test(register, C_Code)

        elif option==8:
            mortgages_per_country_test(register)
        
        elif option==9:
            Country = str(input("Please, enter a country:\n"))
            most_popular_car_of_a_country_test(register, Country)

        elif option==10:
            Balance = float(input("Please, enter a quantity:\n"))
            Gender = str(input("Please, enter a gender:\n"))
            date_of_birth_balance_test(register, Balance, Gender)

        elif option==11:
            account_with_the_most_balance_of_each_country_test(register)
        else:
            print("Invalid option, please try again")
        print()
        menu()
        option = int(input(Fore.WHITE + "\nEnter your option: "))

if __name__=="__main__":
    main()
