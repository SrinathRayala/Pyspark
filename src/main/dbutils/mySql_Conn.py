import mysql.connector as mc
import datetime
#from mysql.connector import errorcode as er
connection =mc.connect(user='db_user',
           password='db_pass',
           host='104.197.104.102',
           database='retail_db')
orders_cursor =connection.cursor(prepared=True)
query="select * from orders where order_status=%s limit 10"
query_inst=("""
INSERT INTO orders_
    (order_id,order_date,order_customer_id,order_status)
values
    (%s,%s,%s,%s)
""")
query_update=("""
UPDATE orders_
        SET order_status= %s
        where order_id = %s
""")
query_delete=("""
DELETE FROM orders_ WHERE order_id = %s
""")
order_date=datetime.datetime(2020,1,2,0,0,0)
#orders_cursor.execute(query,('COMPLETE',))
orders_cursor.execute(query_inst, (4,order_date,100,"COMPLETE",))
orders_cursor.execute(query_update,('CANCELED',1))
orders_cursor.execute(query_delete,('1'))
connection.commit()
#for order in orders_cursor:
#    print(order)
