#Strings are array
a= "KESHAV"
print(a[3])
#for Loop on strings
for x in 'banana':
    print(x, end=" ")

#lenght function on strings
print("\n",len(a))

#To check if a certain phrase or character is present in a string 
#we can use the keyword in.
#in keyword gives us boolean value true or false


txt="hello world welcome to python"
print("welcome" in  txt)
#if condition with in keyword
if "welcome" in txt:
    print("yes welcome is present in the txt variable")
#not in keyword
if "expensive" not in txt:
    print("yes expensive is not present in the txt variable")
#slicing strings
print(txt[2:5])
print(txt[:5])
print(txt[2:])
print(txt[-5:-2])
print(txt[-5:])
print(txt[:-2]) 
