from datetime import datetime
from re import sub

def datetime_parsing(string):
    return datetime.strptime(string,'%m/%d/%Y').date()

def balance_parsing(string):
    return float(sub(r'[^\d.]', '', string))

def bool_parsing(str):
    if str == 'true':
        res =True
    elif str == 'false':
        res=False
    return res

