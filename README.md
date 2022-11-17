# FIrst proyect of the first semester - Progamming Fundamentals
Autor/a: IONEL TUDOR CRISTIAN LACATUS   uvus:HPD8118

This proyect was created in order to analyze many bank accounts owners data, data which can be found in the following Kaggle link "https://www.kaggle.com/datasets/imranjanihindi78/bank-account". The original dataset has 10 columns, but there is not any bool class in any of them, so a "Mortgage" column was added in order to represent if the owner of their bank account is paying a mortage. This bool column was randomly generated using the website "https://mockaroo.com/". Also, it is important to mark that we will use `BD` as an abbreviation of Bank Data.

## Structure of the folders of the proyect

* **/src**: Contains the different modules of this proyect using Python.
  * **BD_functions.py**: Contains useful functions for the Data Analysis of different bank accounts in a database.
  * **BD_test_functions.py**: Contains functions to test the `BD_functions.py`functions.
  * **BD_test.py**: Contains functions to test the `BD_test_functions.py`functions.
  * **parsers.py**: Contains functions for data parsing.
* **/data**: Contains the dataset of the proyect.
    * **bank_account_sample**: File with the bank accounts owners data.
    
## Structure of the *dataset*

In our dataset we can find 878 rows, each row represents different global accounts with their respective owners data, and if they are currently paying a mortgage. For each row there are 11 types of data, then, the dataset is made of 11 columns, with the following description: 


* **First_name**: Of type str, it is the first name of the bank account owner.
* **Last_name**: Of type str, it is the last name of the bank account owner.
* **Email**: Of type str, it is the email of the bank account owner.
* **Address**: Of type str, it is the address of the bank account owner.
* **Phone_Number**: Of type str, it is the phone number of the bank account owner.
* **Date_Of_Birth**: Of type date, it is the date birth of the bank account owner.
* **Balance**: Of type float, it is the available balance in the bank account.
* **Credit_Card**: Of type int, it is the credit card number.
* **Country_Code**: Of type str, it represents the country using an abbreviation.
* **Card_Type**: Of type str, it is the card type.
* **Mortgage**: Of type boolean, it represent if the bank owner is paying a mortage.

## Implemented types

To analyse the data of the dateset, we have defined the following named tuple:

`BD = namedtuple("BD","First_name,Last_name,Email,Address,Phone_Number,Date_Of_Birth,Balance,Credit_Card,Country_Code,Card_Type,Mortage")`

And the classes are:

`BD(str(First_name), str(Last_name), str(Email), str(Address), str(Phone_Number),datetime_parsing(Date_Of_Birth), balance_parsing(Balance), int(Credit_Card),str(Country_Code), str(Card_Type), bool_parsing(Mortage))`



## Implemented functions
For the moment we have implemented the following modules:

### BD.py
The functions that that we can find in this module are used to get the different data of the different bank accounts in the database

* **lector(file)**: This function reads the data of the CSV file, and it returns a list of tuple with the data of CSV file
* **filter_by_country_code_and_card_type(register, Country_Code, Mortgage)**: This function filters the bank accounts by two conditions, whether they are paying a mortgage or not, and a given country
* **different_country_codes(register)**: This function shows all the country codes that appear in the database
* **compute_average_balance_of_a_country(register, Country_Code)**: This function computes the average balance from the different bank accounts of a given country
* **obtain_accounts_with_max_or_min_balance_of_a_country(register, Country_Code, function)**: This function obatin the bank account with the most or with the least balance of a given country
* **obtain_descending_sorted_bank_account_balances(register, Country_Code)**: This function obtains a descending sorted list depending on the balance from the different bank accounts from a given country
* **credit_cards_of_countries(register)**: This function obtain the amount of different card types that we can find in a given country, and their names


### BD_test_functions.py
In this proyect, we have defined the following test function that test the functions in the BD.py module, each test function will have the same name as the main function adding `_test`.

* **information(register))**: This function shows some information of the register.
* **filter_by_country_code_and_card_type_test(register, Country_Code, Mortgage)**:This function tests the function 'filter_by_country_code_and_card_type'
* **different_country_codes_test(register)**: This function tests the function 'different_country_codes'
* **compute_average_balance_of_a_country_test(register, Country_Code)**: This function tests the function 'compute_average_balance_of_a_country'
* **obtain_accounts_with_max_or_min_balance_of_a_country_test(register, Country_Code, function)**: This function tests the function 'obtain_accounts_with_max_or_min_balance_of_a_country'
* **obtain_descending_sorted_bank_account_balances_test(register, Country_Code)**: This function tests the function 'obtain_descending_sorted_bank_account_balances'
* **credit_cards_of_countries_test(register)**: This function tests the function 'credit_cards_of_countries'

### BD_test.py
This module simply shows the results of the 'BD_test_functions' module, using a menu to choose between different options

* **menu()**: This function displays the option menu with the different options that could be chosen
* **main()**: This function displays the data of the option that has been chosen

### Parsers
This module has the following parsing data functions:

* **datetime_parsing(string)**: Given a string with format `%m/%d/%Y`, it returns an object of type date with the date that appears in the string.
* **balance_parsing(string)**: Given a string with format `$______`, it returns an object of type float with the balance that appears in the string.
* **bool_parsing(string)**: Given a string `true` or `false`, it returns an object of type bool.
