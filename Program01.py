def getApple ():
    apple_func = int(input("Apples you want to buy: "))
    return apple_func

def getOrange ():
    orange_func = int(input("Oranges you want to buy: "))
    return orange_func

def gettotalPrice ():
     totalprice_func = ((apple*20) + (orange*25))
     return totalprice_func

def displayOutput (totalPriceF):
    print(f"The total amount is {totalPriceF}")

apple = getApple()
orange = getOrange()
totalPrice = gettotalPrice()
displayOutput (totalPrice)