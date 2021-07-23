import random
import turtle


def isInScreen(w, t):           #烏龜在幹嘛
    if random.random() > 0.1:   # probability
        return True     #90%機率烏龜可以繼續活動
    else:
        return False    #剩下一成烏龜會stop


t = turtle.Turtle()     #一隻叫t的烏龜
wn = turtle.Screen()    #烏龜出現的地方

t.shape('turtle')      #會是烏龜的樣子
while isInScreen(wn, t):   #不確定coin會翻轉幾次，所以用while loop而非for loop
    coin = random.randrange(0, 2)
    if coin == 0:              # heads 
        t.left(90)
    else:                      # tails
        t.right(90)

    t.forward(50)

wn.exitonclick()     #點一下離開頁面
