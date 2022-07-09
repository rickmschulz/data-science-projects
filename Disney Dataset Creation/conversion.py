'''
TODO

Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value

money_conversion("$12.2 million") --> 12200000
money_conversion("$790,000") --> 790000

use test_money_conversion.py to test your solution
'''

from locale import atof, setlocale, LC_NUMERIC
import re


setlocale(LC_NUMERIC, 'en-US')


def word_to_value(word):
    value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
    return value_dict.get(word.lower(), 1)


def money_conversion(value):

    formatNumber = lambda n: n if n%1 else int(n)
    
    if value == None or value == 'unknown' or value == '':
        return None
    elif isinstance(value, list):
        if len(value) == 0:
            return None
        value = value[0]

    new_value = re.search(r'(?<=\$)\d+[\d\.\,]*', value)
    modifier = re.search(r"thousand|million|billion", value, flags=re.I)

    if new_value and modifier:
        return formatNumber(atof(new_value.group())*word_to_value(modifier.group()))
    elif new_value:
        return formatNumber(atof(new_value.group()))


money_conversion('$12.2 million')
