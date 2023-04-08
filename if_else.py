# budget = 1000
# price = 900
# if(budget > price):
#     print("you can buy the item")
# else:
#     print("please earn more")

# budget = int(input("Enter your budget:"))
# price = int(input("Enter the price of the item you want to buy:"))
# if(budget>price):
#     print("You can buy the item")
# else:
#     print("you cannot buy the item")

# budget = int(input("Enter your budget:"))
# price = int(input("Enter the price of the item you want to buy:"))
# if(budget>price):
#     print("You can buy the item and you are left with Rs. ", budget-price)
# else:
#     print("you cannot buy the item")

budget = int(input("Enter your budget:"))
price1 = int(input("Enter the price of the first item:"))
price2 = int(input("Enter the price of the second item:"))

if(budget > price1+price2):
    print("you can buy both items.")
elif(budget < price1 & price2):
    print("you cannot buy even one item")
elif(budget < price1 + price2):
    if (price1 - price2 > 0):
        print("You can buy only one item. If you wish to buy both items you should get a loan of Rs. ", price1 - price2)
    else:
        print("You can buy only one item. If you wish to buy both items you should get a loan of Rs. ", price2 - price1)
    