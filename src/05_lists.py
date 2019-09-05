# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print(x)

#Append: Basically push in javascript

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
for i in y:
    x.append(i)
print(x)

# basically: 
# for(var i = 0; i < y.length; i++){
#     x.push(y[i])
# }
# console.log(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
x.remove(8)
print(x)

# I don't know what's equivalent in javascript but it would be:
# x.splice(4,1)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x.insert(5, 99)
print(x)

# Append won't work because it only works with one element
# insert can do multiple elements


# Print the length of list x
# YOUR CODE HERE 
print(len(x))

# basically x.length

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
    print(i*1000)