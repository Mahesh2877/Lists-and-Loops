a = [1, 3, 6, 9, 11]
print("Input array is ")
print(a)

#Creating a new array by apppending elements to an existing(albeit empty) array
b = []
for x in a:
    b.append(x * 2)
print("Double of input array is ")
print(b)

#Create a new array by implementing the for loop inside the array creation statement
c = [x ** 2 for x in a]
print("Square of input array is ")
print(c)
