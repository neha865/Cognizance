import pandas as pd
l1 = input("enter the string : ")
li = l1.split()
print("Sample input :")
print(li)
ser = pd.Series(li)
li = ser.str.capitalize()
print("Output : ")
for i in li :
    print(i,end = " ")
print()


