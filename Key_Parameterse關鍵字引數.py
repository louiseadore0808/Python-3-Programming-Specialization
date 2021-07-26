# 用引數(argument)所對應的parameter的名稱來指令引數，即使指定順序與def function不一樣也沒問題
# 引數 argument：傳入函式的值。
# 參數 parameter：函數對可接受引數的定義。
#Python呼叫函式(function)時傳入的引數(argument)有兩種類型。

    # positional argument：傳入值前不指定參數名或傳入的iteralbe前加上*。他的值會依序被複製到對應的參數上
    # keyword argument：傳入值前指定參數名(e.g.name=john)或在傳入的dictionary前加上**。

# Define a function called multiply. It should have one required parameter, a string. 
# It should also have one optional parameter, an integer, named mult_int, with a default 
# value of 10. The function should return the string multiplied by the integer. 
# (i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”)

def multiply(a, mult_int=10): #函數multiply定義 a (position)和mult_int (key argument)兩個參數
    return a*mult_int
multiply(2) # 呼叫函數multiply傳入一個引數

# Currently the function is supposed to take 1 required parameter, and 2 optional parameters, 
# however the code doesn’t work. Fix the code so that it passes the test. 
# This should only require changing one line of code.

#def waste(var="Water", mar, marble="type"):  # Non-default argument follows default argument
#    final_string = var + " " + marble + " " + mar
#    return final_string


def waste(mar, var="Water", marble="type"):  # 要先設default argument
    final_string = var + " " + marble + " " + mar
    return final_string
