def order_system(order_type,*items,**customer_info):
    print("="* 20)
    print("Your Order".center(20))
    print("="* 20)
    print("Order Type: ", order_type)
    print("Items:")
    for item in items:
        print("".expandtabs(2),item)
    print("Customer Info:")
    print("".expandtabs(2),f"Name: {customer_info["name"]}")
    print("".expandtabs(2),f"Phone: {customer_info["phone"]}")
    print("".expandtabs(2),f"Payment method: {customer_info["payment_method"]}")

order_system("dine-in","Biryani","Haleem","Karahi",name="Wahab",phone=123,payment_method="Cash")