def getMoney():
    money_Func = int(input("Amoount of Money: "))
    return money_Func

def getapplePrice():
    appleprice_Func = int(input("Price of Apple: "))
    return appleprice_Func

def gettotalApples():
    totalapples_Func = int(money/applePrice)
    return totalapples_Func

def getChange():
    change_Func = (money%applePrice)
    return change_Func

def displayOutput (totalApplesF, changeF):
    print(f"You can buy {totalApplesF} apples and your change is {changeF} pesos.")

money = getMoney()
applePrice = getapplePrice()
totalApples = gettotalApples()
change = getChange()
displayOutput (totalApples, change)    