#Q1:List and its default Functions

# L1=["Bannana", "Apple","Orange","Grapes"]
# print(L1[2])
# print(L1[-1])
# print(L1[1:4])
# print(L1.append("Gava"))
# print(L1)
# L1.remove("Gava")
# print(L1)
# print(len(L1))
# L2=L1.copy()
# print(L2)

#Q2: Dic and its default functions:

dict1={1:"Dhiraj",2:"Ram",3:"Sham"}
print(dict1.items())
print(dict1.keys())
print(dict1[2])
dict1.pop(3)
print(dict1)
dict1[3]="Sham"
print(dict1)
print(dict1.get(1))

#Q3: Sets and its default function:

d={2,7,3,7,5}
print(d) #Sorted and uniques value
d.add(8)
print(d)
d1={2,7}
print(d1.issubset(d))


#Q4 Tuple and its defaukt functions:

T=(1,2,4,2)
print(T)
print(T.count(2))
print(T.index(4))

#Q5: Strings

Name1="Dhiraj"
Name2="Bhasme"
Name3=411014
Name4="Eon"

print(Name1+" "+ Name2+" "+ str(Name3)) #"+" concat two strings
print(Name1+" "+Name2+ "\nPune")
print(Name1+Name2+"\"Pune")