# FIrst proyect of the first semester - Progamming Fundamentals

This proyect was created in order to analyze many bank accounts owners data, at first the dataset that we first used can be found in the following Kaggle link "https://www.kaggle.com/datasets/imranjanihindi78/bank-account", but this data set was not interesting at all, as we can find in it some irrelevant information as the credit number of the owner. Also the information of this dataset was not very credible at all.

A new dataset inspired in the kaggle dataset was created, removing some irrelevant information, an adding more relevant information (as the car make of the owner, whether the owner is paying or not a mortgage...), so we could preserve the idea of the data set, making a new one more interesting.

Creating a new dataset was possible thanks to "https://mockaroo.com/", a very useful dataset generator.

Also, it is important to mark that we will use `BD` as an abbreviation of Bank Data.

## Structure of the folders of the proyect

* **/src**: Contains the different modules of this proyect using Python.
  * **BD_functions.py**: Contains useful functions for the Data Analysis of different bank accounts in a database.
  * **BD_test_functions.py**: Contains functions to test the `BD_functions.py`functions.
  * **BD_test.py**: Contains functions to test the `BD_test_functions.py`functions.
  * **BD_plot.py**: Contains functions to plot some `BD_functions.py`functions.
  * **parsers.py**: Contains functions for data parsing.
* **/data**: Contains the dataset of the proyect.
    * **bank_account_sample**: File with the bank accounts owners data.
    
## Structure of the *dataset*

In our dataset we can find 977 rows, each row represents different global accounts with their respective owners data, For each row there are 11 types of data, then, the dataset is made of 9 columns, with the following description: 


* **Position**: Of type int, it is the the position in the dataset of the bank account owner.
* **Full_name**: Of type str, it is the full name of the bank account owner.
* **Gender**: Of type str, it is the the gender of the bank account owner.
* **Date_Of_Birth**: Of type date, it is the date birth of the bank account owner.
* **Country**: Of type str, it is the country where the bank account owner is currently living.
* **Card_Type**: Of type str, it is the card type.
* **Balance**: Of type float, it is the available balance in the bank account.
* **Mortgage**: Of type boolean, it represent if the bank owner is paying a mortage.
* **Car_maker**: Of type str, it is the car make that has the bank account owner(if it is empty, then the bank account owner does not have a car).

## Implemented types

To analyse the data of the dateset, we have defined the following named tuple:

`Info = namedtuple("BD", "Position,Full_name,Gender,Date_Of_Birth,Country,Card_Type,Balance,Mortgage,Car_maker")`

And the classes are:

`Info(int(Position),str(Full_name), str(Gender), datetime_parsing(Date_Of_Birth), str(Country), str(Card_Type), balance_parsing(Balance), bool_parsing(Mortgage), str(Car_maker)))`



## Implemented functions
We have implemented the following modules:

### BD.py
The functions that that we can find in this module are used to get the different data of the different bank accounts in the database

* **reader(file)**: This function reads the data of the CSV file, and it returns a list of tuple with the data of CSV file
* **filter_by_country_and_mortgage(register, Country, Mortgage)**: This function filters the bank accounts by two conditions, whether they are paying a mortgage or not, and a given country
* **different_countries(register)**: This function shows all the countries that appear in the database
* **compute_average_balance_of_a_country(register, Country)**: This function computes the average balance from the different bank accounts of a given country
* **obtain_accounts_with_max_or_min_balance_of_a_country(register, Country, function)**: This function obatin the bank account with the most or with the least balance of a given country
* **obtain_descending_sorted_bank_account_balances(register, Country)**: This function obtains a descending sorted list depending on the balance from the different bank accounts from a given country
* **credit_cards_of_countries(register)**: This function obtain the amount of different card types that we can find in a given country, and their names
* **mortgages_per_country(register)**: This function obtains the quantity of mortgages that are being payed in each country
* **most_popular_car_of_a_country(register, Country)**: This function obtains the most popular car of a given country
* **date_of_birth_balance(register, Balance, Gender)**: This function returns a dictionary the percentage of people of a specified gender that have more than a given balance
* **account_with_the_most_balance_of_each_country(register)**: This function obtains a dictionary with the accounts with the most balance of each countries
* **cars_of_a_country(register, Country)**: This function counts the total number of different cars in a country


### BD_test_functions.py
In this proyect, we have defined the following test function that test the functions in the BD.py module, each test function will have the same name as the main function adding `_test`.

* **information(register))**: This function shows some information of the register.
* **filter_by_country_and_mortgage_test(register, Country, Mortgage)**:This function tests the function 'filter_by_country_and_mortgage'
* **different_countries_test(register)**: This function tests the function 'different_countries'
* **compute_average_balance_of_a_country_test(register, Country)**: This function tests the function 'compute_average_balance_of_a_country'
* **obtain_accounts_with_max_or_min_balance_of_a_country_test(register, Country, function)**: This function tests the function 'obtain_accounts_with_max_or_min_balance_of_a_country'
* **obtain_descending_sorted_bank_account_balances_test(register, Country)**: This function tests the function 'obtain_descending_sorted_bank_account_balances'
* **credit_cards_of_countries_test(register, C_Code)**: This function tests the function 'credit_cards_of_countries'
* **mortgages_per_country_test(register)**: This function tests the function 'mortgages_per_country'
* **most_popular_car_of_a_country_test(register, Country)**: This function tests the function 'most_popular_car_of_a_country'
* **date_of_birth_balance_test(register, Balance, Gender)**: This function tests the function 'date_of_birth_balance'
* **account_with_the_most_balance_of_each_country_test(register)**: This function tests the function 'account_with_the_most_balance_of_each_country'




### BD_test.py
This module simply shows the results of the 'BD_test_functions' module, using a menu to choose between different options

* **menu()**: This function displays the option menu with the different options that could be chosen
* **main()**: This function displays the data of the option that has been chosen

### BD_plot.py
This module plots some interesting functions of BD.py

* **mortgages_per_country_plot(register, country)**: This function plots the information of some given countries from the 'mortgages_per_country' function
* **date_of_birth_balance_plot(register, year, Balance, Gender)**: This function displays the data of some given dates of birth from the 'date_of_birth_balance' function
* **three_most_popular_cars_of_a_country_plot(register, Country)**: This function displays the data of some given dates of birth from the 'cars_of_a_country' function

### Parsers
This module has the following parsing data functions:

* **datetime_parsing(string)**: Given a string with format `%m/%d/%Y`, it returns an object of type date with the date that appears in the string.
* **balance_parsing(string)**: Given a string with format `$______`, it returns an object of type float with the balance that appears in the string.
* **bool_parsing(string)**: Given a string `true` or `false`, it returns an object of type boolean.
