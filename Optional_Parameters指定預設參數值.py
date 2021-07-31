# 預設值參數(Default Argument)：在函式定義的參數中，將可以選擇性傳入的參數設定
# 一個預設值，當來源端有傳入該資料時，使用來源端的資料，沒有傳入時，則依照設定的預
# 設值來進行運算
# 必要參數(Required Argument)一定要放在預設值參數(Optional Argument)的前面
# Optional Parameters:
#   define default values for formal parameters, which made it optional to provide values 
#   for those parameters when invoking the functions
# 要注意default argument是在函數被定義時計算的！不是在執行的時候，所以就算後面再改也不會變
# 而且不可以將mutable datatype: dictionary or string當成default argument使用

def dk(a, L=[]):
    L.append(a)
    return L
print(dk(1))    #L=[1] value saved
print(dk(7))    #L=[1,7]
print(dk(3, ['Hello'])) #L=[1,7] mutate to ['Hello'] and append 3 => L = ['Hello', 3]
print(dk(5, ['Hello']))

initial = 7
def f(x, y=3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))
# keyword arguments always have to come after any positional arguments 
# that don't specify a keyword
f(2)
f(2, 5) #y=3 -> y=5
f(2, 5, 8)  # -> z=8

initial = 7

def f(x, y=3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

#不要設default value為mutable object, that object will be shared in 
# all invocations of the function
initial = 10  # default values are only evaluated when we declare the function. 
# When we declare this function f initial had the value seven, and so we can just almost 
# replaced this with the value seven. It doesn't matter that we changed initial later on, 
# z is going to have the value seven by default.
f(2) #initial in def不變

# Write a function called str_mult that takes in a required string parameter and an optional integer
#  parameter. The default value for the integer parameter should be 3. The function should return the
#  string multiplied by the integer parameter.
def str_mult(a, b=3):
    return a*b

# When we write key=some_function in the function invocation, the word key is there because
# it is the name of the parameter, specified in the definition of the sort function,
# not because we are using keyword-based parameter passing.

# You will be sorting the following list by each element’s second letter, a to z. 
# Create a function to use when sorting, called second_let. It will take a string as input 
# and return the second letter of that string. Then sort the list, create a variable called 
# sorted_by_second_let and assign the sorted list to it. Do not use lambda.

# It depends on how sorted works when it has a key parameter that takes a function as value:
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(x):
    return x[1]

sorted_by_second_let = sorted(ex_lst, key=second_let)
# The sorted function loops through each item of the list when it is used like this. 
# That is why there is no need for a for loop.

# Below, we have provided a list of strings called nums. Write a function called last_char that 
# takes a string as input, and returns only its last character. Use this function to sort the list 
# nums by the last digit of each number, from highest to lowest, and save this as a new list 
# called nums_sorted.


nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(s):
    return s[-1]

nums_sorted = sorted(nums, reverse=True, key=last_char)
print(nums_sorted)

# Once again, sort the list nums based on the last digit of each number from highest to lowest.
# However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums, reverse=True, key=lambda x: x[-1])
