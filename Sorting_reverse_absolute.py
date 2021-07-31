a = ['Apple', 'banana', 'Cherry', '12months', 'Ant', 'Ap3le']
print(sorted(a)) # number > Capital > order

L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))

# First, let’s define a function absolute that takes a number and returns its absolute value. 
# (Actually, python provides a built-in function abs that does this, but we are going to 
# define our own, for reasons that will be explained in a minute.)

L1 = [1, 7, 4, -2, 3]


def absolute(x):
    if x >= 0:
        return x
    else:
        return -x


print(absolute(3)) # 一般用法
print(absolute(-119))

for y in L1:
    print(absolute(y))

# 也可以像下方這樣
L2 = sorted(L1, key=absolute) # 在function內叫另一function
print(L2)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))

# 1. You will be sorting the following list by each element’s second letter, a to z. 
# Create a function to use when sorting, called second_let. 
# It will take a string as input and return the second letter of that string. 
# Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. 
# Do not use lambda.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
def second_let(a):
    for i in ex_lst:
        