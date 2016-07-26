list_of_desserts = ["candie", "biscuit", "ice cream"]
for dessert in list_of_desserts:
    if dessert == "cake":
        print("{}!!!!".format(dessert))
        break
    else:
        print('Not a cake')
else:
    print('The cake is a lie')
