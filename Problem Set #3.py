def ConvertingCurrency():

    currency = {"United States Dollar" : 0.99, "European Euro" : 1, "Ethiopian Birr" : 52.23, "Philippine Peso" : 57.75}
    listOfKeys = currency.keys()
    listOfKeys = list(listOfKeys)
    print("Select the type of currency you have:")
    for key in listOfKeys:
        print(key)

    original_currency=input(":")
    
    if (original_currency) in currency.keys():
        original_currency=currency.get(original_currency)

    else:
        return ConvertingCurrency()
    value=int(input("Enter how much money you have:"))

    print("Enter the type of currency you would like to convert to:")
    for key in listOfKeys:
        print(key)
    convert_currency=input(":")
    if (convert_currency) in currency.keys():
        x=currency.get(convert_currency)
    else:
        return ConvertingCurrency()

    amount=(value/original_currency)*x
    print("You have " + str(amount)+ " " + (convert_currency))

def GroceryList(food):
    ShoppingList = {"Apple" : 1.50,
                     "Orange" : 1.00,
                     "Banana" : 1.00,
                     "Bagel" : 1.25,
                     "Spinach" : 4.25,
                     "Milk" : 2.75,
                     "Eggs" : 3.25,
                     "Cake" : 8.00,
                     "Pasta" : 3.50}
    y=0

    for items in food:
        y=(ShoppingList.get(items))+y

    print("You have purchased:" + str(food))
    print("Your total is:" + str(y))

if __name__== "__main__":

    ConvertingCurrency()

    GroceryList(["Apple", "Banana", "Spinach", "Bagel", "Pasta"])
