from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, String, MetaData, select
import os

password = os.getenv("PASSWORD")

engine = create_engine(f'postgresql+psycopg2://postgres:{password}@localhost/red30', 
	echo=True)
metadata = MetaData()

# sales_table = Table('sales', 
#       metadata,  
#       Column('order_num', Integer, primary_key=true),
#       Column('cust_name', String),
#       Column('prod_number', String),
#       Column('prod_name', String),
#       Column('quantity', Float),
#       Column('price', Float),
#       Column('discount', Float),
#       Column('order_total', Float))

sales_table = Table('sales', metadata, autoload_with=engine)

metadata.create_all(engine)

with engine.connect() as conn:

    for row in conn.execute(select(sales_table)):
        print(row)

        insert_statement = sales_table.insert().values(order_num=1105910,
        cust_name='Syman Mapstone',
        prod_number='EB521',
        prod_name='Understanding Artificial Intelligence',
        quantity=3,
        price=19.5,
        discount=0,
        order_total=58.5)

        conn.execute(insert_statement)

        update_statement = sales_table.update().where(
            sales_table.c.order_num==1105910
        ).values(quantity=2, order_total=39)

        conn.execute(update_statement)

        reselect_statement = sales_table.select().where(
            sales_table.c.order_num==1105910
        )

        updated_sale = conn.execute(
            reselect_statement
        ).first()

        print(updated_sale)

        delete_statement = sales_table.delete().where(
            sales_table.c.order_num==1105910
        )

        conn.execute(delete_statement)

        not_found_set = conn.execute(reselect_statement)

        print(not_found_set.rowcount)
