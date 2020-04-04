mylist = [5, 3, 1, 0, -2, -4, -8]

i = 0
sum = 0
while (i < len(mylist) and mylist[i] > 0):
    sum += mylist[i]
    i += 1
print("Sum of the Positive integers in the input list is " + str(sum))
