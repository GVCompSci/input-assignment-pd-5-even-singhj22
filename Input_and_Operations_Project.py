'''
Created on Oct 1, 2018

@author: Jugat Singh

Input and Operations Project

Python Pd.5 even
'''
#Input statements

name=input('Please input your name:')

telephone_number=input('Please input your phone number:')

product=input('Please enter the name of the product you would like to purchase:')

price=float(input('Price of the item:'))

quantity=int(input('Quantity to Purchase:'))

#Display Information

print(name)
print(telephone_number)
print('Purchase Information:')
print(product, "\t", "Qty:", quantity, "\t", "Price:", price)
print('\n')

#Calculations

subtotal= price*quantity
tax=subtotal*0.06
total=subtotal+tax

#Display Calculations

print('Subtotal: $',subtotal,'\t', 'Tax: $', tax,'\t', 'Total: $', total )



#
