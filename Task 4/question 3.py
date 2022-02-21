list=[["Roll No","Name","Marks"]]
def add(list):
    while True:
        rollno=int(input("Enter the roll no. : "))
        name=input("Enter the name :")
        marks=float(input("Enter the Marks : "))
        l1=[rollno,name,marks]
        list.append(l1)
        c=input("Do uh want to continue y or n : ").lower()
        if c!='y':
            break
    return list
add(list)
#answer for subdivision 1
print()
print("Answer for subdivision i)")
for i in list:
    print ("{:<8} {:<15} {:<4}".format( i[0], i[1],i[2]))
#answer for subdivision 2
print()
print("Answer for subdivison ii)")
i=list[2]
print ("{:<8} {:<15} {:<4}".format( i[0], i[1],i[2]))
