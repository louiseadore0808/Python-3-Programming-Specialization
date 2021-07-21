while True:
    print('this phrase will always print')
    break
    print('Does this phrase print?')

print('We are done with the while loo')

x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue    #this step will loop back to while condition -> 3<10 ->才進入line14
    if x % 3 == 0:
        x += 5      # 3+5=8 ->back to while, 8<10, 8+5 = 13>10 ->進入下一行
    x += 1
print("Done with our loop! X has the value: " + str(x))