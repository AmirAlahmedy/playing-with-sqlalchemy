from sqlalchemy import Column, String, Integer, Float, create_engine, ForeignKey, select, func, group_by, having
from sqlalchemy.orm import registry, relationship, Session
import os

mysq_root_password = os.getenv("PASSWORD")

engine = create_engine(f'mysql+mysqlconnector://root:{mysq_root_password}@localhost:3306/red30', echo=True)

mapper_registry = registry()

Base = mapper_registry.generate_base()


class Sale(Base):
    __tablename__ = 'sales'
    order_num = Column(Integer, primary_key=True)
    order_type = Column(String(length=10))
    cust_name = Column(String(length=100))
    prod_category = Column(String(length=50))
    prod_number = Column(Integer)
    prod_name = Column(String(length=100))
    quantity = Column(Integer)
    price = Column(Float)
    discount = Column(Float)
    order_total = Column(Float)

    def __repr__(self):
        return "<Sale(order_num='{0}')>".format(self.order_num)


with Session(engine) as session:
    # sales = [
    #     Sale(order_type='purchase', cust_name='Amir Alahmedy', prod_category='Tech', prod_number=4684, prod_name='Ebook',
    #          quantity=1, price=100, discount=0, order_total=100),
    #     Sale(order_type='purchase', cust_name='Amir Alahmedy', prod_category='Tech', prod_number=4684, prod_name='Ebook',
    #          quantity=1, price=100, discount=0, order_total=100),
    #     Sale(order_type='purchase', cust_name='Amir Alahmedy', prod_category='Tech', prod_number=4684, prod_name='Ebook',
    #          quantity=1, price=100, discount=0, order_total=100),
    #     Sale(order_type='purchase', cust_name='Amir Alahmedy', prod_category='Tech', prod_number=4684, prod_name='Ebook',
    #          quantity=1, price=100, discount=0, order_total=100),
    #     Sale(order_type='purchase', cust_name='Amir Alahmedy', prod_category='Tech', prod_number=4684, prod_name='Ebook',
    #          quantity=1, price=100, discount=0, order_total=100),
    # ]
    #
    # session.bulk_save_objects(sales)
    # session.commit()

    smt = select(Sale)
    .group_by(Sale.order_num)
    .having(Sale.price == func.max(Sale.price))
    results = session.execute(smt)
    sale = results.scalar()

    print(sale)

    session.commit()
Base.metadata.create_all(engine)


