#in this code my objetive is study the properties of tuple and list in python

tuple=(2,4,7)#this is one variable(invariable and compost) content two,four and seven
firt=tuple[0]#this is one variable content firt index for tuple
#this prove that the tuple index is acessable

list=[2,4,7]#this is one variable(variable and compost) receiving two,four and seven
firt=list[0]#this is one variable content firt index for list
#this prove that the list index is acessable

list[0]=1#firt elemente in list receiving one
#this prove that the list index is acessable

print(list)#write in the screen the list
#this prove that the tuple index can support print

#tuple[0]=4#return one error,then tuple is invariable
#this prove that the tuple index can't support redefined

print(tuple)#write in the screen the tuple
#this prove that the tuple index can support print

elements_in_tuple=''#creats a element receiving one string content nothing
for element in tuple:#acessing all elements in tuple
    elements_in_tuple+=str(element)+' '#in the end return all elements in tuple containing a space between elements
print(elements_in_tuple)#write all the elements in Tuple on the screen divided by space
#this prove that the tuple index can support loop structure

elements_in_list=''#creats a element receiving one string content nothing
for element in list:#acessing all elemets in list
    elements_in_list+=str(element)+' '#in the end return all elements in list containing a space between elements
print(elements_in_tuple)#write in your screen all
#this prove that the list index can support loop structure

#del tuple[0]#return an error because the tuple does not support adding and remove of elements
# this prove that the tuple can't support add and remove elements

list.append('legal')#add legal in the last index of list
del list[len(list)-1]#delete last element in list
# this prove that the tuple can support add and remove elements

list=tuple(list)#transform list in tuple
#del list[0]#return an error because the tuple does not support adding and remove of elements
#this prove that comand "tuple" transform one list in tuple change your propiety

while True:#freeze pronpt
    pass