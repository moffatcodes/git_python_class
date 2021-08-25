#Unordered collection, unique items
our_list = [4,2,2,3,4,5,4,7,8,9,14,11,12,13,13,15,13,17,19,19,20]
our_tupple = (4,2,2,3,4,5,4,7,8,9,14,11,12,13,13,15,13,17,19,19,20)#Cannot be changed
our_set= {2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15, 17, 19, 20}#All the duplicates are removed.

#If you compare our tupple to tupple(our_list). It should be equal.
print(set(our_list))
print(set(our_tupple))

set_1 = {2,3,4,5}
set_2 ={5,8,9,10}

#unique values
set_3 =set_1.union(set_2)
print(set_3)
print(our_tupple==our_set)
print(our_tupple)
print(our_set)
print(our_list)
print(list(our_set
