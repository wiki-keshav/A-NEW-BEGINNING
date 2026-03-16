'''if we add f infront of a string and put variables and operations in placeholders{} 
then a variable can contain both string and numbers '''


price=6.35
txt=f"The price of banana is {price} rupees"
print(txt)


#we can also perform operations in the placeholders
#A placeholder can include a modifier to format the value.


quantity=12
txt2=f"The price of {quantity} bananas is {quantity * price:.2f} rupees"
print(txt2)


