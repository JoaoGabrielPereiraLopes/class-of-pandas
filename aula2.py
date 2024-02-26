import random
"""this line import the libary random for sort one item in list cidades
for sort one item in cidade I use the metod choise 
the metod choise return one random value in one compost variable"""

list1 = [1,2,3] #defining list1 to one list possessing the values 1,2 and 3
print(type(list1))#print type of list1
list2=[ [1,2,3], [4,5,6] , [7,8,9] ]#defining list1 to one list possessing the values [1,2,3],[4,5,6],[7,8,9] and each element within list2 are one list too 
print(type(list2))#print type list2
print(list1[0],list1[1],list1[2])#print all list in list2
for x in list2:#x received all value in list2
    result=''#definig result to one string empty
    for y in x:#y received all value in the lists in lista2
        result+=str(y)+' '#y and one space are add in y in the text form from result
    print(result)#print result
select=list2[1]#creat a one variable what recieved a list2 index one which have value equal [4,5,6]
print(select)#print select
citys=['Pequim','Los Angeles','Rio de Janeiro','Londres','Berlim','París']#defining citys to one list possessing the values Pequim,Los Angeles,Londrez,Berlim and París
choice= random.choice(citys)# return one ramdom value in citys
print(f"the city choise is: {choice}")#print choise
a=[1,2,3]#a recived type list witch the values 1,2 and 3
a.append(15)#add value 15 to list a
print(a)#print list a
b=[7,8,9]#b recived type list witch the values 7,8 and 9
for x in b:#x received all values in b
    a.append(x)#add the values of list b in list a
print(a)#print list a
while True:#freezes prompt
    pass