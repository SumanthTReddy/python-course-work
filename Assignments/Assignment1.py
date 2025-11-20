#Assignment-1

# All Data Types Example – Food Order (with number of items)

order_id = 5678                                                           # int
delivery_fee = 35.50                                                      # float
restaurant = "Mehfil Restaurant"                                          # str
is_express_delivery = True                                                # bool
items = ["Biryani", "Cold Drink", "Chicken Wings"]                        # list
delivery_details = ("7 PM - 7:30 PM", "Near Big Bazaar", "Kothapet")      #tuple
payment_methods = {"UPI", "Cash"}                                         # set
order_summary = {                                                         # dict
    "total_items": len(items),
    "status": "Preparing"
}

order = {
    "order_id": order_id,
    "restaurant": restaurant,
    "items": items,
    "delivery_fee": delivery_fee,
    "details": delivery_details,
    "express": is_express_delivery,
    "payment_methods": payment_methods,
    "summary": order_summary
}

print("Order Placed:")
print(order)
print("\nNumber of items in this order:", len(items))
