#Lists declare
#Indexes and slicing
#Addition
#Append, Insert, Remove. Pop== NOT ALL LISTS OPERATION ARE LISTED HERE
#Lists can contain a  large number of items and the items can be any data type
#Integers, Float, Boolean, Other lists, Strings
#Our_list positions are (0,1, 2, 3 ,4 , 5, 6)
#Indexes are positions in the list
#Python indxes start from 0
#Return items from this list
#the_list [Index of the list][Index of the item in the inner list]

#our_list = [2,5, True, False, ["Nairobi", "Mombasa"], "Hello World"]
#the_list [Index of the list][Index of the item in the inner list]
print(len(our_list))
print(our_list[4][0])
print(our_list[3])
our_list= [0,1, 2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20]
#list slicing
#list[index_of_the_position:index_of_the_last_position: how_many_items_
#list[start:stop-1(exclusive):step]
#print(our list[0:5])
numbers = [0, 1,2,3,4,5,6,7,8,9,10]
even_numbers = numbers [2::2]
not_odd = numbers[1::2]
print(not_odd)
#not """
#OOP- Object Oriented Programming
#Classes are blue prints for objects
#Alter objects
#All data
#Append, Remove, Insert, Pop, Push
#Append method adds an item as the last item in a list
#syntax for append
#list.append()
our_list=0,1,2,3,4,5,6,7,8, 9, 10,11,12,13,14,15,16,17,18,19,20
our_list.append(20)
print(our_list)#0, 1, 2, 3,4 ,5, 6, 7, 8, 9,10]


#insert(index, item)
print(ouur_list)

#pop method
#It removes the last element. It removes that specific item you indicate
our_list.pop[2]#the_list [Index of the list][Index of the item in the inner list]
#Count tells the number of a particular item in the list\
print(our_list.count(2))
#sort tells the list to sort in an assending order
our_list
#dir.list will show all the attributs of data that we have
#This will give you data types such as str, float
