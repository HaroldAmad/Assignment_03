def getApple ():
    apple_func = input("Apple: ")
    return apple_func

def getOrange ():
    orange_func = input("Orange: ")
    return orange_func

def gettotalPrice ():
     totalPrice_func = int((apple * 20) + (orange * 25))
     return totalPrice_func

apple = getApple()
orange = getOrange()
totalPrice = gettotalPrice()