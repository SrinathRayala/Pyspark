import mysql.connector as mc
from mysql.connector import errorcode as ec
import pandas as pd
import datetime
def get_connection(user,password,host,db):
    try:
        connection = mc.connect(user =user,
                                 password=password,
                                 host=host,
                                 database=db
                                 )
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
        else:
            print(error)
    return connection
def get_cursor(connection):
    return connection.cursor()
def get_orders():
    orders_path="C:\\retail_db\\data-master\\retail_db\\orders\\orders_status"
    orders_schema=[
        "order_id",
        "order_date",
        "order_customer_id",
        "order_status"
    ]
    orders= pd.read_csv(
        orders_path,
        header=None,
        names=orders_schema)
    return orders
def load_orders(connection,cursor,query,orders):
    for idx, order in orders.iterrows():
        cursor.execute(query,(order.order_id,order.order_date,order.order_customer_id,order.order_status))
        connection.commit()
def load_orders_batch(connection,cursor,query,orders):
    print(datetime.datetime.now())
    data_batch = []
    count=1
    for idx,order in orders.iterrows():
        data_batch.append(tuple(order))
        if (count%1000 ==0):
            cursor.executemany(query,data_batch)
            connection.commit()
            data_batch=[]
        count=+1
    cursor.executemany(query,data_batch)
    connection.commit()
connection = get_connection('db_user','db_pass','35.239.196.43','retail_db')
print("connection>>>>>>" + str(connection) )
cursor = get_cursor(connection)
orders = get_orders()
orders.count()
print("orders.count()>>>>>>" + str(orders.count()) )
query=("""INSERT INTO orders_batch
        (order_id,order_date,order_customer_id,order_status)
        VALUES
        (%s,%s,%s,%s)""")
load_orders_batch(connection,cursor,query,orders)