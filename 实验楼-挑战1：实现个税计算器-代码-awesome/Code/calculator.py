#!/usr/bin/env python3

from collections import namedtuple

TaxTableItem = namedtuple('TaxTableItem',['start_point', 'tax_rate', 'quick_subtractor'])

TAX_START_POINT = 3500

TAX_TABLE = [
    TaxTableItem(80000, 0.45, 13505),
    TaxTableItem(55000, 0.35, 5505),
    TaxTableItem(35000, 0.3, 2755),
    TaxTableItem(9000, 0.25, 1005),
    TaxTableItem(4500, 0.2, 555),
    TaxTableItem(1500, 0.1, 105),
    TaxTableItem(0, 0.03, 0)
]

def calc_tax(income):
    taxable = income - TAX_START_POINT
    if taxable <= 0:
        return '0.00'
    for item in TAX_TABLE:
        if taxable > item.start_point:
            tax = taxable * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax)

def main():
    import sys
    if len(sys.argv) != 2:
        print('Parameter Error')
    try:
        income = int(sys.argv[1])
    except ValueError:
        print('Parameter Error')

    print(calc_tax(income))


if __name__ == '__main__':
    main()      
