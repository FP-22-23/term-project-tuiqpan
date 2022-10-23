# FIrst proyect of the first semester - Progamming Fundamentals
Autor/a: IONEL TUDOR CRISTIAN LACATUS   uvus:HPD8118

This proyect was created in order to analyze many bank accounts owners data, data which can be found in the following Kaggle link "https://www.kaggle.com/datasets/imranjanihindi78/bank-account". The original dataset has 10 columns, but there is not any bool class in any of them, so a "Mortage" column was added in order to represent if the owner of their bank account is paying a mortage. This bool column was randomly generated using the website "https://mockaroo.com/". Also, it is important to know that we will use `BD` as an abbreviation of Bank Data.

## Structure of the folders of the proyect

* **/src**: Contains the different modules of this proyect using Python.
  * **BD.py**: Contains useful functions for the Data Analysis of different bank accounts.
  * **BD_test.py**: Contains functionts to test the `poverty.py`functions.
  * **parsers.py**: Contains functions for data parsing.
* **/data**: Contains the dataset of the proyect.
    * **bank_account_sample**: File with the bank accounts owners data.
    
## Structure of the *dataset*

In our dataset we can find 878 rows, each row represents different global accounts with their respective owners data, and if they are currently paying a mortage. For each row there are 11 types of data, then, the dataset is made of 11 columns, with the following description: 


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
* **Mortage**: Of type boolean, it represent if the bank owner is paying a mortage.

## Implemented types

To analyse the data of the dateset, we have defined the following named tuple:

`BD = namedtuple("BD","First_name,Last_name,Email,Address,Phone_Number,
Date_Of_Birth,Balance,Credit_Card,Country_Code,Card_Type,Mortage")`

And the classes are:

`BD(str(First_name), str(Last_name), str(Email), str(Address), str(Phone_Number),datetime_parsing(Date_Of_Birth), balance_parsing(Balance), int(Credit_Card),str(Country_Code), str(Card_Type), bool(Mortage))`



## Implemented functions
For the moment we have implemented the following modules:

### BD.py

* **lector(file)**: This function reads the data of the CSV file, and it returns a list of tuple with the data of CSV file.


### BD_test.py
In this proyect, we have defined the following test function that test the functions in the BD.py module, each test function will have the same name as the main function adding `_test`.

* **lector_test(file)**: This function tests the lector function in the BD.py module.

### Parsers
This module has the following parsing data functions:

* **datetime_parsing(string)**: Given a string with format `%m/%d/%Y`, it returns an object of type date with the date that appears in the string.
* **balance_parsing(string)**: Given a string with format `$______`, it returns an object of type float with the balance that appears in the string.
