print("****************.Manage Product Prices.*************")

product_name=[]
product_price=[]

while True:
    print("##############.Manage Product Prices.##############")
    print("1.Insert product")
    print("2.Display product")
    print("3.Update product")
    print("4.Delete product")
    print("5.Search product")
    print("6.Sort product")
    print("7.Exit ")

    choice=int(input("Enter your choice:"))

    if choice==1:

        product=(input("Enter your product:"))
        product_name.append(product)
     
        price=int(input("Enter your product price:"))
        product_price.append(price)

        print("product inserted successfully.")

    elif choice==2:
        if len(product_name) ==0:
            print("No products Are Available")

        else:
            print("products :-")

            for i in range(len(product_name)):
                           print("Product:", product_name[i], "Price:", product_price[i])
    elif choice==3:
        product2=input("Enter product Name to Update:")
        if  product2 in product_name: 
            product_name.index(product)
            new_price=int(input("Enter Updated Price: "))

    elif choice==4:
        product3=input("Enter Product Name To Delete:")
        if  product3 in product_name:
            index=product_name.index(product3)
            product.pop(index)
            print("product inserted successfully.")

        else:
            print("Product Not Found:")

    elif choice==5:
        product4=input("Enter Product Name to search:")
        if  product4 in product_name: 
            index=product_name.index(product4)
            print("product found:")
            print("product:",product_name[index])
            print("price:",product_price[index])
        else:
            print("Product Not Found:")

        
    else:
        break
    

        