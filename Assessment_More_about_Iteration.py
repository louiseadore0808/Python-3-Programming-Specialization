# Write a function, sublist, that takes in a list of numbers as the parameter. 
# In the function, use a while loop to return a sublist of the input list. 
# The sublist should contain the same values of the original list up until it reaches
# the number 5 (it should not contain the number 5).
def sublist(lst):
    alst = []
    num = 0
    while num < len(lst) and lst[num] != 5: #設定index range並且不讓alst包含5
        alst.append(lst[num])
        num += 1
    return alst
print(sublist([1,2,3,4,5,6,7]))

# Write a function, sublist, that takes in a list of strings as the parameter. 
# In the function, use a while loop to return a sublist of the input list. 
# The sublist should contain the same values of the original list up until it reaches 
# the string “STOP” (it should not contain the string “STOP”).
def sublist(lst):
    n_lst = []
    num = 0
    while num < len(lst) and lst[num] != 'STOP':
        n_lst.append(lst[num])
        num += 1
    return n_lst

# Write a function called check_nums that takes a list as its parameter, 
# and contains a while loop that only stops once the element of the list is the 
# number 7. What is returned is a list of all of the numbers up until it reaches 7.

def check_nums(lst):
    num = 0
    n_lst = []
    while num < len(lst) and lst[num] != 7: #要設index range
        n_lst.append(lst[num]) #不能用n_lst = lst，會讓n_lst包含7即以後element
        if lst[num] == 7:
            break
        num += 1            #不能寫在if前,會造成indexError,list index out of range #放在這才能讓if statement被通過，不然lst[0]不會測試到
    return n_lst
print(check_nums([7,9,10,12,13,7,8,3,2,4,51]))
    #有問題的寫法
def check_nums(lst):
    num = 0
    n_lst = []
    while num < len(lst) and lst[num] != 7: 
        n_lst.append(lst[num]) 
        num += 1                #寫在這會讓index out of range, 只是這裡while 有寫lst[num] != 7 所以還是可以跑，換下面寫法就會有問題
        if lst[num] == 7:
            break
    return n_lst
print(check_nums([7,9,10,12,13,7,8,3,2,4,51]))

def check_nums(lst):
    num = 0
    n_lst = []
    while num < len(lst): 
        n_lst.append(lst[num]) 
        num += 1                #這裏沒有測試到 lst[0] == 7，所以明明index 0 就該break，結果到 lst[5] 才停下
        if lst[num] == 7:
            break
    return n_lst
print(check_nums([7,9,10,12,13,7,8,3,2,4,51]))

# Challenge: Write a function called beginning that takes a list as input and contains a while 
# loop that only stops once the element of the list is the string ‘bye’. What is returned is a 
# list that contains up to the first 10 strings, regardless of where the loop stops. 
# (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element,
# the first 4 are returned.) If you want to make this even more of a challenge, do this without 
# slicing.
def beginning(lst):
    i = 0
    n_lst = []
    while i < 10 and lst[i] != 'bye':
        n_lst.append(lst[i])
        if lst[i] == 'bye':
            break
        i += 1
    return n_lst
        
print(beginning(['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']))

# Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does 
# the same thing, but using a while loop instead of a for loop. Assign the accumulated total in 
# the while loop code to the variable sum2. Once complete, sum2 should equal sum1.

sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
sum2 = 0
i = 0
while i < len(lst):
    sum2 += lst[i]
    i += 1


# Write a function called stop_at_z that iterates through a list of strings. Using a while loop, 
# append each string to a new list until the string that appears is “z”. The function should 
# return the new list.

def stop_at_z(lst):
    i = 0
    while i < len(lst):
        if lst[i] == 'z':
            return lst[0:i]
        i += 1
    return lst[0:i]
