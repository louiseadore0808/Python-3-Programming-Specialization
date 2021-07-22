#The listener loop:透過input來執行while loop
theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): ")) #0 is Sentinel Values提示loop結束

    theSum = theSum + x

print(theSum)