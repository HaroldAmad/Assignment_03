def getApple ():
    apple_func = int(input("Apple: "))
    return apple_func

def getOrange ():
    orange_func = int(input("Orange: "))
    return orange_func

def gettotalPrice ():
     totalPrice_func = ((apple*20) + (orange*25))
     return totalPrice_func

def displayOutput (totalPriceF,):
    print(f"The total amount is {totalPriceF}")

apple = getApple()
orange = getOrange()
totalPrice = gettotalPrice()
displayOutput (totalPrice)