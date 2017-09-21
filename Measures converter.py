# -*- coding: utf-8 -*-
# Author: Ajda Pavčič

print "This program converts distances measured in kilometers to miles."
print "To start the Unit Converter please type the number next to the conversion you would like to perform."


while True:
    kilometers = int(raw_input ("Enter value (numbers only) in kilometers").replace(',',''))
    # conversion factor mile_value = 0.621371
    # calculate miles
    miles = kilometers * 0.621371
    print '%s kilometers is equal to %s miles' %( kilometers, miles)

else:
    print "This value is invalid please make sure that you entered it correctly."
