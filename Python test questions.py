import pandas as pd
import numpy as np

# Write a function that determines if two lists of numbers are equal
# (First Method)
list1 = []
list2 = []

lister = input("What numbers go in list 1? (separate with comma)")
lister2 = input("What numbers go in list 2? (sep. with comma)")

list1 = lister.split(",")
list1 = [int(list) for list in list1]
list2 = lister2.split(",")
list2 = [int(list) for list in list2]

## Easy way, numbers have to occupy same position
counter = 0
for i in range(len(list1)):
    if list1[i] != list2[i]:
        print("Your lists are not the same")
        counter += 1
        break

if counter==0:
    print("Your lists are the same")

# (Second Method)

list1 = []
list2 = []

lister = input("What numbers go in list 1? (separate with comma)")
lister2 = input("What numbers go in list 2? (sep. with comma)")

list1 = lister.split(",")
list1 = [int(list) for list in list1]
list2 = lister2.split(",")
list2 = [int(list) for list in list2]

## Numbers do not need to occupy same position
bigcount = 0
for i in range(len(list1)):
    lilcount = 0
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            lilcount += 1
            list2[j] = -9999
            break
    if lilcount == 0:
        print("Your lists are not equal")
        bigcount += 1
        break

for list in list2:
    if list != -9999:
        print("Your lists are not the same")
        bigcount += 1

if bigcount == 0:
    print("Your lists are the same")

# (Third Method)

list1 = []
list2 = []

lister = input("What numbers go in list 1? (separate with comma)")
lister2 = input("What numbers go in list 2? (sep. with comma)")

list1 = lister.split(",")
list1 = [int(list) for list in list1]
list2 = lister2.split(",")
list2 = [int(list) for list in list2]

## Numbers do not need to occupy same position
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            list1[i] = -9999
            list2[j] = -9999
            break

count = 0
for list in list2:
    if list != -9999:
        print("Your lists are not the same")
        count +=1
        break

if count == 0:
    for list in list1:
        if list != -9999:
            print("Your lists are not the same")
            count += 1
            break

if count == 0:
    print("Your lists are the same")


# Write a function that counts how many times each letter in a string
# occurs. Count letters in word "interview"
inputstring = input("What is your input string? ")
inputs = [c for c in inputstring]
print(inputs)
lettcount = {}
for s in inputs:
    if s in lettcount:
        lettcount[s] += 1
    else:
        lettcount[s] = 1

#for h in inputs:
#    lettcount[h] += 1

print(lettcount)


# Write a function that accepts an array of integers and returns the
# largest number we can get by multiplying two of them
myInt = input("Type in a few integers, separated by commas: ")
intArray = myInt.split(",")
intArray = [int(num) for num in intArray]
intArray.sort(reverse=True)
multi = intArray[0] * intArray[1]
print(str(intArray[0]) + " x " + str(intArray[1]) + " = " + str(multi))



# Write a function that finds the most frequent element in an array
arr = input("Input an array of elements, separated by commas: ")
arr = arr.split(",")
print(arr)
arruq = []
arruq_fq = []
for x in arr:
    if x not in arruq:
        arruq.append(x)

for x in arruq:
    arruq_fq.append(0)

for i in range(len(arr)):
    position = arruq.index(arr[i])
    arruq_fq[position] += 1
print(arruq)
print(arruq_fq)

max_inx = arruq_fq.index(max(arruq_fq))
print(arruq[max_inx])


# Write a function that determines if its string argument is a
# palindrome

stringipt = input("Please input a string: ")
string_back = stringipt[::-1]
if stringipt == string_back:
    print(stringipt + " and " + string_back + ". This is a pallindrome")
else:
    print(stringipt + " and " + string_back + ". This is not a pallindrome")
