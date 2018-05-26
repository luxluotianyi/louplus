#!/usr/bin/env python3

import sys

returndata = {}
def calculate(*args):
    for arg in args:
        data = arg.split(":")
        ID = data[0]
        wages = data[1]

        try:
            ID = int(ID)
            wages = int(wages)
        except:
            print("Parameter Error")
        social = wages * 0.08 + wages * 0.02 + wages * 0.005 + wages * 0.06
        #social = format(social, '.2f')
        taxable = wages - social - 3500

        taxPayable = 0
        if taxable <= 0:
            taxPayable = format(0,'.2f')
        elif taxable <= 1500:
            taxPayable = format(taxable * 0.03 - 0, '.2f')
        elif taxable < 4500:
            taxPayable = format(taxable * 0.1 - 105, '.2f')
        elif taxable < 9000:
            taxPayable = format(taxable * 0.2 - 555, '.2f') 
        elif taxable < 35000:
            taxPayable = format(taxable * 0.25 - 1005, '.2f')
        elif taxable < 55000:
            taxPayable = format(taxable * 0.3 - 2755, '.2f')
        elif taxable < 80000:
            taxPayable = format(taxable * 0.35 - 5505, '.2f')
        elif taxable > 80000:
            taxPayable = format(taxable * 0.45 - 13505, '.2f')

        post_tax_wage =wages - float(taxPayable) - social

        
        returndata[ID] = post_tax_wage


    for key, value in returndata.items():
        print("{}:{:.2f}".format(key,value))
if __name__ == '__main__':
    args = sys.argv[1:]
    calculate(*args)



