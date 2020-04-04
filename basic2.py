mylist = [5, 3, 1, 0, -2, -4, -8]

#Finding the sum of the positive integers in "mylist" through while loop
i = 0
sum = 0
while (i < len(mylist) and mylist[i] > 0):
    sum += mylist[i]
    i += 1
print("Sum of the Positive integers in the input list - calculated through while loop = " + str(sum))


#Finding the sum of the positive integers in "mylist" through for loop and break
sum = 0
for element in mylist:
    if element <= 0:
        break
    sum += element
print("Sum of the Positive integers in the input list - calculated through for loop and break = " + str(sum))
