def sumTo(aBound):
    '''Return the sum of 1+2+3 ... n''' #in this case: n means aBound
    
    theSum = 0
    aNumber = 1
    while aNumber <= aBound:   #this line is condition
        theSum += aNumber      #run this block see if condition is true
        aNumber += 1           #loop back to while condition to see if stil ture
    return theSum
print(sumTo(4))
print(sumTo(1000))

#Write a while loop that is initialized at 0 and stops at 15. If the counter is an
# even number, append the counter to a list called eve_nums.
count = 0
eve_nums = []
while count <= 15:
    if count % 2 == 0:
        eve_nums.append(count)
    count += 1
print(eve_nums)

#Below, we’ve provided a for loop that sums all the elements of list1. 
#Write code that accomplishes the same task, but instead uses a while loop. 
#Assign the accumulator variable to the name accum.
list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

num = 0
accum = 0
while num < len(list1): #設定num=0, index 由0開始最多到6，因為list1長度為7
    accum += list1[num]
    num += 1
print(accum)

#Write a function called stop_at_four that iterates through a list of numbers. 
#Using a while loop, append each number to a new list until the number 4 appears. 
#The function should return the new list.
lst = [0, 9, 4.5, 1, 7, 4, 8, 9, 3]
def stop_at_four(lst):
    num = 0
    alist = []
    while num < len(lst) and lst[num] != 4:
        alist.append(lst[num])
        num += 1
    return alist
lst = [1, 6, 2, 3, 9]
print(stop_at_four(lst))
