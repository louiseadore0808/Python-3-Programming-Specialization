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
        eve_nums += count
print(eve_nums)