#List Types
li1 = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']

print(li1)
print(li2)

#Output:
#[1, 2, 3, 4, 5]
#['a', 'b', 'c', 'd', 'e']

# [start:stop:step]
# start: index of the first element to include in the slice
# stop: index of the element to exclude from the slice
# step: step size, which is the number of elements to skip between each element in the slice

#Accessing List Elements
li = [0,1, 2, 3, 4, 5]
print(li[0:])  # Output: [0,1, 2, 3, 4, 5]
print(li[:5])  # Output: [0,1, 2, 3, 4]
print(li[0::2])  # Output: [0,2,4]
print(li[0:4:2])  # Output: [0,2]
print(li[-1::2])  # Output: [5]

#List Methods
# append(): Adds an element to the end of the list
# insert(): Inserts an element at a specific index in the list
# remove(): Removes an element from the list
# pop(): Removes the last element from the list
# sort(): Sorts the elements of the list
# reverse(): Reverses the order of the elements in the list
# count(): Returns the number of occurrences of an element in the list
# index(): Returns the index of the first occurrence of an element in the list
# clear(): Removes all elements from the list
# copy(): Returns a copy of the list
# extend(): Adds the elements of another list to the end of the current list
# count(): Returns the number of occurrences of an element in the list        

li = [1, 2, 3, 4, 5]
li.append(6)  # Output: [1, 2, 3, 4, 5, 6]
li.insert(2, 7)  # Output: [1, 2, 7, 3, 4, 5, 6]
li.remove(3)  # Output: [1, 2, 7, 4, 5, 6]
li.pop()  # Output: [1, 2, 7, 4, 5]
li.sort()  # Output: [1, 2, 4, 5, 6, 7]
li.reverse()  # Output: [7, 6, 5, 4, 2, 1]
li.count(2)  # Output: 1
li.index(4)  # Output: 2
li.clear()  # Output: []
li.copy()  # Output: [7, 6, 5, 4, 2, 1]
li.extend([8, 9, 10])  # Output: [7, 6, 5, 4, 2, 1, 8, 9, 10]

#List unpacking
a, b, c = [1, 2, 3]
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

