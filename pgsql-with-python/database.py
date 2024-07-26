import psycopg2
import os

def insert_sale(cur, order_num, cust_name, prod_number, prod_name, quantity, price, discount):
    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount
    sale_data = {
        'order_num': order_num,
        'cust_name': cust_name,
        'prod_number': prod_number,
        'prod_name': prod_name,
        'quantity': quantity,
        'price': price,
        'discount': discount,
        'order_total': order_total
    }

    stmt = ''' INSERT INTO sales VALUES (%(order_num)s,
    %(cust_name)s, %(prod_number)s, %(prod_name)s, %(quantity)s,
    %(price)s, %(discount)s, %(order_total)s)'''

    cur.execute(stmt, sale_data)


if __name__ == "__main__":
    conn = psycopg2.connect(database="red30", 
        user="postgres", 
        password=os.getenv("PASSWORD"), 
        host="localhost",
        port="5432")

    cursor = conn.cursor()

    # cursor.execute('''CREATE TABLE SALES(ORDER_NUM INT PRIMARY KEY,
    # CUST_NAME TEXT,
    # PROD_NUMBER TEXT,
    # PROD_NAME TEXT,
    # QUANTITY INT,
    # PRICE REAL,
    # DISCOUNT REAL,
    # ORDER_TOTAL REAL);''')

    # sales = [ (1100935, "Spencer Educators", "DK204","BYOD-300", 2, 89, 0, 178),
    # (1100948, "Ewan Ladd", "TV810", "Understanding Automation", 1, 44.95, 0, 44.95),
    # (1100963, "Stehr Group", "DS301", "DA-SA702 Drone", 3, 399, .1, 1077.3),
    # (1100971, "Hettinger and Sons", "DS306", "DA-SA702 Drone", 12, 250, .5, 1500),
    # (1100998, "Luz O'Donoghue", "TV809", "Understanding 3D Printing", 1, 42.99, 0, 42.99) ]

    # cursor.executemany("INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", sales)

    print("Input sale data:\n")
    order_num = int(input("What is the order number?\n"))
    cust_name = input("What is the customer's name?\n")
    prod_number = input("What is the product number?\n")
    prod_name = input("What is the product name?\n")
    quantity = float(input("How many were bought?\n"))
    price = float(input("What is the price of the product?\n"))
    discount = float(input("What is the discount, if there is one?\n"))
    print("Inputting sale data:\n")

    insert_sale(cursor, order_num, cust_name, prod_number, prod_name, quantity, price, discount)

    conn.commit();
    conn.close();
