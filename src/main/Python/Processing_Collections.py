path="C:/retail_db/data-master/retail_db/orders/orders_status"
orders_file=open(path)
orders_raw=orders_file.read()
orders=orders_raw.splitlines()
print(orders[:10])
