from BD_test_functions import *

def menu():
    print("Welcome, please choose an option:\n\n"
    "[0] Information of this database\n[1] Filter by country code and, whether the people of that country are paying "
    "a mortgage or not\n[2] Show different country "
    "codes\n[3] Compute the average balance of a given country\n[4] Obtain the account with the most/least balance in a "
    "given country\n[5] Obtain the descending bank account order depending on the balance of the accounts of a given country\n"
    "[6] Obtain the different types of card types in a given country")

def main():

    register = reader("./data/bank_account_sample.csv")

    menu ()

    option = int(input("Enter your option: "))
    
    if option==0:
        information(register)

    elif option==1:
        Country_Code = str(input("Please, enter a country code: "))
        Mortgage = bool(input("Please, enter 'False' or 'True': "))
        filter_by_country_code_and_card_type_test(register, Country_Code, Mortgage)

    elif option==2:
        different_country_codes_test(register)

    elif option==3:
        Country_Code = str(input("Please, enter a country code: "))
        compute_average_balance_of_a_country_test(register, Country_Code)

    elif option==4:
        Country_Code = str(input("Please, enter a country code: "))
        function = str(input("Would you like to obtain the account with the 'Most' or with the 'Least' balance of the given country: "))
        if function == "Most":
            function=max
        elif function == "Least":
            function=min

        obtain_accounts_with_max_or_min_balance_of_a_country_test(register, Country_Code, function)

    elif option==5:
        Country_Code = str(input("Please, enter a country code: "))
        obtain_descending_sorted_bank_account_balances_test(register, Country_Code)

    elif option==6:
        C_Code = str(input("Please, enter a country code: "))
        credit_cards_of_countries_test(register, C_Code)
    else:
        print("Invalid option, please try again")
       
if __name__=="__main__":
    main()