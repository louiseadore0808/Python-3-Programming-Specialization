def f(x):
    return x - 1
# can also write in
lambda x: x-1 # x: input, x-1: return object 

print(f)  # <function f>
print(type(f))  # <class 'function'>
print(f(3)) # 2

print(lambda x: x-2) 
# def lambda(x):
#    return x-2

print(type(lambda x: x-2))  # <function <lambda>>
print((lambda x: x-2)(6))   # 4
# def lambda(x):
#    return x-2
# print(lambda(6))


def last_char(s):
    return s[-1]
# can also write in
last_char = (lambda s: s[-1])

# Once again, sort the list nums based on the last digit of each number from highest to lowest. 
# However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums, reverse=True, key=lambda x: x[-1])
