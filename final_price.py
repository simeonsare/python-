def calculate_discount():
    price = float (input("enter price:"))
    discount_percent = float (input("enter discount:"))

    if discount_percent >=20:
        final_price = price*((100-discount_percent)/100)
    else:
        final_price = price
    print(final_price)
calculate_discount()
