# 預設值參數(Default Argument)：在函式定義的參數中，將可以選擇性傳入的參數設定
# 一個預設值，當來源端有傳入該資料時，使用來源端的資料，沒有傳入時，則依照設定的預
# 設值來進行運算
# 必要參數(Required Argument)一定要放在預設值參數(Optional Argument)的前面
# Optional Parameters:
#   define default values for formal parameters, which made it optional to provide values 
#   for those parameters when invoking the functions

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

# Write a function called str_mult that takes in a required string parameter and an optional integer parameter. The default value for the integer parameter should be 3. The function should return the string multiplied by the integer parameter.
def str_mult(a, b=3):
    return a*b
